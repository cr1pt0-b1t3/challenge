# ITASEC24 - CTF Workshop

## [web] SecretCheckAI (3 risoluzioni)

Scopri il potenziale segreto di ogni frase con l'intelligenza artificiale su SecretCheckAI!

Sito: [http://secretcheckai.challs.olicyber.it](http://secretcheckai.challs.olicyber.it)

## Soluzione

Il controllo della flag (segreto) viene effettuato tutto con Javascript. Per scoprire quale è la flag possiamo vedere
quando il controllo in `checkSecret` si interrompe perchè il carattere è sbagliato usando il debugger degli strumenti
sviluppatore o inserire un `console.log`.
