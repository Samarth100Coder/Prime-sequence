lower=int(input("Enter lower limit: "))
upper=int(input("Enter upper limit: "))

for c in range(lower, upper+1):
    if c>1:
        for d in range(2,c):
            if c%d==0:
                break
        else:
            print(c)