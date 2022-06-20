from tqdm import tqdm 
import time 
  
  
for i in tqdm (range (100),  
               desc="Loading…",  
               ascii=True, ncols=99, ): 
    time.sleep(0.01) 
      
print("Complete.") 