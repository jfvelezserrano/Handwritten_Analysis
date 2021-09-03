import time

from genera_palabras_al_azar import genera_palabras_al_azar

start = time.time()
train_set = complete_set(list_random_strings)
print("Tiempo:", time.time()-start)