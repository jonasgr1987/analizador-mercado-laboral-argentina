import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from datetime import datetime

def generar_grafico_tendencias(conteo_areas):
    """
    Genera un gráfico de barras con las 6 áreas profesionales, escala entera y fuentes citadas.
    """
    # Ordenamos las áreas de mayor a menor demanda
    areas_ordenadas = sorted(conteo_areas.items(), key=lambda x: x[1], reverse=True)
    
    nombres = [item[0] for item in areas_ordenadas]
    valores = [item[1] for item in areas_ordenadas]
    
    # Mes y año actual dinámico
    meses = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
        7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    ahora = datetime.now()
    periodo_actual = f"{meses[ahora.month]} {ahora.year}"
    
    # Creamos la figura
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(nombres, valores, color='#2980b9', width=0.55)
    
    # Forzamos números enteros en el eje Y
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    
    # Títulos profesionales
    ax.set_title(f"Demanda de Empleo por Área en Argentina — ({periodo_actual})", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Áreas Profesionales", fontsize=12, labelpad=10)
    ax.set_ylabel("Cantidad de Ofertas de Empleo", fontsize=12, labelpad=10)
    
    plt.xticks(rotation=20, fontweight='semibold', fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    
    # Cita de fuentes abajo
    fuente_texto = "Fuentes analizadas: Remotive API / Bumeran Argentina / Manpower (Métrica estimada mensual)"
    plt.figtext(0.12, 0.02, fuente_texto, fontsize=9, style='italic', color='dimgray')
    
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    
    # Guardar imagen
    plt.savefig("tendencias_empleos.png", dpi=300)
    print(f"\n[ÉXITO] Gráfico actualizado correctamente.")
    
    plt.show()