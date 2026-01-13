
from flask import Flask, render_template
import limpieza as lp

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
    
    ventas_ciudad = df.groupby('Ciudad')['ValorVenta'].sum().to_dict()

    registros = df.to_dict(orient='records')
    
    return render_template('index.html', 
                           datos=registros, 
                           resumen_ciudad=ventas_ciudad)

if __name__ == "__main__":
    print("--- EJECUTANDO ANÁLISIS EN CONSOLA ---")
    df_consola = obtener_datos_procesados()
    print("\nIniciando servidor web en http://127.0.0.1:5000")
    app.run(debug=True)