var resp = ''

async function getgender(){
    const url = '/getgender';

    const json = await fetch(url)
    const valor = await json.json()
    
    if(valor.gender != resp){
        resp = valor.gender;
        switch(resp){
            case 'rock':
                document.getElementById('gender').innerHTML = `
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
    `

          play('rock');

    break;
    case 'sertanejo':
        document.getElementById('gender').innerHTML = `
                <p class="text-white absolute top-4 text-3xl font-sans">Sertanejo</p>
      <hr class="w-[40vw] absolute top-[10vh]">
      <div class="cont w-[40vw] h-[40vh] absolute bottom-0 flex fo">

        <div class="row1 w-[20vw] h-[40vh] flex items-center justify-evenly flex-col">

          <div class="musics">
            <p class="text-white text-xs">Gusttavo Lima e Você - Gusttavo Lima</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">As andorinhas - Trio Parada Dura</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Cê Topa - Luan Santana</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Boate Azul - Bruno & Marrone</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Evidências - Chitãozinho e Chororó</p>
          </div>

        </div>

        <div class="row2 w-[20vw] h-[40vh] flex items-center justify-evenly flex-col">

          <div class="musics">
            <p class="text-white text-xs">Dormi na praça - Bruno & Marrone</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Tocando em frente - Almir Sater</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">50 Reais - Maiara e Maraísa</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">10% - Maiara e Maraísa</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Sinônimos - Chitãozinho e Chororó, Zé Ramalho</p>
          </div>

        </div>
      </div>
    `
    play('sertanejo')
    break;
    case 'pop':
      document.getElementById('gender').innerHTML = `
      <p class="text-white absolute top-4 text-3xl font-sans">Pop</p>
      <hr class="w-[40vw] absolute top-[10vh]">
      <div class="cont w-[40vw] h-[40vh] absolute bottom-0 flex fo">

        <div class="row1 w-[20vw] h-[40vh] flex items-center justify-evenly flex-col">

          <div class="musics">
            <p class="text-white text-xs">Billie Jean - Michael Jackson</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Girls just wanna have fun - Cyndi Lauper</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Bad romance - Layd Gaga</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Wanna be - Spicy Girls</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Locked out of heaven - Bruno Mars</p>
          </div>

        </div>

        <div class="row2 w-[20vw] h-[40vh] flex items-center justify-evenly flex-col">

          <div class="musics">
            <p class="text-white text-xs">Baby one more time - Britney Spears</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Wrecking ball - Miley Cyrus</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Shake it off - Taylor Swift</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Blinding Lights - The Weekend</p>
          </div>

          <div class="musics">
            <p class="text-white text-xs">Levitating - Dua Lipa, DaBaby</p>
          </div>

        </div>
      </div>
      `
      play('pop')
    break;
        }
    }
    

    
}


setInterval(getgender, 100);



function play(g){
  switch (g){
    case 'pop':

    break;
    case 'rock':

    break;
    case 'sertanejo': 

    break;
  }
}