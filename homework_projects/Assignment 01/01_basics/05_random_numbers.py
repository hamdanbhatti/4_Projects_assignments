import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    
    numbers: list[int] = []

    for i in range(N_NUMBERS):

     numbers.append(random.randint(MIN_VALUE, MAX_VALUE))

    print("The random numbers are:")
    for number in numbers:
        print(number, end=" ")
    print()

    print("The random numbers sorted are:")
    numbers.sort()
    for number in numbers:
        print(number, end=" ")
    print()


if __name__ == '__main__':
    main()