<h1>The Jam Store</h1>

<h3>Para instalar las dependencias del proyecto:</h3>

    pip install -r requirements.txt

<h3>Notaciones:</h3>

<ul>
<li>Apps: Con '_' (ejemplo_nombre)</li>
<li>Variables / Campos de modelos: Con '_' (ejemplo_nombre)</li>
<li>Funciones: Con '_' (ejemplo_nombre)</li>
<li>Clases: Con 'camelCase' (ejemploNombre). Excepto modelos, que serán con '_'</li>
<li>Ficheros (imágenes, textos, htmls, etc...): Con '-' (ejemplo-nombre)</li>
<li>Verbose names: Minúsculas y con espacios (ejemplo nombre)</li>
<li>Para devolver un contexto hay que crear una variable y devolverla</li>
<li>Para comparar 2 objetos utilizamos el id</li>
</ul>


<h3>Para compilar el scss al fichero app.css del proyecto:</h3>

    python manage.py sass static/style/scss/app.scss static/style/css/app.css


<h3>Para exportar los datos guardados en la base de datos de una aplicación:</h3>

    python -Xutf8 manage.py dumpdata productos > productos.json


<h3>Para importar los datos guardados en el fichero a la base de datos:</h3>

    python manage.py loaddata productos.json