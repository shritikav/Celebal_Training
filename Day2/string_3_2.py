
def count_characters(text):
    letters = [char for char in text if char.isalpha()]
    digits = [char for char in text if char.isdigit()]
    special_symbols = [
        char for char in text
        if not char.isalpha() and not char.isdigit()
    ]

    print("Number of letters:", len(letters))
    print("Number of digits:", len(digits))
    print("Number of special symbols:", len(special_symbols))


if __name__ == "__main__":
    text = input("Input String : ")
    count_characters(text)
