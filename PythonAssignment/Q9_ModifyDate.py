"""Correct the malformed date string, for e.g. "45/8/2018" to "14/9/2018" """

days,months,year=list(map(int,input().split("/")))
while(days>=30):
    days-=30
    months+=1
while(months>=12):
    months-=12
    year+=1
print(str(days)+"/"+str(months)+"/"+str(year))