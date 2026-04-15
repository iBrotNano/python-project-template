# Kommentar in Python

# Mehrzeiliger Kommentar
"""
Kommentar 1
Kommentar 2
"""

"""
Kommentar 1
Kommentar 2
"""

# Ausgabe auf der Konsole mit der Funktion print()
print(
    'Hello "Python"!'
)  # \ leitet eine Escape-Sequenze ein, hier um " zu maskieren, so daß diese nicht interpretiert werden
print("Hello Python!")
print('Hello "Python"!')  #
print('Hello "\'Python"!')  # um ' zu maskieren
print("Hello \nPython!")  # \n => "newline" (Zeilenumbruch)
# vgl. Escape-Sequenzen: https://www.w3schools.com/python/gloss_python_escape_characters.asp

#
print("Hello", "Python", "!")
print("Hello", "Python", "!", sep="_", end="")  # Statt Leerzeihen _ und statt \n => ""
# sep und end sind sogenannte Keyword-Parameter
# "Hello","Pyhton","!" sind Postionale Parameter

# Variablen in Pyhton
# In Variablen(Container) kann man Werte Ablegen

vorname = "Peter"  # str
alter = 33  # int

alter = alter + 1
alter += 1  # Kurzschreibweise

vorname = input("\nWie ist dein Name?")
print("\nHallo", vorname, ", herzlichen Glückwunsch zum ", alter, "zigsten !")

alter = input("Wie alt bist Du?")  # input liefert einen str


# alter += 1 # => TypeError: can only concatenate str (not "int") to str
alter = int(alter) + 1  # Typecast in int
alter = str(alter)  # Typecast in str

# print("\nHallo",vorname,", herzlichen Glückwunsch zum ", alter,"zigsten !")
begruessung = (
    "Hallo " + vorname + " , herzlichen Glückwunsch zum " + alter + " zigsten !"
)  # Strings-Verknüpfen mit +
print(begruessung)


# Datentyp abfragen mit type()
print(type(alter), type(vorname), type(33))

# weitere Datentypen float,bool
gewicht = 82.5  # float (merkmal ist der Punkt)
ist_online = True  # bool ("True" oder "False")
print(type(gewicht), type(ist_online))
