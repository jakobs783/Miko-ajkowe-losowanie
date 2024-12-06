# Miko-ajkowe-losowanie


## System do Mikołajkowego losowania


Cel:

Losowanie par dla wymiany prezentów wśród znajomych, z automatycznym powiadomieniem przez SMS.



Jak działa:

 Losowanie: System losuje pary z listy uczestników, uwzględniając reguły wykluczeń (np. członkowie rodziny lub pary nie losują siebie nawzajem).
 
 Powiadomienie: SMS-y z wynikami są wysyłane do każdego uczestnika przez aplikację "Łącze z telefonem".
 
 Raport: Wyniki losowania są wyświetlane w konsoli.



Technologia:

  Aplikacja: "Łącze z telefonem" na Windows i Android.
  
  Automatyzacja: Skrypt Python wykorzystuje bibliotekę pyautogui do iintegracji z "Łącze z telefonem" w celu wysyłania SMS-ów.
  
  Wiadomość SMS: Personalizowana, z podziałem na 5 lini.



Przykład SMS-a:

   > WIADOMOSC TESTOWA - O 16:00 PRAWDZIWE LOSOWANIE
   >  
   > Czesc user3!
   > W tym roku wylosowalxs: user1 ;) Przygotuj prezent!
   > Za pomyslnosc sprawy słusznej!
   > 
   > pst, daj znac smsem ze dostalxs



Jak użyć:

- zainstaluj python3
- pip install pyautogui
- Przesuń mysz na odpowiedni przycisk tworzenia wiadomości i odczytaj współrzędne wykonując pyautogui.position.py
- spersonalizuj skrypt Losowanie Swiateczne.py i wykonaj



ToDo:

- wynik losowania do pliku
- listę osób niech pobiera z pliku .txt
- zmiana integracji z GUI na API
