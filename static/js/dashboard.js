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



