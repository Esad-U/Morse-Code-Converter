class Morse:

    morse = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-...", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....", 'i': "..",
             'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.",
             's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--",'x': "-..-", 'y': "-.--", 'z': "--..", ' ': "/",
             '.': ".-.-.-"}

    def convert_to_morsecode(self, sentence):
        sentence = list(sentence)
        morsecode = []
        for i in sentence:
            morse_letter = self.morse.get(i)
            morsecode.append(morse_letter)
        morsecode = " ".join(morsecode)
        return morsecode