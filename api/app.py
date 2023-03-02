from api import create_app

app = create_app('default')
app_context = app.app_context()
app_context.push()

@app.route("/")
def home():
    return "<h1>Microservicio RecepcionOrden</h1>"