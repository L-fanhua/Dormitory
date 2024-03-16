# _*_ coding: utf-8 _*_
from . import home
from flask import render_template,url_for
from app.home.form import Search
@home.route('/',methods=['GET','POST'])
def search():
    form = Search()
    if form.validate_on_submit():
        keyword = form.keyword.data
        return render_template(url_for('home.search',form=form))
    render_template(url_for('home.search',form=form))
