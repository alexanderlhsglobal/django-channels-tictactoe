from django.http.response import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class Index(View):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        room_code = request.POST.get('room_code')
        char_choice = request.POST.get('character_choice')
        return redirect('game', room_code, char_choice)

class Game(View):
    template_name = 'game.html'
    
    def get(self, request, *args, **kwargs):
        choice = kwargs['choice']
        room_code = kwargs['room_code']
        
        if choice not in ['X', 'O']: raise Http404('Choice does not exist')
        
        context = {
            'char_choice' : choice,
            'room_code' : room_code
        }
        
        return render(request, self.template_name, context)