from django import forms
from core.models import NovoTopico, Post

class NovoTopicoForm(forms.ModelForm):
    class Meta:
        model = NovoTopico
        fields = "__all__"

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
