"""Given a number, find the largest number by deleting single digit (order of digits will remain same)"""

input_list=list(map(int,list(str(input()))))
input_list.remove(min(input_list))
print("".join(list(map(str,input_list))))