// Añadir producto al carrito a través de un enlace
let botonAnadirAlCarrito = $('#anadir-al-carrito');
let formularioAnadirAlCarrito = $('#formulario-anadir-al-carrito');

botonAnadirAlCarrito.on('click', function() {
    formularioAnadirAlCarrito.submit();
})