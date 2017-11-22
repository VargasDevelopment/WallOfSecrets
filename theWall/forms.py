from django import forms
from theWall.models import Post

class PostForm(forms.ModelForm):
    key = forms.CharField(widget=forms.TextInput(attrs={'style' : 'color:black'}), required=True, max_length=140, help_text="Key")
    content = forms.CharField(widget=forms.TextInput(attrs={'style' : 'color:black'}), help_text="Post Content: ")

    class Meta:
        model = Post
        fields = ('key', 'content',)