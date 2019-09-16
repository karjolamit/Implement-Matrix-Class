import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def dot_product(vector_one, vector_two):                        #Dot product of 2 vectors
    result = 0
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]
    return result

def get_row(matrix, row):                                       #Access row of defined matrix
    return matrix[row]
    
def get_column(matrix, column_number):                          #Access column of defined matrix 
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])
    return column

class Matrix(object):                                           #Create class matrix

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)                                      # number of rows
        self.w = len(grid[0])                                   # number of columns

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):                                       #Create a determinant function
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():                                 #Check for square matrix and size not > 2x2
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h==1:                                            #determinant value for 1x1 matrix 
            det_mat=self.g[0][0]
        elif self.h==2:                                          #determinant value for 2x2 matrix
            det_mat = self.g[0][0]*self.g[1][1]-self.g[0][1]*self.g[1][0]
        return det_mat

    def trace(self):                                             #Create a trace function
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():                                 #Check for square matrix 
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        sum=0                                                
        for i in range(self.h):                                  #for loop to get sum of diag elements
            sum = sum + self.g[i][i]
        return sum
            

    def inverse(self):                                           #Create a determinant function
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():                                 #Check for square matrix and size not > 2x2
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inv = zeroes( self.h, self.w )                           #Initializing 
        
        if self.h == 1:                                          #Inverse value for 1x1 matrix 
            inv[0][0]= 1 / self.determinant()
            return inv
        elif self.h == 2:                                        #Check for invertibility of 2x2 matrix
            if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
                raise ValueError('The matrix is not invertible.')
            else:                                                #Inverse value for 2x2 matrix 
                factor = 1 / self.determinant()
                inv[0][1] = -self.g[0][1] * factor
                inv[1][0] = -self.g[1][0] * factor
                inv[1][1] = self.g[0][0] * factor
                inv[0][0] = self.g[1][1] * factor
            return inv

    def T(self):                                                 #Create a transpose function 
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = zeroes( self.w, self.h )              #Initializing 
        for i in range(self.w):                                  #For loop to access column and row elements
            for j in range(self.h):
                matrix_transpose.g[j][i] = self.g[i][j]
        return matrix_transpose

    def is_square(self):    
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):                                     #Create addition of two matrices function
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:               #Check if dimaensions of both matrices are same or not
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        # initialize matrix to hold the results
        matrixSum = []                                           #Initialize
        
        for i in range(self.h):                                  #For loop to add matrices
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] + other[i][j]) # add the matrices
            matrixSum.append(row)
        return Matrix(matrixSum)                                 #Use Matrix for getting output in matrix form

    def __neg__(self):                                           #Create a negation function of a matrix
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        mat = []                                                 #Initialize
        for i in range(self.h):                                  #Access rows
            mat_row = []
            for j in range(self.w):                              #Access columns
                mat_row.append(-1*self.g[i][j])                  #Apply negation to all elements
            mat.append(mat_row)
        return Matrix(mat)
                

    
    def __sub__(self, other):                                    #Create subtraction of two matrices function
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        # initialize matrix to hold the results
        matrixNeg = []                                           #Initialize
        
        for i in range(self.h):                                  #For loop to subtract matrices
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] - other[i][j]) # add the matrices
            matrixNeg.append(row)
        return Matrix(matrixNeg)

    def __mul__(self, other):                                    #Create a matrix multiplication function
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        ### Store the number of rows in A and the number
        ###       of columns in B. This will be the size of the output
        ###       matrix
        
        m_rows = len(self.g)
        p_columns = len(other[0])
        
        result = []                                             #Dimension is m_rows X p_columns
        
        for i in range(m_rows):
            row = []
            rowA = self.g[i]
            for j in range(p_columns):               
                row.append(dot_product(get_row(self.g,i),get_column(other.g,j))) #Calculates dot product of row and column elements 
            result.append(row)
        return Matrix(result)
        

    def __rmul__(self, other):                                  #Create a scalar multiplication function
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):                   #Checks if other is a scalar
            pass
            #   
            # TODO - your code here
            #
            mat = []                                            #Initialize
            for i in range(self.h):                             #For loop to calculate scalar multiplictaion
                mat_row = []
                for j in range(self.w):
                    mat_row.append(other*self.g[i][j])
                mat.append(mat_row)
            return Matrix(mat)         
