const needsButton = document.getElementById("needs-button")
const needsModal = document.getElementById("needs-modal")
const needsCloseButton = document.getElementById("needs-close-button")
const modalBlur = document.getElementById("needs-modal-blur")

needsButton.onclick = function() {
    document.documentElement.style.overflow = "hidden"
    modalBlur.style.visibility = "visible"
    needsModal.style.display = "flex"
}

needsCloseButton.onclick = function() {
    needsModal.style.display = "none"
    modalBlur.style.visibility = "hidden"
    document.documentElement.style.overflow = "auto"
}

