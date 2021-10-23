import LA 
import pytest


#global test inputs 
test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
test_vector_03 = [3, 6, 9]

test_matrix_01 = [[1,2,3],[4,5,6],[7,8,9]]
test_matrix_02 = [[8,3,4],[6,15,7],[0,72,1]] 
test_matrix_03 = [[1,1,1],[2,2,2],[3,3,3]]

# Problem #0

def test_add_vectors(): 
    # add_vectors(test_vector_01,test_vector_02) should output [4,3,6]
    assert LA.add_vectors(test_vector_01,test_vector_02) == [4,3,6]
    # add_vectors(test_vector_01, test_vector_03) should ouput [4,8,13]
    assert LA.add_vectors(test_vector_01,test_vector_03) == [4,8,13]

#Problem 01

def test_vector_scalar_multi():
    assert LA.vector_scalar_multi(test_vector_01,2) == [2,4,8]
    assert LA.vector_scalar_multi(test_vector_03,2) == [6,12,18]



#Problem 02

def test_matrix_scalar_multi():
    assert LA.matrix_scalar_multi(test_matrix_01,2) == [[2,4,6],[8,10,12],[14,16,18]]
    assert LA.matrix_scalar_multi(test_matrix_01,3) == [[3,6,9],[12,15,18],[21,24,27]]
  

#Problem 03

def test_add_matrices():
    assert LA.add_matrices(test_matrix_01,test_matrix_02) == [[9,5,7],[10,20,13],[7,80,10]]
    assert LA.add_matrices(test_matrix_01, test_matrix_03) == [[2,3,4],[6,7,8],[10,11,12]]
  

#Problem 04

def test_matrix_vector_multi():
    assert LA.matrix_vector_multi(test_matrix_01,test_vector_01) == [37,44,51]
    assert LA.matrix_vector_multi(test_matrix_01, test_vector_02) == [21,27,33]


#Problem 05

def test_matrix_matrix_multi():
    assert LA.matrix_matrix_multi(test_matrix_01,test_matrix_02) == [[48,63,78],[115,143,171],[295,368,441]]
    assert LA.matrix_matrix_multi(test_matrix_01, test_matrix_03) == [[12,15,18],[24,30,36],[36,45,54]]

#HW04 Problems: 

#test inputs 
a = 2-2j 
b = 3
c = 3 + 3j 

vector_a = [2, 3+3j, -5-5j]
vector_b = [2,3,-5]
vector_c = [1,2,2-2j]
vector_d = [1,3,3-3j]

def test_conjugate():
    assert LA.conjugate(a) == 2+2j 
    assert LA.conjugate(b) == 3 

def test_absolute_value():
    assert LA.absolute_value(c) == (18)**(1/2)
    assert LA.absolute_value(a) == (8)**(1/2)

def test_p_norm_finite():
    assert LA.p_norm_finite(vector_b) == (38)**(1/2)
    assert LA.p_norm_finite(vector_b,3) == (160)**(1/2)

def test_inf_norm():
    assert LA.inf_norm(vector_a) == (50)**(1/2)
    assert LA.inf_norm(vector_b) == (5)

def test_p_norm():
    assert LA.p_norm(vector_b) == (38)**(1/2)
    assert LA.p_norm(vector_a, inf = True) == (50)**(1/2)

def test_inner_product():
    assert LA.inner_product(vector_c, vector_d) == 19
    assert LA.inner_product(vector_a, vector_b) == (38-34j)
