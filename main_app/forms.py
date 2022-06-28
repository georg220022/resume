from django.forms import ModelForm, Textarea
from .models import MyProject

class PostForm(ModelForm):

    class Meta:
        model = MyProject
        fields = '__all__'
        labels = {
            "text": "Сообщение",
        }
        widgets = {
            'text': Textarea(attrs={'cols': 60, 'rows': 10}),
        }