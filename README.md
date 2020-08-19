# djpanel
Django + Panel + Bokeh (boilerplate)

This project is a boilerplate: Django integration with Panel and Bokeh libraries.

## Instruction to run

Make sure you use Python>3.8.

1. `git clone git@github.com:macwis/djpanel.git`
2. `cd djpanel`
3. `virtualenv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`
6. `python manage.py migrate`
7. `daphne djpanel.asgi:application`
8. Open in your web browser: http://localhost:8000/sliders/
