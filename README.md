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

2. Szerszy opis działania podzespołów wersji nr.2. Dokładniej w tej sekcji zostanie opisany sposób działania klasy Bucket, zostanie wsyjaśnione podstawowe nazewnictwo i sposób interpretacji oraz wyjasnienie aktualnego działania klasy main

2.1 Klasa Bucket jak sama nazwa wskazuje odnosi się do tzw. wiadra roboczej nazwy zbiorników cylindrycznych, które symuluje, w trakcie tworzenia obiektu tej klasy podajemy jej podstawowe paramtry:



