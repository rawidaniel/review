#!/usr/bin/python3

"""
Run flask application
"""
from website import create_app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)