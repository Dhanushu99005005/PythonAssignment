"""Generate accumulated strings.e.g. abcd ==> A-Bb-Ccc-Dddd"""

input_string=str(input()).upper()
acc_list=[]
count=0
for i in input_string:
    acc_list.append(i+chr(ord(i)+32)*count)
    count+=1
print("-".join(acc_list))