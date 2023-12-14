// closing and opening the needs modal
const needsModal = document.querySelector("#needs-modal") 
const needsButton = document.getElementById("needs-button")

needsButton.onclick = function() {
    needsModal.showModal()
    document.body.style.overflow = "hidden"
}

// needsCloseButton.onclick is lower down, as it has more functionality than just closing

// closing and opening the surplus modal
const surplusModal = document.querySelector('#surplus-modal')
const surplusButton = document.getElementById("surplus-button")
const surplusCloseButton = document.getElementById("surplus-close-button")

surplusButton.onclick = function() {
    surplusModal.showModal()
    document.body.style.overflow = "hidden"
}

surplusCloseButton.onclick = function() {
    surplusModal.setAttribute("closing", "");

    surplusModal.addEventListener(
        "animationend",
        () => {
            surplusModal.removeAttribute("closing");
            surplusModal.close();
            document.body.style.overflow = "auto"
        },
        { once: true }
    );
}


// function for creating a new item, and rendering a new item with inputs instead of fields
function createNewItem(){
    const neededModalItemsList = document.getElementById("needed-items-list")
    let itemCounter = 0
    return function () {
        itemCounter++
        neededModalItemsList.insertAdjacentHTML('beforeend', `
        <div id='creating-item' class="item">
            <input id='number-of-units-${itemCounter}' type='number' value='0'>
            <input id='unit-type-${itemCounter}' type='text' value='units'> of 
            <input id='item-name-${itemCounter}' type='text' value='item'>
        </div>
        `)
        return itemCounter
    }
}



// these are the "buckets" in the eraser.io diagrams
let needsNewItemClasses = [];
// this func uses closure (i think thats what its called)
const needsModalNewItem = createNewItem()

// adding a new item to the needs modal (NOT saving it)
const needsNewButton = document.getElementById("needs-new-button")
needsNewButton.onclick = function() {
    // creates a new item with inputs as fields, and save the class name
    needsNewItemClasses.push(needsModalNewItem()) 
}


// taken from Django's docs <3
function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
return "";
}
  

// the close and save button on the needs modal
const needsCloseAndSave = document.getElementById("needs-close-button")
needsCloseAndSave.onclick = function() {
    // TODO run through every input and put that info into needsPOSTRequest
    // data should look something like count, units description, and item name
    let needsPOSTRequest = [];

    const POSTRequestOptions = {
        method: 'POST', 
        headers: {'Content-Type': 'application/json',
                  "X-CSRFToken": getCookie("csrftoken"),
                  "Accept": "application/json",}, 
        // TODO this needs to be changed when the API changes to iterate through a 
        // JSON object!!
        // extra want field to avoid redundant 'want' fields in needsPOSTRequest
        body: JSON.stringify({...needsPOSTRequest[0], ...{"want": true}})
    }

    // TODO not sure how the logic should go from here down..
    // figure out how to distinguish which field belongs to which input...
    const POSTResponse = fetch('http://127.0.0.1:8000/items/manage-item/', POSTRequestOptions)
        .then(function (response) {
            return (response.json())
        })
        .then(function (data) {
            for (let i in data) {
                // TODO
                // not finished, this won't just be some massive loop!
                console.log(i)
            }
        })

    if (POSTResponse.ok) {
        // actually close the modal
        needsModal.setAttribute("closing", "");

        needsModal.addEventListener(
            "animationend",
            () => {
                needsModal.removeAttribute("closing");
                needsModal.close();
                document.body.style.overflow = "auto"
            },
            { once: true }
        );
    }
    else {
        console.log("Something went wrong, and I have no user feedback!")
    }
}






