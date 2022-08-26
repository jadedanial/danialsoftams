//Empty input
function emptyInput(label, input, button, status){

    document.getElementById(input).value = "";
    document.getElementById(button).style.display = "none"

    if(status == "normal"){
        document.getElementById(label).style.color = "#a676f1";
    }else{
        document.getElementById(label).style.color = "#55247a54";
    }

    var i = document.getElementById(input);

    if(i.tagName === "SELECT"){
        i.classList.remove("advance-search-select-hide-arrow");
    }

}

//Change focus
function changeFocus(label, input, element, string){

    var i = document.getElementById(input);
    i.focus();

    if(string != ""){
        var m = document.getElementById(label);
        var n = document.getElementById(element);
        if(n.tagName.toLowerCase() === "select"){
            var text= n.options[n.selectedIndex].text;
            m.innerHTML = string + text;
        }
    }

}

//Show label
function showLabel(label, input, button, elementID, status){

    var i = document.getElementById(input);

    if(i.value != ""){
        if(i.tagName.toLowerCase() === "select"){
            if(elementID == "Employee Shift Group"){
                for(var x = 0; x < i.length; x++){
                    var tableShow = document.getElementsByClassName(i[x].innerHTML);
                    for(var y = 0; y < tableShow.length; y++){
                        tableShow[y].style.display = "";
                    }
                    if(i.value != "Show All"){
                        if(i.value != i[x].innerHTML){
                            for(var z = 0; z < tableShow.length; z++){
                                tableShow[z].style.display = "none";
                            }
                        }
                    }
                }
            }
        }
        document.getElementById(label).style.color = "#a676f1";
        document.getElementById(button).style.display = "block";
    }else{
        if(status == ""){
            document.getElementById(label).style.color = "#55247a54";
            document.getElementById(button).style.display = "none";
        }
    }

    document.getElementById(input).type = "text";
    document.getElementById(input).style.color = "#000000";
    document.getElementById(input).classList.add("advance-search-select-hide-arrow");
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

        document.getElementById("chevron-menu").style.display = "none";
        document.getElementById("app-logo").style.display = "inline-flex";
        document.getElementById("menu-home").style.display = "block";
        document.getElementById("menu-maintenance").style.display = "none";
        document.getElementById("menu-administration").style.display = "none";
        document.getElementById("menu-reports").style.display = "none";
        document.getElementById("menu-inventory").style.display = "none";
        document.getElementById("menu-assets").style.display = "none";
        document.body.classList.add('active');
        document.getElementById("chevleft").className = "fas fa-chevron-right";

    }else if(m == 2){

        document.getElementById("menu-maintenance").style.display = "block";
        document.getElementById("menu-administration").style.display = "none";
        document.getElementById("menu-reports").style.display = "none";
        document.getElementById("menu-inventory").style.display = "none";
        document.getElementById("menu-assets").style.display = "none";

    }else if(m == 3){

        document.getElementById("menu-maintenance").style.display = "none";
        document.getElementById("menu-administration").style.display = "block";
        document.getElementById("menu-reports").style.display = "none";
        document.getElementById("menu-inventory").style.display = "none";
        document.getElementById("menu-assets").style.display = "none";

    }else if(m == 4){

        document.getElementById("menu-maintenance").style.display = "none";
        document.getElementById("menu-administration").style.display = "none";
        document.getElementById("menu-reports").style.display = "block";
        document.getElementById("menu-inventory").style.display = "none"; 
        document.getElementById("menu-assets").style.display = "none";   

    }else if(m == 5){

        document.getElementById("menu-maintenance").style.display = "none";
        document.getElementById("menu-administration").style.display = "none";
        document.getElementById("menu-reports").style.display = "none";
        document.getElementById("menu-inventory").style.display = "block";
        document.getElementById("menu-assets").style.display = "none";

    }else if(m == 6){

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

//Export to Excel file
function exportToExcel(table){

    TableToExcel.convert(document.getElementById(table), {
        name: "Schedule.xlsx",
        sheet: {
            name: "Schedule"
        }
      });

}