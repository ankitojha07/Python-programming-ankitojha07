def add():
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    c = a + b
    return c


if __name__ == '__main__':
    print("Calculation function : ")
    ans = add()
    print(ans)
