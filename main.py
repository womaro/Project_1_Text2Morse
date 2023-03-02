import winsound

MORSE = {
    "A": "._", "B": "_...", "C": "_._.", "D": "_..", "E": ".", "F": ".._.", "G": "__.", "H": "....", "I": "..",
    "J": ".___", "K": "_._", "L": "._..", "M": "__", "N": "_.", "O": "___", "P": ".__.", "Q": "__._", "R": "._.",
    "S": "...", "T": "_", "U": ".._", "V": "..._", "W": ".__", "X": "_.._", "Y": "_.__", "Z": "__..",
}

print(MORSE)


frequency = 1000  # Set Frequency To 2500 Hertz
duration = 350  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

frequency = 1000  # Set Frequency To 2500 Hertz
duration = 150  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)