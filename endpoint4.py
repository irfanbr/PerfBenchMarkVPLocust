from locust import HttpLocust, TaskSet, task
 
class Transactions(TaskSet):
    @task
    def end4(ep):
        ep.client.get("/endpoint4")

class WorkModel(HttpLocust):
    task_set = Transactions
    min_wait = 0
    max_wait = 0
    stop_timeout = 300