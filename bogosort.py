import random
import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def is_sorted(data):
    return all(a <= b for a, b in zip(data, data[1:]))

def bogosort_steps(data):
    """Generador que yield el estado de la lista después de cada shuffle."""
    data = list(data)
    while not is_sorted(data):
        random.shuffle(data)
        yield list(data), False
    yield list(data), True

if __name__ == "__main__":
    mi_lista = [4, 2, 5, 1, 3]
    print(f"Lista original: {mi_lista}")

    MAX_INTENTOS = 500_000
    gen = bogosort_steps(mi_lista)
    intentos = [0]
    terminado = [False]

    fig, ax = plt.subplots(figsize=(8, 5))
    fig.patch.set_facecolor("#1e1e2e")
    ax.set_facecolor("#1e1e2e")

    n = len(mi_lista)
    barras = ax.bar(range(n), mi_lista, color="#cba6f7", edgecolor="#1e1e2e", linewidth=0.5)

    ax.set_xlim(-0.5, n - 0.5)
    ax.set_ylim(0, max(mi_lista) * 1.15)
    ax.set_xticks([])
    ax.tick_params(colors="#cdd6f4")
    for spine in ax.spines.values():
        spine.set_edgecolor("#313244")

    titulo = ax.set_title("Bogosort — intentos: 0", color="#cdd6f4", fontsize=13, pad=12)
    ax.set_ylabel("Valor", color="#89b4fa", fontsize=10)

    def actualizar(_):
        if terminado[0]:
            return barras

        try:
            estado, listo = next(gen)
        except StopIteration:
            return barras

        intentos[0] += 1

        for barra, val in zip(barras, estado):
            barra.set_height(val)
            barra.set_color("#a6e3a1" if listo else "#cba6f7")

        if listo:
            titulo.set_text(f"Bogosort — listo en {intentos[0]} intentos")
            titulo.set_color("#a6e3a1")
            terminado[0] = True
        else:
            titulo.set_text(f"Bogosort — intentos: {intentos[0]}")

        if intentos[0] >= MAX_INTENTOS:
            titulo.set_text(f"Límite alcanzado: {MAX_INTENTOS} intentos")
            titulo.set_color("#f38ba8")
            terminado[0] = True

        return barras

    ani = animation.FuncAnimation(
        fig,
        actualizar,
        interval=100,
        blit=False,
        cache_frame_data=False,
    )

    plt.tight_layout()
    plt.show()
