# ITASEC24 - CTF Workshop

## [web] DividiFacile (10 risoluzioni)

DividiFacile: la soluzione online per suddividere le spese senza stress, in modo rapido e preciso.

Sito: [http://dividifacile.challs.olicyber.it](http://dividifacile.challs.olicyber.it)

## Soluzione

Leggendo il sorgente scopriamo che la challenge restituisce la flag quando il risultato della divisione è maggiore o
uguale ad infinito. Per fare questo in Javascript è sufficiente dividere per zero, infatti, effettuando la richiesta
usando come divisore zero otteniamo la flag.
