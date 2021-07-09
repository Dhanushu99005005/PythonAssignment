"""In a given list, count no.of elements smaller than their mean"""

input_list=list(map(int,input().split()))
mean_of_nums=sum(input_list)/len(input_list)
for i in input_list:
    if i<mean_of_nums:
        print(i,end=" ")