"""Find the no.of people in a bus, given the data of people onboarding & alighting at each station"""

station_num=int(input())
onboarding=list(map(int,input().split()))
alighting=list(map(int,input().split()))
passengers=[0]*len(onboarding)
passengers[0]=onboarding[0]-alighting[0]
for i in range(1,len(onboarding)):
    passengers[i]=passengers[i-1]+onboarding[i]-alighting[i]
print(passengers[station_num])