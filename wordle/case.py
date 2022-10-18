from .constant import *

class Case:
    """this Class represnt the result might get when
        try a word so accept only three colors which are 
        following 🟩🟨🟫to create an object :
        ```python
        case = Case([🟩,🟨,🟫,🟩,🟨])
        ```
        to access a specifique combi we use `case.char_1`
        we can also use it with `char_2,..,char_5`
        to get the case on the shape of list we use 
        `case.get_list()`"""
    def __init__(self,combination:list[str]) -> None:
        assert combination[0] in ALLOWED_COLORS, "the first in the combination is not in the allowed colors"
        assert combination[1] in ALLOWED_COLORS, "the second in the combination is not in the allowed colors"
        assert combination[2] in ALLOWED_COLORS, "the third in the combination is not in the allowed colors"
        assert combination[3] in ALLOWED_COLORS, "the forth in the combination is not in the allowed colors"
        assert combination[4] in ALLOWED_COLORS, "the fifth in the combination is not in the allowed colors"
        
        self.char_1 = combination[0]
        self.char_2 = combination[1]
        self.char_3 = combination[2]
        self.char_4 = combination[3]
        self.char_5 = combination[4]

    def __str__(self) -> str:

        """the return of this function is list of the color
        we get from the game when we performe a gess
        """
        return "Case("+self.char_1+self.char_2+self.char_3+self.char_4+self.char_5+")"

    def get_list(self) -> list[str]:

        """this function methode is gave us case as a list
        ## difinition:
            param:
                -self
            return:
                -a list of string.
        """
        return [self.char_1,self.char_2,self.char_3,self.char_4,self.char_5]

