const makeAnAccountButton = document.getElementById("make-an-account");
const makeAnAccountURL = makeAnAccountButton.dataset.url;
makeAnAccountButton.onclick = function () {
    location.href = makeAnAccountURL;
};

const faqButton = document.getElementById("faq-button");
const faqURL = faqButton.dataset.url;
faqButton.onclick = function () {
    location.href = faqURL;
};

console.log(faqURL, makeAnAccountURL);
