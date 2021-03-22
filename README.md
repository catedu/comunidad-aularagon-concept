# comunidad_test website

Code for site at: http://localhost


## Getting started

Make sure Python 3.5 or higher is installed on your system.
Open this directory in a command prompt, then:

1. Install the software:
   ```
   pip install -r requirements.txt
   ```

2. Run the development server:
   ```
   python manage.py runserver
   ```

3. Go to http://localhost:8000/ in your browser, or http://localhost:8000/admin/
   to log in and get to work!

## Documentation links

* To customize the content, design, and features of the site see
  [CodeRed CMS](https://docs.coderedcorp.com/cms/).

* For deeper customization of backend code see
  [Wagtail](http://docs.wagtail.io/) and
  [Django](https://docs.djangoproject.com/).

* For HTML template design see [Bootstrap](https://getbootstrap.com/).

---

For running it with docker use:

```bash
### for local development
docker-compose -f docker-compose.local.yml up

### for production
docker-compose up -d
```

For running juypterlab in dev mode run:

```bash
docker exec comunidad-aularagon_web_1 python manage.py shell_plus
```

---
Made with ♥ using [Wagtail](https://wagtail.io/) +
[CodeRed CMS](https://www.coderedcorp.com/cms/)
