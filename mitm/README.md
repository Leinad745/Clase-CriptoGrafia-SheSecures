# Doble Candado

**Categoría:** Crypto · **Dificultad:** Fácil · **Formato de flag:** `SheSecures{...}`
**Archivos:** `chall.py`, `output.txt`

---

## Historia

Son las 3:14 de la madrugada. La pantalla de **5ub4k3m1** es la única luz encendida en el departamento.

Hace semanas que sigue la pista de **Cerbero**, un grupo que vende accesos robados en foros clandestinos. Esta noche, por fin, su sniffer capturó tráfico de uno de sus servidores. Entre cientos de paquetes encontró dos que llaman su atención:

- Un **mensaje de bienvenida** que el servidor envía automáticamente a cada nuevo miembro. 5ub4k3m1 ya lo había visto en texto plano al infiltrarse en el foro: `"Hola, bienvenida!"`. Ahora tiene **ese mismo mensaje, cifrado**.
- Un **mensaje privado** entre los administradores, cifrado con las **mismas llaves**. Ese es el que le interesa.

En un repositorio mal configurado también encontró el script que usan para cifrar.

Los administradores de Cerbero confían en su **doble candado**. 5ub4k3m1 sabe que dos candados débiles no hacen uno fuerte, y que no necesita abrirlos uno después del otro: puede atacarlos **desde los dos lados a la vez** y encontrarse **en el medio**.

**Ayuda a 5ub4k3m1 a descifrar el mensaje privado de Cerbero.**
