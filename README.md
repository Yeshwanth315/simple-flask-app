---

# Flask App

This is a simple Flask web application with basic routing, a test case, and CI/CD integration using GitHub Actions. The app displays a message on the homepage and includes unit tests to ensure the homepage works as expected.

## 🚀 Features

- **Flask Web App**: A basic Flask app that renders a homepage with a message.
- **Testing**: Unit tests using `pytest` to ensure the functionality of routes.

## 🛠 Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/simple-flask-app.git
cd simple-flask-app
```

### Install dependencies

Make sure Python 3.10+ is installed. Then, set up a virtual environment and install the necessary packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Set up environment variables (optional)

You can configure environment variables for local development or deployment (if required):

```bash
export FLASK_ENV=development
```

---

## 🚀 Running the App

To run the Flask app locally, use:

```bash
python run.py
```

Visit `http://127.0.0.1:5000/` in your browser to see the app in action.

---

## 🧪 Running Tests

You can run the tests with `pytest` to ensure everything is working:

```bash
pytest
```

---

## 🔧 GitHub Actions

This project is configured with GitHub Actions to run tests and deploy on changes to the `main` branch. The workflow file is located in `.github/workflows/flaskapi.yaml`.

---

## 🧰 Project Structure

```
flask_app/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       └── index.html
├── tests/
│   └── test_app.py
├── app.py
├── requirements.txt
├── Dockerfile
├── .github/
│   └── workflows/
│       └── flaskapi.yaml
├── Procfile
└── README.md
```

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
