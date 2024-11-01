console.clear();
const express = require('express');
const multer = require('multer');
const path = require('path');

const app = express();
const upload = multer(); 
const port = 3030;

app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ limit: '50mb', extended: true }));

app.use(express.static(path.join(__dirname, 'public')));

app.use('/', require('./routes/dashboard/index.js'));
app.use('/', require('./routes/admin/index.js'));
app.use('/', require('./routes/feedback/index.js'));

app.listen(port, () => {
    console.log(`🧨 | Servidor rodando em: http://localhost:${port} !`);
});
