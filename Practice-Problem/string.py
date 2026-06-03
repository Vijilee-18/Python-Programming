noWord = 0
noVowels = 0
noConsonants = 0
highestWordLength = 0
highestString = ""

string = input("Enter a String: ").lower()

subString = ""

for ch in string:

    
    if ch.isalpha():
        if ch in "aeiou":
            noVowels += 1
        else:
            noConsonants += 1

    
    if ch != " ":
        subString += ch
    else:
        noWord += 1

        if len(subString) > highestWordLength:
            highestWordLength = len(subString)
            highestString = subString

        subString = ""


if subString:
    noWord += 1

    if len(subString) > highestWordLength:
        highestWordLength = len(subString)
        highestString = subString

print(
    f"There are {noVowels} vowels, "
    f"{noConsonants} consonants, "
    f"{noWord} words and the longest word is "
    f"'{highestString}' with a length of {highestWordLength}"
)