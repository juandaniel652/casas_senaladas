from casas import datos

html = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Registro de Direcciones</title>

<style>

body{
    font-family: Arial, sans-serif;
    background-color:#f2f4f7;
    margin:0;
    padding:30px;
}

.contenedor{
    max-width:1200px;
    margin:auto;
    background:white;
    border-radius:15px;
    padding:30px;
    box-shadow:0 5px 15px rgba(0,0,0,0.1);
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
    padding:14px;
}

td{
    padding:12px;
    border-bottom:1px solid #ddd;
}

tr:nth-child(even){
    background:#fafafa;
}

tr:hover{
    background:#eef3f8;
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

    html += f"""
<tr>
<td>{fila['fecha']}</td>
<td>{fila['territorio']}</td>
<td>{fila['direccion']}</td>
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

with open("casas_senaladas.html", "w", encoding="utf-8") as archivo:
    archivo.write(html)

print("casas_senaladas.html generado correctamente")