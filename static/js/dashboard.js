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
        <div id='js-item-${itemCounter}' class="item">
            <input id='number-of-units-${itemCounter}'type='number' value='0'>
            <input id='unit-type-${itemCounter}' type='text' value='units'> of 
            <input id='item-name-${itemCounter}' type='text' value='item'>
        </div>
        `)
        return itemCounter
    }
}


// these are the "buckets" in the eraser.io diagrams
let needsItemIndexes = [];
// this func uses closure (i think thats what its called)
const needsModalNewItem = createNewItem()

// adding a new item to the needs modal (NOT saving it)
const needsNewButton = document.getElementById("needs-new-button")
needsNewButton.onclick = function() {
    // creates a new item with inputs as fields, and save the class name
    needsItemIndexes.push(needsModalNewItem()) 
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
    async function createItems() {
        // data should look something like count, units description, and item name
        let needsPOSTRequest = [];

        // gathering data for needsPOSTRequest 
        // TODO is there a more JS way to do this?
        for (let counter of needsItemIndexes) {
            const item_name = document.querySelector("#item-name-" + counter).value
            const units_description = document.querySelector("#unit-type-" + counter).value
            const count = document.querySelector("#number-of-units-" + counter).value
            const addedItem = {
                "item_name": item_name,
                "units_description": units_description,
                "count": count,
                // input id is to identify which input to assign errors to (if there are any)
                "input_id": counter,
            }
            needsPOSTRequest.push(addedItem)
        }

        const POSTRequestOptions = {
            method: 'POST', 
            headers: {'Content-Type': 'application/json',
                    "X-CSRFToken": getCookie("csrftoken"),
                    "Accept": "application/json",}, 
            // extra want field to avoid redundant 'want' fields in needsPOSTRequest
            body: JSON.stringify({needsPOSTRequest, ...{"want": true}})
        }

        // figure out how to distinguish which field belongs to which input...
        const POSTResponse = await fetch('http://127.0.0.1:8000/items/manage-item/', POSTRequestOptions)
            if (POSTResponse.status == 201) {
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
                const POSTResponseData = await POSTResponse.json()
                for (let errors of POSTResponseData) {
                    // getting the input id, then going thru errors
                    const inputId = errors[1]["input_id"]
                    const itemWithError = document.getElementById("js-item-" + inputId)
                    const rawErrorMessages = errors[0]
                    let errorMessages = ""
                    for (let key in rawErrorMessages) {
                        errorMessages += "<li>" + rawErrorMessages[key][0] + "</li>"
                    }
                    // TODO not sure why this reduce func isnt working :(
                        // just using a for loop to populate error messages atm
                    // const errorMessages = Object.keys(rawErrorMessages).reduce(
                    //     (allErrors, curError) => allErrors += ("<li>" + "a" + "</li>"))
                    itemWithError.insertAdjacentHTML('beforebegin', `
                        <ul>
                            ${errorMessages}
                        </ul>
                    `)
                } 
            }        
        }
    createItems()
}
        
    






