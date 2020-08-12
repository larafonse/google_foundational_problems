import sys
def dynamic_fibonacci(n, fiv_dict):
    
    for i in range(2,n+1):
        if fiv_dict.get(i):
            continue
            
        fiv_dict[i] = fiv_dict[i-1] + fiv_dict[i-2]
    
    return(fiv_dict)

if __name__ == '__main__':
    
    fiv_dict = {
        0:0,
        1:1
    }
    
    input_arr = []
    
    for line in sys.stdin.readlines(): 
        n = int(line)
        input_arr.append(n)
        if not fiv_dict.get(n):
            fiv_dict = dynamic_fibonacci(n, fiv_dict)
    
    for val in input_arr:
        print(fiv_dict[val])
            
            
            