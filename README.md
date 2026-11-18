# Plantilla para análisis

Este repositorio es una base común para desarrollar y organizar análisis de datos y modelos económicos. Incluye ejemplos para que puedas iniciar a partir de código existente, en lugar de comenzar desde cero, y una estructura compartida para identificar a las personas responsables, documentar los objetivos y dar seguimiento a cada análisis.

## Ejemplos incluidos

En `src/analisis/` hay notebooks de ejemplo con distintos enfoques:

- `Regresion_lineal.ipynb`: regresión lineal.
- `Dif_dif.ipynb`: diferencias en diferencias.
- `VECM.ipynb`: modelo vectorial de corrección de errores.

Úsalos como referencia y adapta o copia el que mejor se ajuste a tu pregunta. Verifica los datos, supuestos y resultados antes de reutilizar un modelo.

## Estructura del repositorio

| Ruta | Contenido |
| --- | --- |
| `src/analisis/` | Notebooks y código de los análisis. |
| `src/services/` | Servicios reutilizables, como conexiones a APIs. |
| `data/` | Datos y catálogos de entrada. |
| `resultados/` | Tablas y otros resultados generados por los análisis. |
| `presentacion/` | Presentaciones y materiales para comunicar resultados. |
| `src/config.py` | Configuración y lectura de variables de entorno. |

Procura mantener los insumos, el código y los productos en sus carpetas correspondientes. Evita guardar credenciales o datos sensibles en el repositorio.

## Registro y seguimiento de cada análisis

Al crear un análisis, agrega un notebook o módulo dentro de `src/analisis/` con un nombre descriptivo. En la primera celda Markdown (o al inicio del archivo de código), registra como mínimo:

- **Nombre del análisis**
- **Responsable(s) y fecha de creación**
- **Objetivo y pregunta que busca responder**
- **Datos y periodo analizados**, incluyendo su origen
- **Método o modelo utilizado**
- **Estado**: por ejemplo, en curso, en revisión o terminado
- **Resultados y ubicación de los archivos generados**

Actualiza el estado y las conclusiones conforme avance el trabajo. Así, cada análisis conserva su contexto y es más fácil conocer quién lo creó, para qué se hizo y qué resultados produjo.

## Entorno

El proyecto requiere Python 3.12 o posterior. Las dependencias y su configuración están declaradas en `pyproject.toml`, y `uv.lock` registra las versiones resueltas.

Con [uv](https://docs.astral.sh/uv/getting-started/installation/) instalado, después de clonar el repositorio entra en su directorio y ejecuta:

```shell
uv lock
uv sync
```

`uv lock` actualiza el archivo de versiones resueltas; `uv sync` crea el entorno virtual `.venv` e instala las dependencias del proyecto. Ten en cuenta que `uv sync` también actualiza el archivo de bloqueo cuando es necesario.