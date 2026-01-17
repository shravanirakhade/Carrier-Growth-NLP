# CareerGrowth-NLP
A smart career counselling system leveraging NLP to analyze user input and deliver personalized career recommendations based on interests, skills, and academic background. Built with Python and Django, it provides an intelligent and scalable solution for educational and counselling platforms.

To run a Python Django app on Windows, you'll generally use the same `manage.py` command as you would on other operating systems. Here's a step-by-step guide:

**1. Open a Command Prompt or PowerShell:**

* Press the Windows key, type "cmd" or "PowerShell", and press Enter.
* For PowerShell, you might need to run it as an administrator if you encounter permission issues.

**2. Navigate to Your Project Directory:**

* Use the `cd` command to navigate to the directory that contains your Django project's `manage.py` file.

    For example, if your project is in `C:\Users\YourUser\myproject`, you would type:

    ```bash
    cd C:\Users\YourUser\myproject
    ```

**3. Activate Your Virtual Environment (Recommended):**

* If you've created a virtual environment (which is highly recommended to keep your project dependencies isolated), you need to activate it.

    If your virtual environment is named "venv", the command is:

    ```bash
    venv\Scripts\activate
    ```

* Your command prompt or PowerShell will change to show the virtual environment name in parentheses, like this: `(venv) C:\Users\YourUser\myproject>`.

**4. Run the Development Server:**

* Use the `manage.py` script to start the Django development server:

    ```bash
    python manage.py runserver
    ```

    * If you encounter an error here, make sure that you have activated your virtual environment. If you did not create a virtual environment, try:

        ```bash
        python3 manage.py runserver
        ```

**5. Access Your App in a Browser:**

* Once the server starts, you'll see output in your command prompt or PowerShell similar to this:

    ```
    Starting development server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    Quit the server with CTRL-BREAK.
    ```

* Open your web browser and go to `http://127.0.0.1:8000/`. You should see your Django app running.

**Important Notes:**

* **`python` vs. `python3`:** On Windows, it's common to have both Python 2 and Python 3 installed. The `python` command might refer to Python 2. If you want to be sure you're using Python 3, use `python3` instead. However, if you've set up your system correctly or are in a virtual environment, `python` should point to the correct Python version for your project.
* **Firewall:** Windows Firewall might prompt you to allow Python to access the network. Make sure to allow it so you can access your development server in your browser.
* **Ctrl+C to Stop:** To stop the development server, press Ctrl+C in your command prompt or PowerShell.
