window.addEventListener('DOMContentLoaded', function(){
    const search_form = this.document.getElementById('search_form');
    const search_name_input = this.document.getElementById('search_name_input');
    const search_form_submit_button = this.document.getElementById('search_form_submit_button');

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
        window.location.href = `http://${window.location.host}/search/list/${search_name_input.value.length > 0 ? search_name_input.value: 'empty'}/${new_url.length > 0 ? '?'+ new_url.join('&'): ''}`;
        console.log(`search/list/${search_name_input.value.length > 0 ? search_name_input.value: 'empty'}/${new_url.length > 0 ? '?'+ new_url.join('&'): ''}`);
            
    })

})