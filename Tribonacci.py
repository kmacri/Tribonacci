def tribonacci(n):
    #first three numbers is sequence are 1    
    a=1
    b=1
    c=1
    #return 1 if n is 1-3
    if (n<4):
        return 1
    else:
        #a becomes b, b becomes c and c is sum(a,b,c)
        for i in range(3,n):
            a,b,c = b, c, a+b+c
    return c

def main():
    n=int(input("Enter a number: "))
        

    print(tribonacci(n))


    
#1,1,1,3,5,9,17,31           
            
        
    
