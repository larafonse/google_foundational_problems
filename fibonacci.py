def fibonacci(n):
    a = 0
    b = 1
    
    if n == 0:
        return a
    if n == 1:
        return b
    
    for _ in range(1,n):
        a, b = b, a+b
    
    return b 

if __name__ == "__main__":
    
    print(fibonacci(int(input())))