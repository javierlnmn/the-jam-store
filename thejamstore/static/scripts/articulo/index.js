// Boton añadir a la lista de deseos (aniamcion)

let botonAnadirListaDeseos = $('#boton-anadir-lista-deseos');

botonAnadirListaDeseos.on('click', function() {
    $(this).toggleClass('icono-corazon_activo');
});