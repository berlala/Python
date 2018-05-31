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

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here [done]
        if self.h ==1:
            Det = self[0]       
        if self.h ==2:
            Det = self[0][0]*self[1][1] - self[0][1]*self[1][0]
        print('the determinant is' +str(Det))    
        return Det 
    
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here [done]
        Tra = 0
        for i in range(self.h):
                Tra = Tra + self[i][i]
        print('the trace is' +str(Tra))
        return Tra
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inv = zeroes(self.h,self.w)
        if self.h ==1:
            inv[0][0] = 1/self[0][0]
        if self.h ==2: #only work for 2*2           
            pA = 1/int(self[0][0]*self[1][1]-self[1][0]*self[0][1])
            inv[0][0] = self[1][1]
            inv[0][1] = -self[0][1]
            inv[1][0] = -self[1][0]
            inv[1][1] = self[0][0]
            inv = pA*inv
       # print('the final inverse is' +str(inv))            
        return inv  

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here[done]
        M = zeroes(self.w,self.h) # change from h w to w h on 5/21
        if self.h==1:
            for k in range(self.w):
                M[k][0] = self[0][k]
        if self.w==1:
             for k in range(self.h):
                M[0][k] = self[k][0]            
        if self.h>1 and self.w>1:    
            for i in range(self.w):
                for j in range(self.h):
                    M[i][j] = self[j][i]
        return M
    
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

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here[done]
        #
        addt = zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                addt[i][j] = self[i][j] + other[i][j] 
        #print("the add result is")    
       # print(addt)
        return addt

    def __neg__(self):
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
        # TODO - your code here[done]
        #
        neg = zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                neg[i][j] = -1*self[i][j]
        return neg       

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here[done]
        #
        sub = zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                sub[i][j] = self[i][j] - other[i][j]
        return sub

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here[done]
        #
        mul = zeroes(self.h,other.w)
        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                    mul[i][j] += self[i][k] * other[k][j]
        return mul

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        #[done]
        rmul = zeroes(self.h,self.w)
        if isinstance(other, numbers.Number):
            pass           
 
            for i in range(self.h):
                for j in range(self.w):
                    rmul[i][j] = other * self[i][j]
               # print('the rmul 2 is' +str(rmul))                 
        return rmul
            
            