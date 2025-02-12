import random
import string
import requests

# function that generates a single random character
def random_character():
    choices = string.ascii_letters + string.digits + string.punctuation
    return random.choice(choices)

passwordLength = int(input("How many characters do you want your password to be?"))

# function that generates a password of random characters
def generate_strong_password():
    password = ""
    for i in range(passwordLength):
        password = password + random_character()
    print(password)

generate_strong_password()


# function that gets a random word from a dictionary api
def fetch_word():
    url = "https://random-word-api.herokuapp.com/word?length=2"

    response = requests.get(url)
    word = response.json()[0]
    return word

def replaceLetters(word):
    word = word[0].upper()+ word[1:]
    if "a" in word:
        word = word.replace("a", "@")
    if "b" in word:
        word = word.replace("b", "6")
    if "c" in word:
        word = word.replace("c", "(")
    if "t" in word:
        word = word.replace("t", "7")

    return word


def generate_weaker_password():
    word1 = fetch_word()
    word2 = fetch_word()
    word1 = replaceLetters(word1)
    word2 = replaceLetters(word2)
    password = word1 + word2
    return password



print(generate_weaker_password())
