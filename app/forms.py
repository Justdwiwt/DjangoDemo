from django.forms import ModelForm
from app.models import Moment


class MomentForm(ModelForm):
    class Meta:
        model = Moment
        # 导入所有字段
        fields = '__all__'
