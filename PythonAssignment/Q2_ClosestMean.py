"""In a given list of elements, find the elements which is close to its mean"""

mean_list=sorted(list(map(int,input().split())))
mean_num=sum(mean_list)/len(mean_list)
diff_list=list(map(lambda x:x-mean_num,mean_list))
min_num=min(list(map(abs,diff_list)))
req_num=int(mean_num+min_num)
print(req_num,end=" ")
if(abs(mean_list[mean_list.index(req_num)-1]-mean_num)<=min_num):
    print(mean_list[mean_list.index(req_num)-1])