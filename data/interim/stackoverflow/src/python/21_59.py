from sqlalchemy import Table
from sqlalchemy.engine.base import Engine as sql_engine
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.automap import automap_base
import pandas as pd


def upsert_database(list_input: pd.DataFrame, engine: sql_engine, table: str, schema: str) -> None:
    if len(list_input) == 0:
        return None
    flattened_input = list_input.to_dict('records')
    with engine.connect() as conn:
        base = automap_base()
        base.prepare(engine, reflect=True, schema=schema)
        target_table = Table(table, base.metadata,
                             autoload=True, autoload_with=engine, schema=schema)
        chunks = [flattened_input[i:i + 1000] for i in range(0, len(flattened_input), 1000)]
        for chunk in chunks:
            stmt = insert(target_table).values(chunk)
            update_dict = {c.name: c for c in stmt.excluded if not c.primary_key}
            conn.execute(stmt.on_conflict_do_update(
                constraint=f'{table}_pkey',
                set_=update_dict)
            )
