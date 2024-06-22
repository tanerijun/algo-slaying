# 二分法（Bisection method），是一種方程式根的近似值求法。
# 若要求已知函數 f(x) = 0 的根 (x 的解)，則:
#     先找出一個區間 [a, b]，使得f(a)與f(b)異號。根據堪根定理，這個區間內一定包含著方程式的根。
#     求該區間的中點 m = (a + b) / 2 ，並找出 f(m) 的值。
#     若 f(m) 與 f(a) 正負號相同則取 [m, b] 為新的區間, 否則取 [a, m].
#     重複第2和第3步至理想精確度為止。
# 現在有一個方程式 f(x) = 2 - ex，想求 f(x) = 0的解。已知 f(0)f(1) < 0，請用二分法求解

# Output
# 請輸出x的解
# 四捨五入到小數點後第六位


import math


# Function f(x) = 2 - e^x
def f(x):
    return 2 - math.exp(x)


def bisection_method(a, b, tol=1e-6):
    # Ensure that f(a) and f(b) have opposite signs
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    while (b - a) / 2 > tol:
        m = (a + b) / 2
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m

    return round((a + b) / 2, 6)


if __name__ == "__main__":
    # Given interval [0, 1]
    a = 0
    b = 1

    root = bisection_method(a, b)
    print(root)
