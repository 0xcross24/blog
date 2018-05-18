<<<<<<< HEAD
#!/usr/bin/env python
=======
#!/usr/bin/env python3
>>>>>>> 7e88efda4da329363e4b3c4565a61ee381ba6e4d
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
<<<<<<< HEAD
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
=======

    from django.core.management import execute_from_command_line

>>>>>>> 7e88efda4da329363e4b3c4565a61ee381ba6e4d
    execute_from_command_line(sys.argv)
