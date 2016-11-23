# 706.088 Informatik 1
Fehlerbehandlung, Funktionsweise eines Computers


* Wiederholung:
  * Binärzahlen
  * Binär rechnen
* Fehler-behandlung in Python
* Funktionsweise eines Computers



# Binärzahlen


# Binär rechnen
* addieren
* subtrahieren
  * 2er Komplement
* multiplizieren
* dividieren


# Binär rechnen
* Bit Operatoren
  * shiften
  * AND
  * OR
  * XOR



# Fehler-behandlung in Python


## Fehlerbehandlung in Python
* Ausnahmebehandlung, engl: **Exception Handling**
* Vereinfacht Fehlerbehandlung durch speziellen Mechanismus
* Rückgabewerte von Funktionen können für ordentlichen Programmablauf verwendet werden
* Fehler können strukturiert behandelt werden


## Exception Handling
* Fehler 'wirft' eine _Exception_ (Objekt) nach 'oben', Funktion ist beendet.
* Übergeordnete Funktion kann:
  * fangen, fortfahren
  * fangen, weiterwerfen, Funktion ist beendet
  * lässt passieren, Funktion ist beendet


## Exception Objekt
Enthält Attribute und Methoden (Funktionen) zur Klassifizierung des Fehlers
```python
>>> e = Exception("My custom error")
>>> e.args
('My custom error',)
>>> e = Exception("My custom error","test", 1,2)
>>> e.args
('My custom error', 'test', 1, 2)
```


## Exception werfen
```python
>>> raise Exception("My Exception")
```
```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Exception: My Exception
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## Exception werfen
Nur BaseException und davon Abgeleitete dürfen geworfen werden
```python
>>> raise "test"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: exceptions must derive from BaseException
```


## Eingebaute exceptions
* BaseException
* Exception (Basisklasse für Benutzer)
* SyntaxError
* NameError
* TypeError
* ImportError
* ...


## Exception Behandlung
* _try_ öffnet den Try-Block
* Exceptions aus dem Try-Block werden im Except-Block gefangen
* _except_ definiert welche Exceptions behandelt werden


## Exception fangen
```python
>>> open("/tmp/non_existing_file",'r')
```
```txt
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/non_existing_file'
```
```python
try:
    open("/tmp/non_existing_file")
except OSError as e:
    print("Caught:", e)
```
<!-- .element: class="fragment" data-fragment-index="1" -->
```txt
Caught: [Errno 2] No such file or directory: '/tmp/non_existing_file'
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## try - except - else
```python
try:
    print("all good")
except NameError:
    print("Undefined vars found")
except:
    print("Don't know this error!")
    raise
else:
    print("everything is fine")
```


## except - else
```python
try:
    print("all good")
    open("/tmp/non_existing_file")
except NameError:
    print("Undefined vars found")
except:
    print("Don't know this error!")
    raise
else:
    print("everything is fine")

print("normal program flow")
```
```txt
all good
Don't know this error!
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/non_existing_file'
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## except - else
```python
try:
    print(a) # undefined!
    print("all good")
except NameError:
    print("Undefined vars found")
except:
    print("Don't know this error")
    raise
else:
    print("everything is fine")

print("normal program flow")
```
```txt
Undefined vars found
normal program flow
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## except - else
```python
try:
    print("all good")
except NameError:
    print("Undefined vars found")
except:
    print("Don't know this error!")
    raise
else:
    print("everything is fine")

print("normal program flow")
```
```txt
all good
everything is fine
normal program flow
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## finally
```python
try:
  open("/tmp/non_existing_file",'r')
except FileNotFoundError:
  print("file does not exist")
except:
  print("don't know this error")
  raise
finally:
  print("cleaning up")
