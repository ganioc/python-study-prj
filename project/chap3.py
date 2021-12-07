import numpy
from numbapro import vectorize

@vectorize(["float32(float32, float32)"], target="gpu")
def vectorAdd(a, b):
    return a + b

def main():
    N = 64

    A = numpy.random.rand(N).astype(numpy.float32)
    B = numpy.random.rand(N).astype(numpy.float32)
    C = numpy.zeros(N, dtype=numpy.float32)

    C = vectorAdd(A, B)
    print(C)


if __name__=="__main__":
    main()



