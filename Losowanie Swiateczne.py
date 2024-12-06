# Wymaga odpalenia aplikacji "Łącze z telefonem" oraz dostosowania współrzędnych w zależności od ekranu pyautogui.position.py

import pyautogui
import time
import random

# Uczestnicy: imię i numer telefonu (UZUPEŁNIĆ)
participants = [

   ("user1", "+48123456789"),
   ("user2", "+48123456789"),
   ("user3", "+48123456789"),
   ("user4", "+48123456789"),
   ("user5", "+48123456789"),
   ("user6", "+48123456789"),
   ("user7", "+48123456789"),
   ("user8", "+48123456789")
]

# Wykluczenia (UZUPEŁNIĆ)
exclusions = {
    "user1": ["user2"],
    "user2": ["user1"],
    "user7": ["user8"],
    "user8": ["user7"]

}

def draw_names(participants, exclusions):
    names = [p[0] for p in participants]
    shuffled_names = names[:]
    while True:
        random.shuffle(shuffled_names)
        if all(
            names[i] != shuffled_names[i] and
            shuffled_names[i] not in exclusions.get(names[i], [])
            for i in range(len(names))
        ):
            break
    return dict(zip(names, shuffled_names))

# Losowanie
draw_result = draw_names(participants, exclusions)

# Wyświetl wyniki losowania w konsoli
print("Wyniki losowania:")
for giver, receiver in draw_result.items():
    print(f"{giver} wylosował/a: {receiver}")

# Wysyłanie SMS-ów
for giver, receiver in draw_result.items():
    phone_number = next(p[1] for p in participants if p[0] == giver)
    message1 = f"WIADOMOSC TESTOWA - O 16:00 PRAWDZIWE LOSOWANIE"
    message2 = f"Czesc {giver}!"
    message3 = f"W tym roku wylosowalxs: {receiver} ;) Przygotuj prezent!"
    message4 = f"Za pomyslnosc sprawy slusznej!"
    message5 = f"pst, daj znac smsem ze dostalxs"

    # Kliknij "Nowa wiadomość" (UZUPEŁNIĆ)
    pyautogui.click(2637, 149)  # Dostosuj współrzędne w zależności od ekranu
    time.sleep(2)

    # Wpisz numer telefonu
    pyautogui.typewrite(phone_number)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(2)

    # Wpisz wiadomość
    pyautogui.typewrite(message1)
    pyautogui.keyDown('shift')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.keyUp('shift')
    pyautogui.typewrite(message2)
    pyautogui.keyDown('shift')
    pyautogui.press('enter')
    pyautogui.keyUp('shift')
    pyautogui.typewrite(message3)
    pyautogui.keyDown('shift')
    pyautogui.press('enter')
    pyautogui.keyUp('shift')
    pyautogui.typewrite(message4)
    pyautogui.keyDown('shift')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.keyUp('shift')
    pyautogui.typewrite(message5)
    time.sleep(1)

    # Wyślij wiadomość
    pyautogui.press('enter')
    time.sleep(3)

print("Wszystkie wiadomości zostały wysłane!")