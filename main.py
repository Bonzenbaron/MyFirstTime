name = input("Bitte gebe den Namen des Empfängers ein: ")
mein_name = input("Bitte gebe deinen Namen ein: ")
age = input("Bitte gebe dein Alter ein: ")
city = input("Bitte gebe deine Stadt ein: ")
gender = input("Ist der Empfänger Männlich oder Weiblich? ")
if gender == "Männlich":
    print("Sehr geehrter Herr " + name + ", ")
elif gender == "Weiblich":
    print("Sehr geehrte Frau " + name + ", ")
else:
    print("Okay. Dann nehmen wir Divers")
    print("Sehr geehrte/er Herr/Frau/Divers " + name + ", ")
print(" ")
print("Mein Name ist " + mein_name + " und ich bin " + age + " Jahre alt.")
print("Ich komme aus der Stadt " + city + ".")
input("Bitte beliebige Taste drücken...")