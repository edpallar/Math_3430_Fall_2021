
import LA 
import QR



def back_sub(matrix: list , vector: list) -> list:
    """
    Performs backsubstitution to compute the solution to a given matrix and vector. 

    This function does this by first initializing the result vector to be the same size as the input vector. Then solves for the last element of the result using the last element of the input vector and and the last element of the last column of the input matrix. Then using a for loop, subtracts the elements of the matrix from the corresponding vector index until it reaches the diagonal. Finally, the last loop goes and divides the vector element by the matrix diagonal element as stores it as the result element for that given row. 

    Arguments:
        matrix: a list of column vectors that is an upper-triangular matrix
        vector: a list of floats 
    Returns: 
        result: a vector containing the solution to Ax=b where A is the input matrix and b is the input vector 
    """
  # initiliaze result to be the same size as vector 
    for i in range(len(vector)):
        result: list = [0 for i in vector]
  #solve for the last element of result 
    result[-1] = vector[-1]*(1/matrix[-1][-1])
  # subtract the elements of the matrix from vector
    for index in range(2,len(matrix)+1):
        for sub in range(1,index):
            vector[-index] = vector[-index]-matrix[-sub][-index]
  # divide elements of vector by diagonal element of matrix to equal the result element by going backwards 
    for index in range(2,len(matrix)+1):
        result[-index] = vector[-index]*(1/matrix[-index][-index])
    return result 

def least_squares(matrix:list , vector:list)-> list:
  """
  Performs the least squares operation on a given matrix and vector. 

  We are trying to minimize ||Ax-b||, essentially findind a solution x such that it equals 0. Since we know that A = QR from gram_schmidt, we use that principle here to convert it to Rx = (Q^*)(b). We start by assigning Q and R to different variables, m and r, respectively. Then setting up the vector to be the conjugate transpose of Q times the input vector, we simply use the back sub function to solve rx=v where v = (Q^*)(b)
  Arguments: 
        matrix: a list of column vectors that is an upper-triangular matrix
        vector: a list of floats
  Returns: 
        result: a vector solution to the input matrix A and vector b. 

  """
  # return the Q from reduced QR factorization 
  m:list = QR.gram_schmidt(matrix)[0]
  r:list = QR.gram_schmidt(matrix)[1]
  # set v as the multiplication of Q^* and our input vector
  v:list = LA.matrix_vector_multi(QR.conjugate_transpose(m),vector)
  # perform back sub with "A" = r and "b" = v
  result = back_sub(r,v)
  # return result 
  return result 

