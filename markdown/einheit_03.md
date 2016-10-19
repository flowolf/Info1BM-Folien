# 706.088 Informatik 1
## Funktionen, Teilgebiete der Informatik & Geschichte


## Wiederholung Programmierung



## Hello World <i class="twa twa-party-popper"></i>
```python
print("Hello World!")
```
```bash
Hello World!
```



## Deklaration von Variablen
* Boolsche Werte (True, False)
* Natürliche Zahlen (integer: 1, 11, 100000)
* Reelle Zahlen (float: 0.1, 3.7)
* Text (string: "Kette von Zeichen")
* Kein Wert (None)
* Tupel
* Listen
* Dictionary



## Operatoren

Operatoren definieren die Interaktion <br/> von Variablen und (deren) Werten

| Operator | Beispiel | Ausgabe |
|  ----    | -----    |  -----:  |
| +x, -x | -2 | -2  |
| +, - | 3 + 4 | 7  |
| *, / | 3 * 4 | 12  |


## Operatoren

| Operator | Beispiel | Ausgabe |
|  ----    | -----    |  -----:  |
| //, %  | 13//3, 13 % 3   |  4,1  |
| ** | 3**2 | 9  |


## Operatoren

| Operator | Beispiel | Ausgabe |
|  ----    | -----    |  -----:  |
| not | not True | False  |
| and, or | True or False, True and False  | True, False  |
| <, <=, >=, >, == |  4 > 5  | False |


## Operatoren

Zuweisung

| Operator | Beispiel | Ausgabe |
|  ----    | -----    |  -----:  |
| =  |   a = 4, b = a |  a = 4, b = 4 |
| += |  a += b |  a = 8, b = 4 |
| -= |  a -= b |  a = 4, b = 4 |
| *= |  a *= 3 |  a = 12, b = 4 |
| /= |  a /= b |  a = 3.0, b = 4 |
| //= |  b //= a |  a = 3.0, b = 1.0 |



## Kontrollstrukturen
```python
if True:
  print("always here")
else:
  print("never here")
```
```bash
always here
```



## Schleifen
```python
print("forever")
while True:
    print("and ever")
```
```bash
forever
and ever
and ever
and ever
...
```



## Schleifen
```python
list = ["test1", "test2", "test3"]
for element in list:
    print(element)
```
```bash
test1
test2
test3
```



# Funktionen


## Funktionen
dienen der Kapselung von Code nach logischen Einheiten
```python
pets = ["Hamster", "Cat", "Dog", "Canary"]

def not_a_dog_person(animal):
  return animal.replace("Dog", "Fish")

for pet in pets:
  print("Tom: {:10} Tim: {}".format(pet, not_a_dog_person(pet)))
```
```bash
Tom: Hamster    Tim: Hamster
Tom: Cat        Tim: Cat
Tom: Dog        Tim: Fish
Tom: Canary     Tim: Canary
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## Funktionen
```python
def add(x, y):
    return x + y

def print_result(result):
    print("Result: {}".format(result))

def main():
    a = 10
    b = 20
    c = add(a, b)
    print_result(c)

if __name__ == "__main__":
    main()
```
```bash
Result: 30
```
<!-- .element: class="fragment" data-fragment-index="1" -->


### Definition eines guten Programms
* Funktionalität <!-- .element: class="fragment" data-fragment-index="1" -->
* Lesbarkeit <!-- .element: class="fragment" data-fragment-index="2" -->
* Wartbarkeit <!-- .element: class="fragment" data-fragment-index="3" -->
* Robustheit <!-- .element: class="fragment" data-fragment-index="4" -->
* Korrektheit <!-- .element: class="fragment" data-fragment-index="5" -->
* Effizienz <!-- .element: class="fragment" data-fragment-index="6" -->
* Portierbarkeit <!-- .element: class="fragment" data-fragment-index="7" -->



## Eingabe-/Ausgabe Parameter
```python
import sys

print(sys.argv)
```
```bash
$ python3 sysargv.py test1 123 --flag
['sysargv.py', 'test1', '123', '--flag']
```
<!-- .element: class="fragment" data-fragment-index="1" -->



```python
import sys
sum = 0
for element in sys.argv[1:]:
  sum += int(element) # same as: sum = sum + int(element)
