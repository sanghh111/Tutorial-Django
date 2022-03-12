import re
from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from polls.models import Question
#HTTResponse làm được gì ????

def index(request):
    #nhận tham số requsest để làm gì.
    latest_question_list = Question.objects.all()[:5]

    template = loader.get_template("polls/index.html")

    context = {
        'latest_question_list' : latest_question_list,
    }

    return HttpResponse(template.render(context,request))

def detail(request,question_id):
    return HttpResponse("Câu hỏi số {_question_id}".format(_question_id = question_id))

def results(request,question_id):
    return HttpResponse("Câu hỏi số {_question_id}".format(_question_id = question_id))

def vote(request,question_id):
    return HttpResponse("Câu hỏi số {_question_id}".format(_question_id = question_id))