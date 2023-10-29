from concurrent import futures
import time
from tqdm import tqdm



def progress(index):
    for i in tqdm(range(500*index), position=index, desc=f"Progress {index}", ascii=True):
        time.sleep(.01)
    return index



with futures.ThreadPoolExecutor() as executor:
    result = executor.map(progress, range(2))
print("\n\nresult", list(result))