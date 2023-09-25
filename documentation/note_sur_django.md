
# Application : reservation
#https://realpython.com/django-user-management/
python manage.py createsuperuser
Username : diop
Email address: alphadiop@gmail.com
Password : admin




# activate
conda create --name applications
conda activate applications

# python3 -m venv venv
# source venv/bin/activate
# python -m pip install --upgrade pip
# python -m pip install django

django-admin startproject nomProjet
cd awesome_website
python manage.py startapp users


 # Set up the database
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# Create the superuser
python manage.py createsuperuser

# Start the application (development mode)
python manage.py runserver # default port 8000



    {% block content %}
        <h2>Login</h2>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Login">
        </form>

        <a href="{% url 'main:dashboard' %}">Back to dashboard</a>
        <a href="{% url 'main:password_reset' %}">Reset password</a>
        <a href="{% url 'main:register' %}">Register</a>
    {% endblock %}



{% block content %}
    Hello, {{ user.username|default:'Guest' }} ! {{request.user.is_authenticated}}
{% endblock %}


<a href="{% url 'menu:index' %}"> Page Menu </a>
pour utiliser cette technique, il faut absolument 
definir dans l'url de l'application : app_name = "menu" si l'application est "menu"


<div class = "centered">
   <img id = "main_logo" src = "{% static 'main/images/main_logo.png' %}" alt="logo">
   <a href="{% url 'menu:index' %}"> voir le menu </a>
</div>

.centered{
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

etait dans : main.index.html
<img id = "small_logo" src = "{% static 'main/images/vtc.png' %}">
a href="{% url 'menu:index' %}"><img src="main/images/logo.png" alt="HTML tutorial" style="width:42px;height:42px;"></a>

# ctr+alt+A == add file to git

        <div>
            {% if request.user.is_authenticated %}
                <a href="{% url 'logout' %}"> Logout </a>
            {% else %}
                <a href="{% url 'login' %}"> Login </a>
            {% endif %}
        </div>



    <div class = "lien">
        <a href="{% url 'menu:index' %}"> Page Menu </a>
        <a href="{% url 'taxi:index' %}"> Page Taxi </a>
        <a href="{% url 'vmdtr:index' %}"> Page vmdtr </a>
    </div>

dashboad.html

            {% if user.is_authenticated %}
                <a href="{% url 'logout' %}"> Logout </a>
            {% else %}
                <a href="{% url 'login' %}"> Login </a>
            {% endif %}