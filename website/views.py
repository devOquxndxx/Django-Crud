from django.shortcuts import render, redirect
# lo que sigue para importar es para autenticar, loguear y desloguear usuarios
from django.contrib.auth import authenticate, login, logout
# Importa el sistema de mensajes de Django para mostrar notificaciones al usuario.
from django.contrib import messages
# Importa los formularios personalizados para el registro de usuarios y la adición de registros.
# Estos formularios se definen en el archivo forms.py.
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django.core.paginator import Paginator


def home(request):
    # Renderiza la plantilla 'home.html' y la retorna como respuesta HTTP.
    # No se pasan datos adicionales al contexto (diccionario vacío).
    # Obtiene todos los registros de la base de datos.
    records = Record.objects.all()
    paginator = Paginator(records, 10)  # 10 registros por página
    # Obtiene el número de página de la solicitud GET.
    page_number = request.GET.get('page')
    # Obtiene la página actual de registros.
    records = paginator.get_page(page_number)
    if request.method == 'POST':
        # Obtiene el nombre de usuario del formulario.
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # Verifica las credenciales del usuario.
        # Si el usuario es autenticado correctamente, se inicia sesión.
        if user is not None:  # si el usuario es autenticado correctamente procede a inicar sesion
            login(request, user)
            messages.success(request, "Has iniciado sesion 👋")
            return redirect('home')
        else:
            # Si las credenciales son incorrectas, se muestra un mensaje de error.
            messages.error(request, "Credenciales incorrectas 🚫")
            return redirect('home')
    else:
        # Si el método de la solicitud no es POST, simplemente renderiza la plantilla 'home.html'.
        return render(request, 'home.html', {'records': records})


def login_user(request):
    pass


def logout_user(request):
    logout(request)  # Cierra la sesión del usuario.
    # Muestra un mensaje de éxito al usuario.
    # Muestra un mensaje de éxito al usuario.
    messages.success(request, "You Have Been Logged Out!")
    # Redirige al usuario a la página de inicio (home).
    return redirect('home')
# Esta función define la vista de cierre de sesión (logout) del sitio.


def register_user(request):
    # Verifica si el método de la solicitud es POST.
    if request.method == 'POST':
        # llenamos el formulario con los datos del POST
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Si el formulario es válido, guarda el nuevo usuario en la base de datos.
            messages.success(request, "Usuario creado correctamente")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Autentica al usuario recién creado.
            user = authenticate(username=username, password=password)
            # Inicia sesión con el usuario autenticado.
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()  # Si es GET, mostramos el formulario vacío
        # Renderizamos el formulario (en caso de GET o si el formulario no es válido)
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    # esta funcion define la viste de un registro especifico
    if request.user.is_authenticated:  # Verifica si el usuario está autenticado.
        # Intenta obtener el registro del cliente con el ID proporcionado (pk).
        customer_record = Record.objects.get(id=pk)
        # Renderiza la plantilla 'record.html' con el registro del cliente.
        return render(request, 'record.html', {'customer_record': customer_record})
    # Si el usuario no está autenticado, redirige a la página de inicio con un mensaje de error.
    else:  # Si el usuario no está autenticado.
        # Muestra un mensaje de error al usuario.
        # Muestra un mensaje de error al usuario.
        messages.success(request, "You Must Be Logged In To View That Page...")
        # Redirige al usuario a la página de inicio (home).
        return redirect('home')


# Esta función define la vista para eliminar un registro específico (delete_record) del sitio.
def delete_record(request, pk):
    # Verifica si el usuario está autenticado.
    if request.user.is_authenticated:  # Verifica si el usuario está autenticado.
        # Obtiene el registro del cliente con el ID proporcionado (pk).
        delete_it = Record.objects.get(id=pk)
        # Si el registro existe, lo elimina.
        delete_it.delete()  # Elimina el registro del cliente.
        # Muestra un mensaje de éxito al usuario.
        # Muestra un mensaje de éxito al usuario.
        messages.success(request, "Record Deleted Successfully...")
        # Redirige al usuario a la página de inicio (home).
        # Redirige al usuario a la página de inicio (home).
        return redirect('home')
    # Si el usuario no está autenticado, muestra un mensaje de error y redirige a la página de inicio.
    else:  # Si el usuario no está autenticado.
        # Muestra un mensaje de error al usuario.
        messages.success(request, "You Must Be Logged In To Do That...")
        # Redirige al usuario a la página de inicio (home).
        # Redirige al usuario a la página de inicio (home).
        return redirect('home')
