const sqlite3 = require('sqlite3');
const db = new sqlite3.Database(':memory:');

const PORT = process.env.PORT || 3000,
    FLAG_USER = process.env.FLAG_USER || 'example',
    FLAG = process.env.FLAG || 'ITASEC{placeholder}';

db.serialize(() => {
    db.run("CREATE TABLE presents (user TEXT, info TEXT)");

    const stmt = db.prepare("INSERT INTO presents (user, info) VALUES (?, ?)");
    stmt.run(FLAG_USER, FLAG);
    stmt.finalize();
})

const express = require('express');
const app = express();
app.use(express.json());

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

app.get('/get', (req, res) => {
    const user = req.query.user
    if (!user) {
        res.json({error: 'Invalid user'})
        return;
    }

    db.all(`SELECT info
            FROM presents
            WHERE "user" = '${user}'`, (err, rows) => {
        if (err) {
            res.json({error: `An error occurred: ${err}`})
            return
        }

        res.json({presents: rows.map(x => x.info)})
    })
})

app.get('/add', (req, res) => {
    const user = req.query.user, info = req.query.info
    if (!user || !info || info.length > 256) {
        res.json({error: 'Invalid user or info'})
        return;
    }

    db.exec(`INSERT INTO presents (user, info)
             VALUES ('${user}', '${info}')`, (err) => {
        if (err) {
            res.json({error: `An error occurred: ${err}`})
        } else {
            res.json({})
        }
    })
})

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
