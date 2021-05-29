'''
I/P:n=5
O/P:
*
* *
* * *
* * * *
* * * * *

n=int(input())
for i in range(1,n+1): #3
    for j in range(1,i+1):
    print('*',end='')
    print()

 '''
'''
I/P:5
1           5 5 5 5 5 
2 2         4 4 4 4
3 3 3       3 3 3
4 4 4 4     2 2
5 5 5 5 5   1

#pattern 1
n=int(input())
x=0
for i in range(0,n):
    x+=1
    for j in range(0,i+1):
        print(x,end='')
    print()
    (or)

n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(i,end='')
    print()
'''
'''
#pattern 2
n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print(i,end='')
    print()
        (or)
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end='')
    print()
'''


#pattern 3
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
#pattern 4
n=int(input())
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    
#pattern 5
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
#pattern 6
n=int(input())
for i in range(n,0,-1):
    if i%2==0:
        for j in range(i,0,-1):
            print(j,end=" ")
    else:
        for j in range(1,i+1):
            print(j,end=" ")
    print()
    
#pattern 7
n=int(input())
for i in range(1,n+1):
     for j in range(1,i+1):
            if j%2==0:
               print(0,end=" ")
            else:
                print(1,end=" ")
     print()
    
#pattern 8
n=int(input())
for i in range(1,n+1):
     for j in range(1,i+1):
            if j==1:
               print(i,end=" ")
            else:
                print(j,end=" ")
     print()
    
#right 1
n=int(input())
for i in range(n):
     for j in range(i):
            print(" ",end=" ")
     for j in range(n-i):
         print("*",end=" ")
     print()
    
#right 2
n=int(input())
for i in range(n):
     for j in range(i):
            print(" ",end=" ")
     for j in range(n-i):
         print(n-i,end=" ")
     print()
    
#right 3
n=int(input())
for i in range(n):
     for j in range(i):
            print(" ",end=" ")
     for j in range(n-i):
         print(n-j,end=" ")
     print()
    
#right 4
n=int(input())
for i in range(n+1):
     for j in range(i):
            print(" ",end=" ")
     for j in range(n-i,0,-1):
         print(n-i,end=" ")
     print()
    
#right 5
n=int(input())
for i in range(n+1):
     for j in range(i):
            print(" ",end=" ")
     for j in range(n-i,0,-1):
         print(n-j,end=" ")
     print()
    
#right 6
n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
            print("*",end=" ")
    print()
    
#right 7
n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
            print(j,end=" ")
    print()
    
#right 8
n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
            print(i,end=" ")
    print()


    
        

