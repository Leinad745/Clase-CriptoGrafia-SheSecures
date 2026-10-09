# Criptografía desde cero: de AES a romper un doble candado

**Duración:** 60 min · **Público:** mujeres con conocimientos de ciberseguridad bajos o nulos
**Formato:** teoría corta → práctica guiada → taller con IA

## Resumen de tiempos

| Min | Bloque | Tipo |
|---|---|---|
| 0–5 | Apertura y gancho | Interactivo |
| 5–15 | ¿Qué es la criptografía? Los 4 pilares | Teoría |
| 15–27 | AES: cómo funciona y cómo aparece en un CTF | Teoría + demo |
| 27–45 | Meet-in-the-Middle: teoría y práctica | Práctica guiada |
| 45–57 | Taller de IA: resolver y crear desafíos | Taller |
| 57–60 | Cierre y recursos | — |

---

## 1. Apertura (0–5 min)

- **Gancho:** mostrar en pantalla `Uryyb, fbl gh cebsrfben` (ROT13) y preguntar: "¿Alguien lo puede leer?". Resolverlo entre todas en voz alta.
  → Idea: cifrar = transformar la información para que solo quien tiene la clave la entienda.
- **Qué van a lograr hoy:** "En 1 hora van a romper un cifrado que usa AES, el mismo algoritmo que protege WhatsApp y los bancos. No van a romper AES en sí, sino un **mal uso** de AES."
- Presentación personal en un minuto (CTFs, experiencia) para generar confianza.

## 2. Bases: qué hace y qué aporta la criptografía (5–15 min)

**Definición simple:** técnicas matemáticas para proteger información frente a alguien que la intercepta o la modifica.

**Vocabulario mínimo** (una sola diapositiva):

- Texto plano (plaintext), texto cifrado (ciphertext), clave (key)
- Cifrar / descifrar
- **Simétrica** (una sola clave, como AES) vs **asimétrica** (clave pública y privada, como RSA). Hoy solo simétrica.
- **Principio de Kerckhoffs:** el algoritmo es público; el secreto es solo la clave.

**Los 4 pilares.** Un solo ejemplo para todos: *"Ana le envía a Bea una transferencia de $100"*.

| Pilar | Pregunta que responde | Ataque que evita | Herramienta |
|---|---|---|---|
| **Confidencialidad** | ¿Solo Bea puede leerlo? | Espionaje | Cifrado (AES) |
| **Integridad** | ¿Alguien cambió $100 por $10.000? | Modificación | Hash (SHA-256), MAC |
| **Autenticación** | ¿De verdad lo envió Ana? | Suplantación | HMAC, certificados |
| **No repudio** | ¿Ana puede negar que lo envió? | Negación | Firma digital |

- **Mini demo (1 min):** `echo "hola" | sha256sum` y luego `echo "Hola" | sha256sum`. Una letra distinta cambia todo el hash (efecto avalancha).
- **Pregunta rápida:** "¿Un candado de bicicleta cuál de los 4 pilares cumple?"

## 3. AES (15–27 min)

**Qué es:** cifrado simétrico **por bloques**. Bloques de 16 bytes, claves de 128/192/256 bits. Estándar desde 2001.

**Funcionamiento básico** (sin matemáticas pesadas):

1. El bloque de 16 bytes se ordena en una matriz 4×4.
2. Se repiten **rondas** (10 en AES-128), cada una con 4 pasos:
   - **SubBytes:** cada byte se reemplaza usando una tabla (S-box) → confusión.
   - **ShiftRows:** las filas se desplazan → difusión.
   - **MixColumns:** las columnas se mezclan entre sí.
   - **AddRoundKey:** XOR con la subclave de la ronda.

- **Analogía:** batir una masa 10 veces, cada vez con un ingrediente secreto distinto. Sin la receta (clave) no se puede "desbatir".
- Visualización recomendada: "Rijndael Animation" o CrypTool.

**Modos de operación** (aquí vive la mayoría de los desafíos):

