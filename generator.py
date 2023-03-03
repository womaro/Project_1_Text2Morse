from static import MORSE
import winsound, time


class MorseGenerator:
    def __init__(self):
        self.ALPHABET = MORSE
        self.frequency = 1000
        self.short = 150
        self.long = 350

    def text_to_morse(self, sentence):
        sentence = sentence.upper()
        morse_sentence = ""
        for letter in sentence:
            if letter == " ":
                morse_sentence += "ª"
            else:
                morse_sentence += MORSE[letter]
        return morse_sentence

    def morse_to_sound(self):
        text = input("What do you want to translate?: ")
        morse_sentence = self.text_to_morse(text)
        print(morse_sentence)
        for letter in morse_sentence:
            print(letter)
            if letter == "ª":
                time.sleep(0.5)
            elif letter == ".":
                winsound.Beep(self.frequency, self.short)
            else:
                winsound.Beep(self.frequency, self.long)

    def __str__(self):
        pass
        #return self.morse_sentence
