import numpy as np


def linear(x):
    return x


def linear_dash(x):
    return 1


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_dash(x):
    sig = sigmoid(x)
    return sig * (1 - sig)


def relu(x):
    return np.maximum(0, x)


def relu_dash(x):
    return int(x > 0)


def softmax(x):
    exp_x = np.exp(x - np.max(x))  # for numerical stability
    return exp_x / exp_x.sum(axis=0, keepdims=True)


def softmax_dash(x):
    s = softmax(x)
    return s * (1 - s)


class Layer:
    def __init__(
        self, inp_size, out_size, activation=linear, activation_dash=linear_dash
    ):
        self.inp_size = inp_size
        self.out_size = out_size

        self.weights = np.random.randn(inp_size, out_size)
        self.bias = np.random.randn(out_size)

        self.activation = activation
        self.activation_dash = activation_dash
        self.inp = None

    def feed(self, inp):
        self.inp = inp
        return self.activation(self.weights.T @ inp + self.bias)

    def backprop(self, gradient_till_now, lr):
        assert self.inp is not None

        delta = gradient_till_now * self.activation_dash(
            self.weights.T @ self.inp + self.bias
        )

        self.weights -= lr * np.outer(self.inp, delta)
        self.bias -= lr * delta

        self.inp = None

        return self.weights @ delta


def predict(model, x):
    y_pred = x.copy()
    for layer in model:
        y_pred = layer.feed(y_pred)
    return y_pred


def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def cross_entropy_loss(y_true, y_pred):
    eps = 1e-12
    y_pred = np.clip(y_pred, eps, 1.0 - eps)
    return -np.sum(y_true * np.log(y_pred))


if __name__ == "__main__":
    # model = [
    #     Layer(2, 3, activation=sigmoid, activation_dash=sigmoid_dash),
    #     Layer(3, 1, activation=linear, activation_dash=linear_dash),
    # ]

    # x = np.array([1, 2])
    # y = np.array([3])

    # y_pred = predict(model, x)

    # for _ in range(100):
    #     y_pred = predict(model, x)
    #     loss = mse_loss(y, y_pred)

    #     gradient = 2 * (y_pred - y) / len(y)

    #     for layer in reversed(model):
    #         gradient = layer.backprop(gradient, lr=0.01)

    #     print(loss)

    # print(y_pred)

    import pandas as pd

    df = pd.read_csv("./train.csv")

    model = [
        Layer(784, 128, activation=sigmoid, activation_dash=sigmoid_dash),
        Layer(128, 64, activation=sigmoid, activation_dash=sigmoid_dash),
        Layer(64, 10, activation=softmax, activation_dash=softmax_dash),
    ]

    y = df["label"]
    X = df.drop(columns=["label"]).values / 255.0

    y = pd.get_dummies(y).astype(int).values

    for epoch in range(1000):
        for i in range(len(X)):
            x = X[i]
            y_true = y[i]

            y_pred = predict(model, x)

            loss = cross_entropy_loss(y_true, y_pred)

            gradient = y_pred - y_true
            for layer in reversed(model):
                gradient = layer.backprop(gradient, lr=0.01)

        print(f"Epoch {epoch + 1}, Loss: {loss:.4f}")
