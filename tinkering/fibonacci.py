def fibonacci():
    n = int(input("Choose a number of fibonnacci numbers to generate: "))

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    for num in fibonacci():
        print(num)
