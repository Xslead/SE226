from string_package import (
    reverse_string,
    capitalize_words,
    remove_punctuation,
    count_characters,
    count_words,
    average_word_length
)


def main():

    print("String Analyzer")
    print("--------------")

    sentence = input("Enter a sentence: ")

    print("\nResults:")
    print(f"Original: '{sentence}'")

    capitalized = capitalize_words(reverse_string(sentence))
    print(f"Reverse and Capitalized: '{capitalized}'")

    no_punctuation = remove_punctuation(sentence)
    print(f"Without punctuation: '{no_punctuation}'")

    char_count = count_characters(no_punctuation)
    print(f"Character count (excluding whitespace): {char_count}")

    word_count = count_words(no_punctuation)
    print(f"Word count: {word_count}")

    avg_length = average_word_length(no_punctuation)
    print(f"Average word length: {avg_length:.2f}")

if __name__ == "__main__":
    main()


