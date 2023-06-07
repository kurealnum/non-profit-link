//search function that talks to the api and stuff
async function search() {
  let zip_code = document.getElementById('search');

  if (zip_code.value != null){
    // add the users search to a formdata object
  let search = new FormData()
  search.append("search", zip_code.value)

  // fetch request + return
  let search_field = await fetch('/search', {method:'POST', body:search});
  let search_field_text = await search_field.text();
  document.getElementById('search_return').innerHTML = search_field_text;
  }
}

let input = document.getElementById('search');

//first event is for the search bar updating, the second is for checking the search bar on page reload
input.addEventListener('input', search);
document.addEventListener('DOMContentLoaded', search);

//just to prevent the search bar having a panic attack
document.addEventListener('keydown', function(event) {
  if (event.key === "Enter") {
    event.preventDefault(); 
  }
});
