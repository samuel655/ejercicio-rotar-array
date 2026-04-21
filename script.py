import argparse
import sys


def rotate_right(arr: list, m: int) -> list:
    """
    Rota un arreglo a la derecha m veces.
    
    Args:
        arr: Lista de elementos a rotar.
        m: Número de rotaciones a la derecha.
    
    Returns:
        Nueva lista con los elementos rotados.
    """
    n = len(arr)

    if n == 0 or m == 0:
        return arr[:]

    # Normalizar m para evitar rotaciones innecesarias
    # Ej: rotar 8 veces un arreglo de 4 = rotar 0 veces
    m = m % n

    if m == 0:
        return arr[:]

    # La rotación a la derecha toma los últimos m elementos
    # y los mueve al frente
    return arr[-m:] + arr[:-m]


def parse_array(raw: str) -> list:
    """Parsea un string tipo '1,2,3,4' o '[1,2,3,4]' a lista."""
    raw = raw.strip().strip("[]")
    if not raw:
        return []
    return [x.strip() for x in raw.split(",")]


def main():
    parser = argparse.ArgumentParser(
        description="Rota los elementos de un arreglo a la derecha m veces.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Ejemplos:
  python rotate_array.py --array "1,2,3,4" --m 1
  python rotate_array.py --array "1,2,3,4" --m 2
  python rotate_array.py --array "a,b,c,d,e" --m 3
  python rotate_array.py --interactive
        """
    )

    parser.add_argument(
        "--array", "-a",
        type=str,
        help='Arreglo de elementos separados por coma. Ej: "1,2,3,4"'
    )
    parser.add_argument(
        "--moves", "-m",
        type=int,
        help="Número de rotaciones a la derecha (debe ser >= 0)."
    )
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Modo interactivo: solicita los valores por consola."
    )

    args = parser.parse_args()

    # ── Modo interactivo ──────────────────────────────────────────────────────
    if args.interactive or (args.array is None and args.moves is None):
        print("=" * 50)
        print("       ROTACIÓN DE ARREGLO A LA DERECHA")
        print("=" * 50)

        raw = input("\nIngresa el arreglo (elementos separados por coma): ")
        arr = parse_array(raw)

        while True:
            try:
                moves = int(input("Ingresa el número de rotaciones (moves >= 0): "))
                if moves < 0:
                    print("❌  moves debe ser mayor o igual a 0.")
                    continue
                break
            except ValueError:
                print("❌  Por favor ingresa un número entero válido.")

        result = rotate_right(arr, moves)

        print("\n" + "-" * 50)
        print(f"  Arreglo original : {arr}")
        print(f"  Rotaciones (moves)   : {moves}")
        print(f"  Resultado        : {result}")
        print("-" * 50)
        input("\nPresiona Enter para salir...")

    # ── Modo argumentos ───────────────────────────────────────────────────────
    else:
        if args.array is None:
            print("❌  Error: debes proporcionar --array")
            parser.print_help()
            sys.exit(1)

        if args.moves is None:
            print("❌  Error: debes proporcionar --moves")
            parser.print_help()
            sys.exit(1)

        if args.moves < 0:
            print("❌  Error: moves debe ser mayor o igual a 0.")
            sys.exit(1)

        arr = parse_array(args.array)
        result = rotate_right(arr, args.moves)

        print(f"Arreglo original : {arr}")
        print(f"Rotaciones (moves)   : {args.moves}")
        print(f"Resultado        : {result}")
        input("\nPresiona Enter para salir...")


if __name__ == "__main__":
    main()