window.addEventListener('DOMContentLoaded', function(){
    const messages = document.getElementById('messages');
    const search_input = this.document.getElementById('search_input');
    const search_list_conteiner = this.document.getElementById('search_list_conteiner');
    const search_list = this.document.getElementById('search_list');
    const ajax_timeout = 1000;
    let ajax_call_timeout;

    if (messages.children[0].children.length > 0){
        messages.style.top = '15px';
        this.setTimeout(()=>{
            messages.style.top = '-100%';
        }, 5000);
    }

    function getCookie(name){
        let cookieValue = null;
        if (document.cookie && document.cookie != ''){
            const cookies = document.cookie.split(';');
            for(const i = 0; i<cookies.length; i++){
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length+1) ===(name + "=")){
                    cookieValue = decodeURIComponent(cookie.substring(name.length+1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    function ajax_call(value){
        const search_ajax = new XMLHttpRequest();
        search_ajax.open('POST', 'http://' + window.location.host + '/search-product-data/', true);
        search_ajax.setRequestHeader('x-requested-with', 'XMLHttpRequest');
        search_ajax.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        search_data = `search_data=${value}`
        search_ajax.onreadystatechange = function(data){
            if (this.readyState !== 4){
                return;
            }
            response = JSON.parse(search_ajax.response)
            if (response['search_data']){
                search_list.innerText = '';
                search_list_conteiner.classList.add('active');
                response['search_data'].forEach(element => {
                let search_element =document.createElement('a')
                search_element.innerText = element;
                search_element.href = 'http://' + window.location.host + '/home_search/?search_name=' + element;
                search_list.appendChild(search_element);
                });
            } else {
                search_list_conteiner.classList.remove('active');
            }
            search_response = data.data;
        }
        search_ajax.send(search_data);
    }

    search_input.oninput = function(){
        if (this.value.length >= 2){
            if (ajax_call_timeout){
                clearTimeout(ajax_call_timeout);
            }    
            ajax_call_timeout = setTimeout(ajax_call, ajax_timeout, this.value);
        } else {
            clearTimeout(ajax_call_timeout);
            search_list_conteiner.classList.remove('active')
        }
    }
})