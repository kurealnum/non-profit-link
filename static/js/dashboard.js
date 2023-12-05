const needsButton = document.getElementById("needs-button")
const needsModal = document.querySelector("#needs-modal") //is a dialog element
const needsCloseButton = document.getElementById("needs-close-button")
const modalBlur = document.getElementById("needs-modal-blur")

needsButton.onclick = function() {
    needsModal.showModal()
}

needsCloseButton.onclick = function() {
    needsModal.close()
}

