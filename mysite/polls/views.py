from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello, world. you're at the polls index")

def detail(request, question_id):
    return HttpResponse("You're looking at questing %s." % question_id)

def results(request, queston_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % queston_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)

