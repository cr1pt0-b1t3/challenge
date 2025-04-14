# ITASEC24 - CTF Workshop

## [crypto] XOR minimale (1 risoluzioni)

Chi ha detto che una chiave dev'essere lunga per non essere ripetuta?

Sito: [http://xorminimale.challs.olicyber.it](http://xorminimale.challs.olicyber.it)

## Soluzione

Leggendo il sorgente della challenge, disponibile direttamente sulla pagina web, si può notare che utilizza un carattere
segreto (`secret_char`) per effettuare un'operazione di XOR con la flag. Il primo carattere della flag viene xorato
con `secret_char`, il secondo con `secret_char+1`, il terzo con `secret_char+2`, e così via.

Dato che il formato delle flag è fisso (`ITASEC{...}`), il primo carattere della flag è sicuramente `I` e quindi il
primo carattere della flag cifrata è ottenuto dall'operazione di XOR fra `I` e il `secret_char`.

Possiamo richiedere la flag criptata semplicemente cliccando sul tasto `RUN` per la funzione `get_encrypted_flag()`, e
calcolare `secret_char` effettuando lo XOR fra il primo carattere della flag cifrata e `I`. In questo modo è possibile
calcolare che `secret_char = 0x5b`.

A questo punto, è possibile decifrare la flag semplicemente utilizzando la funzione `minimal_xor` inserendo come primo
parametro la flag cifrata e come secondo parametro `5b`.
