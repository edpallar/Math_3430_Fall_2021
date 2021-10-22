"""
This assignment is due by 11:59pm on 10/22/2021. 

For this assignment you will be adding functinos to the LA.py script from HW03.
All functions must satisfy the same requirements as in HW03. The functions you
will need to add are

#1) A function which takes a scalar as it's input and returns it's absolute
value. Note that this function must be able to take both real numbers and
complex numbers as input!!!

#2) A function which takes the as it's arguments

1) A vector stored as a list.

2) A float valued scalar, set to default as 2. 

and returns the p-norm of the input vector. Which p-norm must be determined using
the float valued scalar input. If no argument is given, it should default to
2. 

#3) A function which takes as it's argument a vector stored as a list and
returns the infinity norm of the input vector.

#4) A function which takes as it's arguments

1) A vector stored as a list.

2) An float valued scalar, set to default as 2.

3) A boolean value, set to default as False.

The function will return the p-norm of the input vector. If the boolean value is
given as True, the function will return the infinity norm of the input vector.
Otherwise it will return the p-norm of the vector corresponding to the float 
scalar argument. This function must use the functions from problem #2 and
problem #3 to earn credit. 

#5) A function which takes as it's arguments two vectors, stored as lists. This
function then returns the inner product of these vectors. Your function must be
able to handle complex numbers!
"""
# write a function that conjugates an input before we start HW 04 
def conjugate(scalar: complex):
  """Gives the conjugate of a complex input
  
  We know that the conjugate of a+bj is a-bj and vice versa . Thus, we can just take the negative multiplication to cover both positive and negative cases. 

  Args: 
    scalar: input in the format of a complex number
  
  Returns:
    conjugate of input 
  """
  result: complex = scalar.real + -scalar.imag*1j
  
  return result 


# Problem 1 
def absolute_value(scalar: complex) -> float: 
  """Returns the absolute value of the scalar input, both real and complex. 

  We are formating in the complex form so that this function does both, for real the j portion is = 0. We are doing this by taking the square root of the multiplication of the input,z, and its conjugate. Then taking the square root of this multiplication will give the absolute value. 

  Args: 
    scalar: in the form of a + bj, where b can equal 0 in real number cases 
  Returns:
    the absolute value of the input, which is a float 
  """
  conjugate: complex = scalar.conjugate()
  result: float = scalar*conjugate 
  result = result**(1/2)
  return result 


# Problem 2 
def p_norm(vector: list, p: int = 2) -> float:
    """
    Computes the p norm of a vector. 
    Set result = 0. For each element of vector, takes absolute value and raises it to the pth power and then adds it to result. Takes pth root of result and then returns result. Defaults to the 2-norm. 

    Args:
        vector: a vector of real numbers, stored as a list 
        p: A positive integer, defaulted to 2. 
         
    Returns: 
    The p-norm of the input vector. 
     """
    result: float = 0  
    for element in vector: 
        if element < 0:
            result += (-element) **p
        else: 
            result += element **p 
    result = result**(1/p)
    return result 



# Problem 3 
def inf_norm(vector: list) -> float : 
  """Returns the infinity norm of a vector input 

  Finds the absolute value of each element of vector, and stores these values in result. We then go through result to find the max value in result to return the infinity norm. 

  Args: 
    vector: list of scalars 
  Returns:
    infinity norm of the vector 
  """
  result: list = [] 
  for index in range(len(vector)):
    result.append(absolute_value(vector[index]))
    print(result)
  return max(result)

vector_a = [2,3,-5]

# Problem 4 
def p_norm_boolean(vector:list, p: float = 2) -> float :
  """Gives the p norm of the input vector, or the inf if p == "inf"

  If p is an integer, gives the p norm using our p_norm function. If p is a string == "inf", will use our inf_norm function. 

  Args:
    vector: list of real numbers, stored as a list
    p: a scalar int or string of "inf"
  
  Returns:
    p norm of the vector input 
  """
  if p == "inf":
    print(inf_norm(vector))
  else: 
    print(p_norm(vector))

print(p_norm_boolean(vector_a,3))

"""
#Problem 5 
def inner_product(vector_1: list, vector_2: list) -> float: 
  Gives the inner product of two input vectors 

  Does this using vector multiplication of one times the conjugate of the other. We have a function for vector multiplication and we have a function for finding the transpose/conjugate of each component of the vector. We then just add the resulting multiplication values to output a scalar. 

  Args: 
    vector_1: vector of scalars, both real and complex 
    vector_2: vector of scalars, both real and complex 
  Returns: 
    float equal to the inner product 
  """


