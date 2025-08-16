#frequency distribution - histogram


st1 = input()
st2 = input()
st3 = input()

d1 = {}
d2 = {}
#find out histogram for st1
for i in st1:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1

#find out histogram for st2
for i in st2:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1

#histogram for st3
for i in st3:
    if i in d2:
        d2[i] += 1
    else:
        d2[i] = 1

if d1 == d2:
    print("YES")
else:
    print("NO")