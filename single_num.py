if __name__ == "__main__":
    
    nums = list(map(int, input().split(',')))
    
    single = 0
    
    for num in nums:
        single^=num
    
    print(single)