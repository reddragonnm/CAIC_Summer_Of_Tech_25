n = 10  # square root of


def f(x):
    return x**2 - n


def f_dash(x):
    return 2 * x


def newton_raphson(f, f_dash, x, num_iters):
    for _ in range(num_iters):
        m = f_dash(x)
        x -= f(x) / m

    return x


if __name__ == "__main__":
    print(newton_raphson(f, f_dash, n, 4))
