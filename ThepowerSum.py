from sys import stdin

def PowerSum(X,N,a=1):
    if X == a**(N):
        return 1
    if X < a**(N):
        return 0
    return PowerSum(X-a**(N),N,a+1)+ PowerSum(X,N,a+1)

def main():
    X = int(stdin.readline().strip())
    while X:
        N = int(stdin.readline().strip())
        print(PowerSum(X,N))
        X = stdin.readline().strip()
        if X:
            X = int(X)
main()



