

def count_vowels(word_to_check: str) -> int:
    """
    Your mission:
    Count how many vowels are inside the given word.

    A vowel is one of these letters:
    a, e, i, o, u

    You must return the number of vowels found.

    Examples:
    count_vowels("cat") returns 1
    count_vowels("hello") returns 2
    count_vowels("sky") returns 0

    Things to think about:
    - You may need a variable to keep count. Hint: ``count = 0''.
    - You may need a loop to check each letter. Hint: ``for ... in word.lower():''
    - You may need an if statement to check whether a letter is a vowel.
    """
    count: int = 0

    for vowel in word_to_check.lower():

        if vowel in ("a", "e", "i", "o", "u"):
            count += 1

    return count


def main():
    user_input: str = input("Enter a word you want to check for vowels: ")
    count: int = count_vowels(user_input)
    if count == 0:
        print("No Vowels Have Been Found!")
    elif count >= 1:
        print("Vowels Have Been Found!")
    else:
        print("something went wrong")


main()
