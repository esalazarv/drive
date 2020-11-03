from app import application

if __name__ == "__main__":
    app = application()
    # use 0.0.0.0 to use it in container
    app.run(host='0.0.0.0', threaded=True)