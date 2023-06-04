// Cambio de color de la cabecera al hacer scroll

let anchoPagina = window.innerWidth;

$(window).resize(function () {
    anchoPagina = window.innerWidth;
    if (anchoPagina <= 480 && $('#cabecera').hasClass('cabecera-onScroll')) {
        $('#cabecera').removeClass('cabecera-onScroll');
    } else if (anchoPagina > 480 && window.scrollY > 0) {
        $('#cabecera').addClass('cabecera-onScroll');
    }
});

$(window).scroll(function (event) {
    if (anchoPagina <= 480) return
    let separacion = $(this).scrollTop();
    if (separacion > 0) {
        $('#cabecera').addClass('cabecera-onScroll');
    } else {
        $('#cabecera').removeClass('cabecera-onScroll');
    }
});


// Animacion del logo al hacer un hover

let letterWrapClass = 'logo-animado';
let letterWrapElements = document.getElementsByClassName(letterWrapClass);

[...letterWrapElements].forEach(el => {
    letterWrap(el, letterWrapClass);
    letterAnimation(el, letterWrapClass);
});



function letterWrap(el, cls) {
    let words = el.textContent.split(' ');
    let letters = [];

    cls = cls || 'logo-animado'

    words.forEach(word => {
        let html = '';
        for (var letter in word) {
            html += `
                <span class="${cls}__caracter">
                <span class="${cls}__caracter-interior" letra="${word[letter]}">
                    ${word[letter]}
                </span>
                </span>
            `;
        };

        let wrappedWords = `<span class="${cls}__palabra">${html}</span>`;
        letters.push(wrappedWords);
    });

    return el.innerHTML = letters.join(' ');
}

function letterAnimation(el, cls) {
    let tl = new TimelineMax({ paused: true });
    let characters = el.querySelectorAll(`.${cls}__caracter-interior`);
    let duration = el.hasAttribute('data-duration') ? el.dataset.duration : 0.3;
    let stagger = el.hasAttribute('data-stagger') ? el.dataset.stagger : 0.03;

    el.animation = tl.staggerTo(characters, duration, {
        y: '-100%',
        ease: Power4.easeOut
    }, stagger);

    el.addEventListener('mouseenter', (event) => {

        event.currentTarget.animation.play();

    }
    );
    el.addEventListener('mouseout', (event) => el.animation.reverse());
}


// Desplegar el modal de busqueda

let modalBusqueda = $('#modal-busqueda');

$('#boton-busqueda').on('click', function () {
    console.log(modalBusqueda);
    modalBusqueda.show();
    $('body').css('overflow', 'hidden');
});

$('#boton-cerrar-modal-busqueda').on('click', function () {
    modalBusqueda.hide();
    $('body').css('overflow', 'auto');
});

$(document).on('keydown', function (event) {
    if (event.keyCode == 27) /* 27 == ESC */ {
        modalBusqueda.hide();
        $('body').css('overflow', 'auto');
    }
});

// Buscar producto al hacer click en el icono (svg) de buscar

let formularioBusqueda = $('#formulario-busqueda');

$('#boton-buscar').on('click', function(){
    formularioBusqueda.submit();
});

// Desplegar el modal de usuario

let modalInicioSesion = $('#modal-usuario');

$('#boton-usuario').on('click', function () {
    modalInicioSesion.show();
    $('body').css('overflow', 'hidden');
});

$('.boton-cerrar-modal-usuario').on('click', function () {
    modalInicioSesion.hide();
    $('body').css('overflow', 'auto');
});

$(document).on('keydown', function (event) {
    if (event.keyCode == 27) /* 27 == ESC */ {
        modalInicioSesion.hide();
        $('body').css('overflow', 'auto');
    }
});

// Funcionalidad input de numero de productos

jQuery('.numero-articulos').each(function () {
    var spinner = jQuery(this),
        input = spinner.find('input[type="number"]'),
        btnUp = spinner.find('.numero-articulos-up'),
        btnDown = spinner.find('.numero-articulos-down'),
        min = input.attr('min'),
        max = input.attr('max');

    btnUp.click(function () {
        var oldValue = parseFloat(input.val());
        if (oldValue >= max) {
            var newVal = oldValue;
        } else {
            var newVal = oldValue + 1;
        }
        spinner.find("input").val(newVal);
        spinner.find("input").trigger("change");
    });

    btnDown.click(function () {
        var oldValue = parseFloat(input.val());
        if (oldValue <= min) {
            var newVal = oldValue;
        } else {
            var newVal = oldValue - 1;
        }
        spinner.find("input").val(newVal);
        spinner.find("input").trigger("change");
    });

});

// Desplegar seccion de ajustes

let botonVerAjustesBusqueda = $('#boton-ver-ajustes-busqueda');
let botonCerrarAjustesBusqueda = $('#boton-cerrar-ajustes-busqueda');
let seccionAjustesBusqueda = $('.seccion-ajustes-busqueda');

botonVerAjustesBusqueda.on('click', function () {
    seccionAjustesBusqueda.show('fast', function () {
        seccionAjustesBusqueda.css('display', 'block');
    });
});

botonCerrarAjustesBusqueda.on('click', function () {
    seccionAjustesBusqueda.hide('fast');
});

// Estilo de los text input

$(".input-login").each(function () {
    if ($(this).val() != "") {
        $(this).parent().addClass("contenedor-input-texto_animacion");
    }
});

$(".login-input").focus(function () {
    $(this).parent().addClass("contenedor-input-texto_animacion contenedor-input-texto_animacion-color");
});

$(".login-input").focusout(function () {
    if ($(this).val() === "")
        $(this).parent().removeClass("contenedor-input-texto_animacion");
    $(this).parent().removeClass("contenedor-input-texto_animacion-color");
})

// Intercambiar entre modales de inicio de sesión y de registro

let modalUsuarioInicioSesion = $('#modal-usuario_inicio-sesion');
let modalUsuarioRegistro = $('#modal-usuario_registro');

let botonVerFormularioRegistro = $('#boton-formulario-registro');
let botonVerFormularioInicioSesion = $('#boton-formulario-inicio-sesion');

botonVerFormularioRegistro.on('click', function() {
    console.log('click');
    modalUsuarioInicioSesion.hide();
    modalUsuarioRegistro.show();
});

botonVerFormularioInicioSesion.on('click', function() {
    modalUsuarioRegistro.hide();
    modalUsuarioInicioSesion.show();
});

// Hacer que los mensajes de popup desaparezcan tras unos segundos

let contenedorMensajesPopup = $('.contenedor-mensajes-popup') 

setTimeout(function() {
    contenedorMensajesPopup.fadeOut(2000);
}, 2500);
