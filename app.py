from bottle import *
import random

@route('/')
def index():
    return 'Heads!' if random.randint(0,1) == 1 else 'Tails'

@route('<name:re:.*>')
def index(name):
    redirect('/')

run(host='localhost', port=8080, reloader=True)
