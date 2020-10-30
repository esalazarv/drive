from app import app
from app.settings import config

if __name__ == "__main__":
    # use 0.0.0.0 to use it in container
    app.run(host='0.0.0.0', threaded=True, debug=config.get("app.debug"))