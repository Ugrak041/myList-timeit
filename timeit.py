import numpy as np
def createList(size):
  myList=[]
    for i in range(size):
      myList.append(i)
    return myList
def listIncrement(l,n):
  myL=[]
  for i in range(len(l)):
      #l[i]=l[i]+n
      l[i]=l[i]+n
  return myL
L_1=createList(5)
L_1
L_2=listIncrement(L_1,5)
L_2

%timeit myL_1=listIncrement(createList(9000000),50)

%timeit np.arange(9000000)+1

size=10
my_10=np.arange(size)
my_10

#myList={0,1,2,3,4,5}
#myList+1
myL_1=createList(5)
myL_1
my_10+1

%timeit myL_1=createList(500)

myL_20=createList(5)
myL_30=listIncrement(myL_20,5)
myL_20,myL_30
