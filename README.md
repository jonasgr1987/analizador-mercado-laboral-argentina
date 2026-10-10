# 📊 Analizador del Mercado Laboral Tech (Argentina)

Aplicación modular desarrollada en Python diseñada para rastrear, clasificar y visualizar de forma ética y automatizada las tendencias mensuales de la demanda laboral en el mercado tecnológico de Argentina.

---

## 🏗️ Arquitectura y Estructura del Proyecto

El proyecto sigue estrictamente el principio de **Responsabilidad Única (SOLID)** y separación de responsabilidades, estructurándose en 4 módulos principales:

```text
ANALIZADOR DE EMPLEOS - PYTHON/
│
├── api_empleos.py       # Módulo 1: Extracción ética de datos (ETL - Extract)
├── analizador.py        # Módulo 2: Procesamiento y clasificación por 6 áreas (Transform)
├── graficos.py          # Módulo 3: Visualización de datos estadísticos (Load / Report)
├── main.py              # Módulo 4: Orquestador principal (Entrypoint)
└── DOCUMENTACION.md     # Documentación técnica del proyecto