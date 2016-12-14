# 706.088 Informatik 1
###Betriebssysteme



## Wiederholung
* Analytische Problemlösung
* Fermi Probleme
* Algorithmus
  * Türme von Hanoi (Rekursion)
* Module
* Klassen (Vererbung)



# Betriebssysteme


## Aufgaben des Betriebssystems

* Verwaltet Ressourcen
  * CPU Zeit, RAM, I/O, Prozesse
* Verwaltet I/O
    * Monitor, Tastatur, Festplatten, Netzwerk
* Zuteilung von Prioritäten
  * CPU Zeit an wichtige Programme
* Verwaltung von Rechten
  * Voneinander unabhängige Benutzer und Programme stören sich nicht.


## Interaktion mit dem Betriebssystem
<p class="wikipedia"><a href="https://commons.wikimedia.org/wiki/File:Operating_system_placement-de.svg#/media/File:Operating_system_placement-de.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Operating_system_placement-de.svg/1200px-Operating_system_placement-de.svg.png" alt="Operating system placement-de.svg"></a><br>Von Golftheman <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=18122125">Link</a></p>



## Komponenten eines modernen Betriebssystems

* Kernel
  * Verbindet Software über Treiber und Firmware mit der Hardware
* Prozesse
  * Jedes gestartete Programm wird als eigener Prozess geführt
  * Prozesse sollen unabhängig voneinander funktionieren. Stürzt Prozess A ab, soll Prozess B weiter laufen.


## Kernel
  <p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Kernel_Layout.svg#/media/File:Kernel_Layout.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Kernel_Layout.svg/1200px-Kernel_Layout.svg.png" alt="Kernel Layout.svg"></a><br>By <a href="//commons.wikimedia.org/w/index.php?title=User:Bobbo&amp;action=edit&amp;redlink=1" class="new" title="User:Bobbo (page does not exist)">Bobbo</a> - <span class="int-own-work" lang="en">Own work</span>, <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=4392180">Link</a></p>



## Komponenten eines modernen Betriebssystems
* Speicherverwaltung
  * Regelt welches Programm auf welchen Bereich im Speicher Zugriff hat
  * Zugriffe eines Programms auf fremde Speicheradressen resultiert in einem Fehler
* Mulit-Tasking
  * Erlaubt das Ausführen von mehreren Programmen 'gleichzeitig' (eigentlich schnell hintereinander)


## Komponenten eines modernen Betriebssystems
###Benutzerschnittstellen
* Grafische Benutzeroberfläche
  * Fenstermanager
  * "Einfachere Handhabung"
* CLI (Command Line Interface)
  * Konsole
  * Server oder Remote Umgebungen



## Geschichte der Betriebssysteme
* bis 1945 kaum relevant
  * Berechnungen und Software waren sehr spezialisiert
* Zwischen 1945 und 1965
  * Anfang 1950 konnte ein Computer nur ein Programm (gleichzeitig) ausführen
  * 1960 erste (erschwingliche) Transistorrechner (in Rechenzentren)


## Geschichte der Betriebssysteme
* Von 1965 bis 1980
  * Timesharing-Systeme (70er Jahre)
    * Main-Frame mit vielen Terminals
  * Prozessrechnersysteme


### Main-Frame
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Telefunken-tr4.jpg#/media/File:Telefunken-tr4.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Telefunken-tr4.jpg/1200px-Telefunken-tr4.jpg" alt="Telefunken-tr4.jpg"></a><br>Von <a href="//commons.wikimedia.org/w/index.php?title=User:Grkauls&amp;action=edit&amp;redlink=1" class="new" title="User:Grkauls (page does not exist)">Grkauls</a> - <span class="int-own-work" lang="de">Eigenes Werk</span>, Gemeinfrei, <a href="https://commons.wikimedia.org/w/index.php?curid=6746612">Link</a></p>


### Main-Frame-Terminal
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Zenith_Z-19_Terminal.jpg#/media/File:Zenith_Z-19_Terminal.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Zenith_Z-19_Terminal.jpg/1200px-Zenith_Z-19_Terminal.jpg" alt="Zenith Z-19 Terminal.jpg"></a><br>By <a rel="nofollow" class="external text" href="http://www.flickr.com/people/15587432@N02">Jamie Cox</a> from Melbourne, USA - <a rel="nofollow" class="external text" href="http://www.flickr.com/photos/15587432@N02/3281139507/">Zenith Z-19 Terminal</a>
Uploaded by <a href="//commons.wikimedia.org/w/index.php?title=User:Mewtu&amp;action=edit&amp;redlink=1" class="new" title="User:Mewtu (page does not exist)">Mewtu</a>, <a href="http://creativecommons.org/licenses/by/2.0" title="Creative Commons Attribution 2.0">CC BY 2.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=8725026">Link</a></p>


