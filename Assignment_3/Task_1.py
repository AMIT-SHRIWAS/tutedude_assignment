def factorial(fact_num):
    if fact_num == 0 or fact_num == 1:
        return 1
    elif fact_num < 0:
        print('invalid input enter positive integer')
    else:
        return fact_num * factorial(fact_num-1)

if __name__ == '__main__':
    fact_num = int(input('Enter a number: '))
    print(f'Factorial of {fact_num} is {factorial(fact_num)}')