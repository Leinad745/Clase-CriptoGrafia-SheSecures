# Clase de Criptografía - SheSecures

Material para una clase introductoria de criptografía de 1 hora, a gente de cualquier nivel de experiencia en ciberseguridad. Cubre los fundamentos de la criptografía, AES, el ataque Meet-in-the-Middle y el uso de IA como apoyo para resolver desafíos CTF.

## Estructura

```
.
├── clase.md          Planificación de la clase: bloques, tiempos y contenidos
├── encryptaes.py     Demo: cifra una imagen con AES-ECB y AES-CBC
├── ai/
│   └── PROMPTS.md    Guía de prompts para usar la IA como tutora en desafíos de cripto

└── mitm/             Desafío CTF "Doble Candado"
    ├── README.md     Enunciado del desafío
    ├── chall.py      Script de cifrado
    └── output.txt    Datos cifrados entregados a las participantes
```

## Contenidos

**clase.md**: estructura de la clase dividida en seis bloques:
1. Apertura
2. Fundamentos: confidencialidad, integridad, autenticación y no repudio
3. AES y modos de operación
4. Meet-in-the-Middle: teoría y práctica
5. Taller de IA
6. Cierre

**encryptaes.py**: cifra `tux.png` con AES en modo ECB y en modo CBC, para mostrar cómo ECB deja visibles los patrones de la imagen. La imagen `tux.png` no está incluida en el repositorio y se debe agregar manualmente.

**ai/**: prompts pensados para que la IA guíe a las estudiantes a entender el problema, el código, la vulnerabilidad y el ataque, sin entregarles la solución.

**mitm/**: desafío de doble cifrado AES (`C = E_K2(E_K1(P))`) con llaves de baja entropía, que se resuelve con un ataque Meet-in-the-Middle a partir de un texto plano conocido.

## Requisitos

- Python 3
- `pycryptodome`
- `Pillow` (solo para `encryptaes.py`)

```bash
pip install pycryptodome Pillow
```

## Uso del desafío

Las participantes reciben `mitm/README.md`, `mitm/chall.py` y `mitm/output.txt`. La flag no está en el código: `chall.py` la lee desde `mitm/.flag.txt`, archivo que solo debe tener la organización.
