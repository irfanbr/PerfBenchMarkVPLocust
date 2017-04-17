from locust import HttpLocust, TaskSet
 
def end1(ep):
        ep.client.get("/endpoint1")
    
def end2(ep):
        ep.client.get("/endpoint2")
    
def end3(ep):
        ep.client.get("/endpoint3")
    
def end4(ep):
        ep.client.get("/endpoint4") 

class Transactions(TaskSet):
	tasks = {end1: 1, end2: 1, end3: 1, end4: 1}      
    
class WorkModel(HttpLocust):
    task_set = Transactions
    min_wait = 0
    max_wait = 0
    stop_timeout = 1800