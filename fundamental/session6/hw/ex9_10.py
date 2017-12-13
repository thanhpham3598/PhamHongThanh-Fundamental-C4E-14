def get_even_list(l):
    even_numbers = []
    for number in l:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


even_list = get_even_list([1, 5, 2, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
