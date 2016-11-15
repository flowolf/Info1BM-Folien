# 706.088 Informatik 1


### Überblick
* Datenstrukturen
* Zahlensysteme
* Bit-Operatoren



# Datenstrukturen


## Datenstrukturen
Dienen dem systematischen Ablegen und Aufrufen von Daten.

* Speicherung
* Organisation
* Effizienz
* regelt Art des Zugriffs


## Datenstrukturen
### Beispiele

* Tupel
* Array
* assoziatives Array (Dictionary)
* Warteschlange (FiFo)
* Stapelspeicher (LiFo)
* Graphen
* Bäume (Binärbaum)


## Array

```python
a = [1,"b","III",4,5]
a[0]
a[2]
a[5]
```
```bash
1
'III'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```


## Dictionary
```python
d = {"element1": 1, "myelement": "python", "python": 3.5}
d['element1']
d['python']
d['myelement']
```
```bash
1
3.5
'python'
```


## Warteschlange (FiFo)
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Data_Queue.svg#/media/File:Data_Queue.svg"><img alt="Data Queue.svg" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/1200px-Data_Queue.svg.png"></a><br>By <a href="https://upload.wikimedia.org/wikipedia/commons/5/52/Data_Queue.svg" class="internal" title="Data Queue.svg">This Image</a> was created by <a href="https://en.wikipedia.org/wiki/User:Vegpuff" class="extiw" title="en:User:Vegpuff">User:Vegpuff</a>. - <span class="int-own-work" lang="en">Own work</span>, <a title="Creative Commons Attribution-Share Alike 3.0" href="http://creativecommons.org/licenses/by-sa/3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=7586271">https://commons.wikimedia.org/w/index.php?curid=7586271</a></p>


## Warteschlange (FiFo)
```python
import queue
q = queue.Queue()
q.put(1)
q.put(2)
q.put("last")

q.get()
q.empty()
q.get()
q.get()
q.empty()
```
```bash
1
False
2
'last'
True
```


