// GLOBAL
const headersForItemApi = {'Content-Type': 'application/json',
                    "X-CSRFToken": getCookie("csrftoken"),
                    "Accept": "application/json",}
const apiUrl = "http://127.0.0.1:8000/items/manage-item/"
const neededDashboardItemsList = document.getElementById("needed-items-dashboard")
const neededModalItemsList = document.getElementById("needed-items-list")



// NEEDS MODAL
const needsModal = document.querySelector("#needs-modal") 
const needsButton = document.getElementById("needs-button")

// showing the modal
needsButton.onclick = function() {
    needsModal.showModal()
    document.body.style.overflow = "hidden"
}

// POST request logic for Needs Modal
const needsNewButton = document.getElementById("needs-new-button")
const needsModalNewItem = createNewItem()
needsNewButton.onclick = createItem

// creates a new item with inputs as fields, and saves the class name
function createItem() {
    needsModalNewItem(postItem)
}

// function for rendering a new item with inputs instead of fields; uses closure
function createNewItem(){
    const neededModalItemsList = document.getElementById("needed-items-list")
    let itemCounter = 0
    return function (buttonFunction, oldName) {
        itemCounter++
        let oldNameData = ""
        console.log("a")
        if (oldName !== "") {
            console.log("b")
            oldNameData = "data-old_name=" + oldName
        }
        neededModalItemsList.insertAdjacentHTML('beforeend', `
        <div id='js-item-${itemCounter}' class="item">
            <input id='number-of-units-${itemCounter}'type='number' value='0'>
            <input id='unit-type-${itemCounter}' type='text' value='units'> of 
            <input id='item-name-${itemCounter}' type='text' value='item'>
            <button ${oldNameData} data-item_id=${itemCounter} id='create-item-${itemCounter}'>&check;</button>
        </div>
        `)
        const newButton = document.getElementById("create-item-" + itemCounter)
        newButton.onclick = buttonFunction
        return itemCounter
    }
}

// makes post req to Item API
async function postItem(event) {
    const itemId = event.target.dataset.item_id
    const itemName = document.getElementById('item-name-' + itemId).value
    const unitsDescription = document.getElementById('unit-type-' + itemId).value
    const numberOfUnits = document.getElementById('number-of-units-' + itemId).value
    const postOptions = {
        method: 'POST',
        headers: headersForItemApi,
        // adding the 'want' field
        body: JSON.stringify({"item_name": itemName, "want": true, "units_description": unitsDescription, "count": numberOfUnits, "input_id": itemId})
    }
    const postReponse = await fetch(apiUrl, postOptions)
    if (postReponse.ok) {
        // delete input fields 
        const toRemove = document.getElementById("js-item-" + itemId)
        toRemove.remove()
        // create a basic item field
        const newModalItem = `
            <div class="item">
                ${numberOfUnits} ${unitsDescription} of ${itemName}
                <button data-name="${itemName}" class="delete-item" id="delete-item-${itemName}"></button>
            </div>
        `
        const newDashboardItem = `
            <div class="item" id="dashboard-delete-item-${itemName}">
                ${numberOfUnits} ${unitsDescription} of ${itemName}
                <button data-name="${itemName}" class="delete-item" id="delete-item-${itemName}"></button>
            </div>
        `
        // if there were errors, but the user corrected them...
        const areErrors = document.getElementById("modal-error-" + itemId)
        if (areErrors) {
            areErrors.remove()
        }
        // render new items
        neededDashboardItemsList.insertAdjacentHTML('beforeend', newDashboardItem)
        neededModalItemsList.insertAdjacentHTML('beforeend', newModalItem)
        // add functionality to the added button
        const newButton = document.getElementById("delete-item-" + itemName)
        newButton.onclick = deleteItem()
    }
    else {
        // render errors
        const errorData = await postReponse.json()
        const itemId = errorData["input_id"]
        const errors = errorData["errors"]
        let displayedErrors = ""
        for (let error of Object.keys(errors)) {
            displayedErrors += "<li>" + errors[error][0] + "</li>"
        }
        const isPresentError = document.getElementById("modal-error-" + itemId)
        // if there's not an error present already, do nothing
        if (!isPresentError) {
            const itemWithError = document.getElementById("js-item-" + itemId)
            itemWithError.insertAdjacentHTML('beforebegin', `
                <ul id="modal-error-${itemId}">
                    ${displayedErrors}
                </ul>
            `)
        }
    }
}

// DELETE request logic for Needs Modal
const deleteButtons = document.getElementsByClassName("delete-item")
for (let button of deleteButtons) {
    button.onclick = deleteItem
}  

// deletes an item
async function deleteItem(event) {
    const deleteButton = event.target
    // TODO ask the user if they're sure they want to delete the item
    // api request
    const itemName = deleteButton.dataset.name
    const deleteOptions = {
        method: 'DELETE',
        headers: headersForItemApi
    }
    const deleteRequest = await fetch(apiUrl + itemName + "/", deleteOptions)
    if (deleteRequest.ok) {
        // delete item in modal
        const dashboardItem = document.getElementById("dashboard-delete-item-" + itemName)
        dashboardItem.remove()
        // removing the modal element
        deleteButton.parentElement.remove()
    }
    else {
        // TODO there should be no way for a delete request to fail, but still
        console.log("Issue with POST request")
    }
}

// PUT request logic for modal
const editButtons = document.getElementsByClassName("edit-item")
for (let button of editButtons) {
    button.onclick = createItemToEdit
}

function createItemToEdit(event) {
    const button = event.target
    const oldName = event.target.dataset.name
    needsModalNewItem(saveEditedItem, oldName)
    button.remove()
}

async function saveEditedItem(event) {
    const itemId = event.target.dataset.item_id
    const oldItemName = event.target.dataset.old_name
    const newItemName = document.getElementById('item-name-' + itemId).value
    const unitsDescription = document.getElementById('unit-type-' + itemId).value
    const numberOfUnits = document.getElementById('number-of-units-' + itemId).value
    const putOptions = {
        method: 'PUT',
        headers: headersForItemApi,
        body: JSON.stringify({"old_item_name": oldItemName, "new_item_name": newItemName, "want": true, "units_description": unitsDescription, "count": numberOfUnits, "input_id": itemId}),
    }
    const putResponse = await fetch(apiUrl, putOptions)
    if (putResponse.ok) {
        // TODO update the item info in dashboard
        // TODO delete the input fields
        // TODO create a new .item div with updated info in modal
        console.log("success!")
    }
    else {
        // TODO there should be no way for a delete request to fail, but still
        console.log("Issue with PUT request")
    }
}

// Close and Save button on needsModal
const needsCloseAndSaveButton = document.getElementById("needs-close-button")
needsCloseAndSaveButton.onclick = function() {
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
    )
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
  
function escapeHtml(string) {
    return String(string).replace(/[&<>"'`=\/]/g, function (s) {
      return entityMap[s];
    });
}





