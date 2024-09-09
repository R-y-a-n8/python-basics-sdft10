#function that takes in a string and returns the count on vowels
 #use for loopexample for char in loops though each character decidin
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)
print(count_vowels("hello world"))
