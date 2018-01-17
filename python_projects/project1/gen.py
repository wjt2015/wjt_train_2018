##
def fac(nMax):
    n,a,b=1,0,1;
    while n <= nMax:
        yield b;
        a,b = b,(a+b);
        n += 1;


