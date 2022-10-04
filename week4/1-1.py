# -*-coding: utf-8 -*-
# 2018112024 강지영

str_list = []

# 파일읽기
def read_file():
    with open("/Users/kangjiyoung/dgu-cs-algorithm/week4/hello.txt", 'r') as file:
        # ,를 기준으로 단어를 끊는다
        str_ = file.readline().split(",")
        for str in str_:
            str_list.append(str)

# 회문인지 아닌지 확인하는 함수
def is_palindrome():
    # 회문인지 아닌지 확인하는 방식 => 기존 문장과 문장을 앞뒤로 뒤집은(reverse)한 문장이 같은지 비교를 한다.
    for str in str_list:
        reverse_str = ''.join(reversed(str))
        if (str == reverse_str):
            print(str,"is a palindrome")
        else:
            print(str,"is not a palindrome")
    
    
read_file()
is_palindrome()
