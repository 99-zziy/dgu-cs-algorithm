# -*-coding: utf-8 -*-
# 2018112024 강지영


A=[30,20,40,10,5,10,30,15];
n = len(A) - 1;

def bubble_sort(arr,n):
    for i in range(n):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(arr)
 
    if n-1 > 1:   
        bubble_sort(arr,n-1)
    
    if n-1 == 1:
        print("Sorted array: ", arr)

bubble_sort(A,n)

