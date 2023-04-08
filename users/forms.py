from .models import Audios
from django import forms


class GenerateAudioFileForm(forms.ModelForm):
    SELECT_ACCENT = (
        ('co.uk', '-- Select one option --'),
        ('com.au', 'English (Australia)'),
        ('ca', 'English (Canada)'),
        ('co.in', 'English (India)'),
        ('ie', 'English (Ireland)'),
        ('com.uk', 'English (UK)'),
        ('us', 'English (US)'),
    )
    SELECT_FILE_TYPE = (
        (None, '-- Select audio format --'),
        ('.mp3', '.mp3'),
        ('.ogg', '.ogg'),
        ('.wav', '.wav')
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'What will be the name of your audio file?'}),
        label='Name',
        required=True,
        help_text='Name provided will be used as name of the generated audio file, e.g. <b>"my-speech", "project-presentation"</b>'
        )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Type your text ...'}),
        label='Text',
        required=True,
        help_text='This text that will be use to generate an audio file',
        )
    accent = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select'}),
        help_text='Select your preferred accent',
        label='Language accent',
        choices=SELECT_ACCENT,
        )
    file_type = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_FILE_TYPE)
    
    class Meta:
        model = Audios
        fields = '__all__'


class UploadAudioFileForm(forms.ModelForm):

    class Meta:
        model = Audios
        fields = []