# -*-coding: utf-8 -*-
# 2018112024 강지영

import random

A=[];

for i in range(10):
    # 1 ~ 100000까지 난수 생성
    num = random.randrange(1, 100000)
    while num in A : # 중복될 경우        
        num = random.randrange(1, 100000) # 다시 난수 생성    
    A.append(num) # 중복 되지 않은 경우만 추가

def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]
  
    for j in range(l , h):
        if arr[j] > x:
            # i를 1 증가시키고 arr[i]와 arr[j]를 swap
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
  
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)
  
def quick_sort(arr,l,h):
  
    # stack 생성
    stack = [0,0,0,0,0,0,0,0,0,0,0]
  
    # stck의 top 초기화
    top = -1
  
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
  
    # stack이 비어있지 않은 동안 반복
    while top >= 0:
  
        # stack에서 pop
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
  
        # pivot을 기준으로 partition
        pv = partition(arr, l, h)
  
        # pivot의 왼쪽에 원소가 2개 이상 있을 경우
        # stack에 push
        if pv-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = pv - 1
  
        # pivot의 오른쪽에 원소가 2개 이상 있을 경우
        # stack에 push
        if pv+1 < h:
            top = top + 1
            stack[top] = pv + 1
            top = top + 1
            stack[top] = h
    
        print(arr)

print("Unsorted Array:",A)
quick_sort(A,0,len(A)-1)
print("sorted Array:",A)
