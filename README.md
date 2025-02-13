# Datahantering
## insamling hårdvara
- Datan kommer att samlas in via en rörelsesensor kopplad till rasberry pico w.
- När sensorn triggas så skickar den enbart data med klockslag, datum och avstånd.
- För att spara ström och bandbredd, formaterar vi datan i en json fil innan vi skickar iväg den från picon. Enkelt att formatera dictonarie/map till json fil.
## Skicka datan från hårdvara till en broker-server.
- för att spara på picons energi skickar vi datan till en mqtt-broker som dirigerar vidare datan om den ska till en client direkt eller till en databas.
- 



