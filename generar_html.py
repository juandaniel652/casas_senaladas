from casas import datos

html = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Registro de Direcciones</title>

<style>

body{
    background:#f5f7fa;
    font-family:Segoe UI, Arial, sans-serif;
    margin:0;
}

.contenedor{
    max-width:1300px;
    margin:40px auto;
    background:white;
    padding:30px;
    border-radius:15px;
    box-shadow:0 0 20px rgba(0,0,0,.1);
}

h1{
    text-align:center;
    color:#333;
    margin-bottom:25px;
}

table{
    width:100%;
    border-collapse:collapse;
}

th{
    background:#34495e;
    color:white;
    padding:15px;
    text-align:center;
    border:1px solid #d0d0d0;
}

td{
    padding:12px;
    text-align:center;
    border:1px solid #d0d0d0;
}

tr:nth-child(even){
    background:#f8f9fb;
}

tr:hover{
    background:#e9f0f7;
}

a{
    color:#0066cc;
    text-decoration:none;
}

a:hover{
    text-decoration:underline;
}

</style>
</head>

<body>

<div class="contenedor">

<h1>Registro de Direcciones</h1>

<table>

<tr>
<th>Fecha</th>
<th>Territorio</th>
<th>Dirección</th>
<th>Manzana</th>
<th>Comentarios</th>
</tr>
"""

for fila in datos:

    direccion = fila["direccion"]

    html += f"""
<tr>
<td>{fila['fecha']}</td>
<td>{fila['territorio']}</td>

<td>
<a target="_blank"
href="https://www.google.com/maps/search/?api=1&query={direccion}">
{direccion}
</a>
</td>

<td>{fila['manzana'].upper()}</td>
<td>{fila['comentarios']}</td>

</tr>
"""

html += """
</table>

</div>

</body>
</html>
"""

with open("index.html","w",encoding="utf-8") as archivo:
    archivo.write(html)