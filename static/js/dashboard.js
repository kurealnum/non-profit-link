const needsButton = document.getElementById("needs-button")
const needsModal = document.getElementById("needs-modal")
const needsCloseButton = document.getElementById("needs-close-button")
const modalBlur = document.getElementById("needs-modal-blur")

needsButton.onclick = function() {
    document.documentElement.style.overflow = "hidden"
    modalBlur.style.display = "block"
    needsModal.style.display = "flex"

    // transition in
    window.setTimeout(function(){
        modalBlur.style.opacity = 1
        needsModal.style.opacity = 1
      },0);
}

needsCloseButton.onclick = function() {
    document.documentElement.style.overflow = "auto"
    modalBlur.style.opacity = 0
    needsModal.style.opacity = 0

    // transition out
    window.setTimeout(() => {
        modalBlur.style.display = "none"
        needsModal.style.display = "none"
    }, 700)
}

