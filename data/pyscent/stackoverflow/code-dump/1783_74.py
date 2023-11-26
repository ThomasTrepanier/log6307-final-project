def check_db(context):
    # Do the code for running "SELECT 1" in the DB
    return

updater.job_queue.run_repeating(check_db, interval=21600, first=21600)
