const express = require('express');
const path = require('path');
const routes = express.Router();
const setMusicas = require('../../controller/admin/setMusics');

routes.get('/admin', (req, res) => {
    res.sendFile(path.join(__dirname, '..', '..', 'public', 'admin.html'));
});

routes.post('/setMusicas', (req, res) => {
    const {reggae, rock, hiphop} = req.body;
    const generosFormated = {
        rock: rock,
        reggae: reggae,
        hiphop: hiphop
    }
    setMusicas(generosFormated);
})

module.exports = routes;
