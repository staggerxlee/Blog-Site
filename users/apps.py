from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    """
    Django only runs signal if the file is imported at startup, thats why this function ensures django loads signal functions whenever app starts
    When django starts the project, it loads each app listed in installed apps, for every app it creates an instance of its configuration files like usersconfig, thats what the self refers to
    Once django finishes settiing that up, meaning all its models and dependencies are ready, it automatically calls self.ready()
    """
    def ready(self): #Predefined Django method name that runs when the app is loaded, To run custom startup code,. django automatically calls ready() which imports signals.py once the app is loaded, the self is the current instance of the app's configuration class (Config)
        import users.signals

    """
    the import is kept inside function to avoid app loading errors, so signals are only loaded once the app is fully loaded up
    """