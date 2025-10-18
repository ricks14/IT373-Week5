from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
    
    def clean_title(self):
        t = self.cleaned_data['title']
        if "test" in t.lower():
            raise forms.ValidationError("Title cannot contain the word 'test'.")
        if len(t) < 3:
            raise forms.ValidationError('Title too short.')
        return t

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'text': forms.Textarea(attrs={'placeholder': 'Write your comment here...'}),
        }
        error_messages = {
            'author': {
                'required': 'Please enter your name.',
                'max_length': 'Name too long.',
            },
            'text': {
                'required': 'Comment text cannot be empty.',
            },
        }