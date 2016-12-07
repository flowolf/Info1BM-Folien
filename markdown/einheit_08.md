# 706.088 Informatik 1
### Analytische Problemlösung, Fermi-Probleme, Türme von Hanoi, Module & Klassen in Python


## Analayische Problemlösung


## Analytisches Denken

* Sachliche Analyse einer Situation
* Pro/Contra Abwägung


## Analytisches Denken

Beschreibt  Fähigkeit von Personen Probleme (und Teilprobleme eines Problems) zu erkennen.
1. **Erkennen** eines **Problems**
2. Erkennen der **Teilprobleme**
  * Art, Umfang, Kontext, Schwierigkeit
3. Formen von **Lösungsansätzen**
  * Für **alle Teilprobleme** individuell
4. **Zusammenführung** von Lösungsansätzen
  * Erstellung eines übergeordneten Lösungsplans


## Beispiele

* Design an evacuation plan for San Francisco
* How many times a day do a clock's hand overlap?
* How many piano tuners are there in the entire world?
* How many golf balls could you fit into a classic American school bus?
* How many vacuum's are made per year in the US?
* How many quarters (placed on top of each other) would it require to reach the top of the Empire State Building?


#### How many quarters (placed on top of each other) would it require to reach the top of the Empire State Building?

1. Problem: Wie viele Münzen brauche ich?
2. Teilprobleme
  1. Wie hoch ist das Empire State Building?
  2. Wie dick ist eine Quarter-Dollar Münze?
3. Teil-Lösungen:
  1. Höhe abschätzen (ca. 400m)
  2. Dicke abschätzen (ca. 1,5mm == 0,0015m)
4. Zusammenführung:
  1. Schlussrechnung:
     400/0.0015 = 266666.66


## Fermi-Probleme<!-- .slide: style="font-size:0.9em" -->

Bezeichnet die quantitative Abschätzung für ein Problem zu dem man kaum Daten zur Verfügung hat

* geht zurück auf Enrico Fermi (Physiker)
  * war bekannt für gute Abschätzungen
  * Bsp: Papierschnipsel in der Luft (Druckwelle) um beim Test der ersten Atombombe die Sprengkraft der Bombe zu testen
* Idee: Kaum direkte Information vorhanden, aber Information über Zusammenhänge im Umfeld.
Diese Zusammenhänge kann man sich zu Nutze machen um 'indirekt' das Problem zu lösen!


## Fermi-Probleme

* **Problem**: Gewisses Allgemeinwissen ("gesunder Hausverstand") ist nötig!
* Um aber tatsächlich eine Lösung zu finden, muss das Vorwissen quantifiziert werden
* Prozess der Quantifizierung muss zusätzlich begründet und 'logisch untermauert' werden
* Durch 'Teilabschätzungen' (Wolkenkratzer und Münze) kann man Gesamtergebnis anschätzen
* Bei Fermi Problemen ist der Lösungsweg meist interessanter als das Ergebnis.



# Algorithmus


## Definition eines Algorithmus
* Ein Algorithmus ist eine **eindeutige Anleitung zur Lösung eines Problems**.
* Algorithmen bestehen aus **endlich vielen**, explizit definierten **Einzelschritten**.
* Sie können als Programm implementiert werden.
* Aber natürlich auch in normaler Sprache formuliert werden.
* Generell gilt: Ein Algorithmus überführt eine **bestimmte Eingabe** in eine **bestimmte Ausgabe**.


## Euklidischer Algorithmus

```txt
1   EUCLID_OLD(a,b)
2       wenn a = 0
3           dann return b
4       sonst solange b ≠ 0
5           wenn a > b
6               dann a ← a - b
7           sonst b ← b - a
8       return a
```


## Eigenschaften von Algorithmen<!-- .slide: style="font-size:0.9em" -->

* **Determiniertheit**
  * Bei gleichen Eingaben liefert der Algorithmus immer die gleichen Ausgaben/Ergebnisse.
* **Determinismus**
  * Jeder Schritt ist eindeutig definiert. Die Abarbeitung des Algorithmus erfolgt immer eindeutig
  und klar definiert. Nicht-Deterministisch: zB: Zufälliges Start-Element wählen.


## Eigenschaften von Algorithmen<!-- .slide: style="font-size:0.9em" -->

* **Finitheit**
  * Der Algorithmus hat endlich viele Befehle/Anweisungen
* **Terminiertheit**
  * Algorithmus ist terminierend, wenn jede Eingabe nach einer endlichen Anzahl von Schritten zu
    * einem gewollten Abbruch oder
    * einem Ergebnis führt
* **Effektivität**
  * Der Effekt/die Auswirkung eines Befehls innerhalb eines Algorithmus muss eindeutig sein.


