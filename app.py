import pandas as pd
import os

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

table_html = df.to_html(classes="table table-striped", index=False, border=0)

html_base = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>DataFrame Interativo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    <script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
</head>
<body class="container mt-4">
    <h1 class="mb-4">Tabela Interativa do DataFrame</h1>
    <div>
        {table_html}
    </div>
    <script>
    $(document).ready(function(){{
        $('table').DataTable({{
            "pageLength": 10,
            "lengthMenu": [5, 10, 20, 50],
            "language": {{
                "search": "Buscar:",
                "lengthMenu": "Mostrar _MENU_ registros",
                "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
                "paginate": {{
                    "first": "Primeiro",
                    "last": "Último",
                    "next": "Próximo",
                    "previous": "Anterior"
                }}
            }}
        }});
    }});
    </script>
</body>
</html>
"""

output_path = os.path.join("templates", "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_base)

print(f"index.html interativo gerado com sucesso em {output_path}!")
