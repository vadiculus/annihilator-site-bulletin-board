window.addEventListener('DOMContentLoaded', function(){
    console.log('awfawgaw');
    const message_text_input = document.getElementById('message_text_input');
    const message_btn = document.getElementById('message_btn');

    console.log(message_text_input);
    message_text_input.addEventListener('keydown', function(event){
        if(event.keyCode == 13){
            message_btn.click();
        };
    });

    message_btn.addEventListener('click', function(){
        message_text_input.value = '';
    });
})