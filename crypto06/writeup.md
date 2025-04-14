# ITASEC24 - CTF Workshop

## [crypto] Condividendo segreti (0 risoluzioni)

Lo sapevi che la crittografia può essere usata per [condividere segreti](https://en.wikipedia.org/wiki/Secret_sharing)?

Sito: [http://condividendosegreti.challs.olicyber.it](http://condividendosegreti.challs.olicyber.it)

## Soluzione

- c'è uno schema di secret sharing tra 6 persone: c'è un segreto e a ognuno viene dato segreto mod p_i, dove i p_i sono
  numeri primi di 50 bit che conosciamo
- se chiediamo le share della flag ce ne vengono date solo 5
- abbiamo un oracle per poter condividere nostri segreti e ottenere le 6 share
- abbiamo un oracle che, prese 6 share, ritorna il segreto

gli ultimi 2 endpoint non servono davvero, ma ci spiegano come funziona lo schema, e come si recuperano i segreti: se
abbiamo 6 share usiamo il teorema cinese del resto per ricostruire il segreto
osservazioni:

- i primi sono da 50 bit e il segreto è da 32 byte = 256 bit (è scritto nel sorgente)
- se faccio CRT con solo 5 share ottengo un segreto che è uguale al segreto vero modulo il prodotto dei primi 5 primi (
  che è di 50 bit), chiamo questo numero segreto_parziale
  -> il segreto vero è segreto = segreto_parziale + k*(prodotto dei primi 5 primi), dove k è piccolo (mancano 6 bit,
  quindi sarà circa 6 bit)
  -> bruteforce di k e ottengo la flag
