import base64

def decoding(text):
    salt = "aquA"
    res = ""

    #dekodowanie base64
    decoded = base64.b64decode(text).decode()

    #kasownie soli z konca zaleznie od dlugosci znakow soli (tutaj -> 4 znaki)
    deleting_salt = decoded[:-len(salt)]

    for i in deleting_salt:
        if i.isalpha():
            if i.isupper():
                #Wielkie litery A-Z
                hash = chr((ord(i) - ord('A') - 73) % 26 + ord('A'))
            else:
                #Małe litery od a-z
                hash = chr((ord(i) - ord('a') - 73) % 26 + ord('a'))
            res += hash
        else:
            res += i

    #odwracanie
    res = res[::-1]
    return res


