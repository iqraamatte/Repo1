import time
import tracemalloc
import matplotlib.pyplot as plt
def linearSearch(array,x,n):
  for i in range (0,n):
    if (array[i]==x):
     return i
    return -1

print("Enter Array:")
array=[int(b) for b in input().split()]
x=eval(input("Enter the search element:"))

n=len(array)
elements=array
times=array
start=time.process_time()
tracemalloc.start()
result=linearSearch(array,x,n)
end=time.process_time()
print("Space required =",tracemalloc.get_traced_memory())
print("time required =",(end-start))
tracemalloc.stop()
if(result == -1):
    print("elements not found")
else:
    print("elements found at index:",result)
    elements.append(len(array))
    times.append(end-start)
    plt.xlabel('list length')
    plt.ylabel('time required')
    plt.plot(elements,times,label='Linear Search')
    plt.grid()
    plt.legend()
    plt.show()