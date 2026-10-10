def clasificar_y_contar_areas(ofertas):
    """
    Clasifica las ofertas de empleo en 6 áreas laborales principales del mercado 
    y cuenta cuántas vacantes hay por cada categoría.
    """
    # Definimos las 6 áreas clave del mercado laboral tech y sus palabras clave asociadas
    areas_clave = {
        "Desarrollo Software": ["python", "javascript", "react", "node", "java", "developer", "software", "frontend", "backend", "fullstack", "devops"],
        "Datos e IA": ["data", "sql", "analyst", "scientist", "ai", "machine learning", "database"],
        "Comercial y Marketing": ["sales", "marketing", "growth", "sdr", "account", "comercial", "seo"],
        "Admin y Finanzas": ["finance", "contable", "admin", "billing", "hr", "recruiter", "finanzas"],
        "Atención al Cliente": ["support", "customer", "success", "helpdesk", "atencion al cliente"],
        "Logística y Ops": ["operations", "logistics", "supply", "ops", "logistica"]
    }
    
    # Inicializamos el diccionario de conteo en 0 para cada área
    conteo_areas = {area: 0 for area in areas_clave.keys()}
    
    for oferta in ofertas:
        titulo = oferta.get("title", "").lower()
        descripcion = oferta.get("company_name", "").lower()
        texto_completo = f"{titulo} {descripcion}"
        
        # Buscamos a qué área pertenece la oferta según las palabras clave
        clasificada = False
        for area, keywords in areas_clave.items():
            for kw in keywords:
                if kw in texto_completo:
                    conteo_areas[area] += 1
                    clasificada = True
                    break
            if clasificada:
                break
                
        # Si no encaja exactamente, la sumamos a Desarrollo Software por defecto
        if not clasificada and len(ofertas) > 0:
            conteo_areas["Desarrollo Software"] += 1
            
    return conteo_areas
