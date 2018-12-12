# 706.088 Informatik 1


# Testing & </br> Pythonic Coding


## Inhalt
* Testing - Theory
* Pytest, Unittest
* PyLint, Pep8, Tox
* Pythonic Code


## Wiederholung


# Warum Testen?
* Fehler früh finden
* Nachweis korrekter Software?
* Test-Driven-Development


## Testschritte in Softwareprojekten
* **Komponententest** (Unit-Test) <i class="fa fa-arrow-left fa-tugraz-color" aria-hidden="true" Title="pytest etc."></i>
* Integrationstest
* Systemtest
* Abnahmetest


## Welche Fehler werden gefunden?
* Programmierfehler
* Semantische Fehler
* *vielleicht* Arithmetische Fehler
* *vielleicht* Laufzeitfehler
* *vielleicht* Logikfehler
* **nicht** Designfehler
* Programmierfehler
  * Syntaxfehler
  * Lexikalischer Fehler


## pytest, Unittest
* [pytest](https://docs.pytest.org/en/latest/) <i class="fa fa-arrow-left fa-tugraz-color" aria-hidden="true" Title="empfohlen"></i>
* [Unittest](https://docs.python.org/3.6/library/unittest.html), in der Standard Lib
  </br>auch bekannt als **PyUnit**


## Demo
pytest [Beispiele](https://docs.pytest.org/en/latest/example/index.html)


## Pep8
* [Python Code Style Guideline](https://www.python.org/dev/peps/pep-0008/)
* vorgeschlagen 2001 von Guido van Rossum
* Tools zum Aufräumen:
  * [Flake8](https://gitlab.com/pycqa/flake8)
  * [PyLint](https://www.pylint.org/)
  * pycodestyle (formerly pep8)
  * mypy


## PyLint
* Codestandard check
* Fehlererkennung
* Refactoring Hilfe
  * [Errorcodes](http://pylint-messages.wikidot.com/all-codes)


## Flake8
* kombiniert (pyflakes und PEP-8 Checks)
* `python3 -m pip install flake8`
* `flake8 your_code.py`
  * [Errorcodes](http://flake8.pycqa.org/en/latest/user/error-codes.html)


## Tox
* [Tox](https://tox.readthedocs.io/en/latest/) will Testprozess für Python standardisieren
* Baut eigene [virtualenv](https://pypi.org/project/virtualenv) Umgebung für jeden Testlauf
* integriert pytest, pyflakes, pylint, pep8 etc.
* testen für verschiedene Python Versionen.


## Continuous Integration
* Automatisches Testen und Deployen aus der Codeverwaltung
* git -> tests -> packaging -> push



# Pythonic Code
> Code, der Eigentheiten von Python ausnützt und den Dialekt der Sprache ausschöpft.

Code Beispiele aus [Raymond Hettingers Talk](https://www.youtube.com/watch?v=OSGv2VnC0go)


## Schleifen
```python
for i in [0, 1, 2, 3, 4, 5, 6]:
  print(i**2)
```
```python
for i in range(7):
  print(i**2)
```
<!-- .element: class="fragment" data-fragment-index="2" -->


## Schleife
```python
fruit_basket = ["banana", "apple", "pear", "plum"]

for i in range(len(fruit_basket)):
  print(fruit_basket[i])
```
```python
for fruit in fruit_basket:
  print(fruit)
```
<!-- .element: class="fragment" data-fragment-index="2" -->


## Schleife rückwärts<!-- .element: class="fragment" data-fragment-index="2" -->
```python
fruit_basket = ["banana", "apple", "pear", "plum"]

for i in range(len(fruit_basket)-1, -1, -1):
  print(fruit_basket[i])
```
```python
for fruit in reversed(fruit_basket):
  print(fruit)
```
<!-- .element: class="fragment" data-fragment-index="2" -->


## Listen mit Index<!-- .element: class="fragment" data-fragment-index="2" -->
```python
fruit_basket = ["banana", "apple", "pear", "plum"]

for i in range(len(fruit_basket)):
  print(i, '=', fruit_basket[i])
```
```python
for i, fruit in enumerate(fruit_basket):
  print(i, '=', fruit)
```
<!-- .element: class="fragment" data-fragment-index="2" -->


## Listen sortiert<!-- .element: class="fragment" data-fragment-index="2" -->
```python
fruit_basket = ["banana", "apple", "plum", "pear"]

for fruit in sorted(fruit_basket):
  print(fruit)
```


## Sortieren mit spezial Funktion<!-- .element: class="fragment" data-fragment-index="2" -->
```python
fruit_basket = ["banana", "apple", "plum", "pear"]
# print( fruits sorted by length )
```
```python
for fruit in sorted(fruit_basket, key=len):
  print(fruit)
```
<!-- .element: class="fragment" data-fragment-index="2" -->


## Lesen bis zum Endzeichen<!-- .element: class="fragment" data-fragment-index="2" -->
```python
blocks = []
while True:
  block = f.read(32)
  if block == '':
    break
  blocks.append(block)
```
```python
blocks = []
for block in iter(partial(f.read, 32), ''):
  blocks.append(block)
```
<!-- .element: class="fragment" data-fragment-index="2" -->


## Ende einer Schleife
```python
def find(seq, target):
  found = False
  for i, value in enumerate(seq):
    if value == target:
      found = True
      break
  if not found:
    return -1
  return i
```
```python
def find(seq, target):
  for i, value in enumerate(seq):
    if value == target:
      break
  else:
    return -1
  return i
```
<!-- .element: class="fragment" data-fragment-index="2" -->


## Schleife über 2 Listen<!-- .element: class="fragment" data-fragment-index="2" -->
```python
fruit_basket = ["banana", "apple", "pear", "plum", "cherry"]
kids = ["tom", "jenny", "william", "betty"]

n = min(len(kids), len(fruit_basket))
for i in range(n):
  print(kids[i], '=', fruit_basket[i])
```
```python
for name, fruit in zip(kids, fruit_basket):
  print(name, '=', fruit)
```
<!-- .element: class="fragment" data-fragment-index="2" -->


## List Comprehensions
```python
result = []
for i in range(10):
  squares = i ** 2
  result.append(squares)
print(sum(result))
```
```python
print(sum( [i**2 for i in range(10)] ))
```
<!-- .element: class="fragment" data-fragment-index="2" -->
```python
# Generator Expression
print(sum( i**2 for i in range(10) ))
```
<!-- .element: class="fragment" data-fragment-index="3" -->
* <!-- .element: class="fragment" data-fragment-index="3" --> PEP zu [Generator Expressions](https://www.python.org/dev/peps/pep-0289/)


## Dictionaries
```python
d = {'banana': 'yellow', 'apple': 'red', 'pear': 'green'}

for k in d:
  print(k)
```
```python
for k in d.keys():
  if k.startswith('p')
    del d[k]
```
<!-- .element: class="fragment" data-fragment-index="2" -->
```python
# upper example changes stuff it's iterating over! That's bad!!
# better do this:
d = {k: d[k] for k in d if not k.startswith('p')}
```
<!-- .element: class="fragment" data-fragment-index="3" -->


## Dictionaries: Keys, Values
```python
d = {'banana': 'yellow', 'apple': 'red', 'pear': 'green'}

for k in d:
  print(k, '=', d[k])
```
```python
for k, v in d.items():
  print(k, '=', v)
```
<!-- .element: class="fragment" data-fragment-index="2" -->
```python
for k, v in d.iteritems():
  print(k, '=', v)
```
<!-- .element: class="fragment" data-fragment-index="3" -->


## Dictionaries erstellen
```python
fruit_basket = ["banana", "apple", "pear", "plum"]
kids = ["tom", "jenny", "william", "betty"]

d = dict(zip(kids, fruit_basket))
```


## Funktions Signaturen
```python
sort_input(input, 30, False)
```
```python
sort_input(input, num=30, reversed=False)
```


## Sequence unpacking
```python
name = student[0]
birthday = student[1]
field_of_study = student[2]

name, birthday, field_of_study  = student
```


## Strings verknüpfen
```python
kids = ["tom", "jenny", "william", "betty",
        "andrea", "tim", "angela"]

s = kids[0]
for kid in kids[1:]:
  s += ', ' + kid

print(', '.join(kids))
```


## Fragen?



## Prüfung
2019-01-23  **i13**  20:00


### Frohe Feiertage
<i class="twa twa-candle twa-4x"></i><i class="twa twa-christmas-tree twa-4x"></i>
### und guten Rutsch!
<i class="twa twa-party-popper twa-4x"></i><i class="twa twa-fireworks twa-4x"></i>
