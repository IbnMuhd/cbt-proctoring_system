from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from app import app, db
from models import User, Exam, Question

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    exams = Exam.query.all()
    return render_template('dashboard.html', exams=exams)

@app.route('/exam/<int:exam_id>')
@login_required
def take_exam(exam_id):
    questions = Question.query.filter_by(exam_id=exam_id).all()
    return render_template('exam.html', questions=questions)

