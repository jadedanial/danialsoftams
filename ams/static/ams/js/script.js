//Reset form
function resetForm(formID){

    var f = document.getElementById(formID);
    f.reset();

    var p = document.getElementsByClassName("primary-input");
    var i = document.getElementsByClassName("input-field");
    var l = document.getElementsByClassName("inner-input-label");
    var b = document.getElementsByClassName("clear-input-button");
    var m = document.getElementById("saved-message");

    for(var w = 0; w < p.length; w++){
        p[w].focus();
    }
    
    for(var x = 0; x < i.length; x++){
        i[x].value = "";
    }
    
    for(var y = 0; y < l.length; y++){
        l[y].style.color = "#55247a54";
    }

    for(var z = 0; z < b.length; z++){
        b[z].style.display = "none";
    }

    if(m.innerHTML != ""){
        m.innerHTML = "";
    }

}

//Empty input
function emptyInput(label, input, button){

    document.getElementById(input).value = "";
    document.getElementById(button).style.display = "none";
    document.getElementById(label).style.color = "#55247a54";

}

//Change focus
function changeFocus(input){

    var i = document.getElementById(input);
    i.focus();

}

//Change filter field
function changeFilter(field, dropdown){

    toggleFilter(dropdown);

    var filter = document.getElementsByClassName("filter-field");
    var f = document.getElementById(field);

    for(var x = 0; x < filter.length; x++){
        filter[x].value = "";
        filter[x].classList.add("hide-filter");
        filter[x].removeAttribute("required");
    }

    if(f){
        f.classList.remove("hide-filter");
        f.setAttribute("required", "true");
        f.focus();
    }

}

//Toggle filter
function toggleFilter(dropdown){

    var d = document.getElementById(dropdown);

    if(d.style.display === "none"){
        d.style.display = "block";
        d.focus();
    }else{
        d.style.display = "none";
    }

}

//Check current filter field to show
function checkCurrentFilter(field){

    var f = document.getElementsByClassName(field);

    for(var x = 0; x < f.length; x++){
        if(f[x].value == ""){
            f[x].classList.add("hide-filter");
        }else{
            f[x].classList.remove("hide-filter");
            f[x].setAttribute("required", "true");
        }
    }

}

//Hide element
function hideElement(element){

    var e = document.getElementById(element);
    e.style.display = "none";

}

//Show label
function showLabel(label, input, button){

    var i = document.getElementById(input);

    if(i.value != ""){
        document.getElementById(label).style.color = "#a676f1";
        document.getElementById(button).style.display = "block";
    }else{
        document.getElementById(label).style.color = "#55247a54";
        document.getElementById(button).style.display = "none";
    }

    document.getElementById(input).type = "text";
    document.getElementById(input).style.color = "#000000";

}

//Filter table
function filterTable(table, input, column){
    
    var t, i, c, f, tr, x;

    t = document.getElementById(table);
    i = document.getElementById(input);
    c = document.getElementById(column);
    f = i.value.toUpperCase();
    tr = t.getElementsByTagName("tr");
    
    for(x = 0; x < tr.length; x++){
        td = tr[x].getElementsByTagName("td")[c.value];
        if(td){
            if(td.innerHTML.toUpperCase().indexOf(f) > -1){
                tr[x].style.display = "";
            }else{
                tr[x].style.display = "none";
            }
        }
    }
} 

//Show menu
function showMenu(m){

    if(m == 1){

        document.getElementById("burger-menu").style.display = "none";
        document.getElementById("app-logo").style.display = "inline-flex";
        document.getElementById("menu-home").style.display = "block";
        document.getElementById("menu-maintenance").style.display = "none";
        document.getElementById("menu-administration").style.display = "none";
        document.getElementById("menu-reports").style.display = "none";
        document.getElementById("menu-inventory").style.display = "none";
        document.getElementById("menu-assets").style.display = "none";
        document.body.classList.add('active');

    }else if(m == "MAINTENANCE"){

        document.getElementById("menu-maintenance").style.display = "block";
        document.getElementById("menu-administration").style.display = "none";
        document.getElementById("menu-reports").style.display = "none";
        document.getElementById("menu-inventory").style.display = "none";
        document.getElementById("menu-assets").style.display = "none";

    }else if(m == "ADMINISTRATION"){

        document.getElementById("menu-maintenance").style.display = "none";
        document.getElementById("menu-administration").style.display = "block";
        document.getElementById("menu-reports").style.display = "none";
        document.getElementById("menu-inventory").style.display = "none";
        document.getElementById("menu-assets").style.display = "none";

    }else if(m == "REPORTS"){

        document.getElementById("menu-maintenance").style.display = "none";
        document.getElementById("menu-administration").style.display = "none";
        document.getElementById("menu-reports").style.display = "block";
        document.getElementById("menu-inventory").style.display = "none"; 
        document.getElementById("menu-assets").style.display = "none";   

    }else if(m == "INVENTORY"){

        document.getElementById("menu-maintenance").style.display = "none";
        document.getElementById("menu-administration").style.display = "none";
        document.getElementById("menu-reports").style.display = "none";
        document.getElementById("menu-inventory").style.display = "block";
        document.getElementById("menu-assets").style.display = "none";

    }else if(m == "ASSETS"){

        document.getElementById("menu-maintenance").style.display = "none";
        document.getElementById("menu-administration").style.display = "none";
        document.getElementById("menu-reports").style.display = "none";
        document.getElementById("menu-inventory").style.display = "none";
        document.getElementById("menu-assets").style.display = "block";
    
    }

}

//Show Password
function revealPassword(){

    var x = document.getElementById("id_password");
    var rev = document.getElementById("reveal-password-icon");

    if(x.type === "password"){
        x.type = "text";
        rev.className = "fa-solid fa-eye";
    }else{
        x.type = "password";
        rev.className = "fa-solid fa-eye-slash";
    }

}