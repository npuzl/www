$(function () {
    $(".inactive").click(function () {
        $(this).removeClass("inactive");
        $(this).addClass("active");
        $(this).siblings().removeClass("active");
        $(this).siblings().addClass("inactive");

    });
    $(".active").click(function () {
        $(this).removeClass("inactive");
        $(this).addClass("active");
        $(this).siblings().removeClass("active");
        $(this).siblings().addClass("inactive");

    });
});
/*
function changeaction() {
    document.formAction.action="http://api.map.baidu.com/place/v2/search?query=ATM机&tag=银行&region=北京&output=json&ak=OjBcT6tnCAVLvvW72G7YRqeV6atemrwp"
}
changeaction();*/