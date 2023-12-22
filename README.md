# Timetable

Tento Python program generuje a hodnotí rozvrhy. Využívá multiprocessing a shuffle pro současný běh generování rozvrhů na více jádrech a proces Watchdog pro ukončení generování, pokud přesáhne stanovený časový limit.

 Programovací prostředí: PyCharm 
  
 Autor: Šimon Bernard C4b

## Třídy

### Timetable:

* Spravuje generaci a hodnocení rozvrhů.
* Využívá třídu TimetableEvaluator k hodnocení vygenerovaných rozvrhů.
* Používá multiprocessing pro současnou generaci.
* Zamíchá rozvrh pro přetížení procesorů po určitou dobu.

### TimetableEvaluator:

* Hodnotí rozvrhy na základě pravidel docházky, penalizace opakování předmětu, penalizace změny místa, penalizace oběda a limitu denního studia.
* Poskytuje metody pro získání instance lekce pro dané číslo předmětu, hodnocení celého rozvrhu a hodnocení rozvrhu jednoho dne.

### Lesson:

* Reprezentuje lekci nebo hodinu ve výuce.
* Ukládá informace, jako jsou ID, název, učitel, název třídy, číslo patra a typ.
* Poskytuje textové reprezentace lekce.

### Watchdog:

* Monitoruje určitý proces a ukončí jej po uplynutí stanoveného časového limitu.
* Používá se k omezení doby generování rozvrhů.

## Spuštění hlavního programu

* git clone https://github.com/SimonBer7/Timetable.git
* cd Timetable
* python main.py


