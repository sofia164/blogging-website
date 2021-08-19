from django import forms

from .models import Post, Category, Comment

choices = Category.objects.all().values_list('category_name', 'category_name')

choice_list=[]

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('post_title', 'category', 'post_body', 'snippet', 'header_image')

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'post_body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add some text'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add some text'}),

        }


