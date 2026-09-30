
"""
Paquete principal del proyecto de detección de emociones.
Este archivo convierte la carpeta en un paquete de Python y expone
las funciones principales para que puedan ser importadas fácilmente.

Ejemplo de uso:
    from github_final_project import emotion_detector
"""

# Importar la función principal desde el módulo emotion_detection
from .emotion_detection import emotion_detector

# Definir qué elementos estarán disponibles al importar el paquete
__all__ = ["emotion_detector"]
