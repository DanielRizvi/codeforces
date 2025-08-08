
def toggle(a):
    if a ==0:
        return 1
    else:
        return 0




r1 = list(map(int,input().rstrip().split()))
r2 = list(map(int,input().rstrip().split()))
r3 = list(map(int,input().rstrip().split()))

#creating the matrix
lst = [r1,r2,r3]

#initial state - all is on
ans = [[1,1,1],[1,1,1],[1,1,1,]]

#iteration through matrix
for i in range(3):
    for j in range(3):
        if lst[i][j]%2 ==1:
            #toggle particular switch
            ans[i][j] = toggle(ans[i][j])
            #deal with adjacent switches
            if i<2:
                ans[i+1][j] = toggle(ans[i+1][j])
            if i>0:
                ans[i-1][j] = toggle(ans[i-1][j])
            if j<2:
                ans[i][j+1] = toggle(ans[i][j+1])
            if j>0:
                ans[i][j-1] = toggle(ans[i][j-1])

#printing the answer to the user

#converting ans to list of string 

for i in range (3):
    ans[i] = [str(el) for el in ans[i]]

for row in ans:
    print(''.join(row))