import time
import random

from polls.models import Question, Choice
from datetime import datetime

from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings

from polls.helpers import calculate_sum


def index_view(request):
    user_agent = request.META['HTTP_USER_AGENT']
    db = settings.DATABASES['default']['ENGINE']

    return HttpResponse('Your user agent is: {}, DB is: {}'.format(user_agent, db))


def contact_us_view(request):
    welcome_text = 'You opened page'
    result = None
    circles = []

    if request.method == 'POST':
        welcome_text = 'You have submitted form'
        number_a = int(request.POST['number_a'])
        number_b = int(request.POST['number_b'])

        result = calculate_sum(number_a, number_b)

        random_color = lambda: random.randint(0, 255)

        for n in range(result):
            color = 'rgb({r}, {g}, {b})'.format(
                r=random_color(),
                g=random_color(),
                b=random_color()
            )
            circles.append({
                'name': '#%s' % n,
                'color': color
            })

    context = {
        'current_time': time.strftime('%H:%M:%S %A'),
        'welcome_text': welcome_text,
        'result': result,
        'circles': circles
    }

    return render(request, 'contact_us.html', context=context)


def questions(request):
    if request.method == 'POST':
        text = request.POST['text']
        q = Question(question_text=text, pub_date=datetime.utcnow())
        q.save()


    questions = Question.objects.all()

    return render(request, 'questions.html', context={'questions': questions})


def question_detail(request, question_pk):

    question = Question.objects.get(id=int(question_pk))

    if request.method == 'POST':
        text = request.POST['text']
        Choice.objects.create(question=question, choice_text=text)

    return render(request, 'question_detail.html', context={'question': question})