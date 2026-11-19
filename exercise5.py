class VigenereCipher:
    """
       VigenereCipher class (TO BE COMPLETED).

       Attributes:
           keyword (str): The word to be used as the key
           offset (int): The ASCII value of the letter 'A'. A static utility attribute to help you calculate
                a letter's position in the alphabet from 0 (A) to 25 (Z).
    """
    offset = ord('A')

    def __init__(self, keyword: str):
        self.keyword = keyword.upper()

    def __shift_letter(self, letter: str, shift: int, forward: bool):
        """
        TO BE COMPLETED

        Private method to shift a letter a number of positions forward or backward in the alphabet.

        YOU CAN REUSE YOUR METHOD FROM EXERCISE 1 WITH MINOR MODIFICATIONS

        Parameters
        ----------
        letter : str
            The letter to be shifted.
        shift: int
            The number to shift
        forward : bool
            Whether to shift forward (True) or backward (False).

        Returns
        -------
        str
            The shifted letter.
        """
        shifted_letter = ''
        position = ord(letter) - self.offset
        if forward:
            position += shift
        else:
            position -= shift
        shifted_letter = chr(position % 26 + self.offset)
        return shifted_letter

    def __generate_shift_list(self, plaintext_length: int):
        """
        TO BE COMPLETED

        Private method to generate a list of integers. Each element is the shift to encrypt the
        plaintext letter at the same position.

        Remember that the Vigenere cipher uses the keyword, repeated as many times as required to
        have the same number of letters as the plaintext, to derive the shift values for each
        plaintext letter.

        Parameters
        ----------
        plaintext_length : int
            The length of the plaintext after whitespace and punctuation has been removed.

        Returns
        -------
        list
            A list of shifts (integers).
        """
        shift_list = []
        for index in range(plaintext_length):
            key_letter = self.keyword[index % len(self.keyword)]
            shift_list.append(ord(key_letter) - self.offset)

        return shift_list

    def encrypt(self, plaintext: str):
        """
        TO BE COMPLETED

        Encrypts a plaintext string.
        It should:
            1. Convert lowercase input to uppercase
            2. Remove whitespace and punctuation from the input
            3. Use self.__generate_shift_list to create the list of shifts for each letter in the plaintext
            4. Use self.__shift_letter to encrypt an individual letter

        Parameters
        ----------
        plaintext : str
            The plaintext string.

        Returns
        -------
        str
            The ciphertext string.
        """
        ciphertext = ''
        plaintext = ''.join(letter for letter in plaintext.upper() if 'A' <= letter <= 'Z')
        shifts = self.__generate_shift_list(len(plaintext))
        for letter, shift in zip(plaintext, shifts):
            ciphertext += self.__shift_letter(letter, shift, forward=True)

        return ciphertext

    def decrypt(self, ciphertext: str):
        """
        TO BE COMPLETED

        Decrypts a ciphertext string
        It should:
            1. Convert lowercase input to uppercase
            2. Remove whitespace and punctuation from the input
            3. Use self.__generate_shift_list to create the list of shifts for each letter in the plaintext
            4. Use self.__shift_letter to decrypt an individual letter

        HINT: You can use the list index notation to retrieve a character at a position in a string
        e.g., if string = "abacab" then string[2] = 'a' (3rd character in the string)

        Parameters
        ----------
        ciphertext : str
            The ciphertext string.

        Returns
        -------
        str
            The plaintext string.
        """
        plaintext = ''
        ciphertext = ''.join(letter for letter in ciphertext.upper() if 'A' <= letter <= 'Z')
        shifts = self.__generate_shift_list(len(ciphertext))
        for letter, shift in zip(ciphertext, shifts):
            plaintext += self.__shift_letter(letter, shift, forward=False)


        return plaintext


def main():
    vig_cipher = VigenereCipher('smarties')
    ciphertext = vig_cipher.encrypt("The quick brown fox jumps over the lazy dog")
    plaintext = vig_cipher.decrypt(ciphertext)
    assert plaintext == 'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'


if __name__ == "__main__":
    main()