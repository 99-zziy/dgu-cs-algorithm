# -*-coding: utf-8 -*-
# 2018112024 강지영

import random

A=[];

for i in range(100):
    # 1 ~ 500까지 난수 생성
    num = random.randrange(1, 500)
    while num in A : # 중복될 경우        
        num = random.randrange(1, 500) # 다시 난수 생성    
    A.append(num) # 중복 되지 않은 경우만 추가

print("Unsorted array: ", A) # 랜덤하게 생성한 100개 숫자
print("")

def selection_sort(arr):
    # 배열의 길이만큼 반복문 실행
    for i in range(len(arr)):
        # 가장 작은 값의 인덱스를 저장할 변수에 i를 초기화
        min_idx = i
        for j in range(i + 1, len(arr)):
            # 만약 가장 작은 값이 다음 값보다 크다면
            if arr[min_idx] > arr[j]:
                min_idx = j # 가장 작은 값의 인덱스 값을 변경

        # swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # 정렬 되는 과정 몇줄만 출력
        if i % 10 == 0:
            print(arr)
            print("")
    print("Sorted array: ", arr) # 오름차순으로 정렬된 100개의 숫자

selection_sort(A)
