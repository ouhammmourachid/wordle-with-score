


class Word:
    def __init__(self,word:str) -> None:
        """
        this class is the one responsble of holding the words 
        to make it easy we don't save the word just like that
        instide we save them in seperect char like this so to 
        to create an object using this class from a word of 
        five charcter :
        ```python
        word = Word('walet')
        ```
        """
        assert len(word) == 5 , "the length of the word is not suitbale it shoud be exactly five char"
        self.char_1 = ord(word[0])
        self.char_2 = ord(word[1])
        self.char_3 = ord(word[2])
        self.char_4 = ord(word[3])
        self.char_5 = ord(word[4])
        
    def __str__(self) -> str:
        return chr(self.char_1)+chr(self.char_2)+chr(self.char_3)+chr(self.char_4)+chr(self.char_5)

