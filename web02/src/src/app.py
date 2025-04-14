import os
import random

from flask import Flask, render_template, make_response

app = Flask(__name__)

FLAG = os.getenv('FLAG')


@app.route('/')
def index():
    return render_template('index.html')


THOUGHTS = [
    "Oggi scegli di essere gentile con te stesso/a. Meriti amore e gentilezza tanto quanto gli altri.",
    "Fai un passo indietro e apprezza la bellezza che ti circonda, anche nelle piccole cose.",
    "Ricorda che dietro ogni persona c'è una storia. Sii gentile, potresti non conoscere il peso che qualcun altro sta portando.",
    "Pratica la gratitudine ogni giorno. Trova almeno tre cose per cui essere grato/a e lascia che la gratitudine illumini la tua giornata.",
    "Offri un sorriso a chi incontri per strada. Un gesto così semplice può illuminare la giornata di qualcun altro.",
    "Ascolta attivamente le persone intorno a te. Spesso, ciò di cui hanno bisogno è solo qualcuno che ascolti senza giudicare.",
    "Lascia un biglietto gentile o un messaggio di incoraggiamento in un luogo pubblico. Potresti rendere migliore la giornata di uno sconosciuto.",
    "Pratica l'autocommiserazione. Tratta te stesso/a con la stessa gentilezza e compassione che riservi agli altri.",
    "Fai una gentilezza anonima. Trova modi creativi per fare del bene senza cercare riconoscimento.",
    "Coltiva relazioni positive. Condividi il tuo tempo e le tue energie con le persone che ti ispirano e ti fanno sentire bene.",
]


@app.route('/talk')
def talk():
    r = make_response(THOUGHTS[random.randrange(len(THOUGHTS))])

    for i, c in enumerate(FLAG):
        r.headers[f'X-Flag-{i}'] = c

    return r


if __name__ == "__main__":
    app.run(debug=True)
