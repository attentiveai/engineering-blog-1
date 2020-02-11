from celery import Celery
from celery_conf import celeryconfig
 
app = Celery()
app.config_from_object(celeryconfig,)
 
@app.task
def adder(x, y):
   return x + y