
def fibo():
    x=0;
    y=1;
    while(x<10):
        #z=x+y;
        #print(z);
        #x=y;
        #y=z;
        print(x);
        x,y=y,x+y;
    return None
        
    

print(fibo())
#0,1,1,2,3,5

