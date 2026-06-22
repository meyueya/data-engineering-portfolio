# DBT Project

Este proyecto DBT está configurado para usar SQLite (mediante `dbt-sqlite`).

## Modelos

| Modelo | Capa | Descripción |
|---|---|---|
| `stg_customers.sql` | staging | Limpia los clientes de la seed, normaliza el email y convierte la fecha de alta. |
| `stg_orders.sql` | staging | Normaliza los pedidos, convierte importes y fechas, y estandariza el estado. |
| `dim_customers.sql` | marts | Crea una dimensión de clientes con sus datos maestros. |
| `fct_orders.sql` | marts | Crea la tabla de hechos de pedidos y la relaciona con la dimensión de clientes. |

El proyecto conserva además `stg_jobs.sql` y `jobs_summary.sql` como ejemplo de análisis de ofertas de empleo.

## Tests

Los tests están declarados en `models/marts/schema.yml`:

- `unique`: comprueba que las claves de clientes y pedidos no se repitan.
- `not_null`: valida las claves y campos obligatorios.
- `relationships`: comprueba que cada `customer_id` de `fct_orders` exista en `dim_customers`.

## Ejecución

```bash
# desde la raíz del repo
bash scripts/setup_env.sh
bash scripts/run_dbt.sh
```

También se pueden ejecutar los comandos directamente desde `dbt_project/`:

```bash
dbt seed --profiles-dir .
dbt run --profiles-dir .
dbt test --profiles-dir .
dbt docs generate --profiles-dir .
```

## Notas

- `profiles.yml` está incluido en `dbt_project/` y el script `run_dbt.sh` exporta `DBT_PROFILES_DIR` apuntando a esa carpeta.
- `seeds/` contiene los datos de ejemplo que se cargan con `dbt seed`.
- Los modelos se organizan en `models/staging/` y `models/marts/`.
