nimi = str(input("Sisestage oma nimi:"))
lubatud_kiirus = int(input("Sisestage lubatud kiirus km/h:"))
tegelik_kiirus = int(input("Sisestage tegelik kiirus km/h:"))
kordaja = int(3)
trahv = int((tegelik_kiirus - lubatud_kiirus) * kordaja)
toene_trahv = min(190, trahv)
tekst = str(nimi + ", kiiruse ületamise eest on teie trahv: " +str(toene_trahv) + " eurot.")
print(tekst)