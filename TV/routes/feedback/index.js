const express = require('express');
const routes = express.Router();

var imageBase64 = '';

routes.get('/getfeedback', (req, res) => {
    if (imageBase64) {
        res.json({ image: imageBase64 });
    } else {
        res.status(400);
    }
});

routes.post('/setfeedback', (req, res) => {
    const imgData = req.body.image;
    if (imgData) {
        imageBase64 = imgData;
        res.send('Imagem recebida e armazenada com sucesso!');
    } else {
        res.status(400).send('Nenhuma imagem recebida');
    }
});

module.exports = routes;
