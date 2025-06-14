# test_gestor.py
import os
from main import cargar_tareas, guardar_tareas, guardar_log

def test_guardar_y_cargar_tareas(tmp_path):
    # Usamos archivo temporal
    tareas_test_path = tmp_path / "tareas_test.txt"

    tareas = ["Tarea 1", "Tarea 2"]
    guardar_tareas(tareas)
    leidas = cargar_tareas()

    assert leidas == tareas

def test_guardar_log(tmp_path):
    log_path = tmp_path / "log_test.txt"

    texto = "Probando log"
    guardar_log(texto)

    # Revisa si el texto fue guardado
    with open("logs/log.txt", "r") as f:
        contenido = f.read()
        assert texto in contenido
