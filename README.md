# ProjectMMM
Project MMM in Python language 

1.Założenia wersji nr.2:

1.1 Main, to jedyny program wykonawczy na ten moment obsługuje generator oraz wywołanie operacji klasy buckets oraz zapis do pliku csv.

1.2 Generator, klasa zajmująca się generowaniem przebiegów sinusoidalnych, prostokątnych, pobudzenia jedynką heavyside'a. Została wykorzystana biblioteka numpy do generacji czasu i sinusa.

1.3 Errors, klasa zajmująca się obsługą wyjątków dla klas generator oraz buckets, obsługuje wyłącznie błędy w podanych zmiennych. Nazwy funkcji mówią same za siebie.

1.4 Test_commands, plik txt zawierający podstawowe przykładowe komendy testowe do obsługi generatora w main. Zawiera odwołania do testownik patrz niżej.

1.5 testownik, plik csv odpowiada za wyświetlanie, należy pamietać, że przesyłając dane do csv z Python, float ma separator kropki, a Libreoffice przecinek, warto skorzystać z ctrl+h. Następnie wstawić wykres. Jezeli korzystamy z notacji anglosaskiej problem ten nie powinien mieć miejsca, można ją ustawić wybierając opcje jak poniżej:

![ustawienia_libreoffice](https://user-images.githubusercontent.com/83645103/163212759-e81f51ea-f3cb-4ec9-a1b4-e80d0e095275.jpg)

Zawiera podstawowo 2400 linii danych, wygenerowanych uprzednio przez program, które symulują przykładowe przebiegi. Parametry dla tej symulacji znajdują się w funkcji main. 

1.6 Klasa Bucket, znajdująca się w pliku buckets.py, z założenia symuluje działanie zbiorników cylindrycznych.

2. Szerszy opis działania podzespołów wersji nr.2. 

Dokładniej w tej sekcji zostanie opisany sposób działania klasy Bucket, wyjaśnione podstawowe nazewnictwo i sposób interpretacji. Podobnie zostanie rozpisana teoria dla klasy Generator, której to zabrakło w poprzedniej wersji projektu oraz opiszemy działanie main.

2.1 Klasa Bucket jak sama nazwa wskazuje odnosi się do tzw. wiadra roboczej nazwy zbiorników cylindrycznych, które symuluje, zastosowano numeryczną wersję metody Taylora dla rozwiązywania równań rożniczkowych. W trakcie tworzenia obiektu tej klasy podajemy jej podstawowe parametry:

![image](https://user-images.githubusercontent.com/83645103/163218336-d37eb81e-6415-4a14-852a-559da28911fe.png)

data - strumień danych wejściowych. Podawanych jako kolejne wartości jednowymiarowej listy.
tank_area - powierzchnia naszego zbiornika.
outlet_area - powierzchnia zwężki wypływu (pot. otworu przez, który ucieka strumień).
step - krok obliczen, predefiniowana wartość 0.01.

Po załadowaniu obiektu parametrami odnoszącymi się do przetwarzanych danych oraz jego wymiarów fizycznych, możemy wykorzystać jedyną funkcję czyli pour_water (pot. lej wodę) dokonuje ona symulacji obliczeń strumienia wejściowego i zwraca jako wartości liste dwuwymiarową gdzie pierwsza kolumna to wysokość wody dla danych chwil czasu, natomiast druga to strumień wypływający przez zwężkę. Poniżej kolejno założenia kocepcyjne implementacji tej funkcji oraz jej implementacja:

![image](https://user-images.githubusercontent.com/83645103/163220282-6dbe0e7b-122d-4f98-b6da-e35f2ea85cce.png)

![image](https://user-images.githubusercontent.com/83645103/163220405-bc252d3e-2dc3-4b02-818c-117833f7bba3.png)
(nastąpiły zmiany związane z błedami w implementacji, poprawny kod jest już dostepny w plikach, szersze objaśnienie w sekcji błedów)

2.2 Klasa Generator, jak sama nazwa wskazuje generuje za pomocą odpowiednich funkcji zadane sygnały. Przy tworzeniu obiektu tej kalasy jedyny parametr jaki zadajemy to ilość próbek na jednostkę czaasu (sample_rate). Nastepnie wywołujemy konkretną funkcje, każda z nich zwraca dwuwymiarową liste, gdzie pierwsza kolumna zawiera kolejne chwile czasu, a druga wartości sygnału dla chwil czasu. Poniżej opis parametrów kolejnych funkcji (typów generowanych przebiegów):

![image](https://user-images.githubusercontent.com/83645103/163225293-0e2e382f-9e6f-41a2-91d1-fd9d596f9334.png)
![image](https://user-images.githubusercontent.com/83645103/163225841-06687218-a0e9-453b-b898-8413a5b4153b.png)
![image](https://user-images.githubusercontent.com/83645103/163225880-8d6bdcad-2b17-45a4-865c-1363b49c214e.png)

start_time - początkowy czas tworzenia przebiegu, niezbędny dla utworzenia czasu w którym będziemy generować przebieg. 
end_time - końcowy czas, zatrzymanie generacji dla tej chwili czasu.
frquency - częstotliwość generowanego przebiegu 
amplitude - amplituda generowanego przebiegu 
period - okres dla fali prostokątnej 
duty_cycle - wspołczynnik wypełnienia fali prostokątenj podawany w procentach od 0 = 0%, do 1 = 100%.
t_on - czas rozpoczęscia się tzw. skoku w jedynce heavyside'a (dokładniej przesuniętej jedyncje heavyside'a).

2.3 W tej sekcji opiszemy sposób działania Main krok po korku:

2.3.1 Stowrzenie obiektu klasy Genreator i zadanie mu paramteru sample_rate:

![image](https://user-images.githubusercontent.com/83645103/163226858-15f90ca6-7ea3-48d1-8097-9c80006eb33b.png)

2.3.2 Stworzenie trzech list (pot. wektorów, stąd nazwa vector) zawierających kolejne przebiegi z klasy Generator. Ważne są czasy podawane jako start i koniec danego przebiegu. Proszę zauważyć, że są one podawane jako 0 -> 40, 40 -> 80, 80 -> 120, to dlatego, iż każda z funkjci generuje przebiegi od podanej chwili czasu do momentu poprzedzającego koniec przebiegu czyli 40-(jednostka czasu), 80-(jednostka czasu), 120-(jednostka czasu). Wyjaśnienie takiego stanu rzeczy w dalszych podpunktach:

![image](https://user-images.githubusercontent.com/83645103/163227666-e6c028e4-f4f5-4bbd-b3a8-6075ad38f339.png)

2.3.3 Stworzenie listy zawierającej nasze przebiegi, stworzenie nowej dwuwymiarowej listy zwierającej tzw. stream, czyli końcowy strumień danych, który zostanie podany na obiekty klasy Bucket. Wcześniej wymieniona notacja pozwala nam na połącznie tych przebiegów, w jeden dłuższy testowy, co zostaje wykonane za pomocą dwóch obiekowych pętli typu for.

![image](https://user-images.githubusercontent.com/83645103/163228155-67e3bde5-3516-42e1-ab98-ee6662a18832.png)

2.3.4 Utworzenie obiektów typu Bucket symulujących działanie układu dwóch zbiorników cylindrycznych oraz wywołanie dla nich funkcji dokonującej operacji matemtycznych:

![image](https://user-images.githubusercontent.com/83645103/163228447-723638d0-1e6d-4357-9033-f80ee8808229.png)

2.3.5 Wysłanie danych przetworzonych przez obiekty typu Bucket do pliku csv. Koleno od lewej do prawej: chwila czasu, wartość wejściowa strumienia, wysokość wody w pierwszym zbiorniku, wysokość wody w drugim zbiorniku:

![image](https://user-images.githubusercontent.com/83645103/163228735-6563c645-6651-4683-aef0-6134341ed3ff.png)

3. Sekcja aktualizacji i naprawionych błędów poprawionych w wersji 2 projektu (aktualizacje tej wersji nie zmiany pomiędzy obecną, a poprzednią):

3.1 Błąd w zaimplementowanej formule matematycznej, strumień wysyłany z zbiornika pierwszego do drugiego był arbitralnie podzielny przez powierzchnię pierwszego zbiornika. Powodem było błędne przeniesienie teoretycznego projektu funkcji na jej odpowiednik w kodzie. Poniżej porównanie przebiegów przed i po. Żółty to przebieg wysokości wody w pierwszym zbiorniku, a zielony w drugim: 

![Podgląd2](https://user-images.githubusercontent.com/83645103/163247511-22e24c2b-9240-48e4-94b7-943274689610.jpg)

![Podgląd2 2](https://user-images.githubusercontent.com/83645103/163247535-73b65b8b-5f2d-4f08-b7fc-c79db63854d3.jpg)

3.2 Błąd w interpretacji metody Taylora. Częstostliwość próbkowania powinna być odwrotnie proporcjonalna do kroku całkowania, aby zachować spójność logiczną. Parametry zadawane w main.py: sample_rate i period są teraz podawane po podzieleniu przez krok całkowania (h). Dodatkowo parametr ten jest wykorzystywany od teraz jako normalna wartość wejściowa w pliku main.py do funkcji obiektów klasy buckets (wcześniej parametr domyślny). Wizualzacja pracy programu przy zadanych parametrach po naprawieniu usterki:

Wprowadzone dane:

![Zrzut ekranu 2022-05-18 160119](https://user-images.githubusercontent.com/83645103/169064722-9702e9b8-6621-4d36-85d4-9a6b3a2ab0c8.jpg)
![Zrzut ekranu 2022-05-18 162235xxxxx](https://user-images.githubusercontent.com/83645103/169064769-99f3443a-41e1-4e2b-b490-c780bf93bdaf.jpg)

Wyniki dla kolejnych kroków całkowania (czerwony - sygnał wejściowy, zielony - wysokość wody w drugim zbiorniku, żółty - zbliżenie na wysokość wody w pierwszym zbiorniku):

Krok wynoszący 0,1:

![0,1(0)](https://user-images.githubusercontent.com/83645103/169065494-8168e80c-d25a-4225-b50e-5499c2ec5aec.jpg)
![0,1(1)](https://user-images.githubusercontent.com/83645103/169065523-e0bac5ec-0c7b-45af-a4d2-2421cf8d2b10.jpg)

Krok wynoszący 0,01:

![0,01(0)](https://user-images.githubusercontent.com/83645103/169065632-c3acccda-b71b-4740-839d-e013a3104453.jpg)
![0,01(1)](https://user-images.githubusercontent.com/83645103/169065658-7c3034c7-d754-461f-b0f6-44d2a7dfaae7.jpg)

Krok wynoszący 0,001:

![0,001(0)](https://user-images.githubusercontent.com/83645103/169066287-3aee632e-3216-4f4b-857e-c836984d2c4a.jpg)
![0,001(1)](https://user-images.githubusercontent.com/83645103/169066311-235816e7-9982-4756-9ed2-4a7197d7c0b4.jpg)



