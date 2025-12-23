// jQuery - a library, design for DOM traversal,
//manipulation, event-handling, animations, Ajax.

//cdn - content delivery network, syntax

//syntax
// $ - alias
//jQuery

// const $elementFromDOM = $('.classname') // classname
// const $elementFromDOM = $('#idname') // for idname
// // const $elementFromDOM = $('tagname') // for tagname

// $()

// const $firstptag = $("p")

// $firstptag.hide();

//select an item

let $article = $("#firstarticle");
console.log($article);

//add event handler/listen - on("event to listen", callbackfn)
//on()
let $btn = $("button");
$btn.on("click", () => {
    $article.toggleClass("hidden");

    // if($article.is(":visible")){
    //    $btn.text("Hide")
    // }else {
    //     $btn.text("Show")
    // }

    $btn.text(
        $article.hasClass("hidden")? "Show": "Hide"
    )
})

//animations
//fade, slude

let $header = $(".header");

$header.on("mouseover", function(){
    $header.text("We have changed this text from jQuery");
    $header.css('font-style','italic')
}).on("mouseout", () =>{
    $header.text("Welcome to WIT 2025 Fall Cohort");
    $header.css({
        color : 'red',
        "background-color" : "lightgrey"
    })
})

// $header.hover()
//    function(){
//     $header.text("We have changed this text from jQuery");
//     $header.css('font-style','italic')
//}
//       function(){
//         $header.text("We have changed this text from jQuery");
//         $header.css('font-style','bold')
//       }


// fadeIn, fadeOut, fadeToggle "slow", "fast", "3000", slidein, slideout, toggle

// $("#laughing").on("click", ()=>{
//     $(".haha").fadeToggle();

// })

// $("#laughing").on("click", ()=>{
//     $(".haha").slideUp();

// })

// $("#laughing").on("click", ()=>{
//     $(".haha").slideDown();

// })

$("#laughing").on("click", ()=>{
    $(".haha").slideToggle();

})


//addclass, removeclass
$("#aside").on("click", ()=>{
    $("section").addClass("asidesection")
})

//removeclass

//siblings, children, documents.ready, event.currenttarget, find, closest

//silings -  acccess sibling element and perform opertations on the siblings

$("h1").siblings().on("click", (event) =>{
    $(event.currentTarget).css("color", "red")
    console.log("current target is", event.currentTarget)
})

//children 
$("section").children().css("background-color", "pink")

//parent
$("aside").parent().css("border", "2px solid green")

//document.ready()
$(document).ready(() =>{

})

//window.onload =function(){
// }

//find 
$(".parentSection").find("detials").css("color","green")