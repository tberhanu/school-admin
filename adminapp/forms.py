from django import forms
from adminapp.models import Post

class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ask or comment here...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)
###################################
