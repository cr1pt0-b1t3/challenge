const express = require('express');

const PORT = process.env.PORT || 3000,
    FLAG = process.env.FLAG || 'ITASEC{placeholder}';

const app = express();
app.use(express.json());

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

app.post('/divide', (req, res) => {
    const amount = parseInt(req.body.amount), pieces = parseInt(req.body.pieces)
    if (isNaN(amount) || isNaN(pieces)) {
        res.json({error: 'Invalid input'})
        return
    }

    const result = amount / pieces
    if (result >= Infinity) {
        res.json({result: `Good job: ${FLAG}`})
        return;
    }

    res.json({result: `Each piece is ${result}`})
})

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
