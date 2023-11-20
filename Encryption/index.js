const {
    scrypt,
    randomFill,
    createCipheriv,
} = require('node:crypto');
const express = require('express')

const cors = require('cors')
const app = express()
const port = 3000



const algorithm = 'aes-192-cbc';
const password = 'thisismysecret';

app.use(cors({
    origin: '*', // Replace with your allowed origin(s)
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE'
}));

app.get('/encrypt', (req, res) => {
    const email = req.query.email
    let encrypt;
    scrypt(password, email, 24, (err, key) => {
        if (err) throw err;
        randomFill(new Uint8Array(16), (err, iv) => {
            if (err) throw err;
            const cipher = createCipheriv(algorithm, key, iv);

            let encrypted = '';
            cipher.setEncoding('hex');

            cipher.on('data', (chunk) => encrypted += chunk);
            cipher.on('end', () => {
                console.log(encrypted)
                encrypt = encrypted;
                res.status(200).send({ "encrypted": encrypt })
            });

            cipher.write('some clear text data');
            cipher.end();
        });
    });

    
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})