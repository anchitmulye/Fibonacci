def fib_recursive(n):
    """
    The function returns the fibonacci sequence till the given input.
    assumes n an int >= 0
    Returns Fibonacci of n
    """
    assert type(n) == int and n >=  0
    if n==0 or n==1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def testFib3(n):
    import time
    seconds=[]
    for i in range(n+1):
        start=time.clock()
        fib_recursive(i)
        end=time.clock()
        net = end-start
        seconds.append(net)
    return seconds

import pylab    
time=testFib3(30)
pylab.plot(time,'--bo')
pylab.title('growth of fibonacci recursive')
pylab.xlabel('numbers')
pylab.ylabel('time in seconds')
pylab.show()