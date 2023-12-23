def main():
    while True:
        try:
            n = int(input("Введите количество критериев (число в целом формате): "))
        except ValueError:
            print("Введите число в целом формате")
        else:
            break
    a=[[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i == j):
                a[i][j] = 1.00
            else:
                print("Введите отношение критерия", i+1 , "к критерию", j+1,"(число в целом формате)")
                while True:
                    try:
                        a[i][j] = int(input())
                    except ValueError:
                        print("Введите число в целом формате")
                    else:
                        break
    sums = ves(a,n)
    for i in range(n):
        print(round(sums[i], 2))

def ves(a,n):
    sum = 0.0
    sum_s = [0.0] * n
    for i in range(n):
        for j in range(n):
            sum += a[i][j]
    for i in range(n):
        for j in range(n):
            sum_s[i] += a[i][j]
    for i in range(n):
        sum_s[i]=sum_s[i]/sum
    return sum_s

if __name__ == "__main__":
    main()