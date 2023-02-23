window.addEventListener('DOMContentLoaded', function(){
    const left_btn = document.getElementById('left-slider-btn');
    const right_btn = document.getElementById('right-slider-btn');
    const slider = document.getElementById('foto-slider');
    const rating_data = document.getElementById('product-rating-data');
    const review_form = document.getElementById('review_form');
    const review_btn = document.getElementById('review_btn');
    let foto_count = 0;

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

    right_btn.onclick = function(){
        if (foto_count >= slider.children.length - 1){
            foto_count = 0;
        } else {
            foto_count++;
        }
        slider.style.transform = `translateX(-${slider.children[0].clientWidth * foto_count}px)`;
    }

    left_btn.onclick = function(){
        if (foto_count <= 0){
            foto_count = slider.children.length - 1;
        } else {
            foto_count--;
        }
        slider.style.transform = `translateX(-${slider.children[0].clientWidth * foto_count}px)`;
    }

    document.getElementsByClassName('delete_review_btn').forEach(element => {
        element.addEventListener('click', function(){
            const removal_question = document.getElementById('removal_question');
            removal_question.style.display = 'block';
        })
    })
    
    this.document.getElementById('question_review_delete_yes').addEventListener('click', function(){
        const removal_question = document.getElementById('removal_question');
        const delete_ajax = new XMLHttpRequest();
        delete_ajax.open('DELETE', document.querySelector('.delete_review_btn').dataset.delete_href, true);
        delete_ajax.setRequestHeader('x-requested-with', 'XMLHttpRequest');
        delete_ajax.onreadystatechange = function(){
            if (delete_ajax.readyState !=4){
                return;
            }
            response = JSON.parse(delete_ajax.response);
            removal_question.style.display = 'none';
            document.getElementById('this_author_review').remove();
        };
        delete_ajax.send()
    })

    this.document.getElementById('question_review_delete_no').addEventListener('click', function(){
        document.getElementById('removal_question').style.display = 'none';
    })

})