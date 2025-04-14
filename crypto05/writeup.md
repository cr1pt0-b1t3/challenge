# ITASEC24 - CTF Workshop

## [crypto] Passwordless Login (0 risoluzioni)

Nulla da vedere qui, solo un classico sistema di login che non serve assolutamente a nulla in pieno stile CTF :)

Sito: [http://passwordlesslogin.challs.olicyber.it](http://passwordlesslogin.challs.olicyber.it)

## Soluzione

La sfida qui è quella di effettuare un login come "Amministratore" senza avere la possibilità di registrare direttamente
questo utente. Il sistema di autenticazione genera un token di login cifrato in AES-ECB, che contiene `username`
e `registration_date`.

1. Registrare due utenti con username simili ma strategicamente scelti: `Bmministratore` e `Amministratori`. La scelta è
   fatta per manipolare i blocchi di cifratura generati.
2. Dal momento che AES-ECB cifra blocchi di testo di dimensione fissa e la cifratura di un blocco è indipendente dagli
   altri, possiamo sfruttare questa proprietà.
3. Ottenere i token cifrati per entrambi gli utenti.
4. Creare un nuovo token manipolato sostituendo il primo blocco del token di `Bmministratore` (che contiene parte
   dell'username cifrato) con il primo blocco del token di `Amministratori`. Questo perché in AES-ECB lo stesso blocco
   di testo chiaro produce sempre lo stesso blocco di testo cifrato se la chiave è la stessa.
5. Utilizzare il token falsificato per autenticarsi come `Amministratore`.
