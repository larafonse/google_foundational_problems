def longest_anagram(string, dictionary):
    count = [0 for _ in dictionary]
    
    for i in range(len(dictionary)):

        word = dictionary[i]
        temp = [l for l in string]

        for letter in word:
            if letter in temp:
                temp.remove(letter)
                count[i]+=1
            else:
                count[i]= 0
                break


    return(dictionary[count.index(max(count))])









print(longest_anagram('batman',['bat','aman','antman']))   