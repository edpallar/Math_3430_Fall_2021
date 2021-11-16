import LA 


def gram_schmidt(matrix):
    """Algorithm for an unstable gram-schmidt for reduced QR factorization
    
    This program starts by setting up the three lists where we will store values. Q and R are the matrices we want to end up with, and V is just a copy of A that we want to manipulate and edit as we go through the code. The for loop with index and inner_index work as two different for loops to assess different elements of the input matrix. The inner_index will begin working on the next element of A to store in V, which is needed to compute the values of Q and R. We find the 2-norm of V to store in R, and then use that value to normalize V and store in Q. The code then uses the inner product of Q and V to find the next value of R. It then uses that new R value to update the next column of V by the equation V = V -Q*R for each index. 

    Args: 
        Matrix: matrices will be stored as lists of lists where each
        component list represents a column of the matrix 

    Returns: 
        A list of two matrices, Q and R. 
    """
    Q = []
    for element in matrix:
      Q.append(element)
    Q = LA.matrix_scalar_multi(Q,0)
    # make V 
    V = []
    for element in matrix:
      V.append(element)

    # make R
    R = []
    for element in matrix:
      R.append([0 for index in range(len(matrix))])
    
    
    for index in range(len(matrix)):
      R[index][index]= LA.p_norm(V[index],2,False)
      
      Q[index] = LA.vector_scalar_multi(V[index], 1/R[index][index])
      
      for inner_index in range(index + 1,len(matrix)):
        R[inner_index][index] = LA.inner_product(Q[index],V[inner_index])
        V[inner_index] = LA.add_vectors(V[inner_index],LA.vector_scalar_multi(Q[index],-R[inner_index][index]))

    return[Q,R]

def orthonormal(matrix):
  """Finds the orthonormal of a set of vectors (a matrix). 

  Since Q is a set of orthonormal vectors in the gram_schimdt program, we can just return Q by returning the 0th element (first one) of the gram_schmidt program. 

  Args:
    matrix: a list of vectors 
  Returns: 
    Q: a matrix of orthonormal vectors from the input vectors 
  """
  result = gram_schmidt(matrix)[0]
  return result 



def conjugate_transpose_1(vector):
  """ Finds the conjugate of a vector 
  
Runs through each element of the vector and calculates conjugate at each step. 

  Args:
      vector: A list  

  Returns:
      vector: A list of conjugate outputs from the vector input 
  """
  result = []
  for index in range(len(vector)):
    result.append(LA.conjugate(vector[index]))
  return result

def transpose(matrix):
  """Finds the transpose of a given matrix 
  
By fixing the for loop across the first column, index runs through the elements of the row and appends them to temp. Once it is done with a row, it appends temp to result, then
resets temp to be empty. 

  Args:
      matrix: A list of lists 

  Returns:
      matrix: A list of lists that is the tranpose of the input. 
  """
  result = []
  for index in range(len(matrix[0])):
    temp = []
    for element in matrix:
      temp.append(element[index])
    result.append(temp)
  return result 

def conjugate_transpose(matrix):
  """Finds the conjugate transpose of aa matrix.
  
  Using the conjugate function to first find the conjugates of each element of the given matrix. Then, use the transpose function to tranpose the matrix. 

  Args:
      matrix: A list of lists 

  Returns:
      matrix: A list of lists that is now the conjugate tranpose of the input.  
  """
  #conjugate entire matrix first 
  result = []
  for index in range(len(matrix)):
    result.append(conjugate_transpose_1(matrix[index]))
  #tranpose matrix 
  result = transpose(result)
  return result 


def basis_vec_builder(int):
  """Gives a basis vector of a specified size 
  
  Function creates a basis vector where the first element is 1 and the int input represents the number of rows and the number of 0's being added (int-1)
  Args:
      int: represents the number of rows in the vector 

  Returns:
      vector: The basis vector 
  """
  result = [1]
  for index in range(1,int):
    result.append(0)
  return result 

def identity_builder(size):
  """Creates a square indentity matrix of a certain input size. 
  
  The function sets up the size first by placing 0 in every spot. Then goes through the diagonal and replaces the 0 with a 1. 

  Args:
      size: an interger specificying the size of the matrix output

  Returns:
      matrix: Outputs a square identity matrix where the diagnol is made of 1's. 
  """
  result = []
  for r in range(0,size):
    result.append([0 for r in range(0,size)])

  for index in range(len(result)):
    result[index][index] = 1
  return result 

def diag_vec(matrix):
  """Returns the vector below the diagonal of the input matrix. 

  It runs two for loops to index through each column and starts at the diagonal and adds the elements below that element. Runs through until i gets to the last element of the diagonal. 

  Args:
      matrix: a list of columns 

  Returns:
      matrix: A list of diag vecs according to their position in the orignal matrix
  """
  result = []
  for index in range(len(matrix)):
    result.append(matrix[index][index:])
  return result

  
def v_builder(matrix, column_number):
  """Give the vector v needed for building F_builder
  
  Adds the two vectors where the first is the multiplication of the 2-norm of the retreived diag_vec and the basis vector. The second vector is just the retrieved diag_vec. 
  

  Args:
      matrix: A matrix of lists of column vectors 
      column_number: an integer that specifies which column of the matrix we are retrieving 

  Returns:
      resul: a vector that will be used in the F_builder function. 
      
  """
  #v=||diag_vec||*e + diag_vec  
  vec = diag_vec(matrix)[column_number]
  print(vec,"vec")
  v = LA.p_norm(vec,2, False)
  print(v,"v")
  result = LA.add_vectors(LA.vector_scalar_multi(basis_vec_builder(len(vec)),v), vec)
  return result 

A = [[1,0,1],[2,1,0]]
print(v_builder(A,0), "v_builder")

def F_builder(vector):
  """This function returns the matrix F needed to build Q. 
  
  By using the v_builder function to access the necessary v for each iteration of F, we use the following equation to find F. 
  F (for every column of A denoted by k)= I - 2* ((v*conjugate_tranpose(v))/(inner_product(v)))

  Args:
      vector: It will take in v from v_builder, which accesses our necessary input matrix. 

  Returns:
      matrix: Returns a matrix of the built F from the input vector v.
  """
  iden = identity_builder(len(vector))
  print(iden,"iden")
  two = 2/(LA.inner_product(vector,vector))
  print(two,"two")
  cv = LA.matrix_matrix_multi([vector],conjugate_transpose([vector]))
  print(cv,"cv")
  
  result = LA.add_matrices(iden,-LA.matrix_scalar_multi(cv,two))
  print(result)
  return result 
  # F (for every column of A denoted by k)= I - 2* ((v*conjugate_tranpose(v))/(inner_product(v)))

print(F_builder(v_builder(A,0)))

def householder(matrix):
  """Gives the householder full QR factorization of a given matrix. 
  
  

  Args:
      matrix ([type]): [description]

  Returns:
      [type]: [description]
  """
  R = []
  for element in matrix:
    R.append(element) 
  Q_list = []
  Q = []
  for index in range(len(matrix)-1):
    #build Q here 
    #append Q to Q_list
    R = LA.matrix_matrix_multi(Q[index],R)
  Q = conjugate_transpose(Q[1])
  for index in range(len(Q_list)):
    Q = LA.matrix_matrix_multi(Q,conjugate_transpose(Q_list[index]))
  return [Q,R]
  