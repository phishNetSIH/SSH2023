# phishNet

# Steps to run
1. Clone this repository into desired directory.
2. Navigate to the directory using terminal.
3. Run `pip install -r "requirments.txt"` to install all requirments.
    - You can use a virtual environment if necessary (use `__venv__` as directory for venv)
4. Run `cd web`
5. Run `python manage.py runserver`.
6. Wait for the following to appear (datetime and version might not be the same)
```
September 23, 2023 - 09:06:58
Django version 4.2.5, using settings 'phishNet_backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
7. Go to `localhost:8000`
8. Enter URL and click submit to get safety analysis.

# Video URL
https://drive.google.com/file/d/1YqOJGMw9fqoeX7QCXnVKcM8qtDJHVqw7/view?usp=sharing

# A Step further
As an added layer of confirmation, we fetch the title of the webpage and cross check against the top three google search results for said title. If the domain of the search result matches with the webpage, the webpage is marked as safe. This reduces false postives.

