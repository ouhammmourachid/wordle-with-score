from .constant import *
from .case import Case

def create_cases() -> list[Case]:
    result :list = []
    for case_1 in ALLOWED_COLORS:
        for case_2 in ALLOWED_COLORS:
            for case_3 in ALLOWED_COLORS:
                for case_4 in ALLOWED_COLORS:
                    for case_5 in ALLOWED_COLORS:
                        result.append(Case([case_1,case_2,case_3,case_4,case_5]))
    return result
