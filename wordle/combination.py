from .case import Case
from .functions import create_cases

class Combination:
    """this class is the one responsable of storing all the case
    that had been created by combining all the possible color:
    [🟩,🟨,🟫,🟩,🟨]"""
    def __init__(self) -> None:
        """to create an object of contribtion we use this folowing
        code :
        ```python
        >> Combination()
        ```
        the code witch is responsable of creating the object is the 
        `create_cases()` .
        """
        self.all :list[Case] = create_cases()
    
    def __str__(self) -> str:
        return 'Combination()'
        