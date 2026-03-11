#1)
from array import array 
arr=array('i',[10,20,30,40,50])
print(len(arr))

#2)
arr = array('i',[10,20,30,40,50])
arr.append(40)
print(len(arr))

#3)
arr = array('i',[10,20,40])
arr.insert(2,30)
print(arr)

#4)
arr = array('i',[10,20,40])
arr.remove(20)
print(arr)

#5)
arr = [10, 20, 40]

arr.insert(2, 30)
print(arr)

#6)
arr = [10, 20, 30, 40]

arr.remove(30)
print(arr)

#7)
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)   
print(a * b)

#8)
arr = [10,20,30,40,50]

print(arr[1:4])   