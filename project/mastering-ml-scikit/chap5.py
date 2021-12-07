# coding: utf-8
from numpy.linalg import inv
from numpy import dot, transpose
X=[[1,6,2], [1,8,1], [1,10,0], [1,14,2], [1,18,0]]
Y=[[7], [9], [13], [17.5], [18]]
print(dot(inv(dot(transpose(X),X)),dot(transpose(X),Y)))
from numpy.linalg import lstsq
print(lstsq(X,Y)[0])
