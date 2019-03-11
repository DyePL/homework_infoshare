while True:
   komenda = (input("Co chcesz zrobić? ")).lower()
   if komenda == ("dodaj"):
       from db import dodaj
       dodaj()
   elif komenda == ("usuń"):
       from db import usun
       usun()
   elif komenda ==  ("sprawdź"):
       sprawdzane = input("Podaj imię: ")
       if sprawdzane in baza:
           print("Kontakt istnieje w bazie.")
       else:
           print("Nie ma kontaktu w bazie.")
   elif komenda == ("ilość"):
       print("Ilość kontaktów w bazie:",len(baza))
   elif komenda == ("wyjdź"):
       print("Do widzenia.")
       exit(0)