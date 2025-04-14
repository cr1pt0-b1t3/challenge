# ITASEC24 - CTF Workshop

## [web] Sito Gentile (7 risoluzioni)

Dove la gentilezza diventa un'abitudine quotidiana e un'ispirazione per un mondo migliore.

Sito: [http://sitogentile.challs.olicyber.it](http://sitogentile.challs.olicyber.it)

## Soluzione

Quando viene effettuata la richiesta a `/talk` il server risponde con il messaggio, ma include anche la flag negli
header. In particolare un carattere per ogni header dal nome `X-Flag-N` dove N è l'indice del carattere.