## Geschichte der Betriebssysteme
* 1980 bis heute
  * Entwicklung von Mikroprozessoren
  * Computer am Arbeitsplatz (Workstations)
    * Mit grafischer Ausgabe
  * Neue Anforderungen an Betriebssystem


## UNIX
### Unix' creators
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Ken_n_dennis.jpg#/media/File:Ken_n_dennis.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/3/36/Ken_n_dennis.jpg" alt="Ken n dennis.jpg"></a><br>K. Thompson & D. Ritchie, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=31308">Link</a></p>


## UNIX Evolution
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Unix_history-simple.svg#/media/File:Unix_history-simple.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Unix_history-simple.svg/1200px-Unix_history-simple.svg.png" alt="Unix history-simple.svg"></a><br>By <a href="//commons.wikimedia.org/wiki/User:Eraserhead1" title="User:Eraserhead1">Eraserhead1</a>, <a href="//commons.wikimedia.org/wiki/User:Infinity0" title="User:Infinity0">Infinity0</a>, <a href="//commons.wikimedia.org/wiki/User:Sav_vas" title="User:Sav vas">Sav_vas</a> - <a rel="nofollow" class="external text" href="http://www.levenez.com/unix/history.html">Levenez Unix History Diagram</a>, <a rel="nofollow" class="external text" href="http://www.ibm.com/developerworks/library/it-schenk1/schenk3.html">Information on the history of IBM's AIX on ibm.com</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=1801948">Link</a></p>


## Geschichte von Linux und BSD
* Universität Berkley, Kalifornien, startet in den 1970ern BSD (Berkley Software Distribution)
  * BSD ist ein UNIX Derivat und kann gratis im Internet bezogen werden.
    * FreeBSD, OpenBSD, NetBSD sind freie Derivate (BSD-Lizenz)

