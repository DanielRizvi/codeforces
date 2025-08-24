import math 

n,m = list(map(int,input().rstrip().split()))

#number of candies each child wants 
lst = list(map(int,input().rstrip().split()))

servings = []
for i in lst:
    serve = math.ceil(i/m)
    servings.append(serve)

#we need to find max valuye from right most part
#we need its index i
ma = max(servings)

#reverse the list
servings.reverse()

#find out index i 
servings.index(ma)

#finding out the position 
ans = n - i


