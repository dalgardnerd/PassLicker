"""Used to convert a text file into a .py file so it can be imported instead of opened"""


dictionary_path = ("popular.txt")
new_file = ("wordlist.py")
count = 0
with open (new_file, 'a', encoding="utf-8") as dict:
    with open(dictionary_path, 'r', encoding="utf-8") as file:
        for word in file:
            dict.write(f"'{word.strip()}',")
        
    
