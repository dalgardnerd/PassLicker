# Apply Settings

from pathlib import Path
import json


def handle_defaults():
    if Path("defaults.json").is_file():
        print("defaults.json found")
        return load_defaults()
    print("No defaults found, creating defaults.json")
    write_defaults("5", "2", "-", "True", "14", "10")
    return load_defaults()


def load_defaults():
    with open("defaults.json", 'r', encoding="utf8") as file:
        data = json.load(file)
        return data


def write_defaults(num_chars, total_words, word_separator, include_digits, expire_days, expire_views):

    default_settings = {
        "num_chars": num_chars,
        "total_words": total_words,
        "word_separator": word_separator,
        "include_digits": "True" if include_digits == True else "False",
        "expire_days": expire_days,
        "expire_views": expire_views
    }

    with open("defaults.json", 'w', encoding='utf8') as file:
        file.write(json.dumps(default_settings))
        print("Writing settings to defaults.json")


if __name__ == "__main__":
    handle_defaults()
