<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoulasalle/git_github/blob/main/ulasalle.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD LA SALLE</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍAS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO DE INGENIERÍA Y MATEMÁTICAS</span><br />
                <span style="font-weight:bold;">CARRERA PROFESIONAL DE INGENIERÍA DE SOFTWARE</span>
            </th>            
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="2"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio / Talleres / Centros de Simulación</td></tr>        
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DE LABORATORIO</span><br />
</div>

<table>
<theader>
<tr><th colspan="2">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>

<tr><td>TÍTULO DE LA PRÁCTICA:</td><td>Calculadora</td></tr>
<tr><td colspan="2">RECURSOS A UTILIZAR:
<ul>
<li><a href="https://guides.github.com/">https://guides.github.com/</a></li>
<li><a href="https://git-scm.com/book/es/v2">https://git-scm.com/book/es/v2</a></li>
</ul>
</td>
</<tr>
<tr><td colspan="2">DOCENTES:
<ul>
<li>Richart Smith Escobedo Quispe (r.escobedo@ulasalle.edu.pe)</li>
</ul>
</td>
</<tr>
</tdbody>
</table>


# OBJETIVOS TEMAS Y COMPETENCIAS

## OBJETIVOS

- Aprender a manejar un sistema de control de versiones de manera colaborativa con varios
usuarios

## TEMAS
- Git
- GitHub

# CONTENIDO DE LA GUÍA

## MARCO CONCEPTUAL

- Instalar Git en el ordenador

	- MS Windows
		- Descargar Git-2.36.0-64-bit.exe desde https://git-scm.com/download/win


## EJERCICIO RESUELTO
Primer repositorio en GitHub
- Creamos un nuevo proyecto en GitHub
    - ![Nuevo Proyecto GitHub](github_proyecto_programacion.png)

- Crearemos un repositorio local usando git init
    ```sh
    D:\La Salle\Ingeniera Web 2022\Calculadora
    git init
    ```

- Crearemos un archivo Readme.md con contenido Markup
    ```sh
    echo "# Calculadora" > README.md
    ```

- Agregaremos este archivo al staging area usando git add .
    ```sh
    git status
    ```
    <pre>
    En la rama main

    No hay commits todavía

    Archivos sin seguimiento:
    (usa "git add <archivo>..." para incluirlo a lo que se será confirmado)
	README.md
    no hay nada agregado al commit pero hay archivos sin seguimiento presentes (usa "git add" para hacerles seguimiento)
    </pre>
    ```sh
    git add README.md
    ```

- Hacemos un primer commit en nuestro repositorio local 
    ```sh
    git commit -m "Mi primer proyecto en github"
    ```
- Asociamos el repositorio local con el repositorio remoto 
    ```sh
    git remote add origin https://github.com/Jona2010/Calculadora.git
    ```

- Actualizamos el repositorio remoto
    ```sh
    git push -u origin main
    ```

- Ahora podemos verificar en GitHub que nuestro repositorio se actualizó con el proyecto local
    - ![Readme.md](Readme.md.png)

- Creamos un archivo Python calculadora.py que establezca una conexión con Flask para ejecutarlo en nuestro navegador web, también creamos dos archivos HTML que serían la calculadora.html y resultado.htmly subimos todo al repositorio GitHub.
    ```sh
    python calculadora.py
    ```
    <pre>
   from flask import Flask,render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__,template_folder="template")



@app.route('/')
def index():
    return render_template('calculadora.html')

@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")
    if(operation == '+'):
        result = var_1 + var_2
    elif(operation == '-'):
        result = var_1 - var_2
    if(operation == '+'):
        result = var_1 + var_2
    elif(operation == '-'):
        result = var_1 - var_2
    elif(operation == '*'):
        result = var_1 * var_2
    elif(operation == '/'):
        result = var_1 / var_2
    elif(operation == '%'):
        result = var_1 % var_2
    else:
        result = 'operacion invalida'
    entry = result
    return render_template('resultado.html', entry=entry)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
    </pre>
    ```sh    
    python --version
    ```
    <pre>
    Python 3.9.7
    </pre>
    ```sh
    python calculadora.py
    ```
    <pre>
    ![Calculadora](github_proyecto_programacion.png)
    </pre>
    ```sh
    git add python calculadora.py
    git commit -m "Calculadora usando python y HTML"
    git push -u origin Jonathan
    ```
    
## CUESTIONARIO
- ¿Por qué Git es una herramienta importante en el curso?
- ¿Qué conductas éticas debe promocionarse cuando se usa un Sistema de Control de Versiones?
- ¿Qué son los entándares de codificación?

## REFERENCIAS Y BIBLIOGRÁFIA RECOMENDADAS
- https://guides.github.com/
- https://git-scm.com/book/es/v2



