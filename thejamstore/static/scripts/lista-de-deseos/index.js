// Añadir producto al carrito a través de un enlace
let botonesAnadirAlCarrito = $('.boton-anadir-al-carrito');

for (let boton of botonesAnadirAlCarrito) {
    $(boton).on('click', function() {
        let formularioAnadirAlCarrito = $('#formulario-anadir-al-carrito-'+$(boton).attr('producto-id'))
        formularioAnadirAlCarrito.submit();
    });
}