$(document).ready(function (){
    let initialTime =10;
    

    function startCountDownFunc(){

        if (initialTime > 0){
            $("#countdown").text(initialTime)
            initialTime--;
            setTimeout(startCountDownFunc, 1000)
        } else{
            $("#countdown").text("Time is up!")
        }
    }
$("#startCountDown").on("click", function(){

    initialTime = 10;
    startCountDownFunc()
})
})