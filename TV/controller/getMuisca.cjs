const fs = require('fs');
const path = require('path');
const music = require('../configs/musicas.json')
const filePath = path.join(__dirname, '../configs/musicas.json');

async function musicF(){
    const data = fs.readFileSync(filePath, 'utf8');
    return JSON.parse(data);
}

module.exports = musicF;