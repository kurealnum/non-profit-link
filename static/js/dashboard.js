class BaseModal {
    constructor(openButtonName, closeButtonName, modalName) {
        this.modalName = document.getElementById(modalName);
        this.openButtonName = document.getElementById(openButtonName);
        this.openButtonName.onclick = () => this.showMyModal(this.modalName);

        this.closeButtonName = document.getElementById(closeButtonName);
        this.closeButtonName.onclick = () => this.hideMyModal(this.modalName);
    }

    showMyModal = (modal) => {
        modal.showModal();
        document.body.style.overflow = "hidden";
    };

    hideMyModal = (modal) => {
        modal.setAttribute("closing", "");
        modal.addEventListener(
            "animationend",
            () => {
                modal.removeAttribute("closing");
                modal.close();
                document.body.style.overflow = "auto";
            },
            { once: true },
        );
    };
}

class ItemModal extends BaseModal {
    constructor(isWant, needOrWant) {
        super(
            `${needOrWant}-button`,
            `${needOrWant}-close-button`,
            `${needOrWant}-modal`,
        );

        this.headersForItemApi = {
            "Content-Type": "application/json",
            "X-CSRFToken": this.getCookie("csrftoken"),
            credentials: "same-origin",
            Accept: "application/json",
        };
        this.apiUrl = "/items/manage-item/";

        this.entityMap = {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#39;",
            "/": "&#x2F;",
            "`": "&#x60;",
            "=": "&#x3D;",
        };

        this.isWant = isWant;
        this.needOrWant = needOrWant;
        this.itemCounter = 0;
        this.dashboardItemsList = document.getElementById(
            `${this.needOrWant}-items-dashboard`,
        );
        this.modalItemsList = document.getElementById(
            `${this.needOrWant}-items-list`,
        );

        this.newItemButton = document.getElementById(
            `${this.needOrWant}-new-button`,
        );
        this.newItemButton.onclick = () => this.createNewItem(this.postItem);

        this.deleteButtons = document.querySelectorAll(
            `.${this.needOrWant}.delete-item`,
        );
        for (let button of this.deleteButtons) {
            button.onclick = this.deleteItem;
        }

        this.editButtons = document.querySelectorAll(
            `.${this.needOrWant}.edit-item`,
        );
        for (let button of this.editButtons) {
            button.onclick = this.createItemToEdit;
        }
    }

    showMyModal = (modal) => {
        modal.showModal();
        document.body.style.overflow = "hidden";
    };

    hideMyModal = (modal) => {
        modal.setAttribute("closing", "");
        modal.addEventListener(
            "animationend",
            () => {
                modal.removeAttribute("closing");
                modal.close();
                document.body.style.overflow = "auto";
            },
            { once: true },
        );
    };

    // oldName exists for PUT requests
    createNewItem = (buttonFunction, oldName) => {
        this.itemCounter++;
        let oldNameData = "";
        if (oldName !== "") {
            oldNameData = "data-old_name=" + oldName;
        }
        this.modalItemsList.insertAdjacentHTML(
            "beforeend",
            `
        <div id='${this.needOrWant}-js-item-${this.itemCounter}' class="item modal-item">
            <input id='${this.needOrWant}-number-of-units-${this.itemCounter}'type='number' value='0'>
            <input id='${this.needOrWant}-unit-type-${this.itemCounter}' type='text' value='units'> of 
            <input id='${this.needOrWant}-item-name-${this.itemCounter}' type='text' value='item'>
            <button ${oldNameData} data-item_id=${this.itemCounter} id='${this.needOrWant}-create-item-${this.itemCounter}'>&check;</button>
        </div>
        `,
        );
        const newButton = document.getElementById(
            `${this.needOrWant}-create-item-` + this.itemCounter,
        );
        newButton.onclick = buttonFunction;
        return this.itemCounter;
    };

