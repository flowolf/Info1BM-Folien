# 706.088 Informatik 1
Softwareentwicklungsprozesse
  * DI Johanna Pirker


* Buchempfehlung
  * **Software Engineering 10**
  * **Ian Sommerville**
<p class=wikipedia style="text-align:left;width:60%;left:0em;position: relative;"><img src="https://www.pearsonhighered.com/assets/bigcovers/0/1/3/3/0133943038.jpg" alt="book cover"></p>



# Software-entwicklung


## Definition Softwareentwicklung 
* **Software** = Computerprogramm + Dokumentation eventuell entwickelt für einen speziellen Markt
* **Gute Software** = Funktionalität, Performance, Benutzbarkeit und Wartbarkeit


## Software-entwicklung vs. Informatik
* **Softwareentwicklung** = Disziplin, welche alle Aspekte der Softwareproduktion beinhaltet
* **Informatik** = Beschäftigt sich mit der Theorie und Grundlagen, Softwareentwicklung beschäftigt sich mit den Arten der Entwicklung und Lieferung von benutzbarer Software


## Systementwicklung
* **System Engineering** = beinhaltet zusätzlich auch alle computer-basierten Systeme (Hardware, Sofware, Prozesse) 


## Attribute Guter Software
* Wartbarkeit
* Zuverlässigkeit 
* Sicherheit
* Effizienz und Performance 
* Angemessenheit, Benutzerfreundlichkeit, Kompatibilität, Verständlich 


## Arten von Anwendungen 
* Eigenständige Anwendungen
* Web-Anwendungen 
* Embedded Control Systems
* Batch Processing 
* Entertainment 
* Modellierungen und Simulationen 
* Datenerfassung und -sammlung
* ... 



# Software-entwicklungs-prozess


## Prozess (1/2)
* **(1) Spezifikation**: 
 Funktionalitäten und Auflagen identifizieren und definieren
* **(2) Design und Implementierung**: 
 Software, welche den Spezifikationen entspricht wird entwickelt 


