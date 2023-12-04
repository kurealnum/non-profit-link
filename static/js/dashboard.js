const needsButton = document.getElementById("needs-button")
const needsModal = document.getElementById("needs-modal")
const needsCloseButton = document.getElementById("needs-close-button")
const modalBlur = document.getElementById("needs-modal-blur")

needsButton.onclick = function() {
    document.documentElement.style.overflow = "hidden"
    modalBlur.style.display = "block"
    needsModal.style.display = "flex"
}

needsCloseButton.onclick = function() {
    needsModal.style.display = "none"
    modalBlur.style.display = "none"
    document.documentElement.style.overflow = "auto"
}

