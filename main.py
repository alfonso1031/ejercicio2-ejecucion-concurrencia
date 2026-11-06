import asyncio
import time


async def realizar_tarea(nombre, segundos):
    print(f"Comienza: {nombre}")
    await asyncio.sleep(segundos)
    print(f"Termina: {nombre}")


async def main():
    inicio = time.perf_counter()

    print("Preparación concurrente del desayuno")
    await asyncio.gather(
        realizar_tarea("Preparar café", 2),
        realizar_tarea("Tostar el pan", 1),
        realizar_tarea("Cocinar los huevos", 3),
    )

    tiempo_total = time.perf_counter() - inicio
    print(f"Desayuno listo. Tiempo total: {tiempo_total:.2f} segundos")


if __name__ == "__main__":
    asyncio.run(main())
