# Verysure

**TTFHW**
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

- Gå in på USB enheten. Klicka på INDEX.HTM Ladda ner den senaste firmware-filen(UF2 för Raspberry Pi Pico W)

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



1. Översiktsdiagram (High-Level Architecture Diagram)
- Syfte: Ge en övergripande bild av hela loT-systemet.
- Innehäll:
- Enheter (sensorer, aktuatorer, gateways).
- Kommunikationskanaler (Wi-Fi, Zigbee, Bluetooth).
- Molntjänster och databaser.
- Användargränssnitt (mobilappar, webbapplikationer).
- Exempel:
- Sensor → Gateway → Molnplattform → Användare.

2. Nätverksdiagram
- Syfte: Visualisera kommunikationsflöden och nätverkstopologi.
- Innehäll:
- Trädbundna och trädlösa nätverk (LAN, WAN, Wi-Fi, 4G/5G).
- Protokoll som MQTT, COAP, HTTP, eller WebSocket.
- Routrar, gateways och nätverksnoder.
- Exempel:
- Enheternas anslutning till nätverket och kommunikationen med molntjänster.

3. Datadiagram
- Syfte: Visa hur data samlas in, bearbetas, lagras och analyseras.
- Innehäll:
- Datakällor (sensorer).
- Dataflöde till bearbetning (real-time eller batch).
- Lagring (databaser, molnbaserade lösningar).
- Dataanalys och visualisering.
- Exempel:
- Sensor → Data Processor → Data Warehouse → Analytics Dashboard.

4. Flödesdiagram (Workflow Diagram)
- Syfte: Beskriva logiken och arbetsflöden i loT-systemet.
- Innehäll:
- Händelsekedjor, t.ex. "om temperatur > X, aktivera fläkt".
- Processer som styrs av loT-enheter.
- Exempel:
- Temperaturavkänning Aktuatoraktivering → Data-loggning.

5. Säkerhetsdiagram
- Syfte: Visualisera säkerhetsätgärder och särbarheter i systemet.
- Innehäll:
- Kryptering av data (TLS/SSL, AES).
- Autentiserings- och auktoriseringsprocesser.
- Nätverkssäkerhet (firewalls, VPN, loT-specifika säkerhetslager).
- Exempel:
-  Sensor → Krypterad Gateway → Krypterad Molntjänst.

6. Deployment Diagram
- Syfte: Beskriva var systemets olika komponenter finns placerade.
- Innehäll:
- Fysiska och virtuella noder (sensornätverk, molnservrar, databaser).
- Kartläggning av nätverkets topologi.
- Exempel:
- Lokala sensorer → Gateway pà plats → Molnserver.

7. Skalbarhetsdiagram
- Syfte: Planera och visa hur systemet kan växa över tid.
- Innehäll:
- Beskrivning av hur fler enheter, användare eller datamängder hanteras.
- Mekanismer för att hantera högre belastning.
- Exempel:
- Lägga till fler sensorer eller gateways utan att päverka prestanda.
