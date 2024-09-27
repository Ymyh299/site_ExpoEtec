var resp = ''

async function getgender(){
    const url = '/getgender';

    const json = await fetch(url)
    const valor = await json.json()
    
    if(valor.gender != resp){
        resp = valor.gender;
        switch(resp){
            case 'rock':
                document.getElementById('main').innerHTML = `
                <div
      class="feedback w-[40vw] h-[50vh] bg-transparent backdrop-blur-sm border-white border-solid border-[1px] rounded-xl flex items-center justify-center">
      <img src="" id="feedback" alt="feedback da camera." class="w-[40vw] h-[50vh] rounded-xl">
    </div>

    <div id="rock" class="genero w-[40vw] h-[50vh] bg-transparent backdrop-blur-sm border-white border-solid border-[1px] rounded-xl flex items-center justify-center relative">
      <p class="text-white absolute top-4 text-3xl font-sans">Rock</p>
      <hr class="w-[40vw] absolute top-[10vh]">
      <div class="cont w-[40vw] h-[40vh] absolute bottom-0 flex fo">

        <div class="row1 w-[20vw] h-[40vh] flex items-center justify-evenly flex-col">

          <div class="musics">
            <p class="text-white text-xs">Master os Puppets - Metallica</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Blitzkrieg bop - Ramones</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Born to be wild - Steppenwolf</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Smoke on the water - Deep Purple</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Highway to hell - AC/DC</p>
          </div>

        </div>

        <div class="row2 w-[20vw] h-[40vh] flex items-center justify-evenly flex-col">

          <div class="musics">
            <p class="text-white text-xs">Johnny B. Goode - Chuck Berry</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Under pressure - Queen</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Carry on my wayward son - Kansas</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">It's my life - Bon jovi</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Sweet Child'o mine - Guns n' roses</p>
          </div>

        </div>
      </div>
    </div>
    `
    break;
    case 'sertanejo':
        document.getElementById('main').innerHTML = `
         <div
      class="feedback w-[40vw] h-[50vh] bg-transparent backdrop-blur-sm border-white border-solid border-[1px] rounded-xl flex items-center justify-center">
      <img src="" id="feedback" alt="feedback da camera." class="w-[40vw] h-[50vh] rounded-xl">
    </div>
        `
        }
    }
    

    
}


setInterval(getgender, 100);