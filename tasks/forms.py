from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'deadline', 'owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
        
        self.fields["deadline"].widget.attrs["class"] += " my-custom-datepicker"

class TaskFilterForm(forms.Form):
    STATUS_CHOISES = (
        ('', 'All'),
        ('todo','To Do'),
        ('in_progress','In Progress'),
        ('done','Done'),
    )

    PRIORITY_CHOISES = (
        ('', 'All'),
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
    )

    status = forms.ChoiceField(choices=STATUS_CHOISES, label='Status', required=False)
    priority = forms.ChoiceField(choices=PRIORITY_CHOISES, label='Priority', required=False)