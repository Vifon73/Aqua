from Encode import encoding
from Decode import decoding

def main():
    print("-" * 20)
    print("Szyfr AquA")
    print("-"* 20)

    while True:
        print("\n wybierz opcje:")
        print("\n 1.Encoding")
        print("\n 2.Decoding")
        print("\n 3.Exit")

        choice = input("\n(opcja 1,2,3)\n")

        if choice == "1":
            msg = input("Wpisz wiadomosc do zaszyfrowania: ")
            res = encoding(msg)
            print("#" * 20)
            print(f"{res}")
            print("#" * 20)
        elif choice == "2":
            msg = input("Wpisz wiadomosc do odszyfrowania:")
            try:
                res = decoding(msg)
                print("#"*20)
                print(f"{res}")
                print("#" * 20)
            except Exception as e:
                print("Zly szyfr")
        elif choice == "3":
            print("byee")
            break
        else:
            print("Blad w wyborze opcji")

if __name__ == "__main__":
    main()