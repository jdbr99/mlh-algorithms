def anagram(a, b):
    a = clean_words(a)
    b = clean_words(b)
    if len(a) != len(b):
        return False
    else:
        count_a = freq_table(a)
        count_b = freq_table(b)

    if count_a == count_b:
        return True
    return False

def clean_words(phrase):
    clean = phrase.lower().strip().replace(" ", "")
    print(clean)
    return clean
        
def freq_table(word):
    temp = {}
    for letter in word:
        if letter in temp:
                temp[letter] += 1
        else:
            temp[letter] = 1
    return temp

first = "di A   RY"
second = "dairy"

print(anagram(first,second))