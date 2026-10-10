from api_empleos import obtener_ofertas_argentina
from analizador import clasificar_y_contar_areas
from graficos import generar_grafico_tendencias

def main():
    print("==================================================")
    print("   ANALIZADOR DE MERCADO LABORAL TECH - ARGENTINA ")
    print("==================================================")
    
    # 1. Obtención ética de datos
    ofertas = obtener_ofertas_argentina()
    
    if ofertas:
        print(f"\n[OK] Se recuperaron {len(ofertas)} ofertas de empleo relevantes para el análisis.")
        
        # 2. Análisis y clasificación por las 6 áreas
        print("\n[PROCESANDO] Clasificando vacantes...")
        conteo_areas = clasificar_y_contar_areas(ofertas)
        
        print("\n--- RESUMEN DE OFERTAS POR ÁREA ---")
        for area, cantidad in conteo_areas.items():
            print(f" • {area}: {cantidad} ofertas detectadas")
            
        # 3. Generación del reporte visual
        print("\n[VISUALIZACIÓN] Generando gráfico estadístico actualizado...")
        generar_grafico_tendencias(conteo_areas)
        
    else:
        print("[AVISO] No se pudieron recuperar ofertas en este momento.")

if __name__ == "__main__":
    main()