import LA



A = [[1,0,1],[2,1,0]]
def unstable_gram_schmidt(A ) : 
    """Algorithm for an unstable gram-schmidt for reduced QR factorization

    How? 

    Args:
        A: A matrix, will be stored as lists of lists where each component list represents a column of the matrix 
    Returns: 
        A list of two matrices, Q and R. 
    """
    
    


def gram_schmidt(matrix):
    """Algorithm for an unstable gram-schmidt for reduced QR factorization
    
    How? 

    Args: 
        Matrix: matrices will be stored as lists of lists where each
        component list represents a column of the matrix 

    Returns: 
        A list of two matrices, Q and R. 
    """
    # make copy of A for Q where Q is A*0 
    Q = []
    for element in A:
      Q.append(element)
    Q = LA.matrix_scalar_multi(Q,0)
    # make V 
    V = []
    for element in A:
      V.append(element)

    # make R
    R = []
    for element in A:
      R.append([0 for index in range(len(A))])
    
    
    for index in range(len(A)):
      R[index][index]= LA.p_norm(V[index],2,False)
      
      Q[index] = LA.vector_scalar_multi(V[index], 1/R[index][index])
      
      
      for inner_index in range(1,len(A)):
        R[inner_index][index] = LA.inner_product(Q[index],V[inner_index])
        V[inner_index] = LA.add_vectors(V[inner_index],LA.vector_scalar_multi(Q[index],-R[index][index]))

    return(Q,R,V)

print(gram_schmidt(A))
