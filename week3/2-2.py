# -*-coding: utf-8 -*-
# 2018112024 강지영

A=[30,20,40,35,5,50,45,10,25,15]

# 합병 정렬
def merge_sort(arr):

    # 배열을 하나씩 쪼개기
    divided_arr = [arr[i: i + 1] for i in range(0, len(arr), 1)]

    # 쪼갠 배열 보여주기
    print("divided_arr", divided_arr)
    
    # 쪼갠 배열이 하나가 될 때까지 반복
    while(len(divided_arr)!= 1):
        tmp_arr = []
        i= 0

        # 정렬되는 과정 보여주기
        print(divided_arr)

        for i in range(0, len(divided_arr), 2):

            # 마지막 배열이 홀수개일 경우
            if i == len(divided_arr) - 1:
                tmp_arr.append(divided_arr[i])
                break

            # 두 배열을 비교하여 작은 값부터 tmp에 추가
            left, right = divided_arr[i], divided_arr[i + 1]
            tmp = []
            while len(left) != 0 and len(right) != 0:
                if left[0] < right[0]:
                    tmp.append(left.pop(0))
                else:
                    tmp.append(right.pop(0))
            tmp_arr.append(tmp + left + right)

        divided_arr = tmp_arr
    return divided_arr[0]
        


print("Unsorted Array:",A)
print("Sorted Array",merge_sort(A))