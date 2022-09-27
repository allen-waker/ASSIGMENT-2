#Write a Python function that takes a list of words and returns the length of the longest one

def main():
    text = input("please enter a list of words to evaluate:")
    
    longest = 0
    for words in text.split():
        if len(words) > longest:
            longest = len(words)
            longest_word = words
    print("the longest word is",longest_word,"with length",len(longest_word))
main()   