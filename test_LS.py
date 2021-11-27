import LS
import pytest

matrix_alpha = [[2,0,0],[4,4,0],[3,1,6]]
vec_a = [9,5,6]
matrix_beta = [[2,0,0],[1,6,0],[1,2,8]]
vec_b = [8,14,8]

def test_back_sub():
    assert LS.back_sub(matrix_alpha,vec_a) == [1,1,1]
    assert LS.back_sub(matrix_beta,vec_b) == [3,2,1]

def test_least_squares():
    assert LS.least_squares(matrix_beta,vec_b) == [3,2,1]
    assert LS.least_squares(matrix_alpha,vec_a) == [1,1,1]

