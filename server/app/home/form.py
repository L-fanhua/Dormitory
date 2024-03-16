# _*_ coding: utf-8 _*_
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class Search(FlaskForm):
    keyword = StringField(
        validators=[
            DataRequired("请输入搜索关键词！")
        ],
        description="搜索关键词",
        render_kw={
            "placeholder": "请输入搜索关键词！",
        }
    )