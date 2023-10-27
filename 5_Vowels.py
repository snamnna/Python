word = input()
word_lowercase = word.lower()

vowels = ["a", "e", "i", "o", "u"]
count = 0

for letter in word_lowercase:
    for i in vowels:
        if letter == i:
            count += 1
            
print("Number of vowels:", count)