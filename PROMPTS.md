# Guía de prompts: la IA como tutora en desafíos de criptografía

Esta guía sirve para **desafíos CTF de criptografía**. La idea es que la IA te acompañe a **entender** el problema, el código, la vulnerabilidad y el ataque, **sin darte nunca la solución**. La flag la consigues tú.

> Copia el prompt y reemplaza lo que está entre `[CORCHETES]`. Sigue las etapas en orden; cada una prepara la siguiente.

---

## Etapa 0 · Configurar a tu tutora (obligatorio)

Pega esto **al inicio de una conversación nueva**, antes de mostrarle cualquier archivo del desafío.

```text
Quiero que seas mi tutora de criptografía. Estoy aprendiendo y resolviendo un
desafío CTF educativo. Durante TODA la conversación sigue estas reglas:

1. NUNCA me des la solución, la flag, ni código que resuelva el desafío
   (ni completo ni por partes que juntas lo resuelvan) pero.
2. Guíame con preguntas que me hagan pensar el siguiente paso. Prefiero
   descubrir las cosas yo.
3. Si te muestro mi razonamiento o mi código, dime si voy bien y DÓNDE mirar.
4. Explica los conceptos con analogías y ejemplos genéricos que NO
   sean el desafío.
5. Si te pido la respuesta directa, recuérdame estas reglas y dame solo
   una pista un poco más concreta que la anterior.
6. Si no estás segura de algo (cálculos, bytes, encodings), dímelo para
   que yo lo verifique.

Responde "Entendido" y pregúntame qué desafío estoy resolviendo.
```

---

## Etapa 1 · Entender el problema

*Objetivo: saber qué te piden, qué tienes y qué te falta, antes de leer código.*

```text
Te comparto el enunciado de un desafío: [ENUNCIADO].
Ayúdame a ordenar la información con preguntas:
¿qué datos tengo?, ¿qué tengo que obtener?, ¿Que puedo interpretar de ello?
No analices todavía cómo resolverlo.
```

```text
En el enunciado aparecen estos términos: [TÉRMINOS].
Explícame cada uno con una analogía de la vida real, en una o dos frases.
```

```text
Yo creo que el desafío consiste en ___ y que el objetivo es ___.
¿Lo entendí bien? Responde "sí", "no" o "casi" y hazme una pregunta
para afinar mi idea.
```

---

## Etapa 2 · Entender el código

*Objetivo: saber qué hace cada línea. Todavía no hay que buscar fallas.*

```text
Este es el código del desafío:
[CÓDIGO]
Explícame qué hace cada bloque, con analogias simples, paso a paso.
NO me digas dónde está la vulnerabilidad ni cómo atacarlo.
```

```text
No entiendo esta línea: [LÍNEA].
¿Qué hace la función [FUNCIÓN] en general? Dame un ejemplo pequeño con
valores inventados, que no tenga relación con el desafío.
```

---

## Etapa 3 · Encontrar la vulnerabilidad

*Objetivo: descubrir **por qué** se puede romper. Es la etapa más importante, así que no la saltes.*

```txt
¿Qué preguntas se haría una persona experta en criptografía al revisar
este código para buscar debilidades? Dame una lista de preguntas
generales, sin responderlas.
```

```txt
Sospecho que la debilidad está en ___ porque ___.
¿Voy bien? Responde "sí", "no" o "caliente/frío" y dame una pista.
```

---

## Etapa 4 · Entender el ataque (sin código)

*Objetivo: saber **qué** vas a hacer y **por qué funciona**, antes de programar.*

```txt
Creo que la vulnerabilidad es ___. ¿Qué familias de ataques existen para
este tipo de problema? Dime solo sus nombres y una idea general de cada uno,
sin aplicarlos a mi desafío.
```

```txt
Explícame el ataque [NOMBRE DEL ATAQUE] con una analogía de la vida real.
Sin código y sin usar los datos de mi desafío.
```

```text
Esta es mi idea para atacar el desafío, en palabras:
1. ___
2. ___
3. ___
¿Tiene sentido? Si falta algo, indicame que puede ser.
```

---

## Etapa 5 · Programar la solución

*Objetivo: escribir el código **tú misma**. La IA solo te enseña las piezas por separado.*

```txt
Necesito hacer [TAREA GENERAL, ej: "guardar muchos valores y buscar rápido
si uno existe"] en Python. ¿Qué herramienta o estructura me sirve?
```

```txt
¿Cómo se usa [FUNCIÓN / LIBRERÍA, ej: "AES en pycryptodome"]?
Dame un ejemplo mínimo con valores inventados, no con los de mi desafío.
```

```txt
¿Cómo convierto entre [FORMATO A] y [FORMATO B] en Python
(ej: hexadecimal y bytes)? Dame un ejemplo pequeño.
```

```txt
Escribí esto para el paso ___ de mi plan:
[MI CÓDIGO]
NO lo reescribas. Dime si la lógica es correcta y, si no,
en qué línea debería fijarme.
```

---

## Etapa 6 · Depurar

*Objetivo: entender los errores para arreglarlos tú misma.*

```txt
Me sale este error:
[ERROR]
Explícame qué significa en general y qué debería revisar.
No me des el código corregido.
```

```txt
Mi programa corre pero no da el resultado esperado: [QUÉ PASA].
¿Cuáles podrían ser 3 causas posibles? Solo lístalas.
```

```txt
¿Cómo puedo probar mi código con un ejemplo pequeño que yo controle,
para saber si la lógica funciona antes de usar los datos reales?
```

---

## Etapa 7 · Reflexionar (después de la flag)

*Objetivo: fijar lo aprendido. Esta etapa es la que hace que lo aprendido se quede.*

```txt
Resolví el desafío. Así lo hice: [RESUMEN].
¿Qué concepto de criptografía aprendí? ¿Dónde aparece en el mundo real?
```

```txt
¿Cómo debería haberse programado este sistema para que fuera seguro?
```

```txt
¿Qué variante de este desafío sería más difícil? ¿Qué tendría que cambiar
en mi ataque?
```

---

## ✅ Buenas prácticas

- **Primero piensa tú, después pregunta.** Escribe tu idea en el prompt ("yo creo que..."): la IA puede corregir un razonamiento, pero no puede pensar por ti.
- **Verifica todo.** La IA se equivoca, sobre todo con cálculos, bytes y encodings. Ejecuta y comprueba.
- **Explícalo sin mirar.** Antes de pasar de etapa, explícale a tu compañera lo que entendiste sin mirar la pantalla. Si no puedes, vuelve a preguntar.
- **Un paso a la vez.** Una pregunta concreta da mejores respuestas que "explícame todo".
- **Usa ejemplos genéricos.** Pide ejemplos que no sean tu desafío; así aprendes la herramienta y no copias la solución.
