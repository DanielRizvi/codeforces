 #number of inputs
n = int(input())
#input n stations a and b values
# a- no of ppl exit
# b -no of ppl entry 

#keepibng track of max passengers at any given time
max_passengers = 0

#how many passengers are right now in the term
cur_passengers = 0

#how many passengers are 

for _ in range(n):
    lst = list(map(int,input().rstrip().split()))
    a = lst[0]
    b = lst[1]
    #updatye the current passangers 
    cur_passengers = cur_passengers - a + b
    #check if this value is greater than max passengers
    if cur_passengers > max_passengers:
        max_passengers = cur_passengers

print(max_passengers)