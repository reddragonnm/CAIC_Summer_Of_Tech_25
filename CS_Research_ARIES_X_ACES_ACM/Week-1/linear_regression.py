import numpy as np


def get_cost(X: np.array, y: np.array, w: np.array, b: float, lambda_: float) -> float:
    m = len(y)
    return (np.sum((X @ w + b - y) ** 2) + (lambda_ * np.sum(w**2))) / (2 * m)


def get_gradient_descent(
    X: np.array, y: np.array, w: np.array, b: float, lambda_: float
) -> tuple[np.array, float]:
    m = len(y)
    y_pred = X @ w + b
    err = y_pred - y

    dJ_dw = (X.T @ err + lambda_ * w) / m  # matrix multiplication magic
    dJ_db = np.sum(err) / m

    return dJ_dw, dJ_db


def linear_regression(
    X: np.array, y: np.array, lr: float, lambda_: float, num_epochs: int
) -> tuple[np.array, float]:
    w = np.random.rand(X.shape[1])
    b = np.random.rand()

    for _ in range(num_epochs):
        cost = get_cost(X, y, w, b, lambda_)
        print(cost)

        dJ_dw, dJ_db = get_gradient_descent(X, y, w, b, lambda_)
        w -= lr * dJ_dw
        b -= lr * dJ_db

    return w, b


if __name__ == "__main__":
    X = np.array([[1, 2], [2, 3], [3, 4]])
    y = np.array([1, 2, 3]).T
    lr = 0.01
    lambda_ = 0.7
    num_epochs = 100

    w, b = linear_regression(X, y, lr, lambda_, num_epochs)
    print(w, b)
