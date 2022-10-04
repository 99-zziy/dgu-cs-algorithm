# -*-coding: utf-8 -*-
# 2018112024 강지영

A = [4,1,3,2,16,9,10,14,8,7]

#힙생성
def create_heap(parent, last_node):
    parent_value = A[parent]

    #좌측 자식
    left = 2 * parent + 1

    #우측 자식
    right = left + 1

    while left <= last_node:
        # 왼쪽 자식보다 오른쪽 자식이 클 경우
        if right <= last_node and A[left] < A[right]:
            child = right 
        # 왼쪽 자식이 오른쪽 자식보다 클 경우
        else:
            child = left
        # 부모보다 자식값이 크면
        if parent_value < A[child]:
            # 자식을 위로 올림
            A[parent] = A[child]
            parent = child
            # 자식들을 새로 지정
            left = parent * 2 + 1
            right = left + 1
        else:
            break
    A[parent] = parent_value

def heap_sort(n):
    i = int(n / 2)
    while i >= 0:
        # 정렬할 배열을 heap로 변환
        create_heap(i, n-1)
        i -= 1
    i = n - 1
    print("created heap",A)

    while i > 0:
        # heap을 생성한 이후에 최대값을 제거하고, i 인덱스의 값과 교환
        A[0],A[i] = A[i],A[0]
        # 남은 원소들로 heap을 재정비
        create_heap(0, i-1)
        i -= 1
    print("sorted heap",A)

heap_sort(10)