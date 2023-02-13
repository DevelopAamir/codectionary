from .models import Creator, Content
from django.forms import ModelForm

class CreatorForm(ModelForm):
    class Meta:
        model = Creator
        fields = '__all__'
       
class UploadContentForm(ModelForm):
    class Meta:
        model = Content
        fields = '__all__'