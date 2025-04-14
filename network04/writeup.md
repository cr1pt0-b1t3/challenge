# ITASEC24 - CTF Workshop

## [network] Le mosse (2 risoluzioni)

So che l'hacker che abbiamo tracciato ha preso la flag. Riesci a riprodurre le sue mosse?

Sito: [http://lemosse.challs.olicyber.it](http://lemosse.challs.olicyber.it)

## Soluzione

Il file pcap contiene il traffico registrato mentre un hacker esegue una serie di richieste HTTP di diverso tipo.
Sappiamo dalla descrizione della challenge che l'hacker ha ottenuto la flag, possiamo quindi riprodurre una ad una tutte
le richieste che ha effettuato. In ordine, le richieste sono:

1. metodo: GET, endpoint: /step1
2. metodo: POST, endpoint: /step2, con parametri hello=world, dead=beef
3. metodo: PUT, endpoint: /step3
4. metodo: DELETE, endpoint /step4

E' possibile eseguirli in sequenza utilizzando Burp Suite oppure un semplice Python script:

```python
URL = "http://lemosse.challs.olicyber.it"
session = requests.Session()
session.get(f'{URL}/step1')
params = {'hello': 'world', 'dead': 'beef'}
session.post(f'{URL}/step2', data=params)
session.put(f'{URL}/step3')
print(session.delete(f'{URL}/step4').text)
```
