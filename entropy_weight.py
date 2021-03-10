import numpy as np
import math

MIN = 0
MAX = 0


# MIN_MAX 방법에 사용되는 함수
def fMAX_MIN(x):
    return (x - MIN) / (MAX - MIN) + 0.1  # 0되면 log 함수의 domain 에서 벗어나는 에러발생


# 엔트로피 계산에 사용되는 함수
def fEntropy(p):
    # print("fEntropy : {}".format(p))
    return p * math.log(p)


def main():
    A = np.mat([[33.2, 12.4], [28.1, 15.3], [20.1, 13.3]])
    m = 3  # row count
    n = 2  # column count
    print("A, matrix data : " + str(A))

    global MIN, MAX
    MAX = float(A.max())
    MIN = float(A.min())
    print("max: {}, min : {}".format(MAX, MIN))

    P = np.mat(A.copy())

    for i in range(m):
        for j in range(n):
            P.itemset((i, j), fMAX_MIN(P.item((i, j))))

    print("P : " + str(P))

    E = []
    for j in range(n):
        s = 0
        for i in range(m):
            s += fEntropy(P.item((i, j)))
        E.append(s)

    # 엔트로피가 음수만 나와!
    print("Entropy : " + str(E))

    D = []
    for num in E:
        D.append(1 - num)

    # 하지만 다양성은 양수네? 이래서 1에서 엔트로피를 빼는건가봐
    print("Diversity : " + str(D))

    W = []
    for num in D:
        W.append(num / sum(D))

    # 그래서 가중치는?
    print("Weight : " + str(W))

    R = []
    for i in range(m):
        w = 0
        for j in range(n):
            w += W[j] * A.item((i, j))
        R.append(w)

    # 가중치를 적용한 각 지역별 점수
    print("Result : " + str(R))


if __name__ == '__main__':
    main()
