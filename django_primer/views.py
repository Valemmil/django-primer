# -*- coding: utf-8 -*-
from collections import defaultdict
from statistics import fmean
from django.views.generic.base import TemplateView
from .models import Score, Student, Subject
from .forms import StudentForm, ScoreForm, SubjectForm
from django.shortcuts import redirect


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        scores = Score.objects.all()
        student_scores = defaultdict(dict)

        subjects = set()
        for score in scores:
            subject_name = score.subject.name
            subjects.add(subject_name)
            student_scores[score.student][subject_name] = score.value

        subjects = sorted(subjects)
        student_statistics = [
            {
                'student': student,
                'scores': [f'{scores[subject]:.1f}' for subject in subjects],
                'avg': fmean([scores[subject] for subject in subjects])
            }
            for student, scores in student_scores.items()
        ]
        context.update(
            {
                'subjects': subjects,
                'student_statistics': student_statistics
            }
        )
        return context


class EditSubject(TemplateView):
    template_name = "edit_subject.html"

    def post(self, request, *args, **kwargs):
        form = SubjectForm(request.POST)
        if form.is_valid() and not (form in Subject.objects.all()):
            form.save()
            return redirect('edit_subjects')

    def get_context_data(self, **kwargs):
        context = super(EditSubject, self).get_context_data(**kwargs)
        form = SubjectForm()
        subjects = Subject.objects.all()

        context.update(
            {
                'form': form,
                'subjects': subjects,
            }
        )
        return context


class EditStudent(TemplateView):
    template_name = "edit_student.html"

    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST)
        if form.is_valid() and not (form in Student.objects.all()):
            form.save()
            return redirect('edit_students')

    def get_context_data(self, **kwargs):
        context = super(EditStudent, self).get_context_data(**kwargs)
        form = StudentForm()
        students = Student.objects.all()

        context.update(
            {
                'form': form,
                'students': students,
            }
        )
        return context


class EditEvaluations(TemplateView):
    template_name = "edit_evaluations.html"

    def post(self, request, *args, **kwargs):
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edit_evaluations')

    def get_context_data(self, **kwargs):
        context = super(EditEvaluations, self).get_context_data(**kwargs)

        form = ScoreForm()
        scores = Score.objects.all()

        context.update(
            {
                'form': form,
                'students_scores': scores,
            }
        )
        return context
