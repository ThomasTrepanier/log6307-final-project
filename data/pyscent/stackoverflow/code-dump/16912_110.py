class BigQueryToXOperator(BaseOperator):
    template_fields = ['sql']
    ui_color = '#000000'

    @apply_defaults
    def __init__(
            self,
            sql,
            keys,
            bigquery_conn_id='bigquery_default',
            delegate_to=None,
            *args,
            **kwargs):
        super(BigQueryToXOperator, self).__init__(*args, **kwargs)
        self.sql = sql
        self.keys = keys # A list of keys for the columns in the result set of sql
        self.bigquery_conn_id = bigquery_conn_id
        self.delegate_to = delegate_to


    def execute(self, context):
        """
        Run query and handle results row by row.
        """
        cursor = self._query_bigquery()
        for row in cursor.fetchall():
            # Zip keys and row together because the cursor returns a list of list (not list of dicts)
            row_dict = dumps(dict(zip(self.keys,row))).encode('utf-8')

            # Do what you want with the row...
            handle_row(row_dict)


    def _query_bigquery(self):
        """
        Queries BigQuery and returns a cursor to the results.
        """
        bq = BigQueryHook(bigquery_conn_id=self.bigquery_conn_id,
                          use_legacy_sql=False)
        conn = bq.get_conn()
        cursor = conn.cursor()
        cursor.execute(self.sql)
        return cursor
