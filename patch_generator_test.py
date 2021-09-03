import time
from genera_palabras_al_azar import genera_palabras_al_azar

start = time.time()
train_set = complete_set(genera_palabras_al_azar())
print("Tiempo:", time.time()-start)