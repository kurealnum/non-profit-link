// GLOBAL
const headersForItemApi = {'Content-Type': 'application/json',
                    "X-CSRFToken": getCookie("csrftoken"),
                    "Accept": "application/json",}

// these are the "buckets" in the eraser.io diagrams
let needsPostBucket = new Set(); // item Ids
let needsDeleteBucket = new Set() // item names



// NEEDS MODAL
const needsModal = document.querySelector("#needs-modal") 
const needsButton = document.getElementById("needs-button")

// showing the modal
needsButton.onclick = function() {
    needsModal.showModal()
    document.body.style.overflow = "hidden"
}

// adding a new item to the needs modal (NOT saving it)
const needsNewButton = document.getElementById("needs-new-button")
const needsModalNewItem = createNewItem()
needsNewButton.onclick = function() {
    // creates a new item with inputs as fields, and saves the class name
    needsPostBucket.add(needsModalNewItem()) 
}

// delete items buttons
const deleteButtons = document.getElementsByClassName("delete-item")
for (let button of deleteButtons) {
    button.onclick = deleteItem
}  

function deleteItem(event) {
    const deleteButton = event.target
    // TODO ask the user if they're sure they want to delete the item
    // add data to needsDeleteBucket
    let itemName = deleteButton.dataset.name
    needsDeleteBucket.add(itemName)

    // delete item in modal, and delete 
    deleteButton.parentElement.remove()
}

// Close and Save button on needsModal
const needsCloseAndSaveButton = document.getElementById("needs-close-button")
needsCloseAndSaveButton.onclick = function() {
    async function createItems() {
        let needsPOSTRequestInfo = [];
        /* 
        data in needsPOSTRequestInfo should look something like this:
        count: 3
        units_description: "verycool"
        item_name: "myitem"
        input_id: 2  (input id is to identify which input to assign errors to (if there are any))
        */ 

        // gathering data for needsPOSTRequestInfo 
        // TODO is there a more JS way to do this?
        for (let counter of needsPostBucket) {
            const item_name = document.querySelector("#item-name-" + counter).value
            const units_description = document.querySelector("#unit-type-" + counter).value
            const count = document.querySelector("#number-of-units-" + counter).value
            const addedItem = {
                "item_name": escapeHtml(item_name),
                "units_description": escapeHtml(units_description),
                "count": count,
                "input_id": counter,
            }
            needsPOSTRequestInfo.push(addedItem)
        }

        const POSTRequestOptions = {
            method: 'POST', 
            headers: headersForItemApi, 
            // extra want field to avoid redundant 'want' fields in needsPOSTRequestInfo
            body: JSON.stringify({needsPOSTRequestInfo, ...{"want": true}})
        }

        // figure out how to distinguish which field belongs to which input...
        const POSTResponse = await fetch('http://127.0.0.1:8000/items/manage-item/', POSTRequestOptions)
            if (POSTResponse.status == 201) {
                // visually add new items to dashboard, and remove old input fields
                const neededDashboardItemsList = document.getElementById("needed-items-dashboard")
                const neededModalItemsList = document.getElementById("needed-items-list")
                // render and delete items
                for (let itemInfo of needsPOSTRequestInfo) {
                    // don't need to escape HTML because we already escaped it
                    const newModalItem = `
                        <div class="item">
                            ${itemInfo["count"]} ${itemInfo["units_description"]} of ${itemInfo["item_name"]}
                            <button data-name="${itemInfo["item_name"]}" class="delete-item" id="delete-item-js-${itemInfo["item_name"]}"></button>
                        </div>
                    `
                    const newDashboardItem = `
                    <div class="item" id="delete-item-${itemInfo["item_name"]}">
                        ${itemInfo["count"]} ${itemInfo["units_description"]} of ${itemInfo["item_name"]}
                    </div>
                    `
                    neededDashboardItemsList.insertAdjacentHTML('beforeend', newDashboardItem)
                    neededModalItemsList.insertAdjacentHTML('beforeend', newModalItem)

                    // adding delete method to new delete button
                    document.getElementById("delete-item-js-" + itemInfo["item_name"]).onclick = deleteItem

                    // removing old input fields
                    const oldInputField = document.getElementById("js-item-" + itemInfo["input_id"])
                    oldInputField.remove()
                }
                // set the post bucket to empty for when the modal is reopened
                needsPostBucket = new Set()
            }
            else {
                // user feedback, i.e. making errors and displaying them
                // the input_id is used to figure out which item had an error
                const POSTResponseData = await POSTResponse.json()
                // we know that error messages is safe, because the response is from our own API
                for (let errors of POSTResponseData) {
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

                    const isPresentError = document.getElementById("modal-error-" + inputId)
                    // if there's not an error present already, do nothing
                    if (!isPresentError) {
                        itemWithError.insertAdjacentHTML('beforebegin', `
                            <ul id="modal-error-${inputId}">
                                ${errorMessages}
                            </ul>
                        `)
                    }
                } 
            }        
        }
    // worth noting that there's almost no way that there can be any errors with this api call
    async function deleteItems() {
        const needsDeleteRequestOptions = {
            method: 'DELETE', 
            headers: headersForItemApi, 
            body: JSON.stringify({"item_names": Array.from(needsDeleteBucket)}) 
        }
        const deleteResponse = await fetch('http://127.0.0.1:8000/items/manage-item/', needsDeleteRequestOptions)
        if (deleteResponse.ok) {
            // remove items from dashboard
            for (let item of needsDeleteBucket) {
                const toDelete = document.getElementById("delete-item-" + item)
                toDelete.remove()
            }
            // set needsDeleteBucket to empty
            needsDeleteBucket = new Set()
            return true
        }
        else {
            return false
        }
    }
    // if there are no issues with managing the items, close the modal
    const didDelete = deleteItems()
    const didCreate = createItems()
    if (didDelete && didCreate) {
        // close the modal
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
}
  


// SURPLUS MODAL
const surplusModal = document.querySelector('#surplus-modal')
const surplusOpenButton = document.getElementById("surplus-button")
const surplusCloseButton = document.getElementById("surplus-close-button")

surplusOpenButton.onclick = function() {
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



// HELPER FUNCTIONS
// function for rendering a new item with inputs instead of fields; uses closure
function createNewItem(){
    const neededModalItemsList = document.getElementById("needed-items-list")
    let itemCounter = 0
    return function () {
        itemCounter++
        // TODO need to rewrite this function to allow itemCounter to be an itemName
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

// function to get a certain cookie, taken from Django's docs <3
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
    
// function to escape potentially dangerous HTML chars
var entityMap = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;',
    '/': '&#x2F;',
    '`': '&#x60;',
    '=': '&#x3D;'
  };
  
  function escapeHtml (string) {
    return String(string).replace(/[&<>"'`=\/]/g, function (s) {
      return entityMap[s];
    });
  }





