import time

def handler(event,context):
    print(time.now())
    print(event)
    return {
        status: 200
        message: another_function(event)
    }

def another_function(event):
    return 'success!!!!'
