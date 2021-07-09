"""Given a string,find the mexican wave"""

input_string=str(input())
mexican_wave=[]
for i in range(len(input_string)):
    mexican_wave.append(input_string[:i]+input_string[i].upper()+input_string[i+1:])
print(mexican_wave)