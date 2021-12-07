#Variabler
antal_pennor = int(input("Hur många pennor vill du köpa?"))
pennor_pris = int(input("Ange priset för pennor"))
total_kostnad_pennor = antal_pennor * pennor_pris

antal_äpplen = int(input("Hur många äpplen vill du köpa?"))
kilo_vikt_äpplen = int(input("Ange vikt för äpplen"))
kilo_pris_äpplen = int(input("Ange pris för äpplen"))
total_kostnad_äpplen = antal_äpplen * kilo_vikt_äpplen/1000 * kilo_pris_äpplen

#Utskriften
print(f"Jag handlade {antal_pennor} pennor med priset {pennor_pris:.2f} kronor, för kostnaden av " 
    f"{total_kostnad_pennor:.2f} kronor och {kilo_pris_äpplen:.3f}kg äpple med "
    f"kilopriset {kilo_pris_äpplen:.2f} för {total_kostnad_äpplen:.2f} kronor."
    f"\nDen totala summan av detta blev {total_kostnad_pennor + total_kostnad_äpplen:.2f} kronor.")

