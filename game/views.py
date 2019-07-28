from django.shortcuts import HttpResponse,loader,HttpResponseRedirect
from random import randrange

# Create your views here.

def manage_guess(request):
    template = loader.get_template('number_guess.html')
    msg = 'Guess the number'
    button_title = 'CHECK'
    button_name = 'game'
    required = 'required'

    if 'user' not in request.session:
        request.session.set_expiry(0)
        rand_num = randrange(1,100)
        request.session['user']= rand_num

    if request.method == 'POST' and 'game' in request.POST:
        guess_num = int(request.POST.get('check'))
        num = request.session['user']
        if guess_num == num:
            msg = 'YOU WON'
            required = ''
            button_title = 'PLAY AGAIN'
            button_name = 'play_again'
            request.session.pop('user', None)
        else:
            if guess_num > num:
                diff=guess_num - num
                if diff>=10:
                    msg = 'Too High'
                else:
                    msg = 'High'
            else:
                diff=num - guess_num
                if diff>=10:
                    msg = 'Too low'
                else:
                    msg = 'low'
        if request.method == 'POST' and 'play_again' in request.POST:
            return HttpResponseRedirect('/./')
    return HttpResponse(template.render({'msg':msg,'button_title':button_title,'button_name':button_name,'required':required}, request))