const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '../../configs/musicas.json');

async function setMusicas(novasMusicas) {
    const musicas = JSON.parse(fs.readFileSync(filePath, 'utf8'));

    musicas.lista = novasMusicas; 

    const jsonString = JSON.stringify(musicas, null, 2);

    fs.writeFileSync(filePath, jsonString, 'utf8');
    
}

module.exports = setMusicas;
