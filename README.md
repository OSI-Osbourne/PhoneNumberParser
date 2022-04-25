# PhoneNumberParser
PhoneNumberParser for the lecture Software Quality at DHBW Horb

## Versionierung
* V1.0 | 30.03.2022 -> Initiale Erstellung
* V1.1 | 24.04.2022 -> Hinzufügen von Story 1, 2 und 3

## Getting Started

## Systemvoraussetzungen
* Python 3.10.*: https://www.python.org/downloads/
* Betriebssystem mit GUI: Windows, Linux, MacOS

  
## Nutzung
* Installieren der requirements.txt
  * Navigiere in den Projektordner wo die requirements.txt vorhanden ist und öffne dort eine Konsole bzw. navigiere über die Konsole
  * folgenden Befehl nutzen: pip install -r requirements.txt
* main.py ausführen
  * Navigiere in den Projektordner und öffne eine Konsole
  * folgenden Befehl nutzen: python3 main.py

## Projektarchitektur
![Projektarchitektur](https://i.imgur.com/cV6LrUX.png)
![Projektarchitektur](https://i.imgur.com/A4YK0kU.png)

## User-Stories

### Story 1 - Erweiterung des CRM-Systems 
Als Mitarbeiter möchte ich eine Lösung in der Form einer Benutzerapplikation, welche mich bei der Aufbereitung von Telefonnummern bei der täglichen Arbeit unterstützt und diese je nach Anwendungsfall optimiert.
> **Status:** Abgeschlossen
> 
> **Prio:** Hoch
> 
> **Story Points:** 2
> 
> **Autor**: Kevin Schock

#### Akzeptanzkriterium:
Die Optimierung ist erfolgreich, wenn die Telefonnummer vom System erkannt wird. Die Optimierung ist optimal, wenn die Telefonnummer in Landesvorwahl, Ortsvorwahl, Hauptnummer und ggf. Durchwahl ausgegeben werden kann.

---
### Story 2 - Telefonnummer für Beratung optimieren
Als Sachbearbeiter möchte ich eine Lösung, in die ich eine beliebe Telefonnummer, z. B. in der Form +49(187)-42031-69, eintragen kann und mir diese optimiert für die weitere Verarbeitung ausgeben lassen kann.
> **Status:** Abgeschlossen
> 
> **Prio:** Hoch
> 
> **Story Points:** 3
> 
> **Autor**: Kevin Schock

#### Akzeptanzkriterium:
Die Optimierung ist erfolgreich, wenn die Telefonnummer vom System erkannt wird. Die Optimierung ist optimal, wenn die Telefonnummer in Landesvorwahl, Ortsvorwahl, Hauptnummer und ggf. Durchwahl ausgegeben werden kann.

---
### Story 3 - Telefonnummer für Analyse optimieren
Als Analyst möchte ich eine Lösung, in die ich eine beliebe Telefonnummer, z. B. in der Form +49(187)-42031-69, eintragen kann und mir diese optimiert für weitere Auswertungen ausgeben lassen kann.

> **Status:** Abgeschlossen
> 
> **Prio:** Hoch
> 
> **Story Points:** 2
> 
> **Autor**: Kevin Schock

#### Akzeptanzkriterium:
Die Optimierung ist erfolgreich, wenn die Telefonnummer vom System erkannt wird. Die Optimierung ist optimal, wenn die Telefonnummer in einem strukturierten Format ausgegeben werden kann.

---
## Definition of Done (DoD)
* Alle Akzeptanzkriterien für jede User-Story wurden Implementiert.
* Die Implementierten Funktionen wurden getestet, Tests mit den Beispielhaften Testdaten wurden durchgeführt. 
* Bugs und fehlende Features wurden überarbeitet und in der Gruppe ausgetauscht.
* Code wurde aussagekräftig kommentiert und die Software-Architektur festgehalten.
* Benutzerfreundlichkeit an Releaseversion getestet und verifiziert.  
* Release Note basierend auf Releaseversion verfasst. 

---
## Testfälle

| Eingabe                        | Ländervorwahl (erwartet) | Ortsvorwahl (erwartet) | Rufnummer (erwartet) | Durchwahl (erwartet) | Strukturiert (erwartet) | ISO-Kürzel (erwartet) | Check   |
|--------------------------------|--------------------------|------------------------|----------------------|----------------------|-------------------------|-----------------------|---------|
| +49 0201 123456                | +49                      | 0201                   | 123456               | ─                    | +49 0201 123456         | DE                    | &check; |
| +44 0201123456                 | +44                      | 0201                   | 123456               | ─                    | +44 0201 123456         |                       | &check; |
| 0033 0201/123456               | +33                      | 0201                   | 123456               | ─                    | +33 0201 123456         |                       | &check; |
| 0049201123456                  | +49                      | 2011                   | 23456                | ─                    | +49 2011 23456          | DE                    | &check; |
| (0)201 1234 56                 | +49                      | 201                    | 1234                 | 56                   | +49 201 1234-56         | DE                    | &check; |
| +49 (941) 790-4780             | +49                      | 941                    | 790                  | 4780                 | +49 941 790-4780        | DE                    | &check; |
| 015115011900                   | +49                      | 1511                   | 5011900              | ─                    | +49 1511 5011900        |                       | &check; |
| +91 09870987 899               | +91                      | 0987                   | 0987                 | 899                  | +91 0987 0987-899       |                       | &check; |
| [+49] (0)89-800/849-50         | +49                      |                        |                      |                      | +49 89-800 849-50       |                       | &check; |
| +49 (8024) [990-477]           | +49                      | 8024                   | 990                  | 477                  | +49 8024 990-477        | DE                    | &check; |

* Invalide Eingabe: Findet eine leere Eingabe statt oder entspricht die Eingabe nicht dem Standard wird eine Fehlermeldung ausgegeben.