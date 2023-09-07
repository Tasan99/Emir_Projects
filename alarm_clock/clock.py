import time
import datetime

from playsound import playsound

CLEAR= "\033[2J"
CLEAR_AND_RETURN="\033[H"



def function(seconds):
    time_elapsed=0
    print(CLEAR)
    while time_elapsed<=seconds:
        time.sleep(1)
        time_elapsed+=1
        if time_elapsed == seconds:
            playsound("sound.mp3")
            break
        print(f"{CLEAR_AND_RETURN} {time_elapsed} {seconds}")










zaman_girdisi = input("Lütfen zamanı girin (SS:DD:SN): ")
zaman_formati = "%H:%M:%S"

zaman_objesi = datetime.datetime.strptime(zaman_girdisi, zaman_formati).time()
print("Girilen zaman:", zaman_objesi)

suanki_zaman = datetime.datetime.now()
suan_saat = suanki_zaman.hour
suan_dakika = suanki_zaman.minute
suan_saniye = suanki_zaman.second

alarm_saat = zaman_objesi.hour
alarm_dakika = zaman_objesi.minute
alarm_saniye=zaman_objesi.second

kalan_saat=(alarm_saat-suan_saat)
kalan_dakika=(alarm_dakika-suan_dakika)
kalan_saniye=(alarm_saniye-suan_saniye)
seconds=kalan_saat*3600 + kalan_dakika*60+ kalan_saniye
function(seconds)

