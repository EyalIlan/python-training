




 document.addEventListener("DOMContentLoaded", function () {
    window.resizeTo(1200, 800);
        eel.get_word();
  });



let Input = document.getElementById('word_input') //get
let ActuallWord = document.querySelector('#game-container h3')
let timer = document.querySelector('#timer_countdown')
let LengthWords = document.getElementById('numberOfWordsLeft')



// VARIBALS
let WriteWord = ''
let Typingword = ''


let minutes = 0
let seconds = 0
let milSeconds = 0



let TimerID = setInterval(() =>{
    milSeconds++

    if(milSeconds === 100){
        seconds += 1
        milSeconds  =  0
    }  
    if(seconds === 60){
        seconds = 0
        minutes += 1
    }
    timer.innerHTML = `${minutes}:${seconds}:${milSeconds}`
    clearInterval(TimerID)
},100)



//EVENTS
Input.addEventListener('input',(p) =>{
    Typingword = p.target.value
    ActuallWord.innerHTML = Typingword
    CheckEqual(Typingword,WriteWord)
})


//FUNCTIONS 
function CheckEqual(Typingword,WriteWord){
    
    
    if(Typingword === WriteWord){
        Typingword = ''
        ActuallWord.innerHTML = ''
        Input.value = ''
        eel.get_word();
    }
}


 

//PYTHON FUNCTIONS 
eel.expose(SuccessAllWords)
function SuccessAllWords(Length){
    LengthWords.innerHTML = Length
    document.getElementById("word_to_be_displayed").innerText = 'Success!!!'

    window.location.href = 'winPage.html'

}

eel.expose(get_word_python)
function get_word_python(x,Length){
    LengthWords.innerHTML = Length
    WriteWord = x
    document.getElementById("word_to_be_displayed").innerText = WriteWord
}