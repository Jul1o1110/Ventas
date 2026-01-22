import matplotlib.pyplot as plt


def generar_graficos(df):

    
    plt.style.use('dark_background')
    color_fondo_tarjeta = '#1e293b' 
    color_acento = '#38bdf8'

    df_temp = df.copy()
    df_temp['Ciudad'] = df_temp['Ciudad'].str.title()
    df_temp['NombreProducto'] = df_temp['NombreProducto'].str.title()


    fig1, ax1 = plt.subplots(figsize=(8, 5))
    fig1.patch.set_facecolor(color_fondo_tarjeta)
    ax1.set_facecolor(color_fondo_tarjeta)

    df_temp.groupby('Ciudad')['ValorVenta'].sum().plot(
        kind='bar', 
        color=color_acento, 
        ax=ax1,
        edgecolor='white',
        linewidth=0.5
    )

    plt.xlabel('Ciudad', color='#94a3b8')
    plt.ylabel('Ventas ($)', color='#94a3b8')
    plt.xticks(rotation=0, color='#f8fafc')
    plt.yticks(color='#f8fafc')
    
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_color('#334155')
    ax1.spines['bottom'].set_color('#334155')

    plt.tight_layout()
    plt.savefig('static/grafico_barras.png', facecolor=fig1.get_facecolor(), transparent=True)
    plt.close()
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    fig2.patch.set_facecolor(color_fondo_tarjeta)

    colores_torta = ['#0ea5e9', '#0284c7', '#0369a1', '#075985', '#0c4a6e']

    df_temp.groupby('NombreProducto')['ValorVenta'].sum().nlargest(5).plot(
        kind='pie', 
        autopct='%1.1f%%', 
        ax=ax2, 
        colors=colores_torta,
        textprops={'color': "white", 'weight': 'bold'},
        wedgeprops={'linewidth': 2, 'edgecolor': color_fondo_tarjeta}
    )
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('static/grafico_torta.png', facecolor=fig2.get_facecolor(), transparent=True)
    plt.close()