## Stapelspeicher (LiFo)
[![Stack](https://upload.wikimedia.org/wikipedia/commons/b/b4/Lifo_stack.png)](https://commons.wikimedia.org/wiki/File:Lifo_stack.png)<!-- .element: class="stretch" -->


## Stapelspeicher (LiFo)
```python
import queue
q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put("last")

q.get()
q.empty()
q.get()
q.get()
q.empty()
```
```bash
'last'
False
2
1
True
```


## Graphen
* bestehen aus **Kanten** und **Knoten**
* Eigenschaften:
  * gerichtete Graphen: Kanten haben Richtung
  * ungerichtete Graphen können in beide Richungen 'begangen' werden.
  * gewichtet: Kanten haben Gewicht
  * zyklisch: Weg von Knoten A zurück zu A ohne eine Kante mehrfach zu gehen


## Graphenoperationen

* Hinzufügen eines Knotens (mit oder ohne Kanten)
* Entfernen des Knotens A, entfernt auch alle Kanten zu A
* Es gibt keine Kanten ohne Knoten an beiden Enden


## Bäume
Sonderform von Graphen
* Bäume: zusammenhängende, azyklische Graphen
  * gerichtet
  * ungerichtet
  * Binärbaum: maximal 2 Nachkommen pro Knoten



# Zahlensysteme


## Dezimal
* **Dezimal**-system: Basis 10 (std. Integer)

| Zahlen | Präfix |
|:-:|:-:|
| 0-9    |  "" (keiner)      |

```python
>>> i = 123
>>> i
123
>>> f = int("99")
>>> f
99
>>>
```


## Hex
* **Hexadezimal**-system: Basis 16

| Zahlen | Präfix |
|:-:|:-:|
| 0-9, A-F   | "0x"       |

```python
>>> h = 0xA
>>> h
10
>>> h2 = 0xFF
>>> h2
255
```


## Oktal
* **Oktal**-system: Basis 8

| Zahlen | Präfix |
|:-:|:-:|
| 0-7    | "0o" (Null-O)  |

```python
>>> o = 0o7
>>> o
7
>>> o2 = 0o144
>>> o2
100
```


## Binär
* **Binär**-system oder **Dual**-system: Basis 2

| Zahlen | Präfix |
|:-:|:-:|
| 0,1    | "0b"  |

```python
>>> b = 0b101
>>> b
5
>>> b2 = 0b111111
>>> b2
63
```


## Binärsystem
* Basis für Computer
* Reduktion auf 2 Zustände
  * 0: kein Strom, Spannung
  * 1: Strom, Spannung


## Binärsystem
* Einzelne Stelle heisst: Bit (**Bi**nary Digi**t**)
* rechteste Stelle: Least Significant Bit (LSB)
* linkeste Stelle: Most Significant Bit (MSB)


## Binärsystem
```python
# Dezimal
i = 2*10**3 + 0*10**2 + 1*10**1 + 6*10**0 # 2016

# Binär
b = 1*2**3 + 1*2**2 + 0*2**1 + 1*2**0 # 13
```


## Binärsystem Umrechnung (n=2)
* x(10) → x(n):
  * x/n ⇒ y, Rest z
  * z an Stelle 0
  * y ⇒ x wenn y != 0
  * von Vorne für Stelle 1, 2, …
  * wenn y = 0 fertig.


## Binärsystem Umrechnung
25(10) → binär:
  * 25/2 ⇒ 12, Rest 1
  * 1 an Stelle 0 (LSB)
  * 12/2 ⇒ 6, Rest 0
  * 0 an Stelle 1
  * 6/2 ⇒ 3, Rest 0
  * 0 an Stelle 2
  * …


  * 3/2 ⇒ 1, Rest 1
  * 1 an Stelle 3
  * 1/2 ⇒ 0, Rest 1
  * 1 an Stelle 4
  * fertig: 11001



## Rechnen im Binärsystem
Grundregeln für Addition:

|||
|---|---|
| 0 + 0 | = 0 |
| 0 + 1 | = 1 |
| 1 + 0 | = 1 |
| 1 + 1 | = 0 (1 Übertrag) |
| 1 + 1 + 1 | = 1 (1 Übertrag) |


## Binäre Addition
|+||
|---|---|
| 0101101 | = 45 |
| 0110110 | = 54 |
| 1111    | = Übertrag |
| 1100011 | = 99 |


## Binäre Subtraktion
Computer führt Addition auf Subtraktion zurück:
möglich durch Zweier-Komplementbildung
* Darstellung von negativen Zahlen:
  * MSB trägt Information über Vorzeichen
* Limit an darstellbaren Zahlen:
  * `s`: verfügbaren Bits
  * Kleinste darstellbare Zahl: `-2**(s-1)`
  * Größte darstellbare Zahl: `2**(s-1)-1`


## Positive und Negative Binärzahlen<!-- .slide: style="font-size:0.9em" -->
| bin | dec | bin  | dec |
|---|:-:|---|:-:|
| 0000 | 0  | 1000 | -8  |
| 0001 | 1  | 1001 | -7  |
| 0010 | 2  | 1010 | -6  |
| 0011 | 3  | 1011 | -5  |
| 0100 | 4  | 1100 | -4  |
| 0101 | 5  | 1101 | -3  |
| 0110 | 6  | 1110 | -2  |
| 0111 | 7  | 1111 | -1  |


## Zweier-Komplementbildung
* ist MSB 1, ist die Zahl negativ
* Schritt 1: alle Bits invertieren
* Schritt 2: zum Schluss 1 addieren

| 5(10) → -5 | 0101(2) | -5(10) → 5  | 1011(2) |
|---|:-|---|:-|
| Schritt 1: invertieren | 1010  |  |  0100  |
| Schritt 2: +1          | 1011  |  |  0101  |


## Subtraktion
Entspricht einer Addition mit dem Zweier-Komplement
* Was geschieht mit Überläufen?
  * werden verworfen

| 6(10) - 2(10) |→| 6(10) + -2(10) |
|---|-:|---|
| 6(10) | 0110 | |
| -2(10)| 1110 | |
|       | 1 0100 | = 4 |


## Multiplikation
kann __manchmal__ durch Verschieben der Bits nach links
durchgeführt werden

* Multiplikation mit `2**n`:
(Shiften um n Bits)

| 3*2 |     | 20*8    |    |
|---|-:|---|-:|
| **3**        | 011  | **20**  |    010100  |
| **2** (2**1) |  10  | **8** (2**3)   |    001000  |
| **6**        | 110  | **160** | 010100000  |


## Ausnahmen Multiplikation
Bei Multiplikation mit Zahlen ungleich `2**n`

```
13(10) *   5(10)
1101   * 101

 1101
+ 0000
+  1101
1000001  = 65
```


## Division
kann __manchmal__ durch Verschieben der Bits nach rechts
durchgeführt werden

* Division mit `2**n`:
(Shiften um n Bits)

| 4//2 = 2 |     | 24//8 = 3    |    |
|---|-:|---|-:|
| **4**        | 100  | **24**       |     11000  |
| **2** (2**1) |  10  | **8** (2**3) |     01000  |
| **2**        |  10  | **3**        |        11  |


## Ausnahmen Division
Bei Division mit Zahlen ungleich `2**n`

```python
25(10) //   5(10)
   11001   // 101  = 101
   110               ^^^
  -101   >----------/ ||
---------             ||
   110                ||
 +1010  Komplement    ||
 +   1                ||
---------             ||
 10001                ||
     10 >-------------/|
     101               |
    -101 >-------------/
---------
     101
   +1010  Komplement
   +   1
---------
   10000 ---> kein Rest
```
<!-- .element: style="font-size:0.42em" -->


## Limitierung der darstellbaren Zahlen
* Gängige Computer haben 32-bit oder 64-bit Architektur:
  * 32-bit: max positive Zahl `2**32 -1`
  * 64-bit: max positive Zahl `2**64 -1`
  * Python kann in Version 3 gut mit langen Zahlen umgehen.
  * Grundproblem bleibt generell für Computer bestehen.


```python
>>> i = 0b11111111111111111111111111111111
>>> i
4294967295
>>> i.bit_length()
32
>>> j = i+1
>>> j.bit_length()
33
>>> bin(j)
'0b100000000000000000000000000000000'
>>> i64 = 0b1111111111111111111111111111111111111111111111111111111111111111
>>> i64.bit_length()
64
>>> i64
18446744073709551615
```


## Umwandlung von 64-bit in 16-bit<!-- .slide: data-background-image="imgs/05/ariane5.gif"-->
* Ariane 5 Explosion [<i class="fa fa-info-circle" aria-hidden="true" title="Info"></i>](http://homepages.inf.ed.ac.uk/perdita/Book/ariane5rep.html) [<i class="fa fa-youtube-square" aria-hidden="true"></i>](https://www.youtube.com/watch?v=PK_yguLapgA)



# Bitoperatoren


## Bitoperatoren<!-- .slide: style="font-size:0.8em" -->
Operatoren für Binärdarstellung

| Operator    |  Zuweisung  |  Ergebnis  |
|  ---        |     ----    |   ----     |
| ~x          |              |  bitweises Komplement <br/> (Einerkomplement)  (= -x-1) |
| ~x+1        |              |  Zweierkomplement  (= -x)  |
| x & y       |   x &= y     |  bitweises UND (AND) |
| x &#124; y  |   x &#124;= y |  bitweises ODER (OR) |
| x ^ y       |   x ^= y      |  bitweises ausschließendes ODER (XOR) |
| x << n      |   x <<= n    |  shiften von x um n Bit nach links  |
| x >> n      |   x >>= n    |  shiften von x um n Bit nach rechts |


## Bitoperatoren
```python
>>> a = 0b1001
>>> b = 0b0110
>>> bin(a | b)
'0b1111'
>>> bin(a & b)
'0b0'
>>> bin(a ^ b)
'0b1111'
>>> bin(~a)
'-0b1010'
>>> bin(~a & b)
'0b110'
```


## Bitoperatoren
```python
>>> a = 0b1001
>>> b = 0b0110
>>> b >>= 1
>>> b
3
>>> bin(b)
'0b11'
>>> bin(a ^ b)
'0b1010'
>>> a << 2
36
>>> bin(a << 2)
'0b100100'
```


# Fragen?


## Nächstes Mal
2016-11-23 16:00

