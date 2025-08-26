import pandas as pd
import os

# 1️⃣ Carrega os dados
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 2️⃣ Seleciona colunas numéricas
numeric_cols = df.select_dtypes(include='number').columns

# 3️⃣ Remove extremos usando percentis (1% e 99%)
lower_percentile = 0.01
upper_percentile = 0.99

df_clean = df.copy()
for col in numeric_cols:
    lower = df[col].quantile(lower_percentile)
    upper = df[col].quantile(upper_percentile)
    df_clean = df_clean[(df_clean[col] >= lower) & (df_clean[col] <= upper)]

# 4️⃣ Converte para HTML
table_html = df_clean.to_html(classes="table table-striped", index=False, border=0)

# 5️⃣ HTML base com DataTables e Bootstrap
html_base = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>DataFrame Interativo Limpo</title>
    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- DataTables CSS -->
    <link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
    <style>
        body {{
            background-color: #f0f8ff;
        }}
        h1 {{
            color: #2c3e50;
            text-align: center;
        }}
        table {{
            font-size: 14px;
        }}
    </style>
    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    <!-- DataTables JS -->
    <script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
</head>
<body class="container mt-4">
    <h1 class="mb-4">Tabela Interativa do Titanic (limpo)</h1>
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

# 6️⃣ Salva na pasta templates
output_path = os.path.join("templates", "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_base)

print(f"index.html interativo e limpo gerado com sucesso em {output_path}!")
