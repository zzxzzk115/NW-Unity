$(document).keyup(function(event) {
    switch (event.keyCode) {
    //ESC ASCII 27
    case 27:
        nw.App.closeAllWindows();
    }
});