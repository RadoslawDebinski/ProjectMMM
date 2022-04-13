# ProjectMMM
Project MMM in Python language 

1.Założenia wersji nr.2:

1.1 Main to jedyny program wykonawczy na ten moment obsługuje generator oraz wywołanie operacji klasy buckets oraz zapis do pliku csv.

1.2 Generator klasa zajmująca się generowaniem przebiegów sinusoidalnych, prostokątnych, pobudzenia jedynką heavyside'a. Została wykorzystana biblioteka numpy do generacji czasu i sinusa.

1.3 Errors klasa zajmująca się obsługą wyjątków dla klas generator oraz buckets, obsługuje wyłącznie błędy w podanych zmiennych. Nazwy funkcji mówią same za siebie.

1.4 Test_commands plik txt zawierający podstawowe przykładowe komendy testowe do obsługi generatora w main. Zawiera odwołania do testownik patrz niżej.

1.5 testownik plik csv odpowiada za wyświetlanie, należy pamietać, że przesyłając dane do csv z Python float ma separator kropki, a Libreoffice przecinek warto skorzystać z ctrl+h. Następnie wstawić wykres. Jezeli korzystamy z notacji anglosaskiej problem ten nie powinien mieć miejsca, można ją ustawić wybierając opcje jak poniżej:

![ustawienia_libreoffice](https://user-images.githubusercontent.com/83645103/163212759-e81f51ea-f3cb-4ec9-a1b4-e80d0e095275.jpg)

1.6 Klasa Bucket znajdująca się w pliku buckets.py, z założenia symuluje działanie zbiorników cylindrycznych.

2. Szerszy opis działania podzespołów wersji nr.2. 

Dokładniej w tej sekcji zostanie opisany sposób działania klasy Bucket, wyjaśnione podstawowe nazewnictwo i sposób interpretacji. Podobnie zostanie rozpisana teoria dla klasy Generator, której to zabrakło w poprzedniej wersji projektu oraz opiszemy działanie main.

2.1 Klasa Bucket jak sama nazwa wskazuje odnosi się do tzw. wiadra roboczej nazwy zbiorników cylindrycznych, które symuluje, w trakcie tworzenia obiektu tej klasy podajemy jej podstawowe parametry:

![image](https://user-images.githubusercontent.com/83645103/163218336-d37eb81e-6415-4a14-852a-559da28911fe.png)

data - strumień danych wejściowych. Podawanych jako kolejne wartości jednowymiarowej listy.
tank_area - powierzchnia naszego zbiornika.
outlet_area - powierzchnia zwężki wypływu (pot. otworu przez, który ucieka strumień).
step - krok całkowania, predefiniowana wartość 0.01.

Po załadowaniu obiektu parametrami odnoszącymi się do przetwarzanych danych oraz jego wymiarów fizycznych, możemy wykorzystać jedyną funkcję czyli pour_water (pot. lej wodę) dokonuje ona symulacji obliczeń strumienia wejściowego i zwraca jako wartości liste dwuwymiarową gdzie pierwsza kolumna to wysokość wody dla danych chwil czasu, natomiast druga to strumień wypływający przez zwężkę. Poniżej kolejno założenia kocepcyjne implementacji tej funkcji oraz jej implementacja:

![image](https://user-images.githubusercontent.com/83645103/163220282-6dbe0e7b-122d-4f98-b6da-e35f2ea85cce.png)

![image](https://user-images.githubusercontent.com/83645103/163220405-bc252d3e-2dc3-4b02-818c-117833f7bba3.png)

2.2 
