from south.db import db
model_class = generate_my_model_class()
fields = [(f.name, f) for f in model_class._meta.local_fields]
table_name = model_class._meta.db_table
db.create_table(table_name, fields)
# some fields (eg GeoDjango) require additional SQL to be executed
db.execute_deferred_sql()
