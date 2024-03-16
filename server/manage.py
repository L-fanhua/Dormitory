# _*_ codding:utf-8 _*_
from app import create_app

from flask import render_template

app = create_app()
app.config['SECRET_KEY']="123456"

@app.errorhandler(404)
def page_not_found(error):
    """
    404
    """
    return render_template("home/404.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
