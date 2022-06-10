// $('.sll1').owlCarousel({
//     items:6,
//     loop:true,
//     margin:50,
//     autoplay:true,
//     autoplayTimeout:2000,
//     autoplayHoverPause:true,
// });

if ($(window).width() < 321) {
    $('.sll1').owlCarousel({
        items:3,
        loop:true,
        margin:20,
        autoplay:true,
        autoplayTimeout:2000,
        autoplayHoverPause:true,
    });
}else if($(window).width() < 650 && $(window).width() > 322){
    $('.sll1').owlCarousel({
        items:4,
        loop:true,
        margin:50,
        autoplay:true,
        autoplayTimeout:2000,
        autoplayHoverPause:true,
    });
}else if($(window).width() < 700 && $(window).width() > 649){
    $('.sll1').owlCarousel({
        items:5,
        loop:true,
        margin:50,
        autoplay:true,
        autoplayTimeout:2000,
        autoplayHoverPause:true,
    });
}else if($(window).width() > 700){
    $('.sll1').owlCarousel({
        items:5,
        loop:true,
        margin:50,
        autoplay:true,
        autoplayTimeout:2000,
        autoplayHoverPause:true,
    });
}