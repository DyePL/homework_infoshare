def dodaj():
    with open("baza.txt", 'a', encoding="utf-8") as baza:
        baza.write('\n')
        baza.write(input("Podaj imię: "))
def usun():
    usuwane = input("Podaj imię: ")
    with open("baza.txt", 'r', encoding="utf-8") as baza:
        lines = baza.readlines()
    with open("baza.txt", 'w', encoding="utf-8") as baza:
        for line in lines:
            if line == usuwane+"\n":
                baza.write(line)
def sprawdz():
    sprawdzane = input("Podaj imię: ")
    if sprawdzane in baza:
        print("Kontakt istnieje w bazie.")
    else:
        print("Nie ma kontaktu w bazie.")
def ilosc():
    print("Ilość kontaktów w bazie:", len(baza))
def wyjdz():
    print("Do widzenia.")
    exit(0)