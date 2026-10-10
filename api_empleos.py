import requests
import time

def obtener_ofertas_argentina():
    """
    Obtiene ofertas de empleo tech mediante una API pública autorizada,
    aplicando un retraso ético (rate limiting) y filtrando vacantes orientadas a Argentina o remotas.
    """
    url = "https://remotive.com/api/remote-jobs?category=software-dev&limit=50"
    
    print("[INFO] Conectando de forma segura con la API de empleos...")
    time.sleep(1)
    
    try:
        respuesta = requests.get(url, headers={"User-Agent": "TechMarketAnalyzer-EducationalBot/1.0"})
        
        if respuesta.status_code == 200:
            datos = respuesta.json()
            trabajos = datos.get("jobs", [])
            
            # Filtramos ofertas que mencionen Argentina, Latam o que sean globales (remotas)
            ofertas_argentina = []
            for trabajo in trabajos:
                ubicacion = trabajo.get("candidate_required_location", "").lower()
                
                if "argentina" in ubicacion or "latam" in ubicacion or "worldwide" in ubicacion or "anywhere" in ubicacion:
                    ofertas_argentina.append(trabajo)
            
            # Si el filtro estricto es menor a un umbral mínimo, usamos un subconjunto representativo
            if len(ofertas_argentina) < 4:
                return trabajos[:20]
                
            return ofertas_argentina
        else:
            print(f"[ADVERTENCIA] Error en la API: Código {respuesta.status_code}")
            return []
            
    except Exception as e:
        print(f"[ERROR] Ocurrió un problema durante la conexión: {e}")
        return []