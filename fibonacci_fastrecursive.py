def fib_fastrecursive(n,memo={}):
    """
    The function returns the fibonacci sequence till the given input.
    assumes n an int >= 0
    Returns Fibonacci of n
    """
    assert type(n) == int and n >=  0
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result =fib_fastrecursive(n-1,memo) + fib_fastrecursive(n-2,memo)
        memo[n] =result
        return result

def testFib1(n):
    import time
    seconds=[]
    for i in range(n+1):
        start=time.clock()
        fib_fastrecursive(n)
        end=time.clock()
        net = end-start
        seconds.append(net)
    return seconds

import pylab 
#num=30   
time=testFib1(30)
pylab.plot(time,'--ro')
pylab.title('growth of fibonacci fast recursive')
pylab.xlabel('numbers')
pylab.ylabel('time in seconds')
pylab.show()