from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Quiz, Question

# Create your views here.


def index(request):
    # return HttpResponse("This will eventually be a list of quizzes...")
    latest_quiz_list = Quiz.objects.order_by('id')
    template = loader.get_template('quiz/index.html')
    context = {
        'latest_quiz_list': latest_quiz_list,
    }
    return HttpResponse(template.render(context, request))


# when you click on a quiz, this will show all the questions in the quiz 
def detail(request, quiz_id):
    questions = get_list_or_404(Question, quiz_foreign_key=quiz_id)
    context = {'questions': questions, 'quiz': Quiz.objects.get(id=quiz_id) }
    return render(request, "quiz/detail.html", context)
    # return render(request, 'quiz/detail.html', {'question': questions})
