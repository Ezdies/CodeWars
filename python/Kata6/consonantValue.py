def valueOfLetter(letter):
    for (i, c) in enumerate("abcdefghijklmnopqrstuvwxyz"):
        if c == letter:
            return i + 1
    return 0


def valueOfWord(word):
    return sum(map(lambda x: valueOfLetter(x), word))


def splitOnVowels(word):
    splittedWords = []
    splittedWord = ""
    for letter in word:
        if letter not in "aeiou":
            splittedWord += letter
        else:
            if splittedWord:
                splittedWords.append(splittedWord)
            splittedWord = ""
    if splittedWord:
        splittedWords.append(splittedWord)
    return splittedWords


def maxValueOfSubstrings(word):
    substrings = splitOnVowels(word)
    return max(map(valueOfWord, substrings))
   
   
print(maxValueOfSubstrings("strength"))  
