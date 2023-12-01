const needsButton = document.getElementById("needs-button")
const needsModal = document.getElementById("needs-modal")
const needsCloseButton = document.getElementById("needs-close-button")

needsButton.onclick = function() {
    needsModal.style.display = "block"
}

needsCloseButton.onclick = function() {
    needsModal.style.display = "none"
}

