Datahantering för Rörelsesensor IoT-projekt

***Insamling av Hårdvara***
Rörelsesensor: Kopplad till en Raspberry Pi Pico W.

**Trigger Villkor:** Data sparas och skickas endast när sensorn triggas.

**Dataformat: **När sensorn triggas skickas data som inkluderar enhets-ID, klockslag, datum och avstånd till en MQTT-broker.

**JSON-formatering:** För att minska trafiken och snabba upp behandlingen formateras datan till JSON på Pico.
**
***Dataöverföring*****
**MQTT-protokoll:** Data skickas från hårdvaran till en MQTT-broker.

**Molnlösning eller Raspberry Pi:** Alternativ inkluderar moln-MQTT-tjänster (t.ex. HiveMQ, EMQX, Adafruit IO, AWS IoT) eller en Raspberry Pi.

**Prenumeration:** MQTT-brokern prenumererar på data från varje enhets-ID.

**Routning:** När en förfrågan har besvarats, dirigeras meddelande direkt med information till klient/app/webbserver/SMS.

**Lagring i Databas:** Data lagras i en relationsdatabas kopplad till varje användare.

***Databasval***
**SQLite:**

Användning: Lätt att använda och komma igång med. Passar för att lagra användarrelaterad data och sensorhändelser.

**Tidsseriedatabas:**

Användning: Bra för tidsstämplad data, sparar data för specifika enheter.

Förslag: Använd InfluxDB för att hantera stora volymer av tidsstämplad data effektivt.

**Dokumentorienterad Databas:**

Användning: Lagrar data i JSON-liknande format. Kan enkelt skalas ut med fler servrar.

Förslag: Använd MongoDB för flexibel datahantering och höga prestandakrav.

**Key-Value Store:**

Användning: Enkel åtkomst och hantering av data.

Förslag: Använd Redis för snabba läs- och skrivoperationer.

Användning av Data
Syfte: Se tidsstämplar på när ett potentiellt inbrott har ägt rum för att underlätta polisens arbete med att följa potentiell inbrottstjuv.

**Notifieringar:** Användaren notifieras omedelbart när något har hänt.

***Sammanfattning***
**Lagringsbehov: **För en hanterbar mängd data med en sensor är SQLite ett bra val för enkelhet och snabb implementering. För större datavolymer och mer komplexa behov kan InfluxDB eller MongoDB övervägas.

**Transport:** Data skickas från sensorn till en MQTT-broker som prenumererar på data och dirigerar den till rätt mottagare och lagringssystem.

**Användning och Analys:** Data används för att övervaka och notifiera användare, samt analysera trender och händelser för säkerhetsändamål
