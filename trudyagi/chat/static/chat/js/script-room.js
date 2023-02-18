console.log('Done!');

const board = document.querySelector('.board');
const chat = document.querySelector('.chat_dialog')
const chatInput = document.getElementById('chat_input');
console.log(chatInput)
const authorInput = document.getElementById('author_input');
const get_room_name = JSON.parse(document.getElementById('room-name').textContent);
console.log(document.querySelector('#room-name').value);
const client = new WebSocket(`ws://${window.location.host}/ws/chat/${get_room_name}/`);

client.addEventListener("message", function( data ){;
    message_data = JSON.parse(data.data);
    const message_construction = document.createElement('div');
    message_construction.classList.add('message');
    message_construction.innerHTML=`<span id='author_name'></span><div class='message_content'>${message_data.message}</div>`;
    chat.appendChild(message_construction);
})

document.getElementById('send_message').onclick = function(){
    if (chatInput.value !== ''){
        const message = {
            "message": chatInput.value
        }
        client.send(JSON.stringify(message));
    }
}

document.getElementById('chat_input').onclick = function(){

}
