from django.core import serializers
from django.db import models
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Exam
from rest_framework.response import Response


serializers.serialize('json', Exam.objects.all())

class Exam:
    def __init__(self, title, discription, photo, answer, date):
        self.title = title
        self.discription = discription
        self.photo = photo
        self.answer = answer
        self.date = date

class ExamSerializer(serializers.Serializer):
    title = models.CharField(max_length=255)
    discription = models.TextField(max_length=4096)
    photo = models.ImageField(upload_to='exam_tasks/%Y/%m/%d', null=True)
    answer = models.CharField(max_length=255)

def serialize_exam(exam):
    return {
        'title': exam.title,
        'discription': exam.discription,
        'photo': exam.photo,
        'answer': exam.answer,
        'date': exam.date
    }

def deserialize_form(exam_data):
    return Exam(
        title=exam_data['title'],
        discription=exam_data['discription'],
        photo=exam_data['photo'],
        answer=exam_data['answer'],
        date=exam_data['date'],
    )