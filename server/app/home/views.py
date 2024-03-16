# _*_ coding: utf-8 _*_
from . import home
from flask import render_template,url_for
from app.home.form import Search

@home.route('/',methods=['GET','POST'])
def search():
    form = Search()
    print("ok")
    if form.validate_on_submit():
        print("ok")
        keyword = form.keyword.data
        print(keyword)
        return render_template("home/search.html",form=form)
    return render_template("home/search.html",form=form)
