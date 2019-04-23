from threading import Timer
from time import sleep


def time_sort(array):
    threads=[]
    sorted_array = []
    for elem in array:
        thread=Timer(elem, lambda x: sorted_array.append(x), args=(elem,))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()
    return sorted_array

#print(time_sort([5,4,3,2,1]))
print(time_sort([3,2,1,4,5]))
