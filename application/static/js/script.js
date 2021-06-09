// getting all required elements
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");
const icon = searchWrapper.querySelector(".icon");
let linkTag = searchWrapper.querySelector("a");
let webLink;

// if user press any key and release
inputBox.onkeyup = (e)=>{
    let userData = e.target.value; //user enetered data
    let emptyArray = [];
    if(userData){
        icon.onclick = ()=>{
            webLink = "https://www.google.com/search?q=IT+jobs+in" + userData;//searching user entered data can be changed to take user to any page (for now a google search).
            linkTag.setAttribute("href", webLink);
            console.log(webLink);
            linkTag.click();
        }
        emptyArray = suggestions.filter((data)=>{
            //filtering array value and user characters to lowercase and return only those words which are start with user enetered chars
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });
        emptyArray = emptyArray.map((data)=>{
            // passing return data inside li tag
            return data = '<li>'+ data +'</li>';
        });
        searchWrapper.classList.add("active"); //show autocomplete box
        showSuggestions(emptyArray);
        let allList = suggBox.querySelectorAll("li");
        for (let i = 0; i < allList.length; i++) {
            //adding onclick attribute in all li tag
            allList[i].setAttribute("onclick", "select(this)");
        }
    }else{
        searchWrapper.classList.remove("active"); //hide autocomplete box
    }
}

function select(element){
    let selectData = element.textContent;
    inputBox.value = selectData;
    icon.onclick = ()=>{
        webLink = "https://www.google.com/search?q=IT+jobs+in+" + selectData; //selecting from drop down can be changed to take user to any page for now a google search.
        linkTag.setAttribute("href", webLink);
        linkTag.click();
    }
    searchWrapper.classList.remove("active");
}

function showSuggestions(list){
    let listData;
    if(!list.length){
        userValue = inputBox.value;
        listData = '<li>'+ userValue +'</li>';
    }else{
        listData = list.join('');
    }
    suggBox.innerHTML = listData;
}

/*Enabling the location CV functionality */
inputBoxL.onkeyup = (e) => {
    let userData = e.target.value; //user enetered data
    let emptyArray = [];
    if (userData) {
        iconL.onclick = () => {
            webLinkL = "https://www.google.com/search?q=" + userData;//searching user entered data can be changed to take user to any page (for now a google search).
            linkTagL.setAttribute("href", webLinkL);
            console.log(webLinkL);
            linkTagL.click();
        }
        emptyArray = locations_suggestions.filter((data) => {
            //filtering array value and user characters to lowercase and return only those words which are start with user enetered chars
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });
        emptyArray = emptyArray.map((data) => {
            // passing return data inside li tag
            return data = '<li>' + data + '</li>';
        });
        searchWrapperL.classList.add("active"); //show autocomplete box
        showSuggestionsL(emptyArray);
        let allList = suggBoxL.querySelectorAll("li");
        for (let i = 0; i < allList.length; i++) {
            //adding onclick attribute in all li tag
            allList[i].setAttribute("onclick", "selectL(this)");
        }
    } else {
        searchWrapperL.classList.remove("active"); //hide autocomplete box
    }
}


function selectL(element) {
    let selectData = element.textContent;
    inputBoxL.value = selectData;
    iconL.onclick = () => {
        webLinkL = "https://www.google.com/search?q=" + selectData; //selecting from drop down can be changed to take user to any page for now a google search.
        linkTagL.setAttribute("href", webLinkL);
        linkTagL.click();
    }
    searchWrapperL.classList.remove("active");
}

function showSuggestionsL(list) {
    let listData;
    if (!list.length) {
        userValue = inputBoxL.value;
        listData = '<li>' + userValue + '</li>';
    } else {
        listData = list.join('');
    }
    suggBoxL.innerHTML = listData;
}
