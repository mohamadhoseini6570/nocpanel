from django import forms
from .models import Agent
from django.forms.models import inlineformset_factory, InlineForeignKeyField
from django.core.exceptions import ValidationError

class AgentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs=
        {'class': 'form-control'}), max_length=10, label='نام',
        error_messages={'required':'پرش کن!'},
        required=True, help_text='نام نماینده را وارد کنید') # CharField has default widget
    # of TextInput, that renders the HTML code <input type="text" ...>.
    email = forms.EmailField(widget=forms.TextInput(attrs=
        {'class': 'form-control'}), label='ایمیل',
        error_messages={'max_length':'ddd'}) # EmailField() has the default widget of 
        # EmailInput and renders as <input type="email" ...>
        # This field also uses the built-in Django validation EmailValidator that
        # requires an @ symbol within the input for it to be considered valid.
    phone = forms.CharField(widget=forms.TextInput(attrs=
        {'class': 'form-control'}), max_length=11, label='تلفن',
        help_text='تلفن نماینده را وارد کنید')
    mobile = forms.CharField(widget=forms.TextInput(attrs=
        {'class': 'form-control'}), max_length=11, label='موبایل')
    role_choices = (
        ('فنی', 'فنی'),
        ('بازرگانی', 'بازرگانی'),
        ('حقوقی', 'حقوقی'),
    ) 
    # role = forms.CharField(widget=forms.Select(choices=role_choices)
    # , label='نقش') this works also like the next line
    role = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}), choices=role_choices, label='نقش')
    notes = forms.CharField(widget=forms.Textarea(
        attrs={'rows':3, 'class': 'form-control'}), label='توضیحات') #  if you are looking to add a multi-line input field to your
        #form, add the Textarea widget to CharField(). Textarea widget renders the 
        # field as <textarea>...</textarea>,
    # notes = forms.Textarea(label='توضیحات') # this doesnt work also like the previous line
    error_css_class = 'error'
    required_css_class = 'bold'

    def __init__(self, *args, **kwargs):
        initial_arguments = kwargs.get('initial', None)
        updated_initial = {}
        if initial_arguments:
            user = initial_arguments.get('user', None)
            if user:
                updated_initial['name'] = getattr(user, 'username', None)
                updated_initial['email'] = getattr(user, 'email', None)
                updated_initial['notes'] = getattr(user, 'is_superuser', None)
        kwargs.update(initial = updated_initial)
        super(AgentForm, self).__init__(*args, **kwargs)
# ----------------------------------------------------------------------

class AgentForm2(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=
        {'class': 'form-control'}), max_length=10, label='نام',
        error_messages={'required':'پرش کن!'},
        required=True, help_text='نام نماینده را وارد کنید') 
    email = forms.EmailField(widget=forms.TextInput(attrs=
        {'class': 'form-control'}), label='ایمیل',
        error_messages={'max_length':'ddd'}) 
    phone = forms.CharField(widget=forms.TextInput(attrs=
        {'class': 'form-control'}), max_length=12, label='تلفن',
        help_text='تلفن نماینده را وارد کنید')
    mobile = forms.CharField(widget=forms.TextInput(attrs=
        {'class': 'form-control'}), max_length=13, label='موبایل')
    role_choices = (
        ('فنی', 'فنی'),
        ('بازرگانی', 'بازرگانی'),
        ('حقوقی', 'حقوقی'),
    )
    role = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}), choices=role_choices, label='نقش')
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'class': 'form-control'})
        , label='توضیحات') 
    error_css_class = 'error'
    required_css_class = 'bold'
    
    class Meta: 
        model = Agent
        fields = '__all__'
    
