# Flask Contacts App

A simple and intuitive web-based contact management application built with Python Flask and SQLite. This application allows you to perform basic CRUD (Create, Read, Update, Delete) operations on contacts.

## Features

- View all contacts in a clean, tabular format
- Add new contacts with name and phone number
- Edit existing contact information
- Delete contacts with confirmation
- Responsive design that works on mobile and desktop
- Flash messages for user feedback

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flask-contacts-app.git
   cd flask-contacts-app
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   ```
   
   If you don't have a requirements.txt yet, install the dependencies manually:
   ```bash
   pip install flask
   ```

## Database Setup

The application uses SQLite and will automatically create a database file at `instance/contacts_updated.db` when you first run the application.

## Running the Application

1. **Set the Flask app**
   ```bash
   # On Windows
   set FLASK_APP=app.py
   
   # On macOS/Linux
   export FLASK_APP=app.py
   ```

2. **Run the development server**
   ```bash
   flask run
   ```

3. **Open your browser**
   Visit `http://127.0.0.1:5000/` to access the application

## Project Structure

```
flask-contacts-app/
├── instance/               # Database and instance-specific files
├── static/                # Static files (CSS, JS, images)
│   └── css/               # Stylesheets
│       └── style.css
├── templates/             # HTML templates
│   ├── add.html           # Add contact form
│   ├── base.html          # Base template
│   ├── edit.html          # Edit contact form
│   └── index.html         # Main contacts list
├── .gitignore            # Specifies intentionally untracked files to ignore
├── app.py                # Main application file
└── README.md             # This file
```

## Using the Application

- **View All Contacts**: Visit the home page to see all your contacts
- **Add a Contact**: Click "Add Contact" and fill in the form
- **Edit a Contact**: Click the "Edit" button next to any contact
- **Delete a Contact**: Click the "Delete" button next to any contact (confirmation required)

## Database Management

To manage your SQLite database, you can use tools like:
- [DB Browser for SQLite](https://sqlitebrowser.org/) (recommended for beginners)
- [SQLiteStudio](https://sqlitestudio.pl/)
- [DBeaver Community Edition](https://dbeaver.io/)

The database file is located at `instance/contacts_updated.db`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Inspired by the need for a simple contact management solution

---

*Created with ❤️ for learning and productivity*
