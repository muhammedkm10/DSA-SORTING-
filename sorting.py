def bubble_sort(list):
    for i in range(len(list) - 1 ,0 , -1):
        for j in range(i):
            if list[j] < list[j+1]:
                t = list[j]
                list[j] = list[j+1]
                list[j+1]= t



def insertion_sort(list):
    for index in range(1,len(list)):
        current = list[index]
        pos = index
        while current > list[pos - 1] and pos > 0:
            list[pos] = list[pos-1]
            pos = pos-1
        list[pos] = current


def selection(list):
    for i in range(len(list)):
        min_value  = min(list[i:])
        min_index = list.index(min_value)
        list[min_index],list[i] = list[i],list[min_index]

def selection1(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[min_index],list[i] = list[i],list[min_index]


def pivot_space(list,first,last):
    pivot = list[first]
    left = first+1
    right = last
    while True:
        while left <= right and list[left] <= pivot:
            left = left+1
        while left <= right and list[right] >= pivot:
            right = right -1
        if right > left:
            break
        else:
            list[left],list[right] = list[right],list[left]
    list[first],list[right] = list[right],list[first]
    return  right


def quick_sort(list,first,last):
    if first < last:
         p = pivot_space(list,first,last)
         quick_sort(list,first,p-1)
         quick_sort(list,p+1,last)


def merge(list):
    if len(list) >1:
        mid = len(list) // 2
        left_list  = list[:mid]
        right_list = list[mid:]

        merge(left_list)
        merge(right_list)


        i  = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if  left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i = i+1
                k = k+1
            else:
              list[k] = right_list[j]
              j  = j+1
              k = k+1
        while i < len(left_list):
            list[k] = left_list[i]
            i = i+1
            k = k+1
        while j < len(right_list):
            list[k] = right_list[j]
            j = j+1
            k = k+1

u = [9,8,7,6,4,3,2]
merge(u)
print(u)














p = [9,8,0]

bubble_sort(p)
insertion_sort(p)
selection1(p)
print(p)