from django.shortcuts import  render
from django . core . mail import send_mail
from django . conf import settings



# Create your views here.
def home(request):
    if request.method == 'POST':
        message = request.POST['email']
        send_mail('contact form',
        message,
        settings.EMAIL_HOST_USER,
        ['irshad.city9@gmail.com'],
        fail_silently=False)

    return render(request,'index.html')