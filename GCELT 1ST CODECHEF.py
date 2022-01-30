#SUM OF FIRST AND LAST DIGIT OF A NUMBER

t=int(input())
for i in range(t):
    x=str(input())
    a=int(x[0])
    b=int(x[-1])
    c=a+b
    print(c)
#FIND SECOND LARGEST NUMBER AMONG a,b,c

testcase=int(input())
for i in range(testcase):
    a,b,c= map(int,input().split())
    largenumber=max(a,b,c)
    smallnumber =min(a,b,c)
    secondlargestnumber=(a+b+c)-largenumber-smallnumber
    print(secondlargestnumber)

#MAHASENA CODECHEF PROBLEM


testcase=int(input())
lst=list(map(int,input().split()))
even,odd=0,0
for i in lst:
    if (i%2==0):
        even+=1
    else:
        odd+=1
if(even>odd):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
#
#
