def fib (N,M):
    if N<=2 or M>=1:
        return 4
    else:
        return fib(N-M)+fib(M-2,N)

    print (fib(7,2))


