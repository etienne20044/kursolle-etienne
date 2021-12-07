exchange_rate_dollar_to_sek = 8.82
print("Detta är ett program där vi kan växla mellan SEK & dollar")
en_sek = float(input("Hur många SEK vill du växla till dollar: "))
dollar = en_sek / exchange_rate_dollar_to_sek
print("Du ville växla {0:.2f} SEK vilket blir {1:.2f} dollar.".format(en_sek, dollar))

#Fel i rad 1: Fel i variabeln: De satte inte ihop.
#Fel i rad 1: Står "," istället för "."
#Fel i rad 2: Saknar citattecken runt stängen.
#Fel i rad 3: