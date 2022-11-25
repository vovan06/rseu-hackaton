from django.shortcuts import render
from rest_framework.views import APIView
from .models import Exam
from .serializers import ExamSerializer
class ExamAPIView(APIView):
    def get (self, request) :
        e = Exam.objects.all()
        return Response({'posts': ExamSerializer(e, many=True).data})
    def post (self, request):
        post_new = Exam.objects.create(
            title=request.data['title'],
            content=request. data[ 'content'],
            cat_id=request.data['cat_id']
            )
        return Response({'post': ExamSerializer(post_new).data})
