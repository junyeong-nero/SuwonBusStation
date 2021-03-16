import numpy as np
import math
import pandas as pd

MIN = 0
MAX = 0
RMS = 0


def prettyPrint(title, mat):
    print(title + '\n' + str(mat) + '\n')
    # mat = pd.DataFrame(mat)
    # mat.columns = [''] * mat.shape[1]
    # print(title + mat.to_string(index=False) + "\n")


# MIN_MAX 방법에 사용되는 함수
def fMAX_MIN(x):
    return (x - MIN) / (MAX - MIN) + 0.01  # 0되면 log 함수의 domain 에서 벗어나는 에러발생


def fNormalization(x):
    return x / RMS + 0.01  # 0되면 log 함수의 domain 에서 벗어나는 에러발생


# 엔트로피 계산에 사용되는 함수
def fEntropy(p):
    # print("fEntropy : {}".format(p))
    return p * math.log(p)


def main():
    # 데이터
    A = np.mat([[33.2, 12.4, 1], [28.1, 15.3, 0], [20.1, 13.3, 0]])
    m = 3  # row count
    n = 3  # column count
    prettyPrint("A, matrix data", A)

    global MIN, MAX, RMS
    MAX = float(A.max())
    MIN = float(A.min())
    RMS = 0
    for i in range(m):
        for j in range(n):
            RMS += A.item((i, j)) ** 2  # square
    RMS = RMS ** 0.5  # root
    print("max: {}, min : {}, rms : {}".format(MAX, MIN, RMS))

    # 정규화
    P = np.mat(A.copy())
    for i in range(m):
        for j in range(n):
            P.itemset((i, j), fNormalization(P.item((i, j))))
            # P.itemset((i, j), fMAX_MIN(P.item((i, j))))
    prettyPrint("P", P)

    # 엔트로피
    E = []
    for j in range(n):
        s = 0
        for i in range(m):
            s += fEntropy(P.item((i, j)))
        E.append(s)
    prettyPrint("Entropy", E)

    # 다양성
    D = []
    for num in E:
        D.append(1 - num)
    prettyPrint("Diversity", D)

    # 가중치
    W = []
    for num in D:
        W.append(num / sum(D))
    prettyPrint("Weight", W)

    # 가중치를 적용한 각 지역별 점수
    R = []
    for i in range(m):
        w = 0
        for j in range(n):
            w += W[j] * A.item((i, j))
        R.append(w)
    prettyPrint("Result", R)


if __name__ == '__main__':
    main()
