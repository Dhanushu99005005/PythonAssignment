"""Find the average speed of vehicle, given the distance travelled for fixed time intervals"""

distance_covered=list(map(int,input().split()))
print(sum(distance_covered)/len(distance_covered))