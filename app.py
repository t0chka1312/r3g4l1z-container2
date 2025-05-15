from flask import Flask, request, render_template_string, redirect, url_for
import os

app = Flask(__name__)

# Versión vulnerable (oculta en comentarios)
VERSION = "WebApp 2.4.0 (CVE-2024-3400)"

# HTML con estilo oscuro + rojo
LOGIN_HTML = r"""
<!DOCTYPE html>
<html>
<head>
    <title>Secure Portal</title>
    <style>
        body {{ background-color: #000; color: #fff; font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
        h1 {{ color: #ff0000; text-shadow: 0 0 5px #f00; }}
        form {{ display: inline-block; background-color: #222; padding: 20px; border-radius: 10px; border: 1px solid #f00; }}
        input {{ display: block; margin: 10px auto; padding: 8px; background: #111; color: #fff; border: 1px solid #f00; }}
        button {{ background: #f00; color: #000; border: none; padding: 10px 20px; cursor: pointer; font-weight: bold; }}
        .error {{ color: #f00; font-weight: bold; }}
        .hidden {{ opacity: 0.5; font-size: 0.8em; }}
        .report-btn {{ 
            display: block;
            margin: 20px auto;
            background: transparent;
            color: #f00;
            border: 1px solid #f00;
            padding: 8px 15px;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <h1>🔒 Secure Portal v2.4</h1>
    <form method="POST">
        <input type="text" name="user" placeholder="Usuario" required>
        <input type="password" name="pass" placeholder="Contraseña" required>
        <button type="submit">Acceder</button>
    </form>
    <a href="/report?name=guest" class="report-btn">Generar Reporte de Usuario</a>
    <p class="hidden"><!-- Versión: {version} --></p>
</body>
</html>
""".format(version=VERSION)

ERROR_HTML = """
<div class="error">
    <h1>⛔ Acceso denegado</h1>
    <p>Credenciales inválidas. Intento registrado.</p>
</div>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return ERROR_HTML + LOGIN_HTML
    return LOGIN_HTML

@app.route("/report")
def report():
    name = request.args.get("name", "Guest")
    return render_template_string("<h1 style='color:#f00'>Reporte para {} en /app/reports</h1>".format(name))

# Endpoint /flag ahora devuelve 403 (prohibido)
@app.route("/flag")
def flag():
    return "Acceso denegado", 403

# La flag real solo es accesible via SSTI
FLAG_CONTENT = "r3g4l1z{SSTI_RCE_0n_Fl4sk_2024}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
