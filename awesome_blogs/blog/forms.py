from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta():
        model=Post
        fields=('author','title','text')
    # adding the widgets now
        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={"class":'editable medium-editor-textarea postcontent'})
            # textinnputclass and poscontent is our own css class
        }

class CommentForm(forms.ModelForm):
    class Meta():
        mmodel = Comment
        fields= ('author','text')

        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'})
            'text':forms.Textarea(attrs={"class":'editable medium-editor-textarea'})
        }
