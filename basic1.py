import numpy as np

a = np.arange(20).reshape(5,4)
print('--------------Basics of array-------------- \n','array','\n',a)
print('dimension',a.ndim, '\n''itemsize',a.itemsize,'\n''shape',a.shape,'\n',
      'dtype',a.dtype,'\n','data @',a.data,'\n','size',a.size)
print('has similar work as a.itemsize' ,a.dtype.itemsize,'\n-----------------------------' )

'''
--------------Basics of array-------------- 
 array 
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]]
dimension 2 
itemsize 4 
shape (5, 4) 
 dtype int32 
 data @ <memory at 0x000001AD70FE6A68> 
 size 20 
 has similar work as a.itemsize 4 
 -----------------------------
'''
print('-----Array creation---\n')
b = np.array([[3,4,5],[9,-1,0]],dtype= int)
print('2D Array integer\n',b)

c = np.array([[3,4,5],[9,-1,0]],dtype = complex )
print('2D Array complex\n',c)

x = np.array([[3,4,5],[9,-1,0]],dtype = float)
print('2D Array float\n',x)

'''
-----Array creation---

2D Array integer
 [[ 3  4  5]
 [ 9 -1  0]]
2D Array complex
 [[ 3.+0.j  4.+0.j  5.+0.j]
 [ 9.+0.j -1.+0.j  0.+0.j]]
2D Array float
 [[ 3.  4.  5.]
 [ 9. -1.  0.]]

'''

a = np.zeros((4,5),dtype= complex,order = 'C')
b = np.ones((2,3,5),dtype= np.int64,order ='F')
c= np.empty((2,4,5),dtype= np.int32,order ='F')
print('null marix-complex\n\n',a,'\nideantity matrix\n\n',b,'\nrandom element array\n\n',c)

'''
null marix-complex

 [[0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
 [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]] 
ideantity matrix

 [[[1 1 1 1 1]
  [1 1 1 1 1]
  [1 1 1 1 1]]

 [[1 1 1 1 1]
  [1 1 1 1 1]
  [1 1 1 1 1]]] 
random element array

 [[[-646932816    6029426    6619239    6029415    6881399]
  [-647078016    6029410    7667822    7209065    7143521]
  [   7798885    6619252    6029433    6226015    3014708]
  [   7077999    6488161    7602291    3342448        100]]

 [[       301    6881388    6029427    6226015    6226030]
  [       301    6881395    7340141    7602281    3539044]
  [   6684704    7340077    6619252    6488110    7929968]
  [   6619236    6357099    7209065    2949175        301]]]

'''



