const express = require('express');
const setGender = require('../../controller/setGender.cjs')
const path = require('path');
const routes = express.Router();
const getMusic = require('../../controller/getMuisca.cjs');

var gender = '';

routes.get('/', (req, res) => {
    res.sendFile('index.html');
});

routes.get('/getGender', async (req, res) => {
    res.json({gender: gender})
})

routes.get('/getMusic', async (req, res) => {
    var link
    const music = await getMusic();
    if(gender == 'rock'){
        link = music.lista.rock
    }else if(gender == 'hiphop'){
        link = music.lista.hiphop
    }else if(gender == 'reggae'){
        link = music.lista.reggae
    }



    res.json({ music: link})
});

routes.post('/setgender', (req, res) => {
    const { gend } = req.body;
    gender = setGender(gend);

    res.sendStatus(200);
});

module.exports = routes;