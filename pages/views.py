from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail as sm
from django.utils.html import strip_tags


# Create your views here.
def home(request):
    template = 'home.html'

    propt = {}

    return render(request, template, propt)


def send_mail(request):
    print("send email")
    recipient = request.GET.get('email', None)
    subject = "test subject"
    message = "test"
    sender = 'baltschun.bot@gmail.com'

    html_message = render_to_string('test.html', {'context': 'values'})
    plain_message = strip_tags(html_message)

    if sender and message:
        res = sm(
            subject=subject,
            message=plain_message,
            from_email=sender,
            recipient_list=[recipient],
            fail_silently=False,
            html_message=html_message
        )

        return HttpResponse("send email success")
    return HttpResponse("email sender and message cant be empty")
