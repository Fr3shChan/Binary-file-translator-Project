import time

from datetime import datetime

from datetime import timedelta

print('Podaj pełną ścieżkę do pliku: ')
sciezka = input()

# Przykład- D:\test\records.bin

with open(sciezka, 'rb') as plik:
    address = 0

    while True:
        # Pozyskiwanie dancyh
        data = plik.read(4)
        typ = plik.read(1)
        dlugosc = plik.read(2)

        if not data:
            break
        # Konwersja długości rekordu
        dlugoscdec = int(dlugosc.hex(), base=16)

        # data
        datadec = int(data.hex(), base=16)

        # Metoda pozyskująca czas i dodająca go do daty startowej
        def get_time_hh_mm_ss(sec):
            td_str = str(timedelta(seconds=sec))
            x = td_str.split(':')
        get_time_hh_mm_ss(datadec)
        x = datetime(2020, 1, 1)
        todays_time = time.time()
        date_from_currentTime = datetime.fromtimestamp(todays_time)
        s = "01/01/2020"
        times = time.mktime(datetime.strptime(s, "%d/%m/%Y").timetuple())
        suma = datadec + times
        date_From_Timestamp = datetime.fromtimestamp(suma)

        # typ rekordu
        typdec = int(typ.hex(), base=16)

        # typ rekordu koniec
        dane_opcjonalne = plik.read(dlugoscdec - 11)
        suma_kontrolna = plik.read(4)

        # Logika zachowania względem typu rekordu
        if typdec == 1:
            typ_nazwa = "Log message"
            x = str(dane_opcjonalne1)
            dane_opcjonalne_ascii = bytearray.fromhex(dane_opcjonalne.hex()).decode()
            print('data zdarzenia        :', date_From_Timestamp, '|', 'typ:', typdec, typ_nazwa, '|','długość rekordu: ', dlugoscdec,'|')
            print('dane opcjonalne       :', dane_opcjonalne.hex(' '))
            print('dane opcjonalne ASCII :', dane_opcjonalne_ascii)
            print('suma kontrolna        :', suma_kontrolna.hex(' '))

        if typdec == 2:
            typ_nazwa = "Raw frame"
            dane_opcjonalne1 = int(dane_opcjonalne.hex(), base=16)
            res = "{0:08b}".format(dane_opcjonalne1, 16)
            print('data zdarzenia        :', date_From_Timestamp, '|', 'typ:', typdec, typ_nazwa, '|','długość rekordu: ', dlugoscdec,'|')
            print('dane opcjonalne       :', dane_opcjonalne.hex(' '))
            print('dane opcjonalne bin   :', str(res))
            print('suma kontrolna        :', suma_kontrolna.hex(' '))

        if typdec == 3:
            typ_nazwa = "Separator"
            print('data zdarzenia        :', date_From_Timestamp, '|', 'typ:', typdec, typ_nazwa, '|','długość rekordu: ', dlugoscdec,'|')
            print('dane opcjonalne       :', dane_opcjonalne.hex(' '))
            print('suma kontrolna        :', suma_kontrolna.hex(' '))

        if typdec == 4:
            dane_opcjonalne_dec = int(dane_opcjonalne.hex(), base=16)
            event = chr(dane_opcjonalne_dec)

            # Logika wyświetlania zdarzeń
            if event == '1':
                komunikat = 'włączenie gazomierza'
                typ_nazwa = "Event"
                print()
                dane_opcjonalne_dec = int(dane_opcjonalne.hex(), base=16)
                print('data zdarzenia        :', date_From_Timestamp, '|', 'typ:', typdec, typ_nazwa, '|','długość rekordu: ',dlugoscdec,'|')
                print('dane opcjonalne       :', dane_opcjonalne.hex(' '))
                print('zdarzenie             :', komunikat)
                print('suma kontrolna        :', suma_kontrolna.hex(' '))

            if event == '2':
                komunikat = 'wyłączenie gazomierza'
                typ_nazwa = "Event"
                print()
                dane_opcjonalne_dec = int(dane_opcjonalne.hex(), base=16)
                print('data zdarzenia        :', date_From_Timestamp, '|', 'typ:', typdec, typ_nazwa, '|','długość rekordu: ',dlugoscdec,'|')
                print('dane opcjonalne       :', dane_opcjonalne.hex(' '))
                print('zdarzenie             :', komunikat)
                print('suma kontrolna        :', suma_kontrolna.hex(' '))

            if event == '3':
                komunikat = 'otwarcie zaworu'
                typ_nazwa = "Event"
                print()
                dane_opcjonalne_dec = int(dane_opcjonalne.hex(), base=16)
                print('data zdarzenia        :', date_From_Timestamp, '|', 'typ:', typdec, typ_nazwa, '|','długość rekordu: ',dlugoscdec,'|')
                print('dane opcjonalne       :', dane_opcjonalne.hex(' '))
                print('zdarzenie             :', komunikat)
                print('suma kontrolna        :', suma_kontrolna.hex(' '))

            if event == '4':
                komunikat = 'zamknięcie zaworu'
                typ_nazwa = "Event"
                print()
                dane_opcjonalne_dec = int(dane_opcjonalne.hex(), base=16)
                print('data zdarzenia        :', date_From_Timestamp, '|', 'typ:', typdec, typ_nazwa, '|','długość rekordu: ',dlugoscdec,'|')
                print('dane opcjonalne       :', dane_opcjonalne.hex(' '))
                print('zdarzenie             :', komunikat)
                print('suma kontrolna        :', suma_kontrolna.hex(' '))
        print('====================================================')

input("Przyciśnij enter by zamknąć program...")
