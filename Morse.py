class Morse:

    morse = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-...", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....", 'i': "..",
             'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.",
             's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--",'x': "-..-", 'y': "-.--", 'z': "--..", ' ': "/",
             '.': ".-.-.-"}

    def __init__(self, pin, dot_delay):
        self.pin = pin
        self.dot_delay = dot_delay
        self.dash_delay = dot_delay * 3

    def convert_to_morsecode(self, sentence):
        sentence = list(sentence)
        morsecode = []
        for i in sentence:
            morse_letter = self.morse.get(i)
            morsecode.append(morse_letter)
        morsecode = " ".join(morsecode)
        return morsecode

    def dot(self):  # Make one dot beep
        GPIO.output(self.pin, 1)
        sleep(self.dot_delay)
        GPIO.output(self.pin, 0)

    def dash(self):  # Make one dash beep
        GPIO.output(self.pin, 1)
        sleep(self.dash_delay)
        GPIO.output(self.pin, 0)

    def convert_and_play(self, sentence):  # Play the converted message
        output = self.convert_to_morsecode(sentence)
        print(sentence, " --> ", output)
        for i in output:
            if i == '.':
                self.dot()
            elif i == '-':
                self.dash()
	    elif i == '/':
                sleep(self.dot_delay)
            elif i == ' ':
                sleep(self.dash_delay)
            else:
                sleep(self.dot_delay)
        GPIO.output(self.pin, 0)
