from django.contrib.gis.db.backends.postgis.base import (
     DatabaseWrapper as PostGISDatabaseWrapper,
)

class DatabaseWrapper(PostGISDatabaseWrapper):
    def prepare_database(self):
        # This is the overwrite - we don't want to call the
        # super() because of a faulty extension creation
     pass
