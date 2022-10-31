def tail(s: list):
    """Funktion som tar bort det första elementet av en lista och returnerar resten av listan
    Exempel: tail([1,2,3,4]) - > [2, 3, 4]"""
    copy_of_s = s[:]  # gör en kopia för att undvika att ändra på listan som ges som argument
    del copy_of_s[0]
    return copy_of_s


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    print(tail(l))

    # Som ni ser har listan l förändrats av anropet till tail.
    # Tail har med andra ord en sidoeffekt
    # Skriv om funktionen tail så att output från programmet blir
    # [2, 3, 4, 5]
    # [1, 2, 3, 4, 5]
    print(l)
