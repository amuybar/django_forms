from django import forms

from myforms.models import Contact,Post


class ContactForm(forms.ModelForm):
    # FORM MODEL
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
    # EMAIL VALIDATION
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('Please enter a valid email address.')
        return email
    # FOR STYLING OUR FORM
    def __init__(self,*args,**kwargs):
        super(ContactForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Enter your full name',
        })
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Enter your email address'
        })
        self.fields['message'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Enter your message',
        })

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','summary','content']
    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Enter Post title',
        })
        self.fields['summary'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Enter Post summary',
        })
        self.fields['content'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Enter Post content',
        })