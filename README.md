# 📊 Benchmark Interactiv de Algoritmi de Sortare (Python / Pygame)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pygame](https://img.shields.io/badge/Pygame-2.5-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Finalizat-brightgreen?style=for-the-badge)

## 📖 Despre Proiect

Acest proiect este o aplicație interactivă creată cu Python și Pygame pentru a testa, analiza și vizualiza performanța diferiților algoritmi de sortare. Scopul nostru este de a oferi un benchmark clar între algoritmii elementari ($O(n^2)$) și cei eficienți ($O(n \log n)$), evidențiind modul în care aceștia interacționează cu memoria prin operațiuni de interschimbare și comparare.

Aplicația se distinge prin faptul că permite vizualizarea animației de sortare pas cu pas, folosind conceptul de *generatori* (`yield`) din Python pentru a păstra interfața grafică responsivă în timpul calculelor.

**Aplicația măsoară și analizează:**
* ⏱️ **Timpul de execuție:** Măsurat precis la finalizarea sortării.
* 🔄 **Operațiunile interne:** Numărul total de comparații și interschimbări (swaps), actualizate live pe ecran.
* 📈 **Comportamentul pe seturi diverse de date:** Liste generate aleator, liste deja sortate, liste sortate invers.

---

## 👨‍💻 Echipa Proiectului

* **Molnar Răzvan** & **Roman Denis**
* **Specializare:** Informatică, Anul II

---

## 🚀 Jurnal de Activitate și Arhitectură Tehnică

✅ **Săptămâna 1-2: Setup și Arhitectura de Bază (Pygame Loop)**
* Am configurat fereastra principală Pygame.
* Am implementat bucla principală de evenimente (`main event loop`).
* Am creat clasa `DrawInformation` pentru gestionarea elementelor grafice.
* Am implementat funcția de generare a listei de numere aleatoare.

✅ **Săptămâna 3-4: Vizualizarea și Primii Algoritmi (Generators)**
* Am implementat funcția de desenare a listei (`draw_list`).
* Am implementat **Bubble Sort** și **Selection Sort** folosind `yield` pentru a menține animația fluidă.
* Am adăugat evidențierea vizuală a elementelor comparate.

✅ **Săptămâna 5-6: UI On-Screen și Sistemul de Metrici**
* Am integrat text renderizat pe ecran pentru afișarea controalelor (SPACE, R, A).
* Am implementat contoarele interne pentru comparații și interschimbări, afișate live.

✅ **Săptămâna 7-8: Algoritmi Avansați și Cazuri de Testare**
* Am implementat **Insertion Sort** și algoritmul recursiv **Quick Sort** (prin `yield from`).
* Am adăugat controale pentru generarea cazurilor de test: liste sortate invers și aproape sortate.

✅ **Săptămâna 9-10: Refactorizare (OOP) și Modul Benchmark Final**
* Am structurat codul în clase modulare (`AlgorithmManager`, `UIManager`).
* Am implementat "Summary Screen" cu statistici detaliate la finalul sortării.
* Am optimizat logica de randare pentru performanță sporită.
* Am finalizat documentația și comentarea codului sursă.
