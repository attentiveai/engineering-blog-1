from celery import Celery
from celery_conf import celeryconfig


app = Celery()
app.config_from_object(celeryconfig,)

out = app.send_task('adder_task_app.adder', args=(1,2))
print(out.get())