# Esta función define la vista para agregar un nuevo registro (add_record) del sitio.


# Esta función define la vista para agregar un nuevo registro (add_record) del sitio.
# Esta función define la vista para agregar un nuevo registro (add_record) del sitio.
def add_record(request):
    # Verifica si el usuario está autenticado.
    # Crea una instancia del formulario AddRecordForm, pasando los datos POST si están disponibles, o None si no hay datos POST.
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:  # Verifica si el usuario está autenticado.
        # Si el método de la solicitud es POST, significa que se está enviando un formulario.
        if request.method == "POST":  # Verifica si la solicitud es POST.
            if form.is_valid():  # Verifica si el formulario es válido.
                # Si el formulario es válido, guarda el nuevo registro en la base de datos.
                # Guarda el nuevo registro en la base de datos.
                add_record = form.save()
                # Muestra un mensaje de éxito al usuario.
                messages.success(request, "Record Added...")
                # Redirige al usuario a la página de inicio (home).
                # Redirige al usuario a la página de inicio (home).
                return redirect('home')
        # Si el método de la solicitud no es POST, simplemente renderiza la plantilla 'add_record.html'.
        # Renderiza la plantilla 'add_record.html' y pasa el formulario como contexto.
        return render(request, 'add_record.html', {'form': form})
    # Si el usuario no está autenticado, muestra un mensaje de error y redirige a la página de inicio.
    else:  # Si el usuario no está autenticado.
        # Muestra un mensaje de error al usuario.
        # Muestra un mensaje de error al usuario.
        messages.success(request, "You Must Be Logged In...")
        # Redirige al usuario a la página de inicio (home).
        # Redirige al usuario a la página de inicio (home).
        return redirect('home')


# Esta función define la vista para actualizar un registro específico (update_record) del sitio.
def update_record(request, pk):
    # Verifica si el usuario está autenticado.
    if request.user.is_authenticated:  # Verifica si el usuario está autenticado.
        # Obtiene el registro del cliente con el ID proporcionado (pk).
        # Obtiene el registro del cliente con el ID proporcionado (pk).
        current_record = Record.objects.get(id=pk)
        # Crea una instancia del formulario AddRecordForm, pasando los datos POST si están disponibles y el registro actual como instancia.
        # Crea una instancia del formulario AddRecordForm, pasando los datos POST si están disponibles y el registro actual como instancia.
        form = AddRecordForm(request.POST or None, instance=current_record)
        # Si el método de la solicitud es POST, significa que se está enviando el formulario.
        if request.method == "POST":
            if form.is_valid():  # Verifica si el formulario es válido.
                # Si el formulario es válido, guarda los cambios en el registro.
                form.save()  # Guarda los cambios en el registro.
                # 3 Muestra un mensaje de éxito al usuario.
                messages.success(request, "Record Has Been Updated!")
                # Redirige al usuario a la página de inicio (home).
                # Redirige al usuario a la página de inicio (home).
                return redirect('home')
            # Renderiza la plantilla 'update_record.html' y pasa el formulario como contexto.
            return render(request, 'update_record.html', {'form': form})
    else:  # Si el usuario no está autenticado.
        # Muestra un mensaje de error al usuario.
        # Muestra un mensaje de error al usuario.
        messages.success(request, "You Must Be Logged In...")
        # Redirige al usuario a la página de inicio (home).
        # Redirige al usuario a la página de inicio (home).
        return redirect('home')
# Renderiza la plantilla 'update_record.html' y pasa el formulario como contexto.
