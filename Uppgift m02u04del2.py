antal_pennor= int(input("Hur många pennor vill du köpa? "))
pris_pennor= int(input("Hur mycket ska pennorna kosta per styck ?"))
total_kostnad_pennor = antal_pennor * pris_pennor

vikt_äpple= int(input("Hur många gram av äpple vill du köpa? "))
vikt_kilo_äpple= vikt_äpple/1000
pris_äpple_kilo=int(input("Ange kilopris för äpplen: "))
total_kostnad_äpple= vikt_kilo_äpple * pris_äpple_kilo 

a1 = f"Penna, {antal_pennor}st á {pris_pennor:.2f}kronor"
a2 = f"{total_kostnad_pennor:.2f}kronor"
a3 = f"Äpple, {vikt_kilo_äpple:.3f}kilo á {pris_äpple_kilo:.2f}kronor"
a4 = f" {total_kostnad_äpple:.2f}kronor"
a5 = f"{total_kostnad_äpple + total_kostnad_pennor:.2f}kronor"

print(f"n\nKvitto\n------------------------------")
print(f"{a1:30s}{a2:>10s}")
print(f"{a3:30s}{a5:>10s}")
print(f"------------------------------")
print(f"{'summa':30s}{a5:>10s}")