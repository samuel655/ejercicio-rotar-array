# 🔄 Rotación de Arreglo a la Derecha
 
Herramienta de consola que rota los elementos de un arreglo hacia la derecha `m` veces, sin perder ningún elemento.
 
## ¿Qué hace?
 
Toma un arreglo y mueve todos sus elementos `m` posiciones hacia la derecha. Los elementos que "salen" por la derecha vuelven a aparecer por la izquierda.
 
```
arr[1, 2, 3, 4]  →  m=1  →  arr[4, 1, 2, 3]
arr[1, 2, 3, 4]  →  m=2  →  arr[3, 4, 1, 2]
arr[1, 2, 3, 4]  →  m=3  →  arr[2, 3, 4, 1]
arr[1, 2, 3, 4]  →  m=4  →  arr[1, 2, 3, 4]
```
 
---
 
## 📁 Archivos incluidos
 
| Archivo               | Descripción                                      |
|-----------------------|--------------------------------------------------|
| `script.py`           | Script principal con la lógica de rotación       |
| `rotar-archivo.exe`   | Lanzador para **Windows** (doble clic)           |
| `README.md`           | Este archivo                                     |
 
---
 
## 🚀 ¿Cómo ejecutarlo?
 
### Requisito único: tener Python instalado (desde python)
 
> Si no lo tienes, descárgalo gratis desde [python.org](https://www.python.org/downloads/)  
> ⚠️ Durante la instalación en Windows, marca la opción **"Add Python to PATH"**
 
---
 
### ▶️ Windows
 
Haz **doble clic** en el archivo `rotar-archivo.exe`.
 
Se abrirá una consola y te pedirá los datos paso a paso.
 
---
 
### ▶️ Directamente con Python (cualquier sistema)
 
**Modo interactivo** (te pregunta los valores):
```bash
python script.py --interactive
```
 
**Modo con argumentos** (todo en una línea):
```bash
python script.py --array "1,2,3,4" --moves 2
```
 
**Ver ayuda:**
```bash
python script.py --help
```
 
---
 
## 💡 Ejemplos de uso
 
```bash
# Rotar 1 vez
python script.py --array "1,2,3,4" --moves 1
# Resultado: [4, 1, 2, 3]
 
# Rotar 2 veces
python script.py --array "1,2,3,4" --moves 2
# Resultado: [3, 4, 1, 2]
 
# Funciona con texto también
python script.py --array "a,b,c,d,e" --moves 3
# Resultado: [c, d, e, a, b]
 
# m mayor al tamaño del arreglo (se normaliza automáticamente)
python script.py --array "1,2,3,4" --moves 9
# Resultado: [4, 1, 2, 3]  (equivale a m=1)
 
# Arreglo vacío
python script.py --array "" --moves 5
# Resultado: []
```
 
---
 
## 🧠 ¿Cómo funciona el algoritmo?
 
La rotación a la derecha en `m` pasos equivale a tomar los **últimos `m` elementos** y moverlos al **frente**:
 
```
arr = [1, 2, 3, 4],  m = 2
 
últimos 2  →  [3, 4]
primeros 2 →  [1, 2]
 
resultado  →  [3, 4] + [1, 2]  =  [3, 4, 1, 2] ✅
```
 
También se normaliza `m` con `m % n` para evitar rotaciones innecesarias cuando `m >= n`.
 
---
 
## ✅ Casos límite manejados
 
| Caso                        | Comportamiento               |
|-----------------------------|------------------------------|
| `m = 0`                     | Devuelve el arreglo original |
| `m >= n`                    | Se normaliza con `m % n`     |
| Arreglo vacío               | Devuelve `[]`                |
| `m` múltiplo de `n`         | Devuelve el arreglo original |