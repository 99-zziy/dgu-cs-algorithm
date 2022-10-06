# -*-coding: utf-8 -*-
# 2018112024 강지영

import random

A=[];

def get_random_list():
    for i in range(1000):
        # 1 ~ 100000까지 난수 생성
        num = random.randrange(1, 100000)
        while num in A : # 중복될 경우        
            num = random.randrange(1, 100000) # 다시 난수 생성    
        A.append(num) # 중복 되지 않은 경우만 추가
    print("random number list",A)

def minimum(n): 
    min = A[0]
    for i in range(1, n):
        if min > A[i]:
            min=A[i]
    print("min number",min)

def maximum(n): 
    max = A[0]
    for i in range(1, n):
        if max < A[i]:
            max=A[i]
    print("max number",max)

def find_min_max(n):
    min = A[0]
    max = A[0]
    for i in range(1,n-1,2):
        if A[i] < A[i+1]:
            small = A[i]
            large = A[i+1]
        else:
            large = A[i]
            small = A[i+1]
        if small < min: 
            min = small
        if large > max:
            max = large
    print("min number",min,"max number",max)



get_random_list()
minimum(1000)
maximum(1000)
find_min_max(1000)