## Prozess (2/2)
* **(3 Verifikation & Validierung**: 
 Die Software wird getestet, ob die den Spezifikationen der Stakeholder (e.g. Kunden) entspricht
* **(4) Weiterentwicklung**: 
 Anpassung an sich ändernde Kundenwünsche 


<a href="http://www.sandraandwoo.com/2012/11/19/0430-software-engineering-now-with-cats/" target="_blank"><p class=wikipedia style="text-align:center;width:100%;center:0em;position: relative;"><img src="http://www.sandraandwoo.com/comics/2012-11-19-0430-software-engineering-now-with-cats.png" alt="reality"></p></a>



# Vorgehensmodelle


## Vorgehensmodelle
* abstrakte Repräsentation vom Softwareentwicklungsprozess
* für große Projekte Mischformen


## Vorgehensmodelle
* Wasserfall Modell (Trennung der Prozesse)
* Evolutionäre Entwicklung / Iterative Entwicklung 
* Komponentenbasierte Entwicklung mit Wiederverwertung
* Agile Softwareentwicklung 
 * Extreme Programming
 * SCRUM
* ...  


## Wasserfallmodell
<p class=wikipedia style="text-align:left;width:100%;left:0em;position: relative;"><a target="_blank" href="https://commons.wikimedia.org/wiki/File:Waterfall_model-de.svg#/media/File:Waterfall_model-de.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Waterfall_model-de.svg/1200px-Waterfall_model-de.svg.png" alt="Waterfall model-de.svg"></a><br>Von Paul Hoadley, Paul Smith and Shmuel Csaba Otto Traian, <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=29119277">Link</a></p>


## Wasserfallmodell
* Vorteile: 
 * klar getrennte Phasen
 * definierte Zeitplunkte für Prozessschritte 
* Nachteile: 
 * frühe Festlegung der gesamten Funktionalität
 * spätere Änderungen kostspielig


## Iterative und Inkrementelle Entwicklung
* Iterativ: Schrittweise Annäherung an die Lösung (Verändern)
* Inkrementell: Kleine Stufen der Zunahme (Hinzufügen)


## Iterative und Inkrementelle Entwicklung
<p class=wikipedia style="text-align:left;width:100%;left:0em;position: relative;"><a target="_blank" href="https://commons.wikimedia.org/wiki/File:Iterative_development_model.svg#/media/File:Iterative_development_model.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Iterative_development_model.svg/1200px-Iterative_development_model.svg.png" alt="Iterative development model.svg"></a><br>Von <a href="//commons.wikimedia.org/wiki/User:Aflafla1" title="User:Aflafla1">Aflafla1</a> - Iterative development model V2.jpg , User:Westerhoff, <a href="http://creativecommons.org/publicdomain/zero/1.0/deed.en" title="Creative Commons Zero, Public Domain Dedication">CC0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=34159246">Link</a></p>


## Iterative und Inkrementelle Entwicklung 
* Anwendung bei kleinen bis mittleren Projekten 
* Vorteile: 
 * Schrittweise Spezifikation
 * Kosten und Aufwand bei Anforderungsänderung geringer 
 * Zunehmendes Verständnis des Kunden
 * Schnelleres Deployment von funktionstüchtiger Software an den Kunden (mit Grundfunktionalitäten)


## Iterative und Inkrementelle Entwicklung 
* Nachteile: 
 * Projektfortschritt schwer messbar (Manager benötigen Deliverables um Fortschritt zu messen)
 * Dokumentation muss ständig aktualisiert werden
 * Ohne Refactoring zwischen den Iterationen wird die Systemstruktur kompliziert und zukünftige Änderungen werden teurer


## Live-Beispiel
* Jetzt zu 2. oder zu 3. "Schere Stein Papier" spielen  
 * Wie gut funktioniert es? Macht es Spass?
 * Eine Regel ändern oder eine neue Regel hinzufügen 
 * noch einmal spielen
 * Wie gut funktioniert es? Macht es Spass?



# Agile Software-entwicklung


## Agile Softwareentwicklung
* Ziel: Flexibilität 


## Extreme Programming
* Agile Methode von Beck (2000)
 * Schrittweise Planung
 * Mini-Releases
 * Simples Design 
 * Refactoring 
 * Test-First Entwicklung
 * Pair Programming 
 * “Kunde” bei Entwicklungsteam 
 * Ständige Integration 


##SCRUM 
<p class=wikipedia style="text-align:left;width:100%;left:0em;position: relative;"><a target="_blank" href="https://commons.wikimedia.org/wiki/File:Scrum_process-de.svg#/media/File:Scrum_process-de.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Scrum_process-de.svg/1200px-Scrum_process-de.svg.png" alt="Scrum process-de.svg"></a><br>Von <a href="//commons.wikimedia.org/wiki/File:Scrum_process.svg" title="File:Scrum process.svg">Scrum_process.svg</a>: <a href="//commons.wikimedia.org/w/index.php?title=User:Lakeworks&amp;action=edit&amp;redlink=1" class="new" title="User:Lakeworks (page does not exist)">Lakeworks</a>
derivative work: <a href="//commons.wikimedia.org/wiki/User:Sebastian_Wallroth" title="User:Sebastian Wallroth">Sebastian Wallroth</a> (<a href="//commons.wikimedia.org/wiki/User_talk:Sebastian_Wallroth" title="User talk:Sebastian Wallroth"><span class="signature-talk">talk</span></a>) - <a href="//commons.wikimedia.org/wiki/File:Scrum_process.svg" title="File:Scrum process.svg">Scrum_process.svg</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=10772971">Link</a></p>


## SCRUM 
* Agiles Projektmanagement
* Sprints: ca 2-4 Wochen 
* Produkt Backlog: Liste von Aufgaben für das Projekt als Planungsstartpunkt
* Selection Phase: Features/Funktionalitäten für Sprint zusammen mit Kunde gewählt
* Development: mit “Daily Meetings” /7 Scrum Master
* Review (Code Review): Ende von Sprint 


## SCRUM 
* Vorteile: 
 * Produkt ist unterteilt in verschiedene überschaubare und verständliche Teile
 * Hohe Fexibilität
 * unrealisierbare Anforderungen schnell identifiziert 
 * Transparenz und Vertrauen durch regelmäßige Kommunikation
 * Vertrauen zwischen Kunde und Entwickler, 
 * Kurze Kommunikationswege 


 ## SCRUM 
* Nachteile:
 * Gesamtüberblick schwierig 
 * Hoher Kommunikationsaufwand 
 * Zeitverlust bei schlechten Sprintplanungen
 * Schwieriger Umsetzbar bei Großprojekten (Höherer Koordinationsaufwand erfordert)  


## Literatur
* Extreme Programming Explained. (Kent Beck, Addison-Wesley, 2000.)
* Running an Agile Software Development Project. (M. Holcombe, John Wiley and Sons, 2008.)
* Get Ready for Agile Methods, With Care. (B. Boehm, IEEE Computer, January 2002.) http://doi.ieeecomputersociety.org/10.1109/2.976920.



# (1) Spezifikation


## Softwareanforderungen
* Lastenheft oder Product Backlog 
 * Customer Requirement, Anforderungen beschreiben) 
