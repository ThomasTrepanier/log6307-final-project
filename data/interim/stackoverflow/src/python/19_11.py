def permanently_delete_experiments_on_mlflow(list_of_experiments_id: list):
    mlflow_client = MlflowClient(tracking_uri=YOUR_EC2_TRACKING_URI)
    commands = []
    for experiment_id in list_of_experiments_id:
        print(f'deleting experiment {experiment_id}')
        os.system(f"aws s3 rm {YOUR_S3_ARTIFACTS_STORE} "
                  f"--recursive --exclude '*' --include '{experiment_id}/*'")
        try:
            mlflow_client.delete_experiment(experiment_id)
        except Exception as e:
            print_red(f'failed to execute mlflow_client.delete_experiment({experiment_id}) \n {str(e)}')
        commands.append(f"YOUR_PATH_TO_DATABASE_ON_EC2{os.sep}database.db{os.sep}{experiment_id} ")
        commands.append(f"YOUR_PATH_TO_DATABASE_ON_EC2{os.sep}database.db{os.sep}.trash{os.sep}{experiment_id} ")
    # format commands to send via ssh to EC2
    commands = f"ssh -i {YOUR_EC2_SSH_KEY_PATH} ubuntu@{YOUR_EC2_IP} rm -r " \
               + ' '.join(commands)
    print('executing on EC2 the following command: \n   ', commands)
    result = subprocess.Popen(commands, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    response, err = result.communicate()
    print('response:', response)
