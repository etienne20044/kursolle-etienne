#Variabler
antal_pennor = 3
kostnad_pennor = 4 
total_kostnad_pennor = antal_pennor * kostnad_pennor

antal_äpple = 1
vikt_äpple = 200
kostnad_äpple_per_kg = 16
total_kostnad_äpple = antal_äpple * vikt_äpple/1000 * kostnad_äpple_per_kg

#Kommatecken
print("Jag har handlat", antal_pennor, "pennor för", total_kostnad_pennor, "kronor och", antal_äpple, "äpple för", total_kostnad_äpple, "kronor vilket tillsammans blev", total_kostnad_pennor + total_kostnad_äpple, "kronor.")

#Plustecken
print("Jag har handlat " + str(antal_pennor) + " pennor för " + str(total_kostnad_pennor) + " kronor och " + str(antal_äpple) + " äpple för " + str(total_kostnad_äpple) + " kronor vilket tillsammans blev " + str(total_kostnad_pennor + total_kostnad_äpple) + " kronor.")

#Strängen byggs upp
s = "Jag har handlat " + str(antal_pennor) + " pennor för " + str(total_kostnad_pennor)
s += " kronor och " + str(antal_äpple) + " äpple för " + str(total_kostnad_äpple)
s += " kronor vilket tillsammans blev " + str(total_kostnad_pennor + total_kostnad_äpple) + " kronor."
print(s)

#Öppen print
print("Jag handlade " + str(antal_pennor) + " pennor för " + str(total_kostnad_pennor), end="")
print(" kronor och " + str(antal_äpple) + " äpple för " + str(total_kostnad_äpple), end="")
print(" kronor vilket tillsammans blev " + str(total_kostnad_pennor + total_kostnad_äpple) + " kronor.")

#Formatmetoden
print("Jag handlade {0} pennor för {1} kronor och {2} äpple för {3:.2f} kronor vilket totalt blev {4:.2f}kronor."
    .format(antal_pennor, total_kostnad_pennor, antal_äpple, total_kostnad_äpple, 
    total_kostnad_äpple + total_kostnad_pennor))

#Fstringmetoden
print(f"Jag handlade {antal_pennor} pennor för {total_kostnad_pennor} kronor och {antal_äpple} äpple för "
    f"{total_kostnad_äpple:.2f} kronor vilket totalt blev {total_kostnad_pennor + total_kostnad_äpple:.2f} kronor.")
