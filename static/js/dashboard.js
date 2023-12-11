// closing and opening the needs modal
const needsModal = document.querySelector("#needs-modal") 
const needsButton = document.getElementById("needs-button")
const needsCloseButton = document.getElementById("needs-close-button")

needsButton.onclick = function() {
    needsModal.showModal()
    document.body.style.overflow = "hidden"
}

needsCloseButton.onclick = function() {
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


// adding a new item to the needs modal (NOT saving it)
const neededModalItemsList = document.getElementById("needed-items-list")
const needsNewButton = document.getElementById("needs-new-button")
let needsPOSTRequest = [];

// html for creating a new item, and rendering a 'completed' new item
const newItem = `
<div id='creating-item' class="item">
    <input id='number-of-units' type='text' value='# of units'>
    <input id='unit-type' type='text' value='units'> of 
    <input id='item-name' type='text' value='item'>
    <button id="create-item">&checkmark;</button>
</div>
`

// check for if the user is already inputting a new item
let isNewItem = false;

needsNewButton.onclick = function() {
    if (isNewItem) {
        // tell the user that they can't create multiple unsaved items
        console.log("You can't do that!")
    }
    else {
        isNewItem = !isNewItem
        neededModalItemsList.insertAdjacentHTML('beforeend', newItem)
        const createItem = document.getElementById("create-item")

        // assigning onclick func every time we create a new `newItem` div
        createItem.onclick = function() {
            isNewItem = !isNewItem;
            const numberOfUnits = document.getElementById("number-of-units").value
            const unitType = document.getElementById("unit-type").value
            const itemName = document.getElementById("item-name").value

            // TODO adding the data to the post request that we'll make when
            // the user saves the modal. to do because this isn't the correct format
            needsPOSTRequest.push(numberOfUnits, unitType, itemName)

            // deleting the old item
            const oldItem = document.getElementById("creating-item")
            oldItem.remove()

            // making the new item
            neededModalItemsList.insertAdjacentHTML('beforeend', `
                <div class="item"> ${numberOfUnits} ${unitType} of ${itemName} </div>
            `)
        }
    }
}




