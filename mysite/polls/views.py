from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at questing %s." % question_id)

def results(request, queston_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % queston_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)

