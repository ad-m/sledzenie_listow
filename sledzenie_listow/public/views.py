# -*- coding: utf-8 -*-
'''Public section, including homepage and signup.'''
from flask import (Blueprint, request, render_template)

from sledzenie_listow.public.forms import SearchForm
from sledzenie_listow.utils import flash_errors
from .utils import quest_range
blueprint = Blueprint('public', __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    return render_template("public/home.html")


@blueprint.route("/search/", methods=['GET', 'POST'])
def search():
    context = {}
    form = SearchForm(request.form, csrf_enabled=False)
    resultset = []
    context['form'] = form
    if form.validate_on_submit():
        resultset = quest_range(form.start.data, form.end.data)
    else:
        flash_errors(form)
    context['resultset'] = resultset

    return render_template('public/search.html', **context)


@blueprint.route("/about/")
def about():
    return render_template("public/about.html")