<section style="height:150px;">
[![](imgs/09/Bsd_daemon.jpg)](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution)
[![](imgs/09/freebsd.jpg)](https://freebsd.org)
[![](imgs/09/openbsd.png)](https://openbsd.org)
[![](imgs/09/netbsd.png)](https://netbsd.org)
</section>


## Geschichte von Linux und BSD
Idealist Richard Stallman gründet das GNU Project (Anfang der 1980er)

<section>
<a href="https://commons.wikimedia.org/wiki/File:Gnu-color-reiss-head.jpg#/media/File:Gnu-color-reiss-head.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/8/85/Gnu-color-reiss-head.jpg" alt="Gnu-color-reiss-head.jpg"></a>
<a href="https://commons.wikimedia.org/wiki/File:Richard_Matthew_Stallman.jpeg#/media/File:Richard_Matthew_Stallman.jpeg"><img src="https://upload.wikimedia.org/wikipedia/commons/f/f7/Richard_Matthew_Stallman.jpeg" alt="Richard Matthew Stallman.jpeg"></a>
</section>
<p class=wikipedia>1: By Joseph W. Reiss for the Free Software Foundation - <a rel="nofollow" class="external text" href="http://www.gnu.org/graphics/reiss-gnuhead.html">Color Gnu Head</a>, <a href="http://artlibre.org/licence/lal/en" title="Free Art License">FAL</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=272866">Link</a></br>
2: By Sam Williams - Taken from the cover of the O'Reilly book <a href="https://en.wikipedia.org/wiki/Free_as_in_Freedom:_Richard_Stallman%27s_Crusade_for_Free_Software" class="extiw" title="w:Free as in Freedom: Richard Stallman's Crusade for Free Software">w:Free as in Freedom: Richard Stallman's Crusade for Free Software</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=208390">Link</a></p>


## Geschichte von Linux und BSD
* Komplett **freie Software** für Endanwender (versus proprietäres UNIX OS)
* Einzelne Programme funktionieren gut, der Kernel, der das UNIX Pendant ersetzen soll, nicht.



## Freie Software


## 4 Freiheiten Freier Software<!-- .slide: data-background="#91D074" data-background-transition="zoom"-->
1. Die Freiheit, das Programm **auszuführen**, wie man möchte, für jeden Zweck.
2. Die Freiheit, die Funktionsweise des Programms zu untersuchen und eigenen Bedürfnissen der Datenverarbeitung **anzupassen**
3. Die Freiheit, das Programm **weiterzuverbreiten** und damit seinen Mitmenschen zu helfen
4. Die Freiheit, das Programm **zu verbessern** und diese Verbesserungen der Öffentlichkeit freizugeben, damit die gesamte Gemeinschaft davon profitiert


## Freie Software
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Floss-license-slide-image.png#/media/File:Floss-license-slide-image.png"><img src="https://upload.wikimedia.org/wikipedia/commons/1/1d/Floss-license-slide-image.png" alt="Floss-license-slide-image.png"></a><br>By David A. Wheeler - <a rel="nofollow" class="external free" href="http://www.dwheeler.com/essays/floss-license-slide.html">http://www.dwheeler.com/essays/floss-license-slide.html</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=41060008">Link</a></p>

Mehr Information zu <a href="https://de.wikipedia.org/wiki/Freie_Software">Freier Software <i class="fa fa-info-circle" aria-hidden="true" title="Info"></i></a>




## Geschichte von Linux und BSD
* 1991 veröffentlicht der finnische Student Linus Torvalds die erste Version des **LINUX Kernel**

<section><p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Linus_Torvalds_(cropped).jpg#/media/File:Linus_Torvalds_(cropped).jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/5/5c/Linus_Torvalds_%28cropped%29.jpg" alt="Linus Torvalds (cropped).jpg"></a><br>Linus Torvalds (2002), <a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=4703850">Link</a></p></section>


## Geschichte von Linux und BSD
* Linux und GNU werden zusammengeführt und es entsteht: **GNU/Linux**, heute meist Linux genannt.

<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Tux.svg#/media/File:Tux.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg" alt="Tux.svg" width="123" height="145"></a><br>By <a rel="nofollow" class="external text" href="http://www.isc.tamu.edu/~lewing/">Larry Ewing</a>, <a rel="nofollow" class="external text" href="http://www.home.unix-ag.org/simon/">Simon Budig</a>, <a rel="nofollow" class="external text" href="https://github.com/garrett/Tux">Garrett LeSage</a> - <a rel="nofollow" class="external autonumber" href="http://www.home.unix-a<i class="twa twa-exclamation-mark twa">g.org/simon/penguin/">[1]</a>, <a rel="nofollow" class="external text" href="https://github.com/garrett/Tux">garrett/Tux</a> on GitHub, <a href="http://creativecommons.org/publicdomain/zero/1.0/deed.en" title="Creative Commons Zero, Public Domain Dedication">CC0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=753970">Link</a></p>


Wer hat bereits Linux verwendet?



#### Wer hat bereits Linux verwendet?
<!-- .slide: data-background-image="imgs/09/900px-APK_format_icon.png" data-background-size="contain"-->
Android™ basiert auf dem Linux Kernel!


Wer hat schon BSD verwendet?

<div>**Mac OS X** ist ein BSD Derivat.</br>
(basiert auf NEXTSTEP/OPENSTEP, das auf BSD basiert)</div>
<!-- .element: class="fragment" data-fragment-index="1" -->


## MS Windows
proprietäres Betriebssystem, grafische Oberfläche
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Microsoft_Windows_1.0.png#/media/File:Microsoft_Windows_1.0.png"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Microsoft_Windows_1.0.png/1200px-Microsoft_Windows_1.0.png" alt="Microsoft Windows 1.0.png"></a><br>By Microsoft - <a class="external free" href="https://commons.wikimedia.org/wiki/File:Microsoft_Windows_1.0_pages2_3.jpg">https://commons.wikimedia.org/wiki/File:Microsoft_Windows_1.0_pages2_3.jpg</a>, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=41709704">Link</a></p>


## Betriebssystem Architekturen (Kernels)<!-- .slide: style="font-size:.8em" -->
* Monolithischer Kernel
  * starke Abhängigkeiten zwischen Komponenten
* Microkernel
  * User-space übernimmt mehr Aufgaben des Kernels
* Hybrid Kernel
  * Mix aus monolithischem und micro Kernel
* Exokernels
  * Research Kernel für sehr minimalistischen Ansatz


## Ressourcenverwaltung

* Interrupts
* Multi-Tasking
* Scheduler
* Deadlock


## Interrupts
* Wichtige Funktion von Betriebssystemen
* Ermöglicht mit der Umwelt zu interagieren
* Ohne Interrupts müsste OS durchgehend alle möglichen Input-Quellen überwachen
* Interrupt wird durch Hardware/Software ausgelöst und meldet dem OS "Handlungsbedarf"
* Je nach Interrupt-Typ wird entsprechend geantwortet (abgearbeitet)


## Prozessor-Zeit & Multi-Tasking
Multi-Tasking bedeutet mehrere Aufgaben 'gleichzeitig' auszuführen
* Prozesse werden sehr schnell nacheinander 'ausgeführt' (Zeit-Multiplexing)
* Echte Parallelisierung ist nur auf Mehr-Kernsystemen möglich (Multiprocessing)
* Betriebssystem steuert welcher Prozess wieviel Zeit erhält


## Prozess Scheduler
* Der Kernel eines Betriebssystems beinhaltet einen so genannten Scheduler
* Dieser bestimmt wie viel Zeit jeder der laufenden Prozesse für Berechnungen zur Verfügung gestellt bekommt
* Er legt auch die Reihenfolge der Prozessor-Zeit-Slots fest
* Verschiedene Strategien sind möglich:
  * Keine Bevorzugung: First come, first serve!
  * Bewertung der Prozesse nach Wichtig-/Dringlichkeit


## Deadlock
Mehrere Prozesse warten auf Ressourcen von anderen Prozessen, keiner kann weiter machen: alle stehen!
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Deadlock_at_a_four-way-stop.gif#/media/File:Deadlock_at_a_four-way-stop.gif"><img src="https://upload.wikimedia.org/wikipedia/commons/2/23/Deadlock_at_a_four-way-stop.gif" alt="Deadlock at a four-way-stop.gif"></a><br>Von <a href="//commons.wikimedia.org/wiki/User:Marble_machine" title="User:Marble machine">Marble machine</a> - <span class="int-own-work" lang="de">Eigenes Werk</span>, <a href="http://creativecommons.org/licenses/by-sa/4.0" title="Creative Commons Attribution-Share Alike 4.0">CC-BY-SA 4.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=47970297">Link</a></p>


## Vermeidung von Deadlock und Race-Conditions<!-- .slide: style="font-size:.85em" -->
* **Mutex** (Mutual Exclusive)
  * Bestimmte Code-Bereiche werden für mehrfachen Zugriff gesperrt (=Prozess schläft)
  * Erst nach Freigabe, kann der nächste Prozess auf die Resource zugreifen (=Prozess aufwecken)
* **Semaphore**
  * Counter (# Ressourcen), wenn 0, Prozess zu Warteschlange
  * Warteschlange:
    * Speichert schlafende Prozesse und kann diese gezielt wecken


## Speicherverwaltung und Swapping<!-- .slide: style="font-size:.85em" -->
Memory Management Unit verwaltet den Speicher und lagert bei Bedarf Daten aus
* Legt fest:
  * Welches Programm auf welche Speicherbereiche zugreifen darf
  * Welche Daten im Speicher ausgelagert werden
    * Auslagern: Daten vom schnellen RAM auf langsame Festplatten
    * Bei Bedarf müssen Daten wieder zurück ins RAM geladen werden


## Arten von Betriebssystemen
* Echtzeit Betriebssysteme:
  * meist in eingebettete Systemen (Auto, Robotik, etc.)
* Single-tasking BS:
  * Nur ein Programm kann ausgeführt werden
* Multi-tasking BS:
  * Mehrer Programme können 'gleichzeitig' ausgeführt werden


## Arten von Betriebssystemen<!-- .slide: style="font-size:.9em" -->
* Einzel- & Multi-User BS:
  * Unterscheidung der Benutzer (z.B.: über Benutzeraccounts)
  * Programme und Speicher (Rechtemanagement) muss verwaltet werden
* Verteilte (Betriebs)Systeme:
  * Verbinden mehrere (verteilte) Computer zu einem System
* Eingebette Betriebssysteme:
  * Werden für spezielle Geräte entwickelt (z.B.: Android, iOS)


## LOC / OS
<section>Lines of Code per Operating System[*](https://docs.google.com/spreadsheets/d/1s9u0uprmuJvwR2fkRqxJ4W5Wfomimmk9pwGTK4Dn_UI/edit#gid=5)[*](http://www.informationisbeautiful.net/visualizations/million-lines-of-code/)</section><!-- .element: style="font-size:.6em"-->

| OS                |  Jahr   |  KLOC (LOC*1000)   |
|  ----    |           :-:    |  ---:   |
| UNIX 1.0 |    1971          |   10    |
| Windows 3.1 |     1992   |  2.500   |
| Mars Curiosity Rover |      |  5.000   |
| Android     |               |  12.000  |
| Boing 787   |               |  14.000  |
| Linux Kernel 3.1 |   2013   |  15.000  |
| Windows 7        |          |  40.000  |
| Mac OS 10.4      | 2005     |  86.000  |
| Debian 5         |  2009    |  324.000 |
| Debian 7         |  2012    |  419.000 |
<!-- .element: style="font-size:.7em"-->
<!--| Windows NT 3.1 |     1993   |  4.500   |-->



## Fragen?



## Frohe Feiertage
<i class="twa twa-candle twa-5x"></i><i class="twa twa-christmas-tree twa-5x"></i>
## und guten Rutsch!
<i class="twa twa-party-popper twa-5x"></i><i class="twa twa-fireworks twa-5x"></i>
