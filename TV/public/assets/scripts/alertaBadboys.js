var badboyNum = 0;
function alerta(){
        const alerta = document.getElementById('alerta');
        alerta.classList.remove('opacity-0');
        alerta.classList.add('opacity-100')
    setInterval(function(){
        alerta.classList.add('opacity-0');
        alerta.classList.remove('opacity-100')
    }, 5000)
    
}


async function badboys(){
    var url = '/getnumbadboy';
    const temp = await fetch(url, {
        method: "GET"
    });
    const resp = await temp.json();
    if(badboyNum != resp.numbad){
        alerta();
        badboyNum = resp.numbad;
    }
}
setInterval(badboys, 500)