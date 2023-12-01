const needsButton = document.getElementById("needs-button")
const needsModal = document.getElementById("needs-modal")

needsButton.onclick = function() {
    needsModal.style.display = "block"
}

window.onclick = function(event) {
    if (event.target != needsModal) {
        needsModal.style.display = "none"
    }
}