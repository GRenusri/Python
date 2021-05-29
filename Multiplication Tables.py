'''
n=int(input())
for i in range(1,21):
    print(n,' X ',i,' = ',n*i)
'''
'''

n=int(input())
for i in range(1,21):
    print(n,' X ',i,' = ',n*i)
    if i%n==0:
        print(' ')
'''

'''
n,val=map(int,input().split())
for i in range(1,21):
    print(n,' X ',i,' = ',n*i)
    if i%val==0:
        print(' ')
'''
'''
n=int(input())
for i in range(1,21):
    print(n,' X ',i,' = ',n*i)
    if (n*i)%2==0:
        print(' ')
'''

'''
n,r=map(int,input().split())
for i in range(1,r+1):
    print(n,' X ',i,' = ',n*i)
'''
'''
n,r=map(int,input().split())
i=1
while True:
    print(n,' X ',i,' = ',n*i)
    if i==r:
        break
    i+=1
'''
'''
n,r=map(int,input().split())
i=1
while i<=r:
    print(n,' X ',i,' = ',n*i)
    i+=1
'''

'''
n,r=map(int,input().split())
i=1
while i!=r+1:
    print(n,' X ',i,' = ',n*i)
    i+=1
'''

'''
n,r1,r2=map(int,input().split())
i=r1
while i<=r2:
    print(n,' X ',i,' = ',n*i)
    i+=1
'''
'''
n,r1,r2=map(int,input().split())
if r1<=r2:
   while r1<=r2:
       print(n,' X ',r1,' = ',n*r1)
       r1+=1
else:
    while r2<=r1:
        print(n,' X ',r2,' = ',n*r2)
        r2+=1

'''
'''
n,r1,r2=map(int,input().split())
if r1>r2:
    r1,r2=r2,r1
while r1<=r2:
    print(n,' X ',r1,' = ',n*r1)
    r1+=1
'''
#To print in reverse order (bottom to top) 
n,r1,r2=map(int,input().split())
inc=1
if r1>r2:
    inc=-1
for i in range(r1,r2+inc,inc):
    print(n,' X ',i,' = ',n*i)
    
