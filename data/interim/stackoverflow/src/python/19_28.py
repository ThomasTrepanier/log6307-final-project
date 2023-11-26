import functools

def your_func(value1):
    return ""

trigger_report = PythonOperator(
    task_id="aaaa",
    python_callable=functools.partial(your_func, value1=1),
    provide_context=True,
    dag=dag
)
