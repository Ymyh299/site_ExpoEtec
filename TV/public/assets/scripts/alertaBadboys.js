
function alerta(){
    const alerta = document.getElementById('alerta');
    alerta.classList.remove('opacity-0');
    alerta.classList.add('opacity-100')
    setInterval(function(){
        alerta.classList.add('opacity-0');
    alerta.classList.remove('opacity-100')
    }, 5000)
    
}