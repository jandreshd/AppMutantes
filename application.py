from flask import Flask
application = Flask(__name__)
# add a rule for the index page.
@application.route('/')
def hello_world():
    return "Hola Mundo! por fin lo lograste"

if __name__ == "__main__":
 # Setting debug to True enables debug output. This line should be
 # removed before deploying a production app.
 application.debug = True
 application.run()