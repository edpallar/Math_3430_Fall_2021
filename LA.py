"""
This homework is due on 10/15/2021 by 11:59pm. 


For this assignment you will be writing a python script to be named LA.py. In
this script you will need to write 6 functions. Every function must 

1) Have a doc string.

2) Have type annotations

3) Be tested using unit testing. 

Once you have finished writing LA.py you will upload it to the same github repo
you used for HW02. The functions you need to write are  
"""
#Test Inputs



test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
test_vector_03 = [3, 6, 9]

test_matrix_01 = [[1,2,3],[4,5,6],[7,8,9]]
test_matrix_02 = [[8,3,4],[6,15,7],[0,72,1]] 
test_matrix_03 = [[1,1,1],[2,2,2],[3,3,3]]

#Example:

# Problem #0

def add_vectors(vector_a: list, vector_b: list) -> list:
    """Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
    """ 
    result = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result

# End Example
# Note that you must add unit tests for problem 0!!!!!
# vector_scalar_multli(test_vector_01,2) should output [2,4,8]
print('Problem0:Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_02)))
print('Should have been [4,3,6]')


#Problem 01

def vector_scalar_multi(vector: list, scalar: float):
  """Multiplies a vector by a scalar.

    Creates a result vector as an empty set. It then goes through each element 
    of the vector and multiplies times the scalar, then stores the value by 
    appending the result vector. This is run with a for loop "n" times, where 
    "n" equals the number of components in vector

    Args:
        vector: A vector stored as a list
        scalar: a float or integer

    Returns:
       The multiplication of the input vector and scalar stored as a list as result. 
    """
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

def matrix_scalar_multi(matrix: list, scalar: "float"):
  """Multiplies a matrix by a scalar.

    Creates a result matrix as an empty set. It then goes through each element 
    of the matrix (which are vectors) and multiplies times the scalar, then 
    stores the value (a vector stored as a list) by appending the result matrix.
    This is run with a for loop "n" times, where "n" equals the number of 
    components in matrix

    Args:
        matrix: A matrix stored as a list of column vectors. 
        scalar: a float or integer

    Returns:
       The multiplication of the input matrix and scalar stored as a new matrix as result. 
    """
  result: "list[list[float]]"= []
  for index in range((len(matrix))):
    result.append(vector_scalar_multi(matrix[index], scalar))
  return result 

# matrix_scalar_multi(test_matrix_01,2) should output [[2,4,6],[8,10,12],[14,16,18]]
print('Problem2:Test Output for matrix_scalar_multi: ' + str(matrix_scalar_multi(test_matrix_01,2)))
print('Should have been [[2,4,6],[8,10,12],[14,16,18]]')

# matrix_scalar_multi(test_matrix_01,3) should output [[3,6,9],[12,15,18],[21,24,27]]
print('Problem2:Test Output for matrix_scalar_multi: ' + str(matrix_scalar_multi(test_matrix_01,3)))
print('Should have been [[3,6,9],[12,15,18],[21,24,27]]')

#Problem 03

def add_matrices(matrix_a: "list[list[float]]", matrix_b: "list[list[float]]"):
  """Adds the two input matrices.

    Creates a result matrix stored as an empty list. Using our function #0, we 
    will add the components (vectors at each index) of each matrix at each 
    element "n" using a for loop running "n" times. Store these sums by 
    appending result vector. 

    Args:
        matrix_a: A matrix stored as a list of column vectors.
        matrix_b: A matrix stored as a list of column vectors.

    Returns:
       The sum of the input matrices stored as a new result list. 
    """
  result: "list[list[float]]"= []
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

def matrix_vector_multi(matrix: "list[list[float]]", vector: "list[float]"):
  """Multiplies a matrix by a vector.

    The number of columns of matrix must equal the number of components in our 
    vector. If that condition is satisfied, we can set it up as a linear 
    combination of A*x = A[1]*x[1] + A[2]*x[2] + ... A[n]*x[n]. Now we see that
    we can just a run a for loop for scalar vector multiplication defined from 
    Problem 1 (store these in another matrix_r) and use Problem zero to add up 
    the resulting vectors into our newnresult matrix. The only thing is we 
    can't add the vectors all at once, so we will have to do it two vector 
    additions at a time. 


    Args:
        matrix: A matrix stored as a column of lists. 
        vector: A vector containing the same amount of elements 

    Returns:
       The multiplication of the input matrix and a vector stored as a new 
       matrix as result. 
    """
  matrix_r: "list[list[float]]" = [0 for element in matrix]
  result: "list[float]"= [0]
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

def matrix_matrix_multi(matrix_1: "list[list[float]]", matrix_2: "list[list[float]]"):
  """Multiplies a matrix by another matrix.

    We will create an empty result list and store the sums of the columns 
    (using the linear-combination matrix multiplication method) using Problem 4
    Instead the vector will be the components of our second matrix and simply 
    store results each as their own index (column of vectors) list in the 
    result matrix. 

    Args:
        matrix_1: A matrix stored as a column of lists. 
        matrix_2: A matrix stored as a column of lists.  

    Returns:
       The multiplication of the input matrices stored as a new 
       matrix as result. 
    """
  result: "list[list[float]]" = []
  for index in range(len(matrix_1)):
    result.append(matrix_vector_multi(matrix_1, matrix_2[index]))
  return result

# matrix_matrix_multi(test_matrix_01,test_matrix_02) should output [[48,63,78],[115,143,171],[295,368,441]]
print('Problem 5:Test Output for matrix_matrix_multi: ' + str(matrix_matrix_multi(test_matrix_01,test_matrix_02)))
print('Should have been [[48,63,78],[115,143,171],[295,368,441]]')

# matrix_matrix_multi(test_matrix_01,test_matrix_03) should output [[12,15,18],[24,30,36],[36,45,54]]
print('Problem 5:Test Output for matrix_matrix_multi: ' + str(matrix_matrix_multi(test_matrix_01,test_matrix_03)))
print('Should have been [[12,15,18],[24,30,36],[36,45,54]]')