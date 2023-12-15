$(document).ready(function () {



    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');

    }

    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#Siriwave").attr("hidden", true);
    }

});