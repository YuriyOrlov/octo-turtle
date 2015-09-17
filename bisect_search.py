x=int(raw_input('Enter your integer number(!not negative!):'))
epsilon=0.01
low=0.0
high=x
ans=(high+low)/2.0
while abs(ans**2-x)>=epsilon:
    if ans**2 < x:
        low=ans
    else:
        high=ans
    ans=(high+low)/2.0
 
print (str(ans) + ' is close to square root of ' + str(x))
