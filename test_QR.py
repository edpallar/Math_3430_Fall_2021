import QR

import pytest

A = [[1,0,1],[2,1,0]]

B = [[1,0,1],[2,1,0],[4,2,1]]


def test_gram_schmidt():
    assert QR.gram_schmidt(A) == [[[1/(2**(1/2)),0, 1/(2**(1/2))],[1/(3**(1/2)), 1/(3**(1/2)), -1/(3**(1/2))]],[[1/(2**(1/2)), 0],[1/(2**(1/2)), 1/(3**(1/2))]]]
    assert QR.gram_schmidt(B) == [[[(1/(2**(1/2))), 0, (1/(2**(1/2)))], [(1/(3**(1/2))), 
(1/(3**(1/2))), (-1/(3**(1/2)))], [-0.408,0.816,0.408]], [[(2**(1/2)), 0, 0], 
[(1/(2**(1/2))), ((3**(1/2))), 0],[3.54, 2.89, 0.408]]]

def test_orthonormal():
    assert QR.orthonormal(A) == [[1/(2**(1/2)),0, 1/(2**(1/2))],[1/(3**(1/2)), 1/(3**(1/2)), -1/(3**(1/2))]]
    assert QR.orthonormal(B) == [[(1/(2**(1/2))), 0, (1/(2**(1/2)))], [(1/(3**(1/2))), (1/(3**(1/2))), (-1/(3**(1/2)))], [-0.408,0.816,0.408]]
