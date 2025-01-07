#import modules
import time

#Variables
sentence = "Type this sentence."
m = 0
n = 0

#Give sentence and user types sentence
print(sentence)
start = time.time()
user = input("")
end = time.time()

#for statement checks for mistakes
for l in sentence:
    if l != user[n]:
        m += 1
    n += 1

#variable to get amount of time taken to type sentence
time = end - start

#Prints results from typing test
print("Time to type:", time, "\n", "Mistakes:", m)