# -*-coding: utf-8 -*-
# 2018112024 강지영

A=[30,20,40,35,5,50,45,10,25,15]

def merge(left,right):

    i,j =0,0
    sorted_list = []

    while i < len(left) and j <len(right):
        # left가 right보다 작을시 sorted_list에 left 추가
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        # right가 left보다 작을시 sorted_list에 right 추가
        else:
            sorted_list.append(right[j])
            j += 1
    # left에 남은 값이 있을시 sorted_list에 추가
    sorted_list += left[i:]
    # right에 남은 값이 있을시 sorted_list에 추가
    sorted_list += right[j:]
    return sorted_list

# 합병 정렬
def merge_sort(arr):
    # 길이가 1이하 이면 반환
    if len(arr) <= 1:
        return arr

    # 리스트 divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 정렬 과정 보여주기
    print("left",left,"right",right)

    return merge(left,right)


print("Unsorted Array:",A)
print("Sorted Array",merge_sort(A))