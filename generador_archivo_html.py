# Definir datos
data = {
    'title': 'Mi Título',
    'content': 'Este es el contenido del div con acentos: áéíóú.'
}

# Construir HTML con declaración de codificación UTF-8
html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documento</title>
</head>
<body>
    <div class="container">
        <h1>{data['title']}</h1>
        <p>{data['content']}</p>
    </div>
</body>
</html>
"""

# Guardar en un archivo con codificación UTF-8
with open('output.html', 'w', encoding='utf-8') as file:
    file.write(html)
