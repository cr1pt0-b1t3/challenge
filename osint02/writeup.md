# ITASEC24 - CTF Workshop

## [osint] Ritorno alle origini (22 risoluzioni)

Quest'anno, con ITASEC24, siamo arrivati alla 8a edizione di [ITASEC](https://itasec.it), la conferenza italiana sulla
cybersicurezza.

Riesci a trovare esattamente quando è stato registrato il dominio [itasec.it](https://itasec.it) la prima volta?

La flag è nel formato: `ITASEC{AAAA-MM-GG hh:mm:ss}`

## Soluzione

Per ottenere informazioni relative alla storia di registrazione di un dominio è sufficiente utilizzare il
comando `whois` disponibile da linea di comando sui sistemi linux.

Il comando `whois`, oltre a restituire le informazione relative ai contatti amministrativi e tecnici del sito, fornisce
indicazioni anche sulla data di scadenza, di ultimo rinnovo e di creazione del dominio. In particolare la prima porzione
di output sul dominio itasec.it è il seguente:

```bash
$ whois itasec.it

*********************************************************************
* Please note that the following result could be a subgroup of      *
* the data contained in the database.                               *
*                                                                   *
* Additional information can be visualized at:                      *
* http://web-whois.nic.it                                           *
*********************************************************************

Domain:             itasec.it
Status:             ok
Signed:             no
Created:            2016-12-07 18:25:53
Last Update:        2023-12-23 00:48:34
Expire Date:        2024-12-07
...
```

L'informazione cercata è quindi corrispondente al valore indicato nel campo "Created".
