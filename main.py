from wordle import Word,Case,Combination,PossibleWord
import time
start = time.perf_counter()
all_word = PossibleWord('./data/data.txt')
end = time.perf_counter()
print(end-start)
