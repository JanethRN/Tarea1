#Se importa la librería Flask y la carpeta template
from flask import Flask, render_template

#variable de instancia app y la carpeta templates
app=Flask(__name__, template_folder='templates')


#decorador ruta raíz
@app.route('/')
#función que retorna la página principal 
def principal(): 
    return render_template('principal.html')

#main del programa
if __name__ == '__main__':
    #debug cada vez que cambiamos dentro del servidor se reinicia automaticamente
    app.run( debug = True)

