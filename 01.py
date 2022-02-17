#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:28:40 2022

@author: alumno probando
"""
from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
"""
a es una variable local no me hace nada
turn me da el turno 
common y tid son variables comunes a todos los procesos
en el 3 empiezan a cederse el paso y no acaban nunca
en el de decker puede pasar lo mismo pero sabemos que en algun 
momento alguno va a entrar.
Deberia haber 800 pasos, si al final no es 800, algo ha habido mal
no ha habido concurrencias.
"""
N=8
def task(common,tid,turn):
    a=0
    for i in range (100): #si pongo 100+tid el ordenador se queda bloqueado, por que el 2 esta esperando.
        print(f'{tid}-{i}:Non-critical Section')
        a+=1
        print(f'{tid}-{i}:End of non-critical Section')
        while turn.value!=tid:
            print(turn.value)
            pass
        print(f'{tid}-{i}:Critical section')
        v=common.value+1
        print(f'{tid}-{i}:Inside critical section')
        common.value=v
        print(f'{tid}-{i}:End of critical section')
        turn.value=(tid+1)%N

def main():
    lp=[]
    common=Value('i',0)
    turn=Value('i',0)
    for tid in range(N):
        lp.append(Process(target=task,args=(common,tid,turn)))
    print(f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    for p in lp:
        p.join()
        
    print(f"valor final del contador{common.value}")
    print("fin")
    
if __name__=="__main__":
    main()
    
    
