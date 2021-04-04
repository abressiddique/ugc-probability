# Given a matrix, check if $P_A(x) - P_{A^{-1}}(x)$ is a constant.
# where P_A(x) is the characteristic polynomial of matrix A
import numpy as np 
print("Enter your 2*2 matrix elements one by one separated by a space")
matrix_elements = list(map(int, input().split())) 
A = np.array(matrix_elements).reshape(2, 2)
print("The matrix you entered is: ")
print(A)
if(A[0][0] + A[1][1] == 0 or A[0][0]*A[1][1] - A[0][1]*A[1][0] == 1):
    print("Difference between the characteristic polynomial of the given matrix and it's inverse is a constant")
else:
    print("Difference between the characteristic polynomial of the given matrix and it's inverse is not a constant")
