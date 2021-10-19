vanus = int(input("Sisesta oma vanus: "))
sugu = input("Sisesta oma sugu: ")
if sugu == "M" or sugu == "m":
    max_pulsi_sagedus = 220 - vanus
if sugu =="N" or sugu =="n":
    max_pulsi_sagedus = 220 - vanus * 0.88
treening = int(input("Sisesta treeningu tüüp: "))
if treening == 1:
    min_puls = max_pulsi_sagedus * 0.5
    max_puls = max_pulsi_sagedus * 0.7
elif treening == 2:
    min_puls = max_pulsi_sagedus * 0.7
    max_puls = max_pulsi_sagedus * 0.8
elif treening == 3:
    min_puls = max_pulsi_sagedus * 0.8
    max_puls = max_pulsi_sagedus * 0.87
min_puls = round(min_puls)
max_puls = round(max_puls)
print("Pulsisagedus peab olema vahemikus " + str(min_puls) + " ja " + str(max_puls) + " vahel.")
    