let input = document.getElementById('search');
    input.addEventListener('input', async function() {
        let zip_code = document.getElementById('search');

        // add the users search to a formdata object
        let search = new FormData()
        search.append("search", zip_code.value)

        // fetch request + return
        let search_field = await fetch('/search', {method:'POST', body:search});
        let search_field_text = await search_field.text();
        document.getElementById('search_return').innerHTML = search_field_text;
    });

//figure out why a 400 error is being thrown on each function call,