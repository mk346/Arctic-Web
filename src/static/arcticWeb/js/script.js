// var MenuItems = document.getElementById("menu-items");

// function menutoggle(){
//     MenuItems.style.maxHeight = "0px";

//     if(MenuItems.style.maxHeight == "0px"){
//      MenuItems.style.maxHeight = "200px";
//     }
//     else{
//      MenuItems.style.maxHeight = "0px";
//     }
// }

$.ajax({
    type: 'GET',
    url: '/Hotel-Json/',
    success: function(response){
        console.log(response.data)
    },
    error: function(error){
        console.log(error)
    }
})


        