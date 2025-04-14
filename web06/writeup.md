# ITASEC24 - CTF Workshop

## [web] GiftList (4 risoluzioni)

Rendi la tua lista dei desideri una realtà con GiftList.

Sito: [http://giftlist.challs.olicyber.it](http://giftlist.challs.olicyber.it)

## Soluzione

Per estrarre la flag associata all'utente sconosciuto è necessario sfruttare una SQL injection possibile per via del
modo in cui le query SQL sono effettuate. Infatti, inserire la stringa dell'utente direttamente nella query è
considerato insicuro poichè usando `' OR 1=1 --` come utente la query risultante
sarà `SELECT info FROM presents WHERE "user" = '' OR 1=1 -- '`. In questa maniera verranno selezionati tutti gli
elementi del database e anche la flag.
