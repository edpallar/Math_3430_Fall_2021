"""
For this homework assignment we will take our work from HW01 and use it to
prepare a python script which will implement our algoirthms as python functions. 

For Problems #0-5 from HW01, Do the following.



1) Write your answer from HW01 in a comment.

2) Below the comment write a function which implements the algorithm from your
comment. If you find that you need to change your algorithm for your python
code, you must edit your answer in the comment. 

3) Test each of your functions on at least 2 inputs. 

4) Upload your .py file to a github repo named "Math_3430_Fall_2021"

This assignment is due by 11:59pm 09/27/2021. Do NOT upload an updated version to github
after that date. 
"""
#Test Inputs

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
test_vector_03 = [3, 6, 9]

test_matrix_01 = [[1,2,3],[4,5,6],[7,8,9]]
test_matrix_02 = [[8,3,4],[6,15,7],[0,72,1]] 
test_matrix_03 = [[1,1,1],[2,2,2],[3,3,3]]
#Example:

#Problem 00

"""
-The Three Questions

Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 

-PsuedoCode

def add_vectors(vector_a,vector_b):

Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

Return the desired result.
"""

def add_vectors(vector_a,vector_b):
  result = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result

# add_vectors(test_vector_01,test_vector_02) should output [4,3,6]
print('Problem 0:Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_02)))
print('Should have been [4,3,6]')

# add_vectors(test_vector_01, test_vector_03) should ouput [4,8,13]
print('Problem 0:Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_03)))
print('Should have been [4,8,13]')

#End Example



#Problem 01
"""
Q1: What do we have?

A1: We have one vector stored as a list, denoted by the name vector_a, and some scalar (either a float or integer). 

Q2: What do we want?

A2: We want the components of vector_a multiplied by the scalar and stored as a list.

Q3: How will we get there?

A3: We will run a for loop n times, where n equals the number of components in vector_a. We will set a new variable equal to an empty list (vector_b) and add the scalar multiplication values for each component to vector_b. 

-PsuedoCode

def vector_scalar_multi(vector, scalar) 

# set up variables 
result = [] 

#notice that vector_b is an empty list 

# add to empty list result using a for loop of multiplying the elements of vector_a x 2, one at a time 
For index in range(len(vector):
	result.append(vector[index] * scalar) 

# return desired list 
Return result 
"""
def vector_scalar_multi(vector, scalar):
  result = []
  for index in range(len(vector)):
    result.append(vector[index] * scalar)
  return result

# vector_scalar_multli(test_vector_01,2) should output [2,4,8]
print('Problem1:Test Output for vector_scalar_multi: ' + str(vector_scalar_multi(test_vector_01,2)))
print('Should have been [2,4,8]')


# vector_scalar_multli(test_vector_03,2) should output [6,12,18]
print('Problem1:Test Output for vector_scalar_multi: ' + str(vector_scalar_multi(test_vector_03,2)))
print('Should have been [6, 12, 18]')


#Problem 02
"""
Q1: What do we have?

A1: We have one matrix stored as a list of columns, denoted by the name matrix, and some scalar. 

Q2: What do we want?

A2: We want the components of matrix multiplied by the scalar and stored as a new matrix.

Q3: How will we get there?

A3: We will run a for loop n times, where n equals the number of columns in 
matrix. We can use the algorithm from above to multiply the scalar times the 
column vectors of the matrix n times and store values in new matrix (result). 

def matrix_scalar_multi(matrix, scalar) 
 
# set up empty matrix (result) of same length as matrix to store new values 

result = [] 

# run the algorithm set up above n times, since we have n stored vectors in our matrix

For index in range(len(matrix)):
	result.append(vector_scalar_multi(matrix[index], scalar))
	
#return resulting matrix 

return result
"""
def matrix_scalar_multi(matrix, scalar):
  result = []
  for index in range((len(matrix))):
    result.append(vector_scalar_multi(matrix[index], 2))
  return result 

# matrix_scalar_multi(test_matrix_01,2) should output [[2,4,6],[8,10,12],[14,16,18]]
print('Problem2:Test Output for matrix_scalar_multi: ' + str(matrix_scalar_multi(test_matrix_01,2)))
print('Should have been [[2,4,6],[8,10,12],[14,16,18]]')

# matrix_scalar_multi(test_matrix_01,3) should output [[3,6,9],[12,15,18],[21,24,27]]
print('Problem2:Test Output for matrix_scalar_multi: ' + str(matrix_scalar_multi(test_matrix_01,3)))
print('Should have been [[3,6,9],[12,15,18],[21,24,27]]')

#Problem 03
"""
Q1: What do we have?

A1: We have two matrices stored as columns of lists. Denoted by the names matrix_a and matrix_b. 

Q2: What do we want?

A2: We want their sum stored as a new matrix.

Q3: How will we get there?

A3: We will create an empty matrix list of the appropriate size and store the sums of
the corresponding components of matrix_a and matrix_b.

def add_matrices(matrix_a,matrix_b):

# Initializing result as an empty list

result = [] 

# Using Algorithm 0 (vector addition), run function add_vectors(matrix_a[index],matrix_b[index]) n times since we have n stored vectors in our matrix_a and matrix_b

for index in range(len(matrix)):
	result[index].append(add_vectors(matrix_a[index],matrix_b[index])):
	
# Return the desired result.

return result
"""
def add_matrices(matrix_a, matrix_b):
  result = []
  for index in range(len(matrix_a)):
    result.append(add_vectors(matrix_a[index],matrix_b[index]))
  return result

# add_matrices(test_matrix_01,test_matrix_02) should output [[9,5,7],[10,20,13],[7,80,10]]
print('Problem 3:Test Output for add_matrices: ' + str(add_matrices(test_matrix_01,test_matrix_02)))
print('Should have been [[9,5,7],[10,20,13],[7,80,10]]')

# add_matrices(test_matrix_01,test_matrix_03) should output [[2,3,4],[6,7,8],[10,11,12]]
print('Problem 3:Test Output for add_matrices: ' + str(add_matrices(test_matrix_01,test_matrix_03)))
print('Should have been [[2,3,4],[6,7,8],[10,11,12]]')

#Problem 04

"""Write an algorithm to implement matrix-vector multiplication using the linear
combination of columns method. You must use the algorithms from Problem #0 and
Problem #1.  


Q1: What do we have? 

A1: We have a matrix stored as columns of lists and a vector stored as a list. 

Q2: What do we want? 

A2: We want a new matrix that holds the values of the matrix multiplication of our initial matrix and vector, where the number of columns of matrix A must equal the number of components in our vector. 

Q3: How will we get there? 

A3: We will get there by first satisfying the condition described above. If that condition is satisfied, we can use Algorithm 0 and 1 to set it up as a linear combination of A*x = A[1]*x[1] + A[2]*x[2] + ... A[n]*x[n]. Now we see that we can just a run a for loop for scalar vector multiplication defined from Problem 1 and use Problem zero to add up the resulting vectors into our new matrix. The only thing is we can't add the vectors all at once, so we will have to do it two vector additions at a time. 
 
 
def matrix_vector_multi(matrix,vector)

# initialize matrix_r as empty list with dimension that has the same number columns (index) as the original matrix. And initialize result list as a list with only one index (to be vector later, just 0 for place holder for now). 

matrix_r = [0 for element in matrix]
result = [0] 

# Use Algorithm 1 to perform the scalar vector multiplication, where the vector is each column index of the matrix list. We are storing these columns in matrix_r for now 
for index in range(len(vector)):
	matrix_r[index]= vector_scalar_multi(matrix[index], vector[index]) 

# We now have a matrix_r list storing columns of vectors as a list, however we need to add all these vectors together to bring down n vectors to 1 vector. Use algorithm 0 to add the matrix_r vectors from above together and store them in result just overriding each time when the addition occurs. 

result = add_vectors(matrix[0],matrix[1])
for index in range(2:len(matrix_r)):
	result = add_vectors(result,matrix_r[index])
# not sure if I did the above pseudocode right, but basically want it to set up the result vector list as matrix[0]+ matrix[1] (to add the first two vectors of the matrix) and save this as result. Then running a for loop to add each matrix element starting at [2] (third column vector) to the previously stored result and save this addition to result. The end goal would be to add the last indexed list (vector) of matrix_r to result to end up with our result vector made of the summations of matrix_r elements (lists of vectors). 

# return result 

return result 
"""
def matrix_vector_multi(matrix, vector):
  matrix_r = [0 for element in matrix]
  result = [0]
  for index in range(len(vector)):
    matrix_r[index] = vector_scalar_multi(matrix[index],vector[index])
  result = add_vectors(matrix_r[0],matrix_r[1])
  for index in range(2,len(matrix_r)):
    result = add_vectors(result, matrix_r[index])
  return result 

# matrix_vector_multi(test_matrix_01,test_vector_1) should output [37,44,51]
print('Problem 4:Test Output for matrix_vector_multi: ' + str(matrix_vector_multi(test_matrix_01,test_vector_01)))
print('Should have been [37,44,51]')

# matrix_vector_multi(test_matrix_01,test_vector_2) should output [21,27,33]
print('Problem 4:Test Output for matrix_vector_multi: ' + str(matrix_vector_multi(test_matrix_01,test_vector_02)))
print('Should have been [21,27,33]')

#Problem 05
"""
Q1: What do we have?

A1: We have two matrices stored as columns of lists. 

Q2: What do we want?

A2: We want their multiplication stored as a new list.

Q3: How will we get there?

A3: We will create an empty list and store the sums of the columns (using the linear-combination matrix multiplication method) using the above method. Instead the vector will be the components of our second matrix and simply store results each as their own index (column of vectors) list in the result matrix. 

def matrix_matrix_multi(matrix_1, matrix_2)

# initialize result as empty list 

result = []

# Use algorithm 4 to perform the matrix matrix multiplication using linear combination method, just running the "matrix_vector_multi" in a for loop until it completes the index (vectors) of the second matrix. A x B matrix = ([A*b1],[A*b2],...[A*bn])

For index in range(len(matrix)):
	result.append(matrix_vector_multi(matrix_1, matrix_2[index]))

# return desired result 
return result 
"""

def matrix_matrix_multi(matrix_1, matrix_2):
  result = []
  for index in range(len(matrix_1)):
    result.append(matrix_vector_multi(matrix_1, matrix_2[index]))
  return result

# matrix_matrix_multi(test_matrix_01,test_matrix_02) should output [[48,63,78],[115,143,171],[295,368,441]]
print('Problem 5:Test Output for matrix_matrix_multi: ' + str(matrix_matrix_multi(test_matrix_01,test_matrix_02)))
print('Should have been [[48,63,78],[115,143,171],[295,368,441]]')

# matrix_matrix_multi(test_matrix_01,test_matrix_03) should output [[12,15,18],[24,30,36],[36,45,54]]
print('Problem 5:Test Output for matrix_matrix_multi: ' + str(matrix_matrix_multi(test_matrix_01,test_matrix_03)))
print('Should have been [[12,15,18],[24,30,36],[36,45,54]]')

