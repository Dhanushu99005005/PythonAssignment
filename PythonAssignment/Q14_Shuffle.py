""" Given a number, find the largest number by shuffling the digits """

input_list=sorted(list(map(int,list(str(input())))))[::-1]
print("".join(list(map(str,input_list))))