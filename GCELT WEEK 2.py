# GCD AND LCM
T=int(input())
for i in range(T):
    num=[int(x) for x in input().split(' ')]
    a=min(num)
    b=max(num)
    multiply=a*b
    while(b):
        a,b=b,a%b
    gcd=a
    lcm=multiply/gcd
    print(gcd,int(lcm))

#TRICOIN PROBLEM CODECHEF

for _ in range(int(input())):
    a,b=map(int,input().split())
    s=0
    for i in range(1,b+1):
        s=max(s,a%i)
    print(s)
t = int(input())
for i in range(t):
    s=int(input())
    r,n=0,1
    while ((n*(n+1)) // 2<=s):
        r = n
        n=n+1
    print(r)

#CHEF AND COUPON PROBLEM
#CODE NAME:COUPON2

T = int(input())
for i in range(T):
    Deliverycharge, Couponprice = map(int, input().split())
    A1,A2,A3=map(int,input().split())
    B1,B2,B3=map(int,input().split())

    ordervalueday1=A1+A3+A2
    if ordervalueday1<150:
        ordervalueday1=ordervalueday1+Deliverycharge


    ordervalueday2=B1+B2+B3
    if ordervalueday2<150:
        ordervalueday2=ordervalueday2+Deliverycharge

    cost_with_coupon= ordervalueday1+ordervalueday2+Couponprice
    cost_without_coupon=A1+A3+A2+Deliverycharge+B3+B2+B1+Deliverycharge

    if cost_with_coupon<cost_without_coupon:
        print("YES")
    else:
        print("NO")


