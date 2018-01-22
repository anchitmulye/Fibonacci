def fib_iterative(n):
    """
    The function returns the fibonacci sequence till the given input.
    assumes n an int >= 0
    Returns Fibonacci of n
    """
    assert type(n) == int and n >=  0
    group=[0,1]
    i=2
    while i<=n:
        group.append(group[i-1]+group[i-2])
        i=i+1
    return group[n]

def testFib2(n):
    import time
    seconds=[]
    for i in range(n+1):
        start=time.clock()
        fib_iterative(i)
        end=time.clock()
        net = end-start
        seconds.append(net)
    return seconds

import pylab    
time=testFib2(30)
pylab.plot(time,'--go')
pylab.title('growth of fibonacci iterative')
pylab.xlabel('numbers')
pylab.ylabel('time in seconds')
pylab.show()