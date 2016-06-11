from . import app
from . import db
from models import Problem
from forms import ProblemForm
from flask import render_template, redirect, url_for

problems_per_page = 20


@app.route('/problems')
def problems():
    problems = Problem.query.order_by(Problem.id).all()
    return render_template('problems.html', problems=problems)


@app.route('/new-problem', methods=['GET', 'POST'])
def new_problem():
    form = ProblemForm()
    if form.validate_on_submit():
        problem = Problem(
            link=form.link
        )
        db.session.add(problem)
        db.commit()
        return redirect(url_for('.problems'))
    return render_template('new_problem.html', form=form)
