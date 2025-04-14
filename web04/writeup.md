# ITASEC24 - CTF Workshop

## [web] QuickNote (4 risoluzioni)

Prendi appunti in modo rapido, semplice e ovunque tu sia su QuickNote. Riuscirai a leggere la nota di `admin`?

Sito: [http://quicknote.challs.olicyber.it](http://quicknote.challs.olicyber.it)

## Soluzione

Per ottenere la nota dell'admin possiamo osservare che il server invia un cookie quando viene creata una nota. Questo
cookie contiene un JSON encodato in Base64 con dentro un campo `username`. Visto che il cookie non è controllato
possiamo modificarlo mettendo come username `admin` ed inviarlo al server per ottenere la flag.
