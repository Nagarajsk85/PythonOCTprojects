def most_frequent(input_string):
    letter_freq = {}
    input_string = input_string.lower()
    for char in input_string:
        if char.isalpha():
            if char in letter_freq:
                letter_freq[char] += 1
            else:
                letter_freq[char] = 1
    sorted_freq = sorted(letter_freq.items(), key=lambda item: item[1], reverse=True)
    for char, freq in sorted_freq:
        print(f"{char}: {freq}")
user_input = input("Enter a string: ")
most_frequent(user_input)
