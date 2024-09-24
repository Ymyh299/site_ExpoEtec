var feedback;

async function getImage(){
    const img = document.getElementById('feedback');
    const url = '/getfeedback';
    const resp = await fetch(url, {
        method: 'GET',
    })
    const respFormat = await resp.json();
    feedback = respFormat.image;
    img.src = `data:image/jpeg;base64,${feedback}`;

}

setInterval(getImage, 33)