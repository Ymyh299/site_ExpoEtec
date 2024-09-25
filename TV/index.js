console.clear();
const express = require('express');
const multer = require('multer');
const path = require('path')
const app = express();
const upload = multer();
const port = 3030;


app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));








app.use('/', require('./routes/dashboard/index.js'));
app.use('/', require('./routes/admin/index.js'));



app.listen(port, () => {
    console.log(`🧨 | Servidor rodando em: http://localhost:${port} !`);
})