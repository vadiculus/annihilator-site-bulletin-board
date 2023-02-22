window.addEventListener('DOMContentLoaded', function(){
    const image_input = document.getElementById('image_input');
    const images_input = document.getElementById('images_input');
    const product_image = document.getElementById('product_image');

    image_input.onchange = function(event){
        const target = event.target;
        console.log('nenr');
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

    document.getElementById('id_sale_type').addEventListener('change', function(event){
        if (this.value == 'f' || this.value == 'e'){
            document.getElementById('id_price').value = null;
            document.getElementById('id_price').disabled = true;
        } else {
            document.getElementById('id_price').disabled = false;
        }
    });
})