from typing import List
import sys

epsilon = 0.001

class Vector(list):
    def __add__(self, other):
        return Vector((other[i] + self[i] for i in range(len(self))))

    def __sub__(self, other):
        return self + (other*(-1))

    def __mul__(self, other):
        return Vector((self[i]*other for i in range(len(self))))

    def __abs__(self):
        return sum((x*x for x in self))


def d(v1: Vector, v2: Vector) -> float:
    return abs(v1-v2)


def kmeans(vectors: List[Vector], k: int, max_iter: int) -> list:
    centroids: list = vectors[0:k]
    prev_centroids = []
    curr_iter = 0
    while curr_iter < max_iter and (curr_iter == 0 or max((d(centroids[i], prev_centroids[i]) for i in range(k)))>=epsilon):
        clusters = [[] for i in range(k)]
        for v in vectors:
            clusters[min(range(k), key=lambda i: d(v, centroids[i]))].append(v)
        prev_centroids = centroids
        centroids = [sum(clusters[i], start=Vector([0 for _ in range(len(vectors[i]))]))*(1/len(clusters[i])) if len(clusters[i]) != 0 else prev_centroids[i] for i in range(k)]
        curr_iter += 1
    return centroids

def main():
    if len(sys.argv) == 6:
        k = sys.argv[1]
        N = sys.argv[2]
        d = sys.argv[3]
        iter = sys.argv[4]
        input_data = sys.argv[5]
    elif len(sys.argv) == 5:
        k = sys.argv[1]
        N = sys.argv[2]
        d = sys.argv[3]
        iter = "200"
        input_data = sys.argv[4]
    else:
        print("An Error Has Occurred")
        exit(1)

    if not N.isnumeric() or not (1 < int(N)):
        print("Invalid number of points!")
        exit(1)
    N = int(N)
    if not k.isnumeric() or not (1 < int(k) < N):
        print("Invalid number of clusters!")
        exit(1)
    if not d.isnumeric() or not (0 < int(d)):
        print("Invalid dimension of point!")
        exit(1)
    if not iter.isnumeric() or not (1 < int(iter) < 1000):
        print("Invalid maximum iteration!")
        exit(1)

    k = int(k)
    d = int(d)
    iter = int(iter)

    with open(input_data) as f:
        vectors = [Vector([float(x) for x in line.strip().split(",")]) for line in f]


    for centroid in kmeans(vectors, k, iter):
        print(",".join("%.4f" % coord for coord in centroid))

if __name__ == '__main__':
    main()