    postItem = async (event) => {
        const itemId = event.target.dataset.item_id;
        const itemName = document.getElementById(
            `${this.needOrWant}-item-name-` + itemId,
        ).value;
        const unitsDescription = document.getElementById(
            `${this.needOrWant}-unit-type-` + itemId,
        ).value;
        const numberOfUnits = document.getElementById(
            `${this.needOrWant}-number-of-units-` + itemId,
        ).value;
        const postOptions = {
            method: "POST",
            headers: this.headersForItemApi,
            body: JSON.stringify({
                item_name: itemName,
                want: this.isWant,
                units_description: unitsDescription,
                count: numberOfUnits,
                input_id: itemId,
            }),
        };
        const postReponse = await fetch(this.apiUrl, postOptions);
        if (postReponse.ok) {
            // delete input fields
            const toRemove = document.getElementById(
                `${this.needOrWant}-js-item-` + itemId,
            );
            toRemove.remove();
            // create a basic item field
            const newModalItem = `
                <div class="item modal-item">
                    <p>${numberOfUnits} ${unitsDescription} of ${itemName}</p>
                    <div class="item-buttons-wrapper">
                        <button data-name="${itemName}" class="delete-item fa-solid fa-trash" id="${this.needOrWant}-delete-item-${itemName}"></button>
                        <button data-name="${itemName}" class="edit-item fa fa-pen" id="${this.needOrWant}-edit-item-${itemName}"></button>
                    </div>
                </div>
            `;
            const newDashboardItem = `
                <div class="item modal-item" id="${this.needOrWant}-dashboard-delete-item-${itemName}">
                    ${numberOfUnits} ${unitsDescription} of ${itemName}
                </div>
            `;
            // if there were errors, but the user corrected them...
            const areErrors = document.getElementById(
                `${this.needOrWant}-modal-error-` + itemId,
            );
            if (areErrors) {
                areErrors.remove();
            }
            // render new items
            this.dashboardItemsList.insertAdjacentHTML(
                "afterbegin",
                newDashboardItem,
            );
            this.modalItemsList.insertAdjacentHTML("beforeend", newModalItem);

            // add functionality to the added buttons
            const newDeleteButton = document.getElementById(
                `${this.needOrWant}-delete-item-` + itemName,
            );
            const newEditButton = document.getElementById(
                `${this.needOrWant}-edit-item-` + itemName,
            );
            newDeleteButton.onclick = this.deleteItem;
            newEditButton.onclick = this.createItemToEdit;

            const isDashboardNotEmpty = document.getElementById(
                `${this.needOrWant}-empty`,
            );
            if (isDashboardNotEmpty) {
                isDashboardNotEmpty.remove();
            }
        } else {
            // render errors
            const errorData = await postReponse.json();
            this.renderErrors(errorData);
        }
    };

    deleteItem = async (event) => {
        const deleteButton = event.target;
        const userConfirmation = confirm(
            "Are you sure that you want to delete this item?",
        );
        if (userConfirmation) {
            const itemName = deleteButton.dataset.name;
            const deleteOptions = {
                method: "DELETE",
                headers: this.headersForItemApi,
            };
            const deleteRequest = await fetch(
                this.apiUrl + itemName + "/",
                deleteOptions,
            );
            if (deleteRequest.ok) {
                // visually remove the deleted item from the dashboard and modal
                const dashboardItem = document.getElementById(
                    `${this.needOrWant}-dashboard-delete-item-${itemName}`,
                );
                dashboardItem.remove();
                // yes we have to go up 2 parents
                deleteButton.parentElement.parentElement.remove();

                // we have to do this weird comparison because of the default "add new button" in this.dashboardItemsList
                if (this.dashboardItemsList.children.length < 1) {
                    this.dashboardItemsList.insertAdjacentHTML(
                        "afterbegin",
                        `
                        <h3 id="${this.needOrWant}-empty">You don't have any items listed!</h3>
                    `,
                    );
                }
            } else {
                // this is very unlikely to happen, so we just use an alert instead of rendering errors
                alert(
                    "Something went wrong! Please try deleting the item again.",
                );
            }
        }
    };

    createItemToEdit = (event) => {
        const oldName = event.target.dataset.name;
        this.createNewItem(this.saveEditedItem, oldName);
        const button = event.target;
        button.remove();
    };

