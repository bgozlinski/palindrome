#  Check if given string is palindrome


def palindrome(word: str) -> bool:
    word = word.replace(' ', '').lower()

    if word != word[::-1]:
        return False

    return True

word = "malayala"
answer = palindrome(word)

if not answer:
    print(f'{word} is not palindrome')
else:
    print(f'{word} is palindrome')
