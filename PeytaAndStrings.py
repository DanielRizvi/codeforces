st1 = input()
st2 = input()

#convert into lower case

lowst1 = st1.lower()
lowst2 = st2.lower()

#compare with ascii values

ans = 0 
for i in range(len(st1)):
    asci_1 = ord(lowst1[i])
    asci_2 = ord(lowst2[i])
    if asci_1 > asci_2:
        ans = 1
        break
    elif  asci_1 < asci_2:
        ans = -1
        break
    else:
        continue 
print(ans)