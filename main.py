from flask import Flask, render_template
import limpieza as lp
import visualizacion as vs

app = Flask(__name__)

def obtener_datos_procesados():
    df = lp.cargar_datos('datos.csv')
    if df is not None:
        df = lp.manejar_nulos(df)
        df = lp.estandarizar_texto(df, 'NombreProducto')
        df = lp.estandarizar_texto(df, 'Ciudad')
        df = lp.limpieza_especifica(df, 'ValorVenta')
        return df
    return None

@app.route('/')
def home():
    df = obtener_datos_procesados()
    if df is not None:
        vs.generar_graficos(df)
        tabla_html = df.to_html(classes='tabla-estilo', index=False)
        return render_template('index.html', tabla=tabla_html)
    return "Error: No se encontró el archivo datos.csv"

if __name__ == "__main__":
    app.run(debug=True)