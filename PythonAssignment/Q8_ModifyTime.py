""" Correct the malformed time string, for e.g "5:70:65" to "6:11:05" """

hours,minutes,seconds=list(map(int,input().split(":")))
while(seconds>=60):
    seconds-=60
    minutes+=1
while(minutes>=60):
    minutes-=60
    hours+=1
print(str(hours)+":"+str(minutes)+":"+str(seconds))