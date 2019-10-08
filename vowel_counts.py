def vowels(a):
    vowels = "aiueoAIUEO"
    freq_table = {}
    for letter in a:
        if letter in vowels:
            if letter in freq_table:
                freq_table[letter] +=1
            else:
                freq_table[letter] = 1
    print(freq_table)

vowels("Testing this $#i7")