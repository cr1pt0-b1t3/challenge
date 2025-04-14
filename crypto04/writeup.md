# ITASEC24 - CTF Workshop

## [crypto] XOR temporale (1 risoluzioni)

Vorrei trovare una buona descrizione per questa challenge, ma non ne ho il tempo

Sito: [http://xortemporale.challs.olicyber.it](http://xortemporale.challs.olicyber.it)

## Soluzione

Questa sfida richiede una comprensione del meccanismo di seeding basato su tempo e di cifratura con XOR. Il seme
utilizzato per la generazione della chiave è dato dai minuti dell'orario corrente (`datetime.now().minutes`), il che
significa che la chiave cambia ogni minuto.

Per ottenere la chiave di cifratura, eseguiamo i seguenti passaggi:

1. Richiediamo la flag cifrata utilizzando il comando `get_encrypted_flag()`.
2. Entro lo stesso minuto, inviamo una richiesta di cifratura per una lunga stringa di zeri (`000...000`). La lunghezza
   di questa stringa supera quella della flag per assicurarci di ottenere l'intera chiave in formato esadecimale.
3. La risposta del server a questa richiesta sarà essenzialmente la chiave XOR usata per la cifratura, dato che lo XOR
   di qualsiasi byte con `0x00` restituisce il byte stesso.
4. Mediante la pagina web è possibile calcolare la flag originale facendo lo XOR tra la chiave ottenuta e la flag
   cifrata.
5. Decifriamo il risultato in esadecimale per ottenere la flag in chiaro.
