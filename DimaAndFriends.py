n = int(input())

total = n + 1 #including dima 

lst = list(map(int,input().rstrip().split()))


curr = sum(lst)

#no of ways 
ans = 0

#dima has 1 to 5 fingers
#total number of fingers will go from curr + 1 to curr + 5

for i in range(1,6):
    if (curr + i) % total != 1:
        #case where dima doesn't have to clean 
        ans +=1
print(ans)