from config import *

app = DevelopmentConfig()

if __name__ == "__main__":
    from Application.controllers import *
    app.run(debug=True, port=8080)