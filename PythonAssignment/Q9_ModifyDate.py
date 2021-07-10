"""Correct the malformed date string, for e.g. "45/8/2018" to "14/9/2018" """

days,months,year=list(map(int,input().split("/")))
print(days,months,year)
months31=[1,3,5,7,8,10,12]
months30=[4,6,9,11]
while(months>12):
    months-=12
    year+=1
while(months<=13 and days>31):
    while(days>=31):
        if months in months31:
            days-=31
            months+=1
        elif months in months30:
            days-=30
            months+=1 
        else:
            days-=28
            months+=1
    if(months==13):
        year+=1
        months=1
    
if months not in months31:
    if months in months30:
        if days == 31:
            days-=30
            months+=1
    else:
        if days>28:
            days-=28
            months+=1
    if(months==13):
        months=1
        year+=1
              
print(str(days)+"/"+str(months)+"/"+str(year))