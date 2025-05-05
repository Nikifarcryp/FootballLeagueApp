📘 Dokumentacja projektu – Aplikacja Piłkarska (stud. Nikifar Markatsynski)
1. 🛠 Usługi dostępne w aplikacji
Aplikacja oferuje trzy główne funkcjonalności analityczne dostępne z poziomu interfejsu użytkownika:
•	Wskaż najlepszą drużynę – funkcja analizująca dane z tabeli wyników i wskazująca drużynę z największą liczbą punktów.
•	Wskaż najlepszego zawodnika – funkcja identyfikująca piłkarza, który zdobył najwięcej bramek w całym turnieju.
•	Wskaż najlepszego zawodnika na daną drużynę – funkcja pozwalająca wskazać zawodnika, który zdobył najwięcej bramek przeciwko określonej drużynie.
 
2. ⚙️ Technologie i architektura
Projekt został zrealizowany w języku Python z wykorzystaniem frameworka Django oraz bazy danych PostgreSQL. Struktura aplikacji oparta jest o wzorzec projektowy MVC (Model–View–Controller).
Na froncie wykorzystano:
•	Bootstrap do stylizacji,
•	HTML jako podstawę struktury stron,
•	Jinja2 jako silnik szablonów do komunikacji z backendem.
 
3. 🧭 Strona główna aplikacji
Na stronie głównej użytkownik widzi tabelę turniejową, uporządkowaną według liczby punktów zdobytych przez drużyny. Poniżej dostępne są trzy kluczowe przyciski:
1.	Best Player (najlepszy zawodnik na daną drużynę) – po wpisaniu nazwy drużyny użytkownik otrzymuje zawodnika, który strzelił jej najwięcej bramek.
2.	Best Team (najlepsza drużyna) – wyświetla drużynę z największą liczbą punktów w klasyfikacji.
3.	Admin Panel – link prowadzący do panelu administracyjnego Django (dostępny tylko dla uprawnionych użytkowników).
 
4. 👤 Role użytkowników i system uprawnień
Aplikacja posiada zautomatyzowany system uprawnień, oparty na podziale użytkowników na trzy grupy:
•	Administratorzy – mają pełny dostęp do systemu: mogą dodawać drużyny, zawodników, mecze oraz zarządzać użytkownikami.
•	Sędziowie – mają ograniczony dostęp do panelu administracyjnego, mogą zarządzać meczami oraz dodawać bramki.
•	Zwykli użytkownicy – mają dostęp tylko do funkcji informacyjnych dostępnych na stronie głównej i nie mają uprawnień do logowania się do panelu admina.
Dostęp do panelu administracyjnego posiadają wyłącznie sędziowie i administratorzy.
 
5. 🗃 Struktura bazy danych
Projekt oparty jest na pięciu powiązanych tabelach:
•	Team – drużyny,
•	Player – zawodnicy,
•	Match – mecze,
•	Goal – bramki,
•	Standing – klasyfikacja.
Wszystkie tabele zostały zaprojektowane zgodnie z wytycznymi przedstawionymi przez dr. Jabłońskiego.
5.1 Automatyzacja
•	Po dodaniu drużyny do tabeli Team, automatycznie tworzony jest dla niej wpis w tabeli Standing z domyślnymi wartościami.
•	Po dodaniu meczu i uzupełnieniu jego wyniku (wygrana, remis, przegrana), aplikacja automatycznie aktualizuje klasyfikację obu drużyn – dodając punkty i aktualizując liczbę zwycięstw, remisów i porażek.
 
6. 📝 Proces dodawania meczu i bramek
Ważną zasadą działania systemu jest kolejność czynności:
1.	Sędzia lub administrator najpierw dodaje mecz do systemu.
2.	Dopiero po jego dodaniu może wprowadzić bramki, które padły w tym meczu.
