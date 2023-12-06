const needsButton = document.getElementById("needs-button")
const needsModal = document.querySelector("#needs-modal") //is a dialog element
const needsCloseButton = document.getElementById("needs-close-button")

needsButton.onclick = function() {
    needsModal.showModal()
}

needsCloseButton.onclick = function() {
    needsModal.setAttribute("closing", "");

    needsModal.addEventListener(
        "animationend",
        () => {
            needsModal.removeAttribute("closing");
            needsModal.close();
        },
        { once: true }
    );
}