* Pflichtenheft -> Design 
 * Development Requirement, wie lösen


## Softwareanforderungen
* Funktionale Anforderungen
 * „Das Produkt soll den Saldo des Kontos am ersten des Monats berechnen.“
* Nichtfunktionale Anforderungen
 * „Das Produkt soll dem Anwender innerhalb von einer Sekunde antworten.“
 * Benutzbarkeit, Zuverlässigkeit, Effizienz, Änderbarkeit, Wartbarkeit, ..


## Anforderungsspezifikation laut IEEE 
* korrekt
* unzweideutig (eindeutig)
* vollständig
* widerspruchsfrei
* bewertet nach Wichtigkeit und/oder Stabilität
* verifizierbar
* modifizierbar
* verfolgbar (traceable)



# (2) Design und Implementierung


## Systemdesign



# (3) Verifikation & Validierung


##  Verifikation & Validierung
* **Validierung**: “Entwickeln wir das richtige Produkt?”
 * wird den Kundenerwartungen entsprochen? 
* **Verifikation**: “Entwickeln wir das Produkt korrekt?”
 * entspricht die Software den Anforderungen?


## Verifikation & Validierung
*  Software Inspektion
 * Review von Spezifikation, Design und Code
 * Programmcode wird überprüft (Statischer Ansatz) 
* Software Test
 * Programm „läuft“ mit Testdaten (Dynamischer Ansatz)
 * Ausgaben und Laufverhalten wird überprüft



# (4) Weiterentwicklung


## Softwareweiterentwicklung
* Neue und veränderte Anforderungen machen Weiterentwicklung notwendig


## Softwareweiterentwicklung
* Fehlerbehebung
 * Sourcecode-Fehler (geringster Aufwand)
 * Desing-Fehler (mittlerer Aufwand) 
 * Requirement-Fehler (größter Aufwand)
* Softwareanpassung an
 * diverse Plattformen
 * neue Systemumgebung
* Funktionsanpassungen u. Erweiterungen (z.B. Gesetzesänderung) 


## Sonderfall: Legacy Systeme (Altsystem)
* In der Vergangenheit entwickelt
* historisch gewachsten
* oft in veralteter Technologien und Programmiersprachen
* meist aufwendige und kostenintensive Systeme
* oft in Unternehmensabläufe verwoben
* Zunehmender Aufwand b. Weiterentwicklung



# Debugging und Fehlersuche


## Fehlertypen
* Artithmetische Fehler
 * Division durch null
 * Precision (schlechtes Runden, e.g. float to int) 
 * Arithmetischer Überlauf

32 Bit (Signed) Integer:
```python

2.147.483.647 + 1 =  -2.147.483.648 

( 01111111 11111111 11111111 11111111 
                                 + 1 = 
= 10000000 00000000 00000000 00000000 )
```


## Fehlertypen
* Logikfehler 
 * Endlosschleifen 
 * Endlose Rekursionen 
 * Off-by.one error in Arrays (OBOE)
* Syntax 

```python
 * a = 0 vs a ==0 
```


## Fehlertypen
* Ressourcen 
 * Null pointer dereferece
 * Falscher Datentyp 
* Interface Errors
 * Interface Misure 
 * Interface Misunderstanding 
 * Timing Errors 


 ## Fehlertypen
* Performance 
 * Runtime Errors / Multi-Threading
 * Deadlock 
 * Race Condition 
 * Mutual Exclusion,... 



# Fragen?

