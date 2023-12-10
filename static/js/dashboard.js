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

needsNewButton.onclick = function() {
    neededModalItemsList.insertAdjacentHTML('beforeend', "<div class='item'><input type='text' value='# of units'><input type='text' value='units'> of <input type='text' value='item'></div>")
}


