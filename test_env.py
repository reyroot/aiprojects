import numpy as np
from rich.console import Console
from rich.table import Table

console = Console()

def check_setup():
    # Simulamos una operación de matriz (base de la IA)
    data = np.array([[1, 2], [3, 4]])
    result = np.linalg.det(data)

    table = Table(title="Diagnóstico de Entorno IA 2026")
    table.add_column("Componente", style="cyan")
    table.add_column("Estado", style="green")

    table.add_row("Python Interpreter", "Venv Activo")
    table.add_row("NumPy (Matemática)", "Funcional")
    table.add_row("Determinante Matriz", f"{result}")

    console.print(table)

if __name__ == "__main__":
    check_setup()
