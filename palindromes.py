def palindrome(a):
    a = a.lower().replace(" ","").replace(",","").replace(".","")
    first_idx = int(len(a)/2)
    first_half = a[:first_idx]
    second_half = a[first_idx:] if not len(a)%2 else a[first_idx+1:] 
    second_half = second_half[::-1]
    print(first_half == second_half)


palindrome("Nazi, ni vida divinizan    ")