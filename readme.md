The app1 works as expected. The app2 tries to use just a bit of app factory
pattern and no code change, so WHY request to app2 results in 'No
application found' in spawned thread code ?


```
Exception in thread Thread-2:
Traceback (most recent call last):
  File "/XXX/flaskthreading/venv/lib/python3.9/site-packages/sqlalchemy/util/_collections.py", line 1008, in __call__
127.0.0.1 - - [07/Jun/2022 14:06:53] "GET / HTTP/1.1" 200 -
    return self.registry[key]
KeyError: <greenlet.greenlet object at 0x7f4f541ad040 (otid=0x7f4f54199d00) current active started main>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3.9/threading.py", line 954, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.9/threading.py", line 892, in run
    self._target(*self._args, **self._kwargs)
  File "/XXX/flaskthreading/app2/views.py", line 12, in printer
    print(User.query.all())
  File "/XXX/flaskthreading/venv/lib/python3.9/site-packages/flask_sqlalchemy/__init__.py", line 552, in __get__
    return type.query_class(mapper, session=self.sa.session())
  File "/XXX/flaskthreading/venv/lib/python3.9/site-packages/sqlalchemy/orm/scoping.py", line 47, in __call__
    sess = self.registry()
  File "/XXX/flaskthreading/venv/lib/python3.9/site-packages/sqlalchemy/util/_collections.py", line 1010, in __call__
    return self.registry.setdefault(key, self.createfunc())
  File "/XXX/flaskthreading/venv/lib/python3.9/site-packages/sqlalchemy/orm/session.py", line 4225, in __call__
    return self.class_(**local_kw)
  File "/XXX/flaskthreading/venv/lib/python3.9/site-packages/flask_sqlalchemy/__init__.py", line 174, in __init__
    self.app = app = db.get_app()
  File "/XXX/flaskthreading/venv/lib/python3.9/site-packages/flask_sqlalchemy/__init__.py", line 1042, in get_app
    raise RuntimeError(
RuntimeError: No application found. Either work inside a view function or push an application context. See http://flask-sqlalchemy.pocoo.org/contexts/.
```


## MVP Usage

```
git clone
pip install -r requirements.txt

# working app
FLASK_APP=app1 flask run
curl http://localhost:5000/

# produces error
FLASK_APP=app2.app flask run
curl http://localhost:5000/
```
