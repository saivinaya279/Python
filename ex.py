n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 18 == 0:
        print("FizzBuzz")
    elif i % 6 == 0:
        print("Fizz")
    elif i % 9 == 0:
        print("Buzz")
    else:
        print(i)