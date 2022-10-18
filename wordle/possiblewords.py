from .word import Word

class PossibleWord:
    """this class will contain all the possible word  that
    can be solution of the wordle game and we will be serialising
    them from the .txt file"""
    def __init__(self,file_name:str) -> None:
        self.words :list[Word]= []
        i:int = 0
        for line in open(file_name,'r'):
            self.words.append(line.rstrip('\n'))
            i += 1
        self.len_remaining = i
    
    def __str__(self) -> str:
        return "PossibleWord()"