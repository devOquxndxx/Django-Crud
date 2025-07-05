# importamos el formulario de creacion de usuario de Django
from django.contrib.auth.forms import UserCreationForm
# importamos el modelo de creacion de usuario de Django
from django.contrib.auth.models import User
# importamos el modulo de formulario para crear formularios personalizados
from django import forms
# importamos el modelo de models.py y poder manejar los datos de la base de datos
from .models import Record

# creamos el formulario de registro de usuario basado en UserCreationForm

class SignUpForm(UserCreationForm):
    # campo de correo electronico
    email = forms.EmailField(
        label = "",
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo Electronico'
        })
    )
    # campo de nombre de usuario
    firstName = forms.CharField(
        label = "",
        max_length = 100,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre (Nombre real)'
        })
    )
    
    # campo de apellido
    lastName = forms.CharField(
        label = "",
        max_length = 100,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apellido'
        })
    )
    
    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email', 'password1', 'password2')
        
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario (Para el login)'
        self.fields['username'].label = ''
        self.fields['username'].help_text = (
            '<span class="form-text text-muted"><small>Requerido. 150 caracteres o menos. Letras, números y @/./+/-/_ solamente.</small></span>'
        )
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = (
            '<ul class="form-text text-muted small">'
            '<li>La contraseña no debe parecerse a tu información personal.</li>'
            '<li>Debe contener al menos 8 caracteres.</li>'
            '<li>No debe ser una contraseña comúnmente usada.</li>'
            '<li>No debe ser totalmente numérica.</li>'
            '</ul>'
        )
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = (
            '<span class="form-text text-muted"><small>'
            'Introduce la misma contraseña que antes, para verificación.'
            '</small></span>'
        )
        
# Formulario para crear un nuevo registro del modelo Record
class AddRecordForm(forms.ModelForm):
    firstName = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre'
        }),
        label=""
    )
    
    lastName = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apellido'
        }),
        label=""
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.widgets.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo Electronico'
        }),
        label=""
    )
    
    phone = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Telefono'
        }),
        label=""
    )
    
    address = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Direccion'
        }),
        label=""
    )
    
    city = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ciudad'
        }),
        label=""
    )
    
    state = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Estado'
        }),
        label=""
    )
    
    zipCode = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Codigo Postal'
        }),
        label=""
    )
    
    class Meta:
        model = Record
        exclude = ('user',)  # Excluimos el campo 'user' ya que se asigna automáticamente


class AddRecordForm(forms.ModelForm):
    # Campo para el primer nombre, requerido, con placeholder y clase CSS.
    firstName = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"}),
        label=""
    )


    # Campo para el apellido, requerido, con placeholder y clase CSS.
    lastName = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Apellido", "class": "form-control"}),
        label=""
    )


    # Campo para el correo electrónico, requerido, con placeholder y clase CSS.
    email = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Correo electrónico", "class": "form-control"}),
        label=""
    )


    # Campo para el teléfono, requerido, con placeholder y clase CSS.
    phone = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Teléfono", "class": "form-control"}),
        label=""
    )


    # Campo para la dirección, requerido, con placeholder y clase CSS.
    address = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Dirección", "class": "form-control"}),
        label=""
    )


    # Campo para la ciudad, requerido, con placeholder y clase CSS.
    city = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Ciudad", "class": "form-control"}),
        label=""
    )


    # Campo para el estado/departamento, requerido, con placeholder y clase CSS.
    state = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Departamento/Estado", "class": "form-control"}),
        label=""
    )


    # Campo para el código postal, requerido, con placeholder y clase CSS.
    zip_code = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Código postal", "class": "form-control"}),
        label=""
    )


    # Define el modelo asociado y los campos excluidos.
    class Meta:
        model = Record  # El formulario se basa en el modelo Record.
        exclude = ("user",)  # El campo user se excluye porque se asigna automáticamente en la vista.


