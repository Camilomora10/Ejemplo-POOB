from sys import stdin

# casos de prueba:
cases = ["148 3","9875 4","123 3","1 5", "100 1"]

def Superdigit(s):
    if len(s) == 1:
        return int(s)
    res = 0
    for i in s:
        res += int(i)
    return Superdigit(str(res))

def operacion(n,k):
    p = str(n*k)
    return Superdigit(p)

def main():
    for i in cases:
        line = list(map(int,i.split()))
        while line:
            print("case#",operacion(line[0], line[1]))
            #line = list(map(int,stdin.readline().strip().split()))
            line = ""
main()
