# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:57:41 2020

@author: jcarl
"""


import redis
import os
import time


r = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=6379, db=0)

redis_ready = False

while not redis_ready:
    try:
        redis_ready = r.ping()
    except:
        print("waiting for redis")
        time.sleep(3)
        
print("setup:redis alive")


#Eliminamos los elementos residuales de la lista
while True:    
    i = r.lpop('queue_entrada')
    if i is None:
        print('setup:limpieza de queue')
        break


#Agregamos los nuevos elementos en decenas
decena = 0
while True:
    x = 0
    while x < 10:
        r.rpush('queue_entrada', decena + x)  #empuja un valor por la derecha right push
        x += 1
    print('se alimento la decena ', decena)
    decena += 10
    time.sleep(3)