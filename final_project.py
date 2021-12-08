import LA 
import QR 
import LS 

# introduction 
print("My name is Eddie Pallares and I am a senior pre-med student and the author of this file. This file is a composition of all the functions I have written all semester.")

print("This file imports three files: LA, QR, and LS. We will go through each import and go through each function written within each of those imports. ")

#LA file 
print("~ LA File Functions: ~ ")
test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
test_matrix_01 = [[1,2,3],[4,5,6],[7,8,9]]
test_matrix_02 = [[8,3,4],[6,15,7],[0,72,1]] 
print("We will first go through LA, which is composed of basic Linear Algebra functions (hence the intials LA on the file). ")
print("---")

print("The first function is add_vectors which takes in two vectors and returns their sum in a vector. For example, if vector_a = [1,2,4] and vector_b = [3,1,2]... then add_vectors will return: ")
print(LA.add_vectors(test_vector_01,test_vector_02))
print("---")

print("The second function is vector_scalar_multi which takes in a vector and a scalar, and returns their multiplication in a vector. For example, if vector_a = [1,2,4] and scalar = 2... then vector_scalar_multi will return: ")
print(LA.vector_scalar_multi(test_vector_01,2))
print("---")

print("The third function is matrix_scalar_multi and takes in a matrix and a scalar and returns their multiplicatoin in a matrix. For example, if matrix_a = [[1,2,3],[4,5,6],[7,8,9]] and scalar = 2... then matrix_scalar_multi will return: ")
print(LA.matrix_scalar_multi(test_matrix_01,2))
print("---")

print("The fourth function is add_matrices and takes in two matrices and returns their sum as a matrix. For example, if matrix_a = [[1,2,3],[4,5,6],[7,8,9]] and matrix_b = [[8,3,4],[6,15,7],[0,72,1]] ... then add_matrices will return: ")
print(LA.add_matrices(test_matrix_01,test_matrix_02))
print("---")

print("The fifth function is matrix_vector_multi and takes in a matrix and a vector and returns their mulitplication in a vector. For example, if matrix_a = [[1,2,3],[4,5,6],[7,8,9]] and vector_a = [1,2,4]... then matrix_vector_multi will return: ")
print(LA.matrix_vector_multi(test_matrix_01,test_vector_01))
print("---")

print("The sixth function is matrix_matrix_mulit and takes in two matrices and returns their multiplication in a matrix. For example, if matrix_a = [[1,2,3],[4,5,6],[7,8,9]] and matrix_b = [[8,3,4],[6,15,7],[0,72,1]] ... then matrix_matrix_multi will return: ")
print(LA.matrix_matrix_multi(test_matrix_01,test_matrix_02))
print("---")

a = 2-2j 
b = 3

vector_a = [2, 3+3j, -5-5j]
vector_b = [2,3,-5]

print("The seventh function is conjugate and takes in a scalar (both real and imaginary) and returns the conjugate. For example, if a = 2-2j... then conjugate will return: ")
print(LA.conjugate(a))
print("---")

print("The eighth function is absolute_value and takes in a scalar and returns the absolute value. For example, if a = 2-2j... then absolute_value will return:  ")
print(LA.absolute_value(a))
print("---")

print("The ninth function is p_norm_finite and takes in a vector and integer and returns the p_norm to the input integer. For example if vector_b = [2,3,-5] and p = 3... p_norm_finite will return: ")
print(LA.p_norm_finite(vector_b,3))
print("---")

print("The tenth function is inf_norm and takes in a vector and returns the infinity norm. For example, if vector_b = [2,3,-5] ... then inf_norm will return: ")
print(LA.inf_norm(vector_b))
print("---")

print("The eleventh function is p_norm and takes in a vector, an integer, and a boolean value and returns either the integer p_norm or if boolean = True, then it returns the infinity_norm. For example, if vector_b = [2,3,-5], p = 2, False... then p_norm will return: " )
print(LA.p_norm(vector_b,2,False))
print("---")

print("The twelvth and last function of this file is inner_product and takes in two vectors and returns the inner product. For example, if vector_a = [2, 3+3j, -5-5j] and vector_b = [2,3,-5]... then inner_product will return: ")
print(LA.inner_product(vector_a,vector_b))
print("---")

#QR file 
print("~ QR File Functions: ~ ")
A = [[1,0,1],[2,1,0]]

B = [[1,0,1],[2,1,0],[4,2,1]]

vector_alpha = [2,2j, 2-2j]

print("The first function in this file is gram_schmidt, which takes in a matrix and returns the reduced QR factorization in the form of two matrices, Q and R. For example if A = [[1,0,1],[2,1,0]]... then gram_schmidt will return:  ")
print(QR.gram_schmidt(A))
print("---")

print("The second function is orthonormal which takes in a matrix and returns a matrix of orthonormal vectors, or Q from the QR factorization. For example, if A = [[1,0,1],[2,1,0]]... then gram_schmidt will return:  ") 
print(QR.orthonormal(A))
print("---")

print("The third function is conjugate_tranpose_1, which takes in a vector and returns a vector with each element conjugated. For example, if vector_alpha = [2,2j,2-2j]... then conjugate_tranpose_1 will return: ")
print(QR.conjugate_transpose_1(vector_alpha))
print("---")

print("The fourth function is tranpose, which takes in a matrix and returns a matrix of opposite dimensions, aka all columns become the rows. For example, if A = [[1,0,1],[2,1,0]] ... then tranpose will return: ")
print(QR.transpose(A))
print("---")

print("The fifth function is conjugate_tranpose, which takes in a matrix and returns a matrix of opposite dimensions with all of its dimensions conjugated, aka all columns become the rows. For example, if A = [[1,0,1],[2,1,0]] ... then tranpose will return: ")
print(QR.conjugate_transpose(A))
print("---")

print("The sixth function is basis_vec_builder, which takes in an integer to make a vector of that size where the first element is 1 and the rest are 0's, known as a basis vector. For example, if the int = 3... then basis_vec_builder will return: ")
print(QR.basis_vec_builder(3))
print("---")

print("The seventh function is identity_builder, which takes in an integer to make a the specified size of an identity matrix. For example, if the int = 3... then identity_builder will return: ")
print(QR.identity_builder(3))
print("---")

print("The eighth function is diag_vec, which takes in a matrix and returns the vectors under the diagnoal of the input matrix. For example, if B = [[1,0,1],[2,1,0],[4,2,1]]... then diag_vec will return: ")
print(QR.diag_vec(B))
print("---")

print("The ninth function is v_builder, which takes in a matrix and an integer and returns the vector needed for building F (v=||diag_vec||*e + diag_vec). For example, if A = [[1,0,1],[2,1,0]]... then v_builder will return: ")
print(QR.v_builder(A,1))
print("---")

print("The tenth function is F_builder, which takes in a vector and returns the matrix F which is  F = I - 2* ((v*conjugate_tranpose(v))/(inner_product(v))). For example, if v = [2,0]... then F_builder will return: ")
print(QR.F_builder([2,0]))
print("---")

#LS file 
print("~ LS File Functions: ~ ")

matrix_alpha = [[2,0,0],[4,4,0],[3,1,6]]
vec_a = [9,5,6]
matrix_beta = [[2,0,0],[1,6,0],[1,2,8]]
vec_b = [8,14,8]

print("The first function in this file is back_sub, which takes in a matrix (A) and a vector (b) and returns a vector to the solution Ax=b. For example, if matrix_alpha = [[2,0,0],[4,4,0],[3,1,6]] and vec_a = [9,5,6]... then back_sub will return:  ")
print(LS.back_sub(matrix_alpha,vec_a))
print("---")

print("The second function in this file is least_squares, which takes in a matrix (A) and a vector (b) and returns a vector to the solution Ax=b. However, A is broken down into its reduced QR factorization using gram_schmidt to make the equation QRx=b -> Rx = (Q^*)(b). For example, if matrix_alpha = [[2,0,0],[4,4,0],[3,1,6]] and vec_a = [9,5,6]... then least_squares will return:  ")
print(LS.least_squares(matrix_beta,vec_b))
print("---")