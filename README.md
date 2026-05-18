# Bogosort — Visualizador

Visualización animada del algoritmo **Bogosort** usando `matplotlib`.

Bogosort es un algoritmo de ordenamiento que funciona barajando la lista aleatoriamente hasta que, por casualidad, queda ordenada. Su complejidad promedio es **O(n · n!)**, lo que lo hace completamente impráctico pero útil para ilustrar conceptos de algoritmos aleatorios y complejidad computacional.

## Cómo funciona

El programa genera un gráfico de barras que representa la lista. En cada iteración:

- Las **barras moradas** indican que la lista aún no está ordenada y se sigue barajando.
- Cuando la lista queda ordenada, todas las **barras se vuelven verdes** y se muestra el total de intentos.

## Requisitos

- Python 3.10+
- matplotlib
- PyQt6

```bash
pip install matplotlib PyQt6
```

## Ejecución

```bash
python bogosort.py
```

> **Nota:** Bogosort es extremadamente lento con listas grandes. Se recomienda usar listas de máximo 5-7 elementos.

## Ejemplo

### Resolviendo

<img width="800" height="575" alt="image" src="https://github.com/user-attachments/assets/c04433d9-0576-4abf-8df7-4575a95243e5" />


<br><br>

### Ya resuelto

<img width="800" height="575" alt="image" src="https://github.com/user-attachments/assets/cb188cd7-a9c8-49fc-a597-fd322b0015ee" />
