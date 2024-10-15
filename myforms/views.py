from django.shortcuts import render
from .forms import ContactForm, PostForm


# Create your views here.
def home_view(request):
    if request.method== 'POST':
        form = ContactForm(request.POST)
        post_form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
        post_form = PostForm()
    return render(request,
                  'home.html',
                  {'form':form, 'post_form':post_form},

                  )