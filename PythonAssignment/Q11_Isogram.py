"""Check whether given string is isogram or not """

input_string=str(input())
print(sorted(list(input_string))==sorted(set(input_string)))