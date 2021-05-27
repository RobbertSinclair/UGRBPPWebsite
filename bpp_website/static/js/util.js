$(document).ready(function() {
    window.scrollTo(0, -50);
    $(".back-to-top").hide();

    $(window).scroll(function() {
        var max_scroll = 100;
        if ($(this).scrollTop() > max_scroll) {
            $(".back-to-top").show();
        } else {
            $(".back-to-top").hide();
        }
    });
});