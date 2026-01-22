import pandas as pd

def cargar_datos(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo)
        print("Archivo cargado.")
        return df
    except FileNotFoundError:
        print("Archivo no encontrado. Revisa el nombre.")
        return None

def manejar_nulos(df):
    df['ValorVenta'] = df['ValorVenta'].fillna('$0')
    return df.dropna(subset=['NombreProducto'])

def estandarizar_texto(df, columna):
    df[columna] = df[columna].str.lower().str.strip()
    return df

def limpieza_especifica(df, columna):
    df[columna] = df[columna].replace({'\$': '', ',': ''}, regex=True).astype(int)
    return df

df = cargar_datos('datos.csv')

if df is not None:
    df = manejar_nulos(df)
    df = estandarizar_texto(df, 'NombreProducto') 
    df = limpieza_especifica(df, 'ValorVenta')
    
    df.to_csv('datos_limpios.csv', index=False)
    print("¡Limpieza terminada! Se ha creado 'datos_limpios.csv'")