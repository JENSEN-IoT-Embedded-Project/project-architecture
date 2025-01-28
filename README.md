# Verysure
# Head 1
*Test*
Uppgift: Beskriv alla komponenter som behövs i verysure readme.

#KOMPONENTER: För ett blink program

## Hårdvara

- Raspberry Pi Pico W

- Kopplingsdäck och Jumper-kablar

- LED

- Motstånd

- USB_kabel

## Mjukvara

- MicroPython

- Thonny IDE

# DoD: Fullständig beskrivning av all hårdvara och mjukvara som behövs för blink:

## Hårdvara:
- Raspberry Pi Pico W: Huvudmikrokontrollern för vårt projekt.

- Kopplingsdäck och Jumper-kablar: För att ansluta komponenterna.

- LED: Lysdioden som ska blinka.

- Motstånd: För att begränsa strömmen till LED:en och förhindra att den brinner ut.

- USB-kabel: För att ansluta Raspberry Pi Pico W till din dator för programmering och strömförsörjning.

## Mjukvara:

- MicroPython: Ett lättviktigt Python-implementering för mikrocontrollers.

- Thonny IDE: En användarvänlig integrerad utvecklingsmiljö (IDE) för MicroPython.


# Steg-för-steg-guide:

## Installera MicroPython:

- Ladda ner den senaste firmware-filen för Raspberry Pi Pico W från MicroPython-webbplatsen

- Håll ned BOOTSEL-knappen på Pico W och anslut den till dator med en USB-kabel. Släpp BOOTSEL-knappen när enheten visas som en USB-enhet på dator.

- Dra och släpp den nedladdade firmware-filen till den anslutna enheten. Pico W kommer att starta om och vara redo att använda MicroPython.

## Installera Thonny IDE:

- Ladda ner och installera Thonny på dator från Thonny-webbplatsen.

- Öppna Thonny och gå till "Tools" > "Options" > "Interpreter".

- Välj "MicroPython (Raspberry Pi Pico)" som interpreter och välj rätt port för anslutna Pico W.

## Anslut Pico W:

- Anslut din Raspberry Pi Pico W till datorn med en USB-kabel. Se till att Thonny IDE känner igen enheten.

## Skriv och kör kod:

- Använd Thonny IDE för att skriva MicroPython-kod. Här är ett exempel på kod för att blinka en LED:

from machine import Pin
from utime import sleep

pin = Pin(15, Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")

- Spara och kör koden i Thonny. LED:en på Pico W kommer att blinka på och av varje sekund.
