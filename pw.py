import math
import random
import json
import requests
from wordlist import wordlist


def load_dictionary():  # Currently unused
    """Counts size of dictionary to set range for random word selection"""
    # set path
    dictionary_path = ("words_alpha.txt")
    with open(dictionary_path, 'r', encoding="utf-8") as file:
        words = file.readlines()
        return words


def find_words(num_chars, total_words):
    """Finds and returns word list from dictionary"""

    words = wordlist
    upper_limit = len(words)
    result = []
    valid_words = 0

    while valid_words < total_words:

        # select word based on upper limit
        select_word = (random.randrange(0, upper_limit))
        word = words[select_word].strip()

        # check if selected word is between min and max characters, append if good
        if len(word) == num_chars:
            result.append(word)
            valid_words += 1

    return result


def get_passphrase(num_chars, total_words, word_separator, include_digits):
    """Take arguments and find_words, put words together including word separator, random digits"""

    word_list = find_words(num_chars, total_words)
    passphrase = ""
    used_words = 0
    for word in word_list:
        passphrase += word.capitalize()
        used_words += 1
        if used_words < total_words:  # this is so that we only apply word separators between words, not at the end of the passphrase
            passphrase += word_separator
    if include_digits:
        digits = (str(math.floor((random.random()*10))))
        # generate two random digits and concat to digits
        digits += (str(math.floor((random.random()*10))))
        passphrase += digits
    return passphrase


def push_passphrase(passphrase, expire_days, expire_views):
    """ push passphrase to pwpush.com with selected expiration parameters"""

    base_url = 'https://pwpush.com'
    endpoint = '/p.json'

    data = {
        'password[payload]': passphrase,
        'password[expire_after_days]': expire_days,
        'password[expire_after_views]': expire_views
    }
    while True:  # ensures we don't get a link with a backslash, barracuda email filtering doesn't like links with backslashes in my use case
        response = requests.post((base_url+endpoint), data)
        token = json.loads(response.content)['url_token']
        if'\\' not in token:
            link = f'https://pwpush.com/en/p/{token}'
            return link
            break
        # deletes any link that has a backslash
        requests.delete(f"{base_url}/p/{token}.json")
