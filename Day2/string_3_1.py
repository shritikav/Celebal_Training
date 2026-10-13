
def count_characters(text):
    letters = 0
    digits = 0
    special_symbols = 0

    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            special_symbols += 1

    print("Number of letters:", letters)
    print("Number of digits:", digits)
    print("Number of special symbols:", special_symbols)


if __name__ == "__main__":
    text = input("Input String : ")
    count_characters(text)
