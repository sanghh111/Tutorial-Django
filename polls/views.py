import re
from django.shortcuts import render

from django.http import HttpResponse

from polls.models import Question
#HTTResponse làm được gì ????

def index(request):
    #nhận tham số requsest để làm gì.
    latest_question_list = Question.objects.all()[:5]
    output = ', '.join([ q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request,question_id):
    return HttpResponse("Câu hỏi số {_question_id}".format(_question_id = question_id))

def results(request,question_id):
    return HttpResponse("Câu hỏi số {_question_id}".format(_question_id = question_id))

def vote(request,question_id):
    return HttpResponse("Câu hỏi số {_question_id}".format(_question_id = question_id))