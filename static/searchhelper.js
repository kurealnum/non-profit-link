let input = document.getElementById('search');
    input.addEventListener('input', async function() {
        let zip_code = document.getElementById('search');
        let search_field = await fetch('/search?request_type=search&zip_code=' + zip_code.value);
        let search_field_text = await search_field.text();
        document.getElementById('search_return').innerHTML = search_field_text;
    });