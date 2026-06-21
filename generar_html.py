
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
    border:1px solid #ddd;
    text-align:center;
}

td{
    padding:12px;
    border:1px solid #ddd;
    text-align:center;
}

tr:nth-child(even){
    background:#f8f9fb;
}

tr:hover{
    background:#eef4ff;
}

a{
    color:#0066cc;
    text-decoration:none;
    word-break:break-word;
}

a:hover{
    text-decoration:underline;
}


/* ===== CELULARES ===== */

@media (max-width:768px){

    .contenedor{
        margin:10px;
        padding:15px;
    }

    h1{
        font-size:1.5rem;
    }

    table,
    thead,
    tbody,
    tr,
    td{
        display:block;
    }

    thead{
        display:none;
    }

    tr{
        background:white;
        margin-bottom:25px;
        border-radius:15px;
        box-shadow:0 3px 10px rgba(0,0,0,.1);
        padding:10px;
    }

    td{
        border:none;
        border-bottom:1px solid #eee;

        display:flex;
        flex-direction:column;

        align-items:flex-start;

        gap:5px;

        text-align:left;

        padding:14px 10px;
    }

    td:last-child{
        border-bottom:none;
    }

    td::before{
        font-weight:bold;
        color:#34495e;
    }

    td:nth-child(1)::before{
        content:"Fecha";
    }

    td:nth-child(2)::before{
        content:"Territorio";
    }

    td:nth-child(3)::before{
        content:"Dirección";
    }

    td:nth-child(4)::before{
        content:"Manzana";
    }

    td:nth-child(5)::before{
        content:"Comentarios";
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
<a href="https://www.google.com/maps/search/?api=1&query={direccion_url}"
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

