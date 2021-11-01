import LA



A = [[1,0,1],[2,1,0]]
"""([[(0.7071067811865475), 0, (0.7071067811865475)], [(0.5773502691896258), 
(0.5773502691896258), (-0.5773502691896258)]], [[1.4142135623730951, 0], 
[(1.414213562373095+0j), (1.7320508075688776+0j)]])"""
B = [[1,0,1],[2,1,0],[4,2,1]]
"""([[(0.7071067811865475), 0, (0.7071067811865475)], [(0.5773502691896258), 
(0.5773502691896258), (-0.5773502691896258)], [0.408,0.816,-0.408]], [[1.4142135623730951, 0, 0], 
[(1.414213562373095), (1.7320508075688776), 0],[3.54, 2.89, 0.408]])"""
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
        V[inner_index] = LA.add_vectors(V[inner_index],LA.vector_scalar_multi(Q[index],-R[index][index]))

    return(Q,R,V)

print(gram_schmidt(A))

print(gram_schmidt(B))
