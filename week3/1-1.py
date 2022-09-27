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

def quick_sort(arr, start, end):
    # 원소가 1개인 경우 함수 종료
    if start >= end: 
        return
    # 첫 번째 원소를 피벗으로 설정
    pv = start
    # 좌측 리스트 시작점
    left = start + 1
    # 우측 리스트 시작점
    right = end
    

    while left <= right:
        # 피벗보다 작은 값을 찾을 때까지 반복
        while left <= end and arr[left] >= arr[pv]:
            left += 1 
        # 피벗보다 큰 값을 찾을 때까지 반복
        while right > start and arr[right] <= arr[pv]:
            right -= 1
        
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            arr[right], arr[pv] = arr[pv], arr[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            arr[left], arr[right] = arr[right], arr[left]


    print(arr)
    # 좌측과 우측 리스트 각각에 대해 동일한 방식으로 퀵 정렬을 수행
    quick_sort(arr, 0, right -1)
    quick_sort(arr, right + 1, end) 

print("Unsorted Array:",A)
quick_sort(A, 0, len(A)-1)
print("sorted Array:",A)