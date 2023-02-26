window.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#room-name-input').onkeyup = function(event){
        if (event.keyCode === 13){
            document.querySelector('#room-name-submit').click();
        }
    };

    document.querySelector('#room-name-submit').onclick = function(event){
        const roomName = document.querySelector("#room-name-input").value;
        window.location.pathname = `chat/${roomName}/`
    }
})