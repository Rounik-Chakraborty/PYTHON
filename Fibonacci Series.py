def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while n > 0:
        fib_sequence.append(a)
        a, b = b, a + b
        n -= 1
    return fib_sequence

# Input number of terms
num_terms = int(input("Enter the number of terms: "))
fib_sequence = fibonacci(num_terms)
print("Fibonacci sequence:", fib_sequence)
