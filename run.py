#!/usr/bin/python3
from flaskblog import app

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
