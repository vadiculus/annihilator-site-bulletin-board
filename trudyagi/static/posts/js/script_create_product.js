window.addEventListener('DOMContentLoaded', function(){
    const image_input = document.getElementById('image_input');
    const images_input = document.getElementById('images_input');
    const product_image = document.getElementById('product_image');
    const characteristics_table = document.querySelector('#characteristics_table tbody');
    const characteristics_obj = {};

    image_input.onchange = function(event){
        const target = event.target;
        const fileReader = new FileReader();
        fileReader.onload = function(event){
            product_image.src = fileReader.result;   
        };

        if (target.files[0]){
            fileReader.readAsDataURL(target.files[0]);
        } else {
            product_image.src = '';
        }
    }

    this.document.getElementById('id_sale_type').addEventListener('change', function(event){
        if (this.value == 'f' || this.value == 'e'){
            document.getElementById('id_price').value = null;
            document.getElementById('id_price').disabled = true;
        } else {
            document.getElementById('id_price').disabled = false;
        }
    });

    this.document.getElementById('add_char').addEventListener('click' ,function(){
        characteristics_table.insertAdjacentHTML('beforeend', '<tr><td class="characteristic_input"><input type="text"></td><td class="value_input"><input type="text"></td></tr>');
    });

    this.document.getElementById('create_submit_btn').addEventListener('click', function(){
        for (const tr of characteristics_table.children){
            if (!tr.classList.contains('table_titles')){
                const characteristic_name = tr.children[0].children[0].value;
                const characteristic_value = tr.children[1].children[0].value;
                if (characteristic_name.length > 0 && characteristic_value.length > 0){
                    characteristics_obj[characteristic_name] = characteristic_value;
                }
            }
        }
        document.getElementById('id_characteristics').value = JSON.stringify(characteristics_obj);
    });
})