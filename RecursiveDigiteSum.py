from sys import stdin

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
    line = list(map(int,stdin.readline().strip().split()))
    while line:
        print(operacion(line[0], line[1]))
        line = list(map(int,stdin.readline().strip().split()))
main()