## Turingmaschine
* Erfunden 1936 von Mathematiker Alan Turing
* Simuliert die Arbeitsweise eines Computers
  * besonders einfach und mathematisch gut zu analysieren
* Eine Turingmaschine macht die Berechenbarkeit eines Algorithmus mathematisch erfassbar
* D.h. eine Turingmaschine ist ein mathematisches Objekt und kann mit mathematischen Methoden untersucht werden


## Turingmaschine<!-- .slide: style="font-size:0.9em;" -->
**Es gilt**:
* Eine Turingmaschine repräsentiert einen Algorithmus bzw. ein Programm
* Eine Berechnung mit einer Turingmaschine erfolgt
  * über die (schrittweise) Manipulation von Zahlen/Symbolen
  * Regeln bestimmen wie diese Zeichen geschrieben bzw. gelesen werden.

Ein Programm das bzw. ein Algorithmus der anhand einer Turingmaschine berechnet
werden kann, wird **Turing-berechenbar** oder **einfach berechenbar** genannt.


## Turingmaschine<!-- .slide: style="font-size:0.9em" -->
Im Steuerwerk der Turingmaschine befindet sich das Programm/der Algorithmus.

Jede Turingmaschine hat außerdem ein unendlich langes Speicherband mit unendlich
vielen Feldern.

Pro Feld kann genau ein Zeichen gespeichert werden.

Zusätzlich gibt es ein definiertes Eingabealphabet und ein Symbol für 'leere Felder'.

Der Lese- und Schreibkopf ist Programmgesteuert und bewegt sich feldweise, entsprechend
der Regeln des Programmes, auf dem Speicherband und kann dort die Zeichen verändern.


## Turingmaschine
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Turingmaschine.svg#/media/File:Turingmaschine.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Turingmaschine.svg/1200px-Turingmaschine.svg.png" alt="Turingmaschine.svg"></a><br>Von derivative work: <a href="//commons.wikimedia.org/w/index.php?title=User:TripleWhy&amp;action=edit&amp;redlink=1" class="new" title="User:TripleWhy (page does not exist)">TripleWhy</a> (<a href="//commons.wikimedia.org/wiki/User_talk:TripleWhy" title="User talk:TripleWhy"><span class="signature-talk">talk</span></a>)
<a href="//commons.wikimedia.org/wiki/File:Turingmaschine.png" title="File:Turingmaschine.png">Turingmaschine.png</a>: de:Benutzer:Denniss - <a href="//commons.wikimedia.org/wiki/File:Turingmaschine.png" title="File:Turingmaschine.png">Turingmaschine.png</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=5754731">Link</a></p>



## Türme von Hanoi
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Tower_of_Hanoi.jpeg#/media/File:Tower_of_Hanoi.jpeg"><img src="https://upload.wikimedia.org/wikipedia/commons/0/07/Tower_of_Hanoi.jpeg" alt="Tower of Hanoi.jpeg"></a><br><a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=228623">Link</a></p>


## Türme von Hanoi
**Spielregeln**
* Turm muss von A nach C (B = Hilfsstapel)
* nur oberste Scheiben dürfen bewegt werden
* Scheiben dürfen nur auf leere Stäbe, oder auf grösseren Scheiben zu liegen kommen


## Türme von Hanoi
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Tower_of_Hanoi.gif#/media/File:Tower_of_Hanoi.gif"><img src="https://upload.wikimedia.org/wikipedia/commons/4/4f/Tower_of_Hanoi.gif" alt="Tower of Hanoi.gif"></a><br>Von <a href="//commons.wikimedia.org/wiki/User:Aka" title="User:Aka">Aka</a> - <span class="int-own-work" lang="de">Eigenes Werk</span>, <a href="http://creativecommons.org/licenses/by-sa/2.5" title="Creative Commons Attribution-Share Alike 2.5">CC BY-SA 2.5</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=24669">Link</a></p>


## Türme von Hanoi
### Algorithmus
```text
n=1 Scheibe
S1-AC

n=2 Scheiben
S1-AB, S2-AC, S1-BC

n=3 Scheiben
S1-AC, S2-AB, S1-CB, S3-AC, S1-BA, S2-BC, S1-AC
```


## Türme von Hanoi
```python
def hanoi(ring,stab1="stab1",stab2="stab2",stab3="stab3"):
    if ring > 0:
        hanoi(ring-1,stab1,stab3,stab2)
        move(ring,stab1,stab3)
        hanoi(ring-1,stab2,stab1,stab3)
        sleep(1)
```


