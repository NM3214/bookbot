def wordcount(text):
    return len(text.split())

def charcount(text):
    chardict = {}
    for char in text.lower():
        if char in chardict:
            chardict[char] = chardict[char] + 1
        else:
            chardict[char] = 1
    return chardict

def sort_by_char(chardict):
    list_of_dict = []
    for key in chardict:
        list_of_dict.append({"char": key, "num": chardict[key]})
    list_of_dict.sort(reverse=True, key=lambda x: x["num"])
    return list_of_dict