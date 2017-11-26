from django import forms
from theWall.models import Post


'''
Class: PostForm

Description:
this is a django specific class. It is used to create the structure of a web form. It has built in restrictions
for length and such. This particular form is for the user to post their message to the site. it integrates with the 
post model.
'''
class PostForm(forms.ModelForm):
    key = forms.CharField(widget=forms.TextInput(attrs={'style' : 'color:black'}), required=True, max_length=140, help_text="Key")
    content = forms.CharField(widget=forms.TextInput(attrs={'style' : 'color:black'}), help_text="Post Content: ")

    class Meta:
        model = Post
        fields = ('key', 'content',)


'''
Class: KeyForm

Description:
this is a django specific class. It is used to create the structure of a web form. It has built in restrictions
for length and such. This particular form does not interact with the database. It is used to take user input of a "key"
so that they can see if their key decrypts any message.
'''
class KeyForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={'style' : 'color:black'}), required=True, max_length=140, help_text="Key")

    class Meta:
        fields = ('key',)