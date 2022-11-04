n = int(input('Type a number, and its factorial will be printed: '))

if n < 0:
    raise ValueError('You must enter a non-negative integer.')
elif n == 1:
    print('Factorial of 1 is: 1')

factorial = 1
for i in range(2, n + 1):
    factorial *= i

print(factorial)
