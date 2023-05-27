// Animacion descripcion destacado

let descripcionDestacado = $('#descripcion-destacado');

$(document).ready(function() { animacionDescripcionDestacado() });

$(window).scroll(function () { animacionDescripcionDestacado() });

function animacionDescripcionDestacado() {
    var elementPos = descripcionDestacado.offset().top;
    var scrollPos = $(window).scrollTop();
    var windowHeight = $(window).height();
    if (elementPos < (scrollPos + windowHeight - 300)) {
        descripcionDestacado.addClass('texto-animado');
    }else {
        descripcionDestacado.removeClass('texto-animado');
    }
}