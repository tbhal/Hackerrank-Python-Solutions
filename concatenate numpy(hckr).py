import numpy

N, M, P = map(int, input().split())

NP = numpy.array([list(map(int, input().split())) for i in range(N)])
MP = numpy.array([list(map(int, input().split())) for j in range(M)])

print(numpy.concatenate((NP, MP), axis = 0))