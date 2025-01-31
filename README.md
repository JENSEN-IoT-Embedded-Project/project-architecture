# Verysure

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

- Håll ned BOOTSEL-knappen på Pico W och anslut den till dator med en USB-kabel. Släpp BOOTSEL-knappen när enheten visas som en USB-enhet på dator.

-ers/ludvignorin/ws/temporary/reactiongame.py'Ladda ner den senaste firmware-filen för Raspberry Pi Pico W från MicroPython-webbplatsen

- Dra och släpp den nedladdade firmware-filen till den anslutna enheten. Pico W kommer att starta om och vara redo att använda MicroPython.

## Installera Thonny IDE:

- Ladda ner och installera Thonny på dator från Thonny-webbplatsen.
  ```bash
    sudo apt install thonny
  ```
  **Via länk**
  <https://thonny.org/> 

- Öppna Thonny och gå till "Tools" > "Options" > "Interpreter".

- Välj "MicroPython (Raspberry Pi Pico)" som interpreter och välj rätt port för anslutna Pico W.

## Anslut Pico W:

- Anslut din Raspberry Pi Pico W till datorn med en USB-kabelm(om du inte reda gjort). Se till att Thonny IDE känner igen enheten.

## Skriv och kör kod:

- Använd Thonny IDE för att skriva MicroPython-kod. Här är ett exempel på kod för att blinka en LED:

```python
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
```
- Spara och kör koden i Thonny. LED:en på Pico W kommer att blinka på och av varje sekund.
