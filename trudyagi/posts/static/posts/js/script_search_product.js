window.addEventListener('DOMContentLoaded', function(){
    const search_form = this.document.getElementById('search_form');
    const search_name_input = this.document.getElementById('search_name_input');
    const search_form_submit_button = this.document.getElementById('search_form_submit_button');
    const category_choice_input = this.document.getElementById('id_category');
    const category_slug_data = this.document.getElementById('slug-data');
    const category_button_name = this.document.getElementById('choice_category_button_name');

    this.document.getElementById('choice_category_button').addEventListener('click', function(){
        document.getElementById('search_rubric_list').classList.toggle('active');
    })

    search_form.addEventListener('submit', function(event){
        event.preventDefault();
        let new_url = [];
        for (elem of this.elements){
            if (elem.type === 'checkbox'){
                if (elem.checked){
                    new_url.push(elem.name+ '=' + elem.value);
                }
            } else {
                if (elem.value.length > 1){
                    new_url.push(elem.name+ '=' + elem.value);
                }
            }
        }
        window.location.href = `http://${window.location.host}/search/${category_choice_input.value ? category_choice_input.value : JSON.parse(category_slug_data.textContent)}/${search_name_input.value.length > 0 ? search_name_input.value: 'empty'}/${new_url.length > 0 ? '?'+ new_url.join('&'): ''}`;        
    })

    console.log(document.getElementsByClassName('choice_rubric_conteiner'));
    for(element of this.document.querySelectorAll('.choice_rubric_conteiner')){
        element.addEventListener('mouseenter', function(event){
            event.preventDefault();
            event.target.children[1].style.display = 'block';
        })
        element.addEventListener('mouseleave', function(event){
            event.target.children[1].style.display = 'none';
        })
    }    

    for(element of this.document.querySelectorAll('.choice_category_conteiner')){
        element.addEventListener('click', function(event){
            category_choice_input.value = this.dataset.slug
            category_button_name.textContent = this.dataset.name
            window.location.href = `http://${window.location.host}/search/${category_choice_input.value ? category_choice_input.value : JSON.parse(category_slug_data.textContent)}/${search_name_input.value.length > 0 ? search_name_input.value: 'empty'}/`;        
        })
    }

})