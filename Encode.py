import base64

def encoding(text):
    res = ""
    salt = "aquA"
    #odwrocenie wiadomosci na poczatku
    reverse = text[::-1]

    #przesuniecie kazdej litery o 73 do przodu
    for i in reverse:
        if i.isalpha():
            if i.isupper():
                #Wielkie litery A-Z
                hash = chr((ord(i) - ord('A') + 73) % 26 + ord('A'))
            else:
                #Małe litery od a-z
                hash = chr((ord(i) - ord('a') + 73) % 26 + ord('a'))
            res += hash
        else:
            res += i
    #dodanie soli na koniec
    res += salt

    #koduj do base64
    encoded = base64.b64encode(res.encode()).decode()
    return encoded
