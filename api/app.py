from api import create_app
from config import db

app = create_app('default')
app_context = app.app_context()
app_context.push()

