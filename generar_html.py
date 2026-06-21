
from casas import datos
from urllib.parse import quote

html = """
<!DOCTYPE html>
<html lang="es">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Registro de Direcciones</title>

<style>

*{
    box-sizing:border-box;
}

body{
    margin:0;
    background:#f5f7fa;
    font-family:Segoe UI, Arial, sans-serif;
}

.contenedor{
    max-width:1300px;
    margin:30px auto;
    padding:25px;
    background:white;
    border-radius:15px;
    box-shadow:0 0 20px rgba(0,0,0,.1);

    overflow-x:auto;
}

h1{
    text-align:center;
    color:#333;
    margin-bottom:25px;
}

table{
    width:100%;
    border-collapse:collapse;
    min-width:800px;
}

th{
    background:#34495e;
    color:white;
    padding:14px;
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
    background:#eaf2ff;
}

a{
    color:#0066cc;
    text-decoration:none;
    font-weight:500;
}

a:hover{
    text-decoration:underline;
}

@media (max-width: 768px){

    .contenedor{
        margin:10px;
        padding:15px;
    }

    h1{
        font-size:1.4rem;
    }

    th, td{
        padding:10px;
        font-size:14px;
    }

}

</style>

</head>

<body>

<div class="contenedor">

<h1>Registro de Direcciones</h1>

<table>

<thead>
<tr>
<th>Fecha</th>
<th>Territorio</th>
<th>Dirección</th>
<th>Manzana</th>
<th>Comentarios</th>
</tr>
</thead>

<tbody>

"""

for fila in datos:

    direccion = fila["direccion"]
    direccion_url = quote(direccion)

    html += f"""
<tr>

<td>{fila['fecha']}</td>

<td>{fila['territorio']}</td>

<td>
<a
href="https://www.google.com/maps/search/?api=1&query={direccion_url}"
target="_blank">
{direccion}
</a>
</td>

<td>{fila['manzana'].upper()}</td>

<td>{fila['comentarios']}</td>

</tr>
"""

html += """

</tbody>

</table>

</div>

</body>
</html>

"""

with open("index.html", "w", encoding="utf-8") as archivo:
    archivo.write(html)

print("index.html generado correctamente.")
