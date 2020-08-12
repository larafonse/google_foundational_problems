def jumpingOnClouds(c):

    i = 0
    jumps = 0
    while i < len(c)-1:
        print(c[i], i)
        if c[i+1] == 1:

            i = i+2
        else:
            if len(c)-2 == i:
                i+=1
            else:
                if c[i+2]== 1:
                    
                    i +=1 
                else:
                    
                    i +=2
        jumps+=1
    print(c[i], i)
    print(jumps)


jumpingOnClouds([0,0,0,1,0,0])