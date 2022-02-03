print("%9d"%(1), end="")
for k in range(2,13) :
    print("%5d" %(k), end="")
print("")
print(65*"-")
for i in range(1,13) :
    print("%2d |"%(i), end="")
    for j in range(1,13) :
        res = i*j
        print("%5d" %(res), end="")
    print('')
