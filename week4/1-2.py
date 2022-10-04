# -*-coding: utf-8 -*-
# 2018112024 강지영

str_list = []

# 파일읽기
def read_file():
    with open("/Users/kangjiyoung/dgu-cs-algorithm/week4/hello.txt", 'r') as file:
        # ,를 기준으로 단어를 끊는다
        str_list = file.readline().split(",")
        for str in str_list:
            if is_palindrome(str): 
                print(str,"is a palindrome")
            else:
                print(str,"is not a palindrome")

# 회문인지 아닌지 확인하는 함수
def is_palindrome(str):
    # 회문인지 아닌지 확인하는 방식 
    # => word[1:-1]처럼 현재 문자열의 첫 번째 문자와 마지막 문자까지 잘라서 다시 넣어줍니다. 
    # 이런 방식으로 첫 번째 문자와 마지막 문자를 제외하면서 회문을 판별합니다.
    if str[0] != str[-1]:
        return False
    if len(str) <= 1:
        return True
    return is_palindrome(str[1:-1])
    
    
read_file()
is_palindrome("hello")
