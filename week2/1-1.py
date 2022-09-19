# -*-coding: utf-8 -*-
# 2018112024 강지영


A=[30,20,40,10,5,10,30,15];

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)

    print("Sorted array: ", arr)
    

bubble_sort(A)


