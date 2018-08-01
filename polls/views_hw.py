from django.http.response import HttpResponse
from django.shortcuts import render


def index_view(request):
    user_agent = request.META['HTTP_USER_AGENT']

    return HttpResponse('Your user agent is: {}'.format(user_agent))


def contact_us_view(request):
    welcoming_text = 'Hello students'
    result = None

    if request.method == 'POST':
        welcoming_text_text = 'You have submitted the form'
        email_address = (request.POST['Your email address'])
        topic = (request.POST['Enter the topic of your message'])
        message = (request.POST['Please, leave your message'])

    context = {

        'welcome_text': welcoming_text,
        'result': result,

    }
    return render(request, 'students.json', context=context)