print(sum)
```
```bash
$ python3 sysargv2.py 1 2 3 4 5 6
21
```
<!-- .element: class="fragment" data-fragment-index="3" -->



# Geschichte der Informatik


## Was ist Informatik
Wissenschaft der ** " systematischen " ** oder " ** automatischen Verarbeitung ** " von " ** Information ** "

**Infor**mation + Auto**matik**


## Geschichte der Informatik
* Aus 3 Teilgebieten zusammengesetzt
  1. Mathematik
  2. Mechanik
  3. Elektronik
* ... oder vom Abakus zum Quantencomputer


## Mathematik und Informatik
* Verschiedene Meilensteine zwischen 30.000 v. Chr.
und 200 n. Chr.
* Abakus (200 n. Chr.)
* Begründung des Dezimalsystem (500 n. Chr.)
* Arabische Ziffern in Europa (1200 n. Chr.)
* Algorithmen zur Überführung von Multiplikationen in Additionen (1600 n. Chr.)



## Geschichte der Informatik
'Logische Maschinen' bereits im 13. Jahrhundert

Wunsch der Automation von mathematischen Berechnungen

Erstes **mechanisches** Rechengerät wurde im Jahr 1623 von Wilhelm Schickard gebaut



### Mathematik, Mechanik und Informatik
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Schickardmaschine.jpg#/media/File:Schickardmaschine.jpg"><img src="imgs/03/Schickardmaschine.jpg" alt="Schickardmaschine.jpg"></a><br/>Schickard'sche Rechenmaschine (1623 n. Chr)
<br/>By <a href="https://de.wikipedia.org/wiki/User:Klaeren" class="extiw" title="de:User:Klaeren">Herbert Klaeren</a> - Transferred from <a class="external autonumber" href="http://de.wikipedia.org/w/index.php?title=Datei:Schickardmaschine.jpg">[1]</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=8159979">Link</a></p>



### Schickard'sche Rechenmaschine

* 1623 n. Chr
* Basierend auf Zahnräderen
* Addition und Subtraktion von bis zu **sechsstelligen** Zahlen
* Speicherüberlauf
  * Akustisches Signal
* Pläne bis 1960 verloren



### Blaise Pascal - Pascaline
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Arts_et_Metiers_Pascaline_dsc03869.jpg#/media/File:Arts_et_Metiers_Pascaline_dsc03869.jpg"><img src="imgs/03/1200px-Arts_et_Metiers_Pascaline_dsc03869.jpg" alt="Arts et Metiers Pascaline dsc03869.jpg"></a><br>Pascaline<br/>By © 2005 <a href="//commons.wikimedia.org/wiki/User:David.Monniaux" title="User:David.Monniaux">David Monniaux</a>&nbsp;/&nbsp;, <a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=186079">Link</a></p>


* Erster (mechanischer) Taschenrechner
* 50 Prototypen
* Öffentliche Präsentation 1645
* Funktionsumfang
  * Addition
  * Subtraktion
  * von 2 Zahlen



## Mathematik, Mechanik und Informatik
* Charles Babbage (1791 - 1871)
  * Mathematiker, Philosoph, Erfinder und Entwickler.
  * “Einer der Väter des (mechan ischen) Computers”
  * Bekannt für die Babbage- oder Difference-Engine zur Lösung polinomialer Gleichungen.


<p class="wikipedia"><a href="https://commons.wikimedia.org/wiki/File:AnalyticalMachine_Babbage_London.jpg#/media/File:AnalyticalMachine_Babbage_London.jpg"><img alt="AnalyticalMachine Babbage London.jpg" src="imgs/03/AnalyticalMachine_Babbage_London.jpg"></a><br>
Analytical Machine von Babbage<br/>
Von Bruno Barral (ByB), <a title="Creative Commons Attribution-Share Alike 2.5" href="http://creativecommons.org/licenses/by-sa/2.5">CC BY-SA 2.5</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=6839854">https://commons.wikimedia.org/w/index.php?curid=6839854</a></p>
<!-- ![Analytical Machine](https://upload.wikimedia.org/wikipedia/commons/a/ac/AnalyticalMachine_Babbage_London.jpg) -->



## Mathematik, Mechanik und Informatik
* Herman Hollerith (1860 - 1929)
  * Erfand das Lochkartensystem zur Datenspeicherung (1884)
  * Automatische Auswertung der gespeicherten Daten durch 'Lochkarten-Leser'
  * Ebnete den Weg zur Speicherung von ersten Computer-Instruktionen.
  * Verwendung der Hollerith Maschine (Tabulating machine
) zur Volkszählung 1890 in den USA


<p class="wikipedia"><a href="https://commons.wikimedia.org/wiki/File:Hollerith_Punched_Card.jpg#/media/File:Hollerith_Punched_Card.jpg"><img alt="Hollerith Punched Card.jpg" src="imgs/03/Hollerith_Punched_Card.jpg" height="287" width="640"></a><br/>
Lochkarte <br/>
By <span lang="en">Unknown</span><a href="//www.wikidata.org/wiki/Q4233718" title="wikidata:Q4233718"></a> - Library of Congress <a rel="nofollow" class="external free" href="http://memory.loc.gov/mss/mcc/023/0008.jpg">http://memory.loc.gov/mss/mcc/023/0008.jpg</a>, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=30538485">https://commons.wikimedia.org/w/index.php?curid=30538485</a></p>



## Konrad Zuse (1910 - 1995)
Entwickelte den **ersten** **Digital**-rechner weltweit, <br/>die **Z3** (1941)

* 600 Relais für den Prozessor
* 1600 Relais für den Speicher
* Basierte auf **binärer Gleitkommaarithmetik**
* So groß wie ein (sehr großer) Kleiderschrank
* 15-20 Arithmetische Operationen / Sekunde
Weitere Informationen zu Konrad Zuse: http://zuse.zib.de


<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Z3_Deutsches_Museum.JPG#/media/File:Z3_Deutsches_Museum.JPG"><img alt="Z3 Deutsches Museum.JPG" src="imgs/03/Z3_Deutsches_Museum.JPG" ></a><br>
Z3 im Deutschen Museum<br/>Von <a href="https://de.wikipedia.org/wiki/User:Venusianer" class="extiw" title="de:User:Venusianer">Venusianer</a> aus der <a href="https://de.wikipedia.org/wiki/" class="extiw" title="de:">deutschsprachigen Wikipedia</a>, <a title="Creative Commons Attribution-Share Alike 3.0" href="http://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=3632073">https://commons.wikimedia.org/w/index.php?curid=3632073</a></p>




## ENIAC
Erster 'rein elektronischer' Rechner
* 1946 vorgestellt
* Elektronenröhren (Vacuum Tubes) zur elektrischen Speicherung von Zahlen
* 17.468 Elektronenröhren
* 167 m²
* 27 Tonnen
* 170 kW
* USD 468.000 ~ heute USD 6.8 Mio


<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Eniac.jpg#/media/File:Eniac.jpg"><img alt="Eniac.jpg" src="imgs/03/Eniac.jpg"></a><br>Eniac</br>Von <span xml:lang="de" lang="de">Unbekannt</span><a href="//www.wikidata.org/wiki/Q4233718" title="wikidata:Q4233718"></a> - <a rel="nofollow" class="external text" href="http://ftp.arl.mil/ftp/historic-computers">U.S. Army Photo</a>, Gemeinfrei, <a href="https://commons.wikimedia.org/w/index.php?curid=55124">https://commons.wikimedia.org/w/index.php?curid=55124</a></p>


### Langlebigkeit von Elektronenröhren
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Elektronenroehren-auswahl.jpg#/media/File:Elektronenroehren-auswahl.jpg"><img src="imgs/03/1200px-Elektronenroehren-auswahl.jpg" alt="Elektronenroehren-auswahl.jpg"></a><br>By Stefan Riepl (<a href="https://de.wikipedia.org/wiki/Benutzer:Quark48" class="extiw" title="de:Benutzer:Quark48">Quark48</a>) - <span class="int-own-work">Self-photographed</span>, <a href="http://creativecommons.org/licenses/by-sa/2.0/de/deed.en" title="Creative Commons Attribution-Share Alike 2.0 de">CC BY-SA 2.0 de</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=14682022">Link</a></p>Ca. alle zwei Tage kam es zu einem Ausfall einer Elektronenröhre

15 Minuten bis fehlerhafte Elektronenröhre gefunden wurde



## First Bug
<i class="twa twa-bug twa-3x"></i>

* Bezeichnung 'Bug' für Fehler in Programmabläufen geht zurück auf Computer Pionierin **Grace Hopper**
* Am 9. September 1947 dokumentierte sie eine Motte in einem Relais des Computers **Mark II Aiken Relay Calculator** im Log-Buch mit den Worten: **"First actual case of bug being found**"


<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:H96566k.jpg#/media/File:H96566k.jpg"><img alt="H96566k.jpg" src="imgs/03/H96566k.jpg"></a><br>By Courtesy of the Naval Surface Warfare Center, Dahlgren, VA., 1988. - U.S. Naval Historical Center Online Library Photograph <a rel="nofollow" class="external text" href="http://www.history.navy.mil/photos/images/h96000/h96566kc.htm">NH 96566-KN</a>, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=165211">https://commons.wikimedia.org/w/index.php?curid=165211</a><br/>
 </p>


<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Commodore_Grace_M._Hopper,_USN_(covered).jpg#/media/File:Commodore_Grace_M._Hopper,_USN_(covered).jpg"><img alt="Commodore Grace M. Hopper, USN (covered).jpg" src="imgs/03/Commodore_Grace_M._Hopper,_USN_(covered).jpg" height="900" width="720"></a><br>Grace Hopper, By James S. Davis - Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=12421475">https://commons.wikimedia.org/w/index.php?curid=12421475</a>
<br/>
Grace Hopper "Queen of Software" [on Letterman <i class="fa fa-youtube-square" aria-hidden="true"></i>](https://youtu.be/1-vcErOPofQ) </p>



## Mailüfterl
* 1955 an der TU Wien von Heinz Zemanek mit Studierenden gebaut.
* erster Volltransistor Rechner am Europäischen Festland
* 3.000 Transistoren, 5.000 Dioden, 20 km Draht, 132 kHz
* Transistorspende von Philips
* erste Berechnung 1958


# Mailüfterl<!-- .element: class="light shadow" -->
<!-- .slide: data-background-iframe="https://www.youtube.com/embed/lvaiEW-Sm4A" -->
[<i class="fa fa-youtube-square" aria-hidden="true"></i> go there](https://www.youtube.com/watch?v=lvaiEW-Sm4A)



## Informatik
Johann von Neumann erfindet 1946 die <br/>**Von Neumann Architektur**:
* Programm und Daten werden gleichzeitig im Hauptspeicher gehalten


## Aufbau eines Computers
Von Neumann Architektur als Referenzmodell für einen Computers

![Von Neumann Architektur](imgs/03/Von-Neumann_Architektur.png)<!-- .element: style="height: 10em;" -->



## Informatik
Shockley, Bardeen und Brattain (Bell Labs) <br/> entdecken 1947 den ersten Transistoreffekt <br/> und stellen den ersten **Transistor** vor.
* 1956 Nobelpreis für Physik



Rechenleistung bis ca. 1960
* 1-2 KByte Speicher
* 0.02 MIPS

Rechenleistung 1986 bis heute
* 8 MByte - ~ 32GByte
* \> 100 MIPS


## Moore's Law
* Anzahl der Transistoren verdoppelt sich in regelmäßigen Abständen (alle 2 Jahre).
→ Leistung in [MIPS](https://en.wikipedia.org/wiki/Instructions_per_second#MIPS) verdoppelt sich auch.


### Moore's Law
<p class="wikipedia"><a href="https://commons.wikimedia.org/wiki/File:Transistor_Count_and_Moore%27s_Law_-_2011.svg#/media/File:Transistor_Count_and_Moore%27s_Law_-_2011.svg"><img alt="Transistor Count and Moore's Law - 2011.svg" src="https://upload.wikimedia.org/wikipedia/commons/0/00/Transistor_Count_and_Moore%27s_Law_-_2011.svg"></a><br>By <a href="//commons.wikimedia.org/wiki/User:Wgsimon" title="User:Wgsimon">Wgsimon</a> - <span class="int-own-work" lang="en">Own work</span>, <a title="Creative Commons Attribution-Share Alike 3.0" href="http://creativecommons.org/licenses/by-sa/3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=15193542">https://commons.wikimedia.org/w/index.php?curid=15193542</a></p>



# Fragen?


## Nächstes Mal
2016-11-09 16:00
