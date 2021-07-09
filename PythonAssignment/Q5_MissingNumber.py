"""Find the missing number, given the original list and modified one"""

original_list=list(map(int,input().split()))
modified_list=list(map(int,input().split()))
check_dict={}
for i in original_list:
    if i in check_dict.keys():
        check_dict[i]+=1
    else:
        check_dict[i]=1

for i in modified_list:
    if i in check_dict.keys():
        check_dict[i]-=1
    else:
        check_dict[i]=-1

for key,value in check_dict.items():
    if value==1:
        print(key,end=" ")