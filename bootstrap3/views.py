from django.contrib.auth import login as login_user, logout as logout_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

def login(request):
    """Attempt to log a user in."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login_user(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'form.html', {
        'title':       'Login',
        'form':        form,
        'form_action': 'Login',
    })

@login_required
def logout(request):
    """Log the current user out."""
    logout_user(request)
    return redirect('home')
