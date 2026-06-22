# Optimización SQL

Esta carpeta compara dos consultas sobre la tabla `jobs`:

- `opt_before.sql`: aplica una función y una búsqueda con comodín, lo que fuerza un escaneo completo.
- `opt_after.sql`: filtra y ordena usando columnas numéricas, una forma más adecuada para aprovechar índices.

El plan de ambas consultas se puede comparar desde la raíz del repositorio con:

```bash
python scripts/sql_opt_demo.py
```
