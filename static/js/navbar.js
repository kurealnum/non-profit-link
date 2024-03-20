const accountDropdown = document.getElementById("my-account");
const searchDropdown = document.getElementById("search");
const learnMoreDropdown = document.getElementById("learn-more");

accountDropdown.onclick = function () {
    searchDropdown.checked = false;
    learnMoreDropdown.checked = false;
};

searchDropdown.onclick = function () {
    accountDropdown.checked = false;
    learnMoreDropdown.checked = false;
};
learnMoreDropdown.onclick = function () {
    searchDropdown.checked = false;
    accountDropdown.checked = false;
};
