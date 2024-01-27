const locationOrOrg = document.getElementById("org");
const locationOptions = document.getElementById("location-options");

const showAndHideDropDowns = () => {
    if (locationOrOrg.value == "org") {
        locationOptions.style.display = "none";
    } else {
        locationOptions.style.display = "block";
    }
};

// when the page loads
showAndHideDropDowns();

locationOrOrg.onchange = showAndHideDropDowns;