    saveEditedItem = async (event) => {
        const editButton = event.target;
        const itemId = editButton.dataset.item_id;
        const oldItemName = editButton.dataset.old_name;
        const newItemName = document.getElementById(
            `${this.needOrWant}-item-name-` + itemId,
        ).value;
        const unitsDescription = document.getElementById(
            `${this.needOrWant}-unit-type-` + itemId,
        ).value;
        const numberOfUnits = document.getElementById(
            `${this.needOrWant}-number-of-units-` + itemId,
        ).value;
        const putOptions = {
            method: "PUT",
            headers: this.headersForItemApi,
            body: JSON.stringify({
                old_item_name: oldItemName,
                new_item_name: newItemName,
                want: this.isWant,
                units_description: unitsDescription,
                count: numberOfUnits,
                input_id: itemId,
            }),
        };
        const putResponse = await fetch(this.apiUrl, putOptions);
        if (putResponse.ok) {
            // visually update the old item's info on the dashboard and moal
            const oldDashboardElement = document.getElementById(
                `${this.needOrWant}-dashboard-delete-item-` + oldItemName,
            );
            const newItemInfo = `${numberOfUnits} ${unitsDescription} of ${newItemName}`;
            oldDashboardElement.setAttribute(
                "id",
                `${this.needOrWant}-dashboard-delete-item-` + newItemName,
            );
            oldDashboardElement.innerHTML = newItemInfo;

            editButton.parentElement.remove();

            const oldModalElement = document.getElementById(
                `${this.needOrWant}-delete-item-` + oldItemName,
            );
            oldModalElement.parentElement.parentElement.remove();

            this.modalItemsList.insertAdjacentHTML(
                "beforeend",
                `
                <div class="item modal-item">
                    <p>${newItemInfo}</p>
                    <div class="item-buttons-wrapper">
                        <button data-name="${newItemName}" class="delete-item fa-solid fa-trash" id="${this.needOrWant}-delete-item-${newItemName}"></button>
                        <button data-name="${newItemName}" class="edit-item fa fa-pen" id="${this.needOrWant}-edit-item-${newItemName}"></button>
                    </div>
                </div>
            `,
            );

            const newDeleteButton = document.getElementById(
                `${this.needOrWant}-delete-item-` + newItemName,
            );
            const newEditButton = document.getElementById(
                `${this.needOrWant}-edit-item-` + newItemName,
            );
            newDeleteButton.onclick = this.deleteItem;
            newEditButton.onclick = this.createItemToEdit;

            // if there were errors, but the user corrected them...
            const areErrors = document.getElementById(
                `${this.needOrWant}-modal-error-` + itemId,
            );
            if (areErrors) {
                areErrors.remove();
            }
        } else {
            const errorData = await putResponse.json();
            this.renderErrors(errorData);
        }
    };

    getCookie = (cname) => {
        let name = cname + "=";
        let decodedCookie = decodeURIComponent(document.cookie);
        let ca = decodedCookie.split(";");
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) == " ") {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    };

    // renders errors SPECIFICALLY for the Item API
    renderErrors = (errorData) => {
        const itemId = errorData["input_id"];
        const errors = errorData["errors"];
        let displayedErrors = "";
        for (let error of Object.keys(errors)) {
            displayedErrors += "<li>" + errors[error][0] + "</li>";
        }
        const isPresentError = document.getElementById(
            `${this.needOrWant}-modal-error-` + itemId,
        );
        // if there's not an error present already, do nothing
        if (!isPresentError) {
            const itemWithError = document.getElementById(
                `${this.needOrWant}-js-item-` + itemId,
            );
            itemWithError.insertAdjacentHTML(
                "beforebegin",
                `
                <ul id="${this.needOrWant}-modal-error-${itemId}">
                    ${displayedErrors}
                </ul>
            `,
            );
        }
    };

    escapeHtml = (string) => {
        return String(string).replace(/[&<>"'`=\/]/g, function (s) {
            return this.entityMap[s];
        });
    };
}

const needsModal = new ItemModal(true, "needs");
const surplusModal = new ItemModal(false, "surplus");
const editOrgInfoModal = new BaseModal(
    "open-edit-info",
    "default-close-edit-info",
    "edit-info-modal",
);
const editAccountInfoModal = new BaseModal(
    "open-edit-account",
    "default-close-edit-account",
    "edit-account-modal",
);

// logic for edit info modal
// code kindly taken from https://gist.github.com/lysender/a36143c002a84ed2c166bf7567b1a913
document.body.addEventListener("htmx:beforeSwap", function (event) {
    // Allow 422 and 400 responses to swap
    // We treat these as form validation errors
    if (event.detail.xhr.status === 422 || event.detail.xhr.status === 400) {
        event.detail.shouldSwap = true;
        event.detail.isError = false;
    }
});

document.addEventListener("htmx:afterRequest", function (event) {
    const editInfoReturn = event.detail.xhr.status;
    // have to check for exact code because detail.successful always evaluates to true?
    if (editInfoReturn == 201) {
        const curElement = event.detail.elt.id;
        if (curElement == "info-form") {
            editOrgInfoModal.hideMyModal(editOrgInfoModal.modalName);
        }
    }
});
