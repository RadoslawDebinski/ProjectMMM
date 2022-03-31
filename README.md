# ProjectMMM
Project MMM in Python language 

Założenia wstępne wersji nr.1

1. Main to jedyny program wykonawczy na razie obsługuje wyłącznie testowanie działania generatora 
2. Generator klasa zajmująca się generowaniem przebiegów sinusoidalnych, prostokątnych, pobudzenia jedynką heavyside'a. Została wykorzystana biblioteka numpy do generacji czasu i sinusa.
3. Poniżej notatki koncepcyjne z tworzenia kodu dla fali prostokątnej:
![Założenia kocecyjne 1](https://user-images.githubusercontent.com/83645103/161130352-936eeb16-f29d-4172-aa9a-e17feb0ef593.jpg)
4. Poniżej notatki koncepcyjne z tworzenia kodu dla impulsu:
![Założenia kocepcyjne 2](https://user-images.githubusercontent.com/83645103/161130372-8a7f9fc1-f285-4c7b-ab65-93de306381ea.jpg)
5. Errors klasa zajmująca się obsługą wyjątków dla klasy Generator, obsługuje wyłącznie błędy w podanych zmiennych. Nazwy funkcji mówią same za siebie.
6. Test_commands plik txt zawierający podstawowe przykładowe komendy testowe do obsługi generatora w main. Zawiera odwołania do testownik patrz niżej.
7. testownik plik csv odpowiada za wyświetlanie, należy pamietać, że przesyłając dane do csv z Python float ma separator kropki, a Libreoffice przecinek warto skorzystać z ctrl+h. Następnie wstawić wykres.
8. Dalsze zmiany obejmą dopracowanie projektu wiader, GUI i ewentualne zmiany genratora to jest wersja podstawowa


Pierwsze poprawki do generatora, błąd geneacji fali prostokątnej został naprawiony

1. Naprawiono błąd związany z generacją fali prostokątnej zmieniono jedną linię kodu, pliki jpg z rozpiską koncepcyjną i przykładem wykorzystania poniżej:

![Problem generacji prostokąta 1](https://user-images.githubusercontent.com/83645103/161130039-5cb8942d-6980-450c-9863-067b0b72cd56.jpg)
![Problem generacji prostokąta 2](https://user-images.githubusercontent.com/83645103/161130126-ba714f11-5b13-4612-9fb8-6ecbfbc32625.jpg)
