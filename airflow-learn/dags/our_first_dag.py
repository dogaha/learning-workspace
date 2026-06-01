from airflow.sdk import dag, task
from datetime import datetime

@dag(dag_id="test_dag", schedule="@daily",start_date=datetime(2026,6,1)) # make sure dag id is unique
def my_dag(): # if no dag_id, function name is used
    @task(task_id="training_model_x") # python operator
    def training_model_a():
        return 1
    
    @task
    def training_model_b():
        return 2

    @task
    def training_model_c():
        return 3
    
    @task.branch
    def choose_best_model(accuraccies: list[int]): #return task you want to run next
        if max(accuraccies) > 2:
            return "accurate"
        return "inaccurate"
    
    @task.bash # bash operator
    def accurate():
        return "echo 'accurate'"
    
    @task.bash
    def inaccurate():
        return "echo 'inaccurate'"

    # running any training model will run choose best model after
    # [training_model_a(), training_model_b(), training_model_c()] >> choose_best_model() > [accurate(),inaccurate()]

    #create list of accuracies and send into model
    accuracies = [training_model_a(), training_model_b(), training_model_c()]
    choose_best_model(accuracies) >> [accurate(),inaccurate()]

my_dag()