- **ECB:** cada bloque se cifra por separado → bloques iguales dan cifrados iguales. Mostrar el **pingüino de Linux cifrado en ECB**.
- **CBC / CTR / GCM:** solo mencionarlos como "las formas correctas".

**Cómo aparece AES en un CTF** — mensaje clave: *"AES nunca se rompe; se rompe cómo se usa".*

- ECB filtra patrones (ataque byte-a-byte).
- IV/nonce reutilizado en CTR → recuperar texto con XOR.
- Padding oracle en CBC.
- **Claves débiles o con poca entropía** → fuerza bruta. *(Conecta con la práctica.)*

**Demo (2 min):**

```python
from Crypto.Cipher import AES
k = b"clave16bytes!!!!"
c = AES.new(k, AES.MODE_ECB).encrypt(b"A"*32)
print(c.hex())   # se ven los dos bloques idénticos
```

## 4. Meet-in-the-Middle (27–45 min) · Práctica central

**Motivación (3 min):** "Si una clave es débil, ¿por qué no cifrar dos veces con dos claves? Doble de seguro... ¿o no?"

**Explicación visual (5 min):**

Notación:

| Símbolo | Significado |
|---|---|
| `P` | Texto plano (conocido) |
| `C` | Texto cifrado |
| `E_K1` / `E_K2` | Cifrar con K1 / con K2 |
| `D_K2` | Descifrar con K2 |
| `M` | Punto medio (la colisión) |

El doble cifrado:

```
C = E_K2( E_K1(P) )

P ──[E_K1]──► M ──[E_K2]──► C
```

El despeje clave: si aplicamos `D_K2` a ambos lados, el cifrado con K2 se cancela:

```
D_K2(C) = E_K1(P)

E_K1(P) = M = D_K2(C)
└─ solo depende de K1    └─ solo depende de K2
```

Así, **un problema con dos incógnitas se convierte en dos problemas de una incógnita**.

- **Fuerza bruta ingenua:** probar todas las parejas (K1, K2). Con 2¹⁶ opciones por llave: 2¹⁶ × 2¹⁶ = **2³² ≈ 4.300 millones** de intentos.
- **Meet-in-the-Middle:** atacar desde ambos extremos.
  1. **Lado izquierdo:** calcular `M = E_K1(P)` para cada K1 posible y guardar `tabla[M] = K1` (65.536 entradas).
  2. **Lado derecho:** calcular `M = D_K2(C)` para cada K2 posible. Si ese M está en la tabla → `E_K1(P) = D_K2(C)` → **colisión**: encontramos K1 y K2.
  3. **Descifrar la flag:** `P_flag = D_K1( D_K2(C_flag) )` (se quita primero K2, luego K1).
  4. **Costo:** 2¹⁶ + 2¹⁶ = **131.072** operaciones en vez de 4.300 millones.
- **Analogía:** dos personas cavan un túnel desde lados opuestos de la montaña y se encuentran en el medio.
- **Dato real:** por esto existe **3DES** y no "2DES". El doble cifrado solo aporta ~1 bit de seguridad.
- **Requisito:** un par conocido texto plano / texto cifrado (known-plaintext).
- **Costo oculto:** memoria. La tabla ocupa espacio (tiempo vs memoria).

**Práctica guiada (10 min)** — archivos en `mitm/`:

- `README.md`: enunciado estilo CTF (historia de 5ub4k3m1 contra el grupo Cerbero + 3 pistas). Leerlo en voz alta para abrir la práctica.
- `output.txt`: datos interceptados fijos (`P`, `C`, `C_flag`), iguales para todas.
- `chall.py`: genera dos claves AES a partir de solo **2 bytes aleatorios** cada una, y publica `P` (texto plano conocido, `"Hola, bienvenida!"`), `C = E_K2(E_K1(P))` y `C_flag` (la flag cifrada con las mismas llaves).
- `solve_alumnas.py`: solver con los pasos en blanco (`# TODO`).
- `solve.py`: solución completa (plan B / para la profesora).

Pasos:

