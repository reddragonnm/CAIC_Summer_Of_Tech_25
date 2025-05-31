import numpy as np


def get_cost(X: np.array, y: np.array, w: np.array, lambda_: float) -> float:
    # cost with L1 regularization

    m = len(y)
    mse_term = np.sum((X @ w - y) ** 2) / (2 * m)  # mean squared error term

    # L1 regularization term
    w = np.copy(w)  # avoid modifying the original weights
    w[0] = 0  # do not regularize the bias term ("bias trick")
    reg_term = lambda_ * np.sum(np.abs(w))

    return mse_term + reg_term


def get_gradient(
    X: np.array, y: np.array, w: np.array, lambda_: float
) -> tuple[np.array, float]:
    # gradient descent with L1 regularization

    m = len(y)
    y_pred = X @ w
    err = y_pred - y

    mse_term = (X.T @ err) / m  # mean squared error gradient

    reg_term = lambda_ * np.sign(w)  # L1 regularization term
    reg_term[0] = 0  # do not regularize the bias term ("bias trick")

    # calculate gradients for L1 regularization
    return mse_term + reg_term  # matrix multiplication magic


def linear_regression(
    X: np.array, y: np.array, lr: float, lambda_: float, num_epochs: int
) -> tuple[np.array, float]:
    # train linear regression model

    w = np.random.rand(X.shape[1])

    for _ in range(num_epochs):
        cost = get_cost(X, y, w, lambda_)
        print(cost)

        w -= lr * get_gradient(X, y, w, lambda_)

    return w


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    X = np.random.rand(100, 1) * 10  # 100 samples, single feature
    y = 2 * X.squeeze() + 1 + np.random.randn(100) * 2  # linear relation with noise

    X_ = np.hstack((np.ones((X.shape[0], 1)), X))  # add bias term (intercept)

    # Train the model
    w = linear_regression(X_, y, lr=0.01, lambda_=0.01, num_epochs=200)

    # Predict values
    y_pred = X_ @ w

    # Plot the results
    plt.scatter(X, y, color="blue", label="Data")
    plt.plot(X, y_pred, color="red", label="Linear Regression")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.legend()
    plt.title("Linear Regression with L1 Regularization")
    plt.show()
