bind = '0.0.0.0:5000'
workers = 1
accesslog = '-'
loglevel = 'error'
timeout = 120
capture_output = True
enable_stdio_inheritance = True
proc_name = "gunicorn"
