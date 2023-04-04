from flaskapp import create_app
from flaskapp.config import ProdConfig

app = create_app(ProdConfig)
if __name__ == '__main__':
    app.run(debug=True)
