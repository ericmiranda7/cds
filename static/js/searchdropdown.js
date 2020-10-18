/* // DROPDOWN JS
stateSearch = document.querySelector('.state');
stateSearch.addEventListener('focusout', removeCities)

function removeCities() {
    citySearch = document.querySelector('.city');
    for (let i = 0; i < citySearch.options.length; i++) {
        if (citySearch.options[i].value == stateSearch.value) {
            citySearch.options[i].disabled = false;
        } else {
            citySearch.options[i].disabled = true;
        }
    }
    console.log(citySearch)
} */

document.onload(initName);

function initName() {
    
}