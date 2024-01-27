const locationOrOrg = document.getElementById("org");
const locationOptions = document.getElementById("location-options");

locationOrOrg.onchange = function () {
    console.log(locationOrOrg);
    if (locationOrOrg.value == "org") {
        locationOptions.style.display = "none";
    } else {
        locationOptions.style.display = "block";
    }
};
