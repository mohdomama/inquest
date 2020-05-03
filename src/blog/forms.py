from django import forms
from .models import BlogPost

# class BlogPostForm(forms.Form):
#     title = forms.CharField()
#     slug = forms.SlugField()
#     content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    # Non redundant approach is to use ModelForms
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if 'omama' in title:
            raise forms.ValidationError(
                "Title can't contain developer name")
        return title
