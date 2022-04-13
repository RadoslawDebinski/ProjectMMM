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
