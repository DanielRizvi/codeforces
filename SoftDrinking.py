
n,k,l,c,d,p,nl,np = list(map(int,input().rstrip().split()))

ml = (k*l) // nl
#liit of salt
salt_limit = p // np
#limit of slices of lemons 
slices = c*d
#finding the bottleneck of all of these
#finding minimum number of toast that can be made
toasts = min(ml,slices,salt_limit)
#to find out number of toats per person (each)
toats_each = toasts //n
print(toats_each)