import LA


def unstable_gram_schmidt(matrix: list) -> list:
    """Algorithm for an unstable gram-schmidt for reduced QR factorization

        This program starts by setting up the three lists where we will store values. Q and R are the matrices we want to end up with, and V is just a copy of A that we want to manipulate and edit as we go through the code. The for loop with index and inner_index work as two different for loops to assess different elements of the input matrix. The inner_index will begin working on the next element of A to store in V, which is needed to compute the values of Q and R. This is different from the stable version as we don't find the 2-norm of V first. The code first stores the values of R and V and then takes the 2-norm of each element of R to make Q at the end.  

    Args:
        A: A matrix, will be stored as lists of lists where each component list represents a column of the matrix 
    Returns: 
        A list of two matrices, Q and R. 
    """
    Q: list = []
    for element in matrix:
      Q.append(element)
    Q = LA.matrix_scalar_multi(Q,0)
    

    # make R
    R: list = []
    for element in matrix:
      R.append([0 for index in range(len(matrix))])
    # make V 
    V: list = []
    # according to the notes, j should run from (1,n+1) and k runs from (1,j)
    for index in range(len(matrix)):
      # copy A onto V then edit later 
      V.append(element)
      for inner_index in range(1,index):
        # conjugate of q muliplied by a = r
        R[inner_index][index] = LA.inner_product(Q[inner_index],V[index])
        # v =v - r(above output)*q
        V[inner_index] = LA.add_vectors(V[inner_index],LA.vector_scalar_multi(Q[index],-R[inner_index][index]))
      # find the 2-norm of diagnol of R 
      R[index][index]= LA.p_norm(V[index],2,False)
      # normalized vectors of v put into Q
      Q[index] = LA.vector_scalar_multi(V[index], 1/R[index][index])
    return[Q,R]
    
    


def gram_schmidt(matrix:list) -> list:
    """Algorithm for an unstable gram-schmidt for reduced QR factorization
    
    This program starts by setting up the three lists where we will store values. Q and R are the matrices we want to end up with, and V is just a copy of A that we want to manipulate and edit as we go through the code. The for loop with index and inner_index work as two different for loops to assess different elements of the input matrix. The inner_index will begin working on the next element of A to store in V, which is needed to compute the values of Q and R. We find the 2-norm of V to store in R, and then use that value to normalize V and store in Q. The code then uses the inner product of Q and V to find the next value of R. It then uses that new R value to update the next column of V by the equation V = V -Q*R for each index. 

    Args: 
        Matrix: matrices will be stored as lists of lists where each
        component list represents a column of the matrix 

    Returns: 
        A list of two matrices, Q and R. 
    """
    Q: list = []
    for element in matrix:
      Q.append(element)
    Q = LA.matrix_scalar_multi(Q,0)
    # make V 
    V: list = []
    for element in matrix:
      V.append(element)

    # make R
    R: list = []
    for element in matrix:
      R.append([0 for index in range(len(matrix))])
    
    
    for index in range(len(matrix)):
      R[index][index]= LA.p_norm(V[index],2,False)
      
      Q[index] = LA.vector_scalar_multi(V[index], 1/R[index][index])
      
      
      for inner_index in range(index + 1,len(matrix)):
        R[inner_index][index] = LA.inner_product(Q[index],V[inner_index])
        V[inner_index] = LA.add_vectors(V[inner_index],LA.vector_scalar_multi(Q[index],-R[inner_index][index]))

    return[Q,R]
