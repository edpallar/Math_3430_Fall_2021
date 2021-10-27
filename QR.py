import LA



A = [[1,0,1],[2,1,0]]
def unstable_gram_schmidt(A: list) -> list: 
    """Algorithm for an unstable gram-schmidt for reduced QR factorization

    How? 

    Args:
        A: A matrix, will be stored as lists of lists where each component list represents a column of the matrix 
    Returns: 
        A list of two matrices, Q and R. 
    """
    
    


def gram_schmidt(matrix: list) -> list: 
    """Algorithm for an unstable gram-schmidt for reduced QR factorization
    
    How? 

    Args: 
        Matrix: matrices will be stored as lists of lists where each
        component list represents a column of the matrix 

    Returns: 
        A list of two matrices, Q and R. 
    """
    # make copy of A for Q where Q is A*0 
    Q: list = []
    for element in A:
      Q.append(element)
    Q = LA.matrix_scalar_multi(Q,0)
    # make V 
    V: list = []
    for element in A:
      V.append(element)
    # make R 
    for element in A:
      R: list = [0 for element in A]
    

    return(Q,R)

print(gram_schmidt(A))
