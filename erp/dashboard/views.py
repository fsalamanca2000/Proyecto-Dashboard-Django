from django.shortcuts import render
from dashboard.models import Cliente
import plotly.express as px
import pandas as pd
# Create your views here.
def dash(request):

    # clientes= Cliente.objects.all()
    
    df = pd.DataFrame({
        "Nombre":["Felipe Salamanca", "Maria Cardona", "Carlos Arciniegas", "Laura Pinzón", "Andres Guerra", "Luisa Mondragón", "Pedro González", "Ana Sanchez", "Diego Sanchez", "Camila Cardenas", "Valentina Velasquez", "Mateo Santamaria", "Sofia Pinzón"],
        "Barrio":["Veraguas Central","Galerias","Santa Barbara", "La Esmeralda","Modelia","Patio Bonito","Barcelona","El Nogal","Toberín","El Retiro","Capellanía","Marsella","Veraguas Central"],
        "Localidad":["Puente Aranda", "Teusaquillo", "Usaquén", "Teusaquillo", "Fontibón", "Kennedy", "Puente Aranda", "Chapinero", "Usaquén", "Chapinero", "Fontibón", "Kennedy", "Puente Aranda"],
        "Fecha_de_compra":["2022-03-15","2023-09-28","2023-06-07","2022-07-23","2022-11-11","2022-02-04","2023-04-19","2023-11-30","2022-05-02","2023-10-15","2023-01-20","2023-08-09","2022-12-25"],
        "Nombre_Producto":["Teclado gaming", "Mouse gaming", "Monitor LED", "Auriculares gaming", "Silla gamer", "Mousepad", "Tarjeta gráfica 3090", "Procesador AMD Ryzen 7 5800X", "Teclado mecánico", "Webcam", "Micrófono gamer", "Alfombrilla RGB", "Auriculares inalámbricos"],
        "Valor_compra":[273452.86,465879.14,1221157.49,571229.31,1265489.72,114656.22,1378904.78,2571540.42,803754.87,425452.86,728320.57,178904.78,950754.87],
    })
    # df['Fecha_de_compra'] = pd.to_datetime(df['Fecha_de_compra'])
    grafico_barras = px.bar(df,x="Nombre_Producto",y= "Valor_compra",title="Valor de cada producto")
    grafico_barras_barrio = px.bar(df,x="Barrio",y= "Valor_compra",title="Valor de compras por barrio", color="Localidad")
    grafico_linea = px.bar(df,x="Fecha_de_compra",y="Valor_compra", title="Compras segun las fechas")
    
    mihtml = grafico_barras.to_html(full_html = False)
    mihtml2 = grafico_barras_barrio.to_html(full_html =False)
    mihtml3 = grafico_linea.to_html(full_html =False)
    context = {
        "nombre": "Felipe",
        # "clientes": clientes,
        "grafica_bar": mihtml,
        "grafica_bar_barrio": mihtml2,
        "grafico_linea": mihtml3
    }
    return render(request, "dashboard/index.html", context)  