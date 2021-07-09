"""Find the difference between two lowest numbers in the list"""

list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
print(min(list1)-min(list2))