1. Leer `chall.py` juntas: "¿Dónde está la debilidad?" → `os.urandom(2)`.
2. Calcular en la pizarra el costo de fuerza bruta vs MITM.
3. Completar `solve_alumnas.py` (pasos 1, 2 y 3).
4. Ejecutar:
   ```bash
   cat output.txt                               # copiar P, C y C_flag
   python3 solve_alumnas.py <P> <C> <C_flag>
   ```
   Resultado esperado: `SheSecures{m33t_1n_th3_m1ddl3_r0cks}` (tarda menos de 1 s).

- **Plan B:** a quien se atrase, entregarle `solve.py` para ejecutarlo y leer los comentarios.

## 5. Taller de IA (45–57 min)

### A. Usar la IA para resolver (6 min)

Enseñar un método de prompting, no copiar y pegar:

1. **Contexto:** "Estoy resolviendo un CTF de criptografía educativo. Este es el código: [...]"
2. **Pedir análisis, no la flag:** "¿Qué debilidad ves? Explícamelo paso a paso."
3. **Ataque y complejidad:** "¿Qué ataque aplica y cuántas operaciones requiere?"
4. **Pedir un esqueleto del solver** y completarlo ellas.
5. **Verificar:** la IA se equivoca (sobre todo con cuentas y bytes/encoding). Siempre ejecutar y comprobar.

**Ejercicio:** cada una le da `chall.py` a la IA con el prompt del paso 2 y comparan respuestas.

### B. Usar la IA para crear desafíos (6 min)

Plantilla de prompt:

> "Crea un desafío CTF de criptografía **nivel principiante** en Python usando pycryptodome. Vulnerabilidad: **[X]**. Entrega: (1) `chall.py` que imprima los datos públicos, (2) `solve.py` comentado en español, (3) una pista progresiva en 3 niveles, (4) la explicación del ataque. Flag con formato `SheSecures{...}`. El solver debe correr en menos de 10 segundos."

**Ideas para [X]** (de fácil a difícil):

- XOR con clave de 1 byte (256 opciones)
- César/ROT + base64 (capas de encoding)
- AES-ECB: detectar bloques repetidos o "cut & paste" de un token `admin=0`
- AES-CTR con nonce reutilizado
- Clave AES derivada de `time.time()` o de un PIN de 4 dígitos
- Doble AES con claves de 2 bytes (MITM, el de hoy) — variante con 3 bytes para las rápidas
- MD5 de una contraseña común (diccionario con rockyou)

**Regla de oro:** probar siempre el desafío que genera la IA antes de usarlo; a veces genera flags imposibles o solvers que no funcionan.

## 6. Cierre (57–60 min)

- **Recap en 3 frases:**
  1. La criptografía da confidencialidad, integridad, autenticación y no repudio.
  2. AES no se rompe; se rompe su mal uso.
  3. Cifrar dos veces no duplica la seguridad.
- **Recursos:** CryptoHack (el mejor para empezar), picoCTF, CyberChef, libro *Serious Cryptography*.
- **Reto para casa:** modificar `chall.py` para usar claves de 3 bytes. ¿Cuánto tarda ahora el MITM? ¿Y la fuerza bruta?

---

## Consejos para dar la clase

- **Dejar todo instalado antes:** `pip install pycryptodome`, o mejor un Google Colab preparado. Evita perder 10 minutos en instalaciones.
- **Bloque en riesgo:** MITM es el más largo. Si hay atraso, recortar la teoría de AES (rondas), no la práctica.
- Nada de jerga sin explicar: cada término nuevo va con una analogía.
- Trabajo en parejas durante la práctica: una escribe, la otra lee y verifica.

## Solución de referencia de `solve_alumnas.py`

<details>
<summary>Ver solución (solo profesora)</summary>

```python
# PASO 1: M = E_K1(P)
tabla = {E(K1, P): K1 for K1 in llaves}

# PASO 2: M = D_K2(C)
M = D(K2, C)

# PASO 3: P_flag = D_K1(D_K2(C_flag))
P_flag = D(K1, D(K2, C_flag))
```

Operaciones: 2¹⁶ cifrados + hasta 2¹⁶ descifrados ≈ 131.072, frente a 2³² ≈ 4.300 millones por fuerza bruta.

</details>