```
```txt
file does not exist
cleaning up
```
<!-- .element: class="fragment" data-fragment-index="1" -->



## assert
* Setzt Bedingung, die, wenn falsch, zu einer Exception führt.
* Nur zur Entwicklung sinnvoll.
* Nur mit &#95;&#95;debug&#95;&#95;``` == True``` aktiv
* Wird mit ```python3 -O``` deaktiviert (&#95;&#95;debug&#95;&#95; = False)


## assert
```python
a = [1,2]
a[0] = 17
assert a == [17,2]
```
```python
a[1] = a[1] + 3
assert a == [17,4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```
<!-- .element: class="fragment" data-fragment-index="1" -->



# Aufbau eines Computers
<i class="twa twa-computer twa-5x"></i>


## Aufbau
<p class=wikipedia style="text-align:center;"><a href="https://commons.wikimedia.org/wiki/File:Personal_Computer_mit_L%C3%BCfter.png#/media/File:Personal_Computer_mit_L%C3%BCfter.png"><img src="https://upload.wikimedia.org/wikipedia/commons/f/fd/Personal_Computer_mit_L%C3%BCfter.png" alt="Personal Computer mit Lüfter.png"></a><br>Symbolbild, <a href="http://creativecommons.org/licenses/by/2.5" title="Creative Commons Attribution 2.5">CC BY 2.5</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=7529997">Quelle</a></p>


## Prozessor - CPU<!-- .slide: style="font-size:0.8em" -->
Central Processing Unit
<p class=wikipedia style="text-align:center;"><a href="https://commons.wikimedia.org/wiki/File:Intel_80486DX2_bottom.jpg#/media/File:Intel_80486DX2_bottom.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Intel_80486DX2_bottom.jpg" alt="Intel 80486DX2 bottom.jpg"></a><br>Intel 80486DX2, <a href="http://creativecommons.org/licenses/by-sa/2.0" title="Creative Commons Attribution-Share Alike 2.0">CC BY-SA 2.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=406957">Link</a></p>


Innenleben Intel 80486DX2
<p class=wikipedia style="text-align:center;"><a href="https://commons.wikimedia.org/wiki/File:80486dx2-large.jpg#/media/File:80486dx2-large.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/80486dx2-large.jpg/1200px-80486dx2-large.jpg" alt="80486dx2-large.jpg"></a><br>Von <a href="https://en.wikipedia.org/wiki/User:Uberpenguin" class="extiw" title="en:User:Uberpenguin">Uberpenguin</a> aus der <a href="https://en.wikipedia.org/wiki/" class="extiw" title="w:">englischsprachigen Wikipedia</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=5820383">Link</a></p>


## Arbeitsspeicher - RAM
<p class=wikipedia style="text-align:center;"><a href="https://commons.wikimedia.org/wiki/File:RAM_n.jpg#/media/File:RAM_n.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/d/d3/RAM_n.jpg" alt="RAM n.jpg"></a><br><a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=12105">Link</a></p>


## Arbeitsspeicher - RAM
Magnetic Core Memory, 1947
<p class=wikipedia style="text-align:center;"><a href="https://commons.wikimedia.org/wiki/File:8_bytes_vs._8Gbytes.jpg#/media/File:8_bytes_vs._8Gbytes.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/8_bytes_vs._8Gbytes.jpg/1200px-8_bytes_vs._8Gbytes.jpg" alt="8 bytes vs. 8Gbytes.jpg"></a><br>By <a rel="nofollow" class="external text" href="http://www.flickr.com/people/17884028@N00">Daniel Sancho</a> from Málaga, Spain - <a rel="nofollow" class="external text" href="http://www.flickr.com/photos/17884028@N00/2852716477/">8 bytes vs. 8Gbytes</a>, <a href="http://creativecommons.org/licenses/by/2.0" title="Creative Commons Attribution 2.0">CC BY 2.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=7686182">Quelle</a></p>


## Mainboard - Hauptplatine
1980
<p class=wikipedia style="text-align:center;"><a href="https://commons.wikimedia.org/wiki/File:Chicony_CH-286N-16_(1280x700_deutsch).jpg#/media/File:Chicony_CH-286N-16_(1280x700_deutsch).jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Chicony_CH-286N-16_%281280x700_deutsch%29.jpg/1200px-Chicony_CH-286N-16_%281280x700_deutsch%29.jpg" alt="Chicony CH-286N-16 (1280x700 deutsch).jpg"></a><br>Von User <a href="https://de.wikipedia.org/wiki/User:Smial" class="extiw" title="de:User:Smial">Smial</a> on <a class="external text" href="http://de.wikipedia.org">de.wikipedia</a> - <span class="int-own-work" lang="de">Eigenes Werk</span>, <a href="http://creativecommons.org/licenses/by-sa/2.0/de/deed.en" title="Creative Commons Attribution-Share Alike 2.0 de">CC BY-SA 2.0 de</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=994248">Link</a></p>


## Mainboard - Hauptplatine
2004
<p class=wikipedia style="text-align:center;"><a href="https://commons.wikimedia.org/wiki/File:ASRock_K7VT4A_Pro_Mainboard_Labeled_German.PNG#/media/File:ASRock_K7VT4A_Pro_Mainboard_Labeled_German.PNG"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/ASRock_K7VT4A_Pro_Mainboard_Labeled_German.PNG/1200px-ASRock_K7VT4A_Pro_Mainboard_Labeled_German.PNG" alt="ASRock K7VT4A Pro Mainboard Labeled German.PNG"></a><br>Von <a href="https://de.wikipedia.org/wiki/Benutzer:Freddy2001" class="extiw" title="de:Benutzer:Freddy2001">Freddy2001</a>
Description by <a href="//commons.wikimedia.org/wiki/User:Leipnizkeks" title="User:Leipnizkeks">User:leipnizkeks</a> – released under same license. - <span class="int-own-work" lang="de">Eigenes Werk</span>, <a href="http://creativecommons.org/licenses/by-sa/2.5" title="Creative Commons Attribution-Share Alike 2.5">CC BY-SA 2.5</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=25441788">Link</a></p>


## Mainboard - Hauptplatine
![](imgs/06/raspberry-pi-1719218_1920.jpg)


## Festplatten
 persistierender/nichtflüchtiger Speicher, billiger, langsamer als RAM.
* Klassische Festplatte:
  * magnetisierbare, rotierende Platten
<p class=wikipedia style="text-align:center;"><a href="https://commons.wikimedia.org/wiki/File:Seagate_ST33232A_hard_disk_inner_view.jpg#/media/File:Seagate_ST33232A_hard_disk_inner_view.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Seagate_ST33232A_hard_disk_inner_view.jpg/1200px-Seagate_ST33232A_hard_disk_inner_view.jpg" alt="Seagate ST33232A hard disk inner view.jpg"></a><br>Von Eric Gaba, Wikimedia Commons user <a href="//commons.wikimedia.org/wiki/User:Sting" title="User:Sting">Sting</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=11278668">Link</a></p>


## Festplatten
Solid State Drive (SSD), Halbleiterlaufwerk
<p class=wikipedia style="text-align:center;"><a href="https://commons.wikimedia.org/wiki/File:Sf-ssd.jpg#/media/File:Sf-ssd.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/7/7d/Sf-ssd.jpg" alt="Sf-ssd.jpg"></a><br>Von <a href="//commons.wikimedia.org/wiki/User:Hans_Haase" title="User:Hans Haase">Hans Haase</a> - <span class="int-own-work" lang="de">Eigenes Werk</span>, <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=26502674">Link</a></p>


## Arbeitsweise
**EVA**-Prinzip
* **E**: Eingabe
  * über Maus, Tastatur, Speichermedien gelangen Daten in den Computer
* **V**: Verarbeitung
  * Der Prozessor (CPU) verarbeitet diese Daten
* **A**: Ausgabe
  * Verarbeitete Daten werden über Ausgabegerät ausgegeben (Bildschirm, Drucker, Festplatte)


## Harvard Architektur
Strikte Trennung von Daten und Befehlen
* Zugriff erfolgt über je einen eigenen Bus.
Entwickelt 1944 (Mark I) von IBM und der Harvard-University
<p class=wikipedia style="text-align:center;"><a href="https://de.wikipedia.org/wiki/Datei:Harvard-architektur.png#/media/File:Harvard-architektur.png"><img src="https://upload.wikimedia.org/wikipedia/de/f/f9/Harvard-architektur.png" alt="Harvard-architektur.png"></a><br>Von Matthias Kleine (April 2005) - Matthias Kleine, <a href="http://creativecommons.org/licenses/by-sa/3.0/legalcode" title="Creative Commons Namensnennung-Weitergabe unter gleichen Bedingungen Unported 3.0">CC BY-SA 3.0</a>, <a href="https://de.wikipedia.org/w/index.php?curid=624441">Link</a></p>


## Harvard Architektur
* **Steuerwerk**: ist für das Einlesen der Befehle zuständig
* **Rechenwerk(e)**: führt entsprechende arithmetische und/oder logische Befehle aus
* **Daten**: enthält gespeicherte oder zu verarbeitende Daten
* **Befehle**: enthalten die einzelnen Befehle eines Programms
* **Bussystem** (Pfeile): transportiert Daten zwischen Einheiten


## Von Neumann Architektur
![Von Neumann Architektur](imgs/01/Von-Neumann_Architektur.svg)


## Von Neumann Architektur
* **CPU**: Besteht aus Rechen- und Steuerwerk
  * **Steuerwerk**: ist für das Einlesen der Befehle zuständig
  * **Rechenwerk**: führt entsprechende arithmetische und/oder logische Befehle aus
* **Arbeitsspeicher**: enthält das Programm sowie alle dafür notwendigen Daten
* **Bussystem**: transportiert Daten zwischen Einheiten
* **Ein-/Ausgabe**: kommuniziert mit der Umwelt


### Von Neumann vs. Harvard Architektur

Von Neumann Architektur:

* <i class="fa fa-plus" aria-hidden="true" alt="+" title="+"></i> Einfacher da Programm und Daten im Speicher liegen, erlaubt einheitliche Routinen des Betriebssystems
* <i class="fa fa-plus" aria-hidden="true" alt="+"></i> Programmcode kann sich selbst modifizieren; leichter zu 'debuggen'
* <i class="fa fa-minus" aria-hidden="true" alt="-"></i> Selbstmodifikation ist Risiko für Stabilität
* <i class="fa fa-minus" aria-hidden="true" alt="-"></i> Es gibt keinen Speicherschutz
* <i class="fa fa-minus" aria-hidden="true" alt="-"></i> Langsamer: eine Leitung für Befehle und Daten


### Harvard vs. Von Neumann Architektur

Harvard Architektur:

* <i class="fa fa-plus" aria-hidden="true" alt="+"></i> Schnellerer Zugriff auf Daten und Programme, durch getrenntes Ansteuern
* <i class="fa fa-plus" aria-hidden="true" alt="+"></i> Speicherschutz einfach umsetzbar
* <i class="fa fa-minus" aria-hidden="true" alt="-"></i> Parallele Zugriffe können zu **Race Conditions** führen
  * Ungewolltes Verhalten von Programmen


## Race conditions
* Bei **Race condition** hängt das Ergebnis einer Operation vom zeitlichen Verhalten der Einzeloperationen ab

**Beispiel**: 2 Systeme wollen Wert einer Zahl erhöhen

| Schritt | System 1 | | System 2| |
| ---     |  ----   |  |  ----   | |
| 0 | Lesen | 0 | | |
| 1 | | | Lesen | 0 |
| 2 | Erhöhen | 1  | | |
| 3 | Schreiben | 1 | | |
| 4 | | | Erhöhen | 1 |
| 5 | | | Schreiben | 1 |
<!-- .element: style="font-size:0.7em" -->


## Moderne Computer
Basieren auf der Von Neumann Architektur

CPU, Arbeitsspeicher und Ein-/Ausgabe Hardware werden durch eine Hauptplatine (**Mainboard**) via **Bussystem** verbunden

Integrierte Hardware im Mainboard (Sound, Netzwerk, Grafik) zählt weiter als Peripherie.


## Funktionsweise CPU<!-- .slide: style="font-size:0.9em" -->
<p class=wikipedia style="text-align:center;"><a href="https://commons.wikimedia.org/wiki/File:Proz1-d.png#/media/File:Proz1-d.png"><img src="https://upload.wikimedia.org/wikipedia/commons/2/2c/Proz1-d.png" alt="Proz1-d.png"></a><br>Von <a href="//commons.wikimedia.org/w/index.php?title=User:PeterFrankfurt&amp;action=edit&amp;redlink=1" class="new" title="User:PeterFrankfurt (page does not exist)">PeterFrankfurt</a> - <span class="int-own-work" lang="de">Eigenes Werk</span>, <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=31990596">Link</a></p>


## Abstrakte Funktionsweise CPU<!-- .slide: style="font-size:0.9em" -->
1. **FETCH**
  * Befehlsadresse lesen und aus Arbeitsspeicher in Register laden
2. **DECODE**
  * Befehl in Register wird dekodiert und entsprechende Schritte für Verarbeitung werden vorbereitet
3. **EXECUTE**
  * Der Befehl wird ausgeführt und das Ergebnis in den Arbeitsspeicher zurück geschrieben
4. **UPDATE** Instruction Pointer
  * Die nächste Befehlsadresse wird eingestellt


## Funktionsweise CPU<!-- .slide: style="font-size:0.8em" -->
<p class=wikipedia style="text-align:left;width:60%;left:0em;position: relative;"><a href="https://commons.wikimedia.org/wiki/File:Proz1-d.png#/media/File:Proz1-d.png"><img src="https://upload.wikimedia.org/wikipedia/commons/2/2c/Proz1-d.png" alt="Proz1-d.png"></a><br>Von <a href="//commons.wikimedia.org/w/index.php?title=User:PeterFrankfurt&amp;action=edit&amp;redlink=1" class="new" title="User:PeterFrankfurt (page does not exist)">PeterFrankfurt</a> - <span class="int-own-work" lang="de">Eigenes Werk</span>, <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=31990596">Link</a></p>
<div style="text-align: left; position: absolute; left: 50%; width: 50%; top: 20%;">
<ol start=1>
<li/> Befehlszähler (**PC**) zeigt auf Adresse im Speicher <br/>
<li/> Steuerwerk legt Adresse auf Bus und startet Lesebefehl <br/>
<li/> wenn RAM bereit, legt Inhalt an Datenleitung an <br/>
<li/> Steuerwerk kopiert den Inhalt des Befelsregisters <br/>
<li/> Befehl wird dekodiert und geprüft <br/>
...
</ol>
</div>


## Funktionsweise CPU<!-- .slide: style="font-size:0.8em" -->
<p class=wikipedia style="text-align:left;width:60%;left:0em;position: relative;"><a href="https://commons.wikimedia.org/wiki/File:Proz1-d.png#/media/File:Proz1-d.png"><img src="https://upload.wikimedia.org/wikipedia/commons/2/2c/Proz1-d.png" alt="Proz1-d.png"></a><br>Von <a href="//commons.wikimedia.org/w/index.php?title=User:PeterFrankfurt&amp;action=edit&amp;redlink=1" class="new" title="User:PeterFrankfurt (page does not exist)">PeterFrankfurt</a> - <span class="int-own-work" lang="de">Eigenes Werk</span>, <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=31990596">Link</a></p>
<div style="text-align: left; position: absolute; left: 50%; width: 50%; top: 20%;">
Nach Dekodieren: <br/><ul><li/> Wenn Befehl grösser oder benötigt Befehl weitere Daten aus Speicher: Schritte 1-3 erneut, und ins entsprechende Prozessorregister geladen.
</ul><ol start=6>
<li/> Steuerwerk involviert benötigte Ressourcen (z.B. ALU)
<li/> ALU führt Befehl aus (z.B: Addition 2er Registerinhalte)
</ol>
</div>


## Funktionsweise CPU<!-- .slide: style="font-size:0.8em" -->
<p class=wikipedia style="text-align:left;width:60%;left:0em;position: relative;"><a href="https://commons.wikimedia.org/wiki/File:Proz1-d.png#/media/File:Proz1-d.png"><img src="https://upload.wikimedia.org/wikipedia/commons/2/2c/Proz1-d.png" alt="Proz1-d.png"></a><br>Von <a href="//commons.wikimedia.org/w/index.php?title=User:PeterFrankfurt&amp;action=edit&amp;redlink=1" class="new" title="User:PeterFrankfurt (page does not exist)">PeterFrankfurt</a> - <span class="int-own-work" lang="de">Eigenes Werk</span>, <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=31990596">Link</a></p>
<div style="text-align: left; position: absolute; left: 50%; width: 50%; top: 20%;">
<ol start=8>
<li/> Ergebnis wird in ein Register geschrieben
<li/> Falls nötig wird das Ergebnis vom Register in RAM gespeichert
<li/> Programmzähler wird erhöht
<li/> Befehl ist abgearbeitet (start bei 1)
</ol>
</div>


## CPU Befehlssätze<!-- .slide: style="font-size:0.9em" -->
2 generelle Gruppen:
* **RISC**
  * Reduced Instruction Set Computing
  * Sehr einfache Befehle (z.B: "ADD")
  * Kleine Anzahl an Befehlen
* **CISC**
  * Complex Instruction Set Computing
  * Komplexe Befehle direkt durchführbar
    * Bsp: Gleitkommazahl-Operationen
  * Große Anzahl an Befehlen


## Arbeitsspeicher - CPU Register<!-- .slide: style="font-size:0.9em" -->
Register in Prozessoren sind sehr klein (aber schnell). Programme benötigen viel mehr Speicherplatz als im Register vorhanden ist.
* Intelligentes Zwischenspeichern von oft gebrauchten Daten im Arbeitsspeicher (RAM)
* Schneller als Laden von Festplatte, aber langsamer als direkt im Prozessor
* Register im Arbeitsspeicher sind nicht persistent
  * Ohne Strom ist Inhalt verloren
* Heute Arbeitsspeicher in "GByte"



# Fragen?


## Nächstes Mal
2016-11-30 16:00
#### Softwareentwicklungsprozess
mit Johanna Pirker
