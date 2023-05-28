from .models import *
from django.forms import ModelForm, TextInput, NumberInput, Select


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["name", "surname", "email"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
        }


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
        }


class ScoreForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].empty_label = 'Ссылка на студента не выбрана'
        self.fields['subject'].empty_label = 'Ссылка на предмет не выбрана'

    class Meta:
        model = Score
        fields = ["student", "subject", "value"]
        widgets = {
            "student": Select(attrs={
                'class': 'form-control'
            }),
            "subject": Select(attrs={
                'class': 'form-control'
            }),
            "value": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите оценку',
                'step': 1,
                'max': 5,
                'min': 1,
            }),
        }
