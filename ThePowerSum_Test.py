from sys import stdin

# casos de prueba:
cases = [["10","2"],["100","2"],["100","3"],["1","1"]]

def PowerSum(X,N,a=1):
    if X == a**(N):
        return 1
    if X < a**(N):
        return 0
    return PowerSum(X-a**(N),N,a+1)+ PowerSum(X,N,a+1)
def main():
    for i in cases:
        X = int(i[0])
        while X:
            N = int(i[1])
            print("case #",PowerSum(X,N))
            X = ""
            #X = stdin.readline().strip()
            #if X:
                #X = int(X)
main()
