# coding=utf-8


print "~~ Unsere Tagesgerichte ~~"

Tagesgerichte = {}

while True:
    Tagesgericht = raw_input("Name des Tagesgerichts: ")
    Preis = raw_input("Preis für %s: " % Tagesgericht)
    Tagesgerichte[Tagesgericht] = Preis

    neu = raw_input("Möchten Sie noch ein weiteres Gericht hinzufügen? Antworten Sie 'Ja' oder 'Nein'")

    if neu == "Nein" or neu == "nein":
        break


print "Tagesgerichte: %s" % Tagesgerichte


with open("menu.txt", "w+") as Tagesgerichte_file:
    for Gericht in Tagesgerichte:
        Tagesgerichte_file.write("%s, %s EUR\n" %(Gericht, Tagesgerichte[Gericht]))

