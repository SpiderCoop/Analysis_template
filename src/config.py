"""
Description:   Contains configuration settings and constants for the application, such as API tokens.
Author:        David Jiménez Cooper - SpiderCoop
Date:          2026-09-30
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Tokens de acceso a servicios externos (INEGI y Banxico)
INEGI_TOKEN = os.getenv("INEGI_TOKEN")
BANXICO_TOKEN = os.getenv("BANXICO_TOKEN")

# Rutas a archivos de datos locales
SERIE_HISTORICA_PATH = 'C:/ABM/Analisis/Sensibilidades_utilidades/data/sh_datos_40.csv'
CAT_CONCEPTOS_PATH = 'C:/ABM/Analisis/Sensibilidades_utilidades/data/cat_conceptos_40.csv'
CAT_INSTITUCIONES_PATH = 'C:/ABM/Analisis/Sensibilidades_utilidades/data/cat_instituciones_40.csv'