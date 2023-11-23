const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'public'));

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.render('index');
});

app.get('/flag', (req, res) => {
    // This is a placeholder. In a real CTF challenge, you would have a more secure method to store and retrieve the flag.
    const flag = 'FLAG{your_flag_here}';
    res.render('flag', { flag });
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