## Türme von Hanoi<!-- .slide: style="font-size:0.8em" -->
<pre>
<i>bewege</i>(3,a,b,c) {
    <i>bewege</i>(2,a,c,b) {
        <i>bewege</i>(1,a,b,c) {
            <i>bewege</i>(0,a,c,b){};
            verschiebe <span style="background:red;">oberste Scheibe</span> von a nach c;
            <i>bewege</i>(0,b,a,c){};
        };
        verschiebe <span style="background:yellow; padding:0 1.5em;">oberste Scheibe</span> von a nach b;
        <i>bewege</i>(1,c,a,b){
            <i>bewege</i>(0,c,b,a){};
            verschiebe <span style="background:red;">oberste Scheibe</span> von c nach b;
            <i>bewege</i>(0,a,c,b){};
        };
    };
    verschiebe <span style="background:blue; color:white; padding:0 3em;">oberste Scheibe</span> von a nach c;
    <i>bewege</i>(2,b,a,c){
        <i>bewege</i>(1,b,c,a){
            <i>bewege</i>(0,b,a,c){};
            verschiebe <span style="background:red;">oberste Scheibe</span> von b nach a;
            <i>bewege</i>(0,c,b,a){};
        };
        verschiebe <span style="background:yellow; padding:0 1.5em;">oberste Scheibe</span> von b nach c;
        <i>bewege</i>(1,a,b,c){
            <i>bewege</i>(0,a,c,b){};
            verschiebe <span style="background:red;">oberste Scheibe</span> von a nach c;
            <i>bewege</i>(0,b,a,c){};
        };
    };
};
</pre>
<p class=wikipedia style="font-size:0.5em">Quelle: <a href="https://de.wikipedia.org/wiki/T%C3%BCrme_von_Hanoi#Randoffscher_Algorithmus">Randolffscher Algorithmus</a></p>


## Laufzeit Türme von Hanoi
### Prakitsche (Un)lösbarkeit
1 Sekunde / Zug:

| Scheiben | Züge    | Zeit  |
| :-------:| ----:    | :----:  |
|     1    |   1     |  1 s  |
|     5    |   31    |  31 s<!-- .element: class="fragment" data-fragment-index="1" --> |
|    10    |   1.023  |  17 min<!-- .element: class="fragment" data-fragment-index="2" --> |
|    20    |   1.048.575 | 12 d<!-- .element: class="fragment" data-fragment-index="3" --> |
|    30    |   1.073.741.823  |  34 a<!-- .element: class="fragment" data-fragment-index="4" --> |



## Module in Python

* helfen Programme aufzuteilen
* Programmcode kann wieder verwendet werden
* einzubinden über `import`
* externe Module/Bibliotheken können importier werden


## Module in Python
* Bsp:
  * `math`
    * `sin()`,`cos()`,`log()`
    * `pi`, `e`
  * `os`
    * `listdir()`,`name()`,...
  * `datetime`
  * `random`


## Einbinden eigener Module
* Bsp:
  * Helfer Funktionen in `myfunctions.py`
  * `import myfunctions`
    * stellt Funktionen von `myfunctions.py` bereit

```python
# myfunctions.py
def helper(test):
    return test*100
```
```python
# myprogram.py
import myfunctions

print(myfunctions.helper(10))
```


## Einbinden eigener Module
```python
# myfunctions.py
def helper(test):
    return test*100
```
```python
# myprogram.py
import myfunctions as mf

print(mf.helper(10))
```


## Module zu Paketen zusammenfassen
* Ordner mit Paketnamen
* Ein File für jedes Modul

```txt
mypackage/
  __init__.py # optional
  myfunctions.py
  module2.py
  module3.py
```
```python
from mypackage import myfunctions
from mypackage import * # alles importieren, setzt __init__.py voraus
```
Siehe Doku [<i class="fa fa-info-circle" aria-hidden="true" title="Info"></i>](https://docs.python.org/3/tutorial/modules.html#packages)


# Objektorientierung in Python


## Objektorientierung in Python
* Hilft bei der Abstrahierung von Problemstellungen
* Datenstrukturen und dazu passende Funktionen werden zu einem Objekt zusammengefasst


## Klassen
```python
class MyClass:
  globalClassCount = 0
  def __init__(self, initialData):
    self.data = initialData
    MyClass.globalClassCount += 1

  def getData(self):
    return self.data
  def getClassCount(self):
    return MyClass.globalClassCount
```


## Demo


## Vererbung
* Verbessert die Wiederverwendbarkeit und Erweiterbarkeit von Code
* Basisklasse vererbt Eigenschaften und Fähigkeiten
* Tochterklasse wird um Funktionalität und Eigenschaften erweitert


## Vererbung
```python
class A:
    def __init__(self):
        self.X = 2
        self.Y = 3
        print("Konstruktor in A")
    def getX(self):
        return self.X
class B(A):
    def getArea(self):
        return self.X * self.Y

b = B()
print(b.getArea())
print(b.getX())
```
```txt
Konstruktor in A
6
2
```
<!-- .element: class="fragment" data-fragment-index="1" -->



# Fragen?


## Nächstes Mal
2016-12-14 16:00
