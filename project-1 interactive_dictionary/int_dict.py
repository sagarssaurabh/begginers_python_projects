import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        print("Did You mean {} ?,If yes press y otherwise n".format(get_close_matches(w,data.keys())[0]))
        inp = input()
        if inp == "y" or inp == "Y":
            w = get_close_matches(w,data.keys())[0]
            return data[w]
        else:
            return "The word Doesn't exist.Please double exist"
    else:
        return "The word Doesn't exist.Please double exist"


word = input("enter word: ")
word = translate(word)
for i in word:
    print(i)
 