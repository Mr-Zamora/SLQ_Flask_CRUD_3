# Progressive Flask and SQL Tutorials

This document outlines three progressive tutorials designed to build toward the Flask Contacts App project. Each tutorial introduces new concepts while reinforcing previous learning.

## Tutorial 1: Basic Flask Web App with HTML/CSS

**Title: "Getting Started with Flask: Your First Web Page"**

**Learning Objectives:**
- Understand basic web concepts (client-server model)
- Set up a Flask development environment
- Create simple routes and templates
- Apply basic CSS styling

**Project: Personal Portfolio Page**

**Project Structure:**
```
portfolio_app/
├── app.py                 # Main Flask application
├── static/               # Static files directory
│   └── css/              # CSS files directory
│       └── style.css     # Main stylesheet
├── templates/            # HTML templates directory
│   ├── base.html         # Base template with common elements
│   ├── index.html        # Homepage
│   ├── about.html        # About page
│   └── projects.html     # Projects page
└── requirements.txt      # Project dependencies
```

**Tutorial Outline:
1. **Setup and Installation**
   - Installing Python and Flask
   - Creating a virtual environment
   - Project structure introduction

2. **Flask Basics**
   - Creating your first Flask application
   - Understanding routes and views
   - Basic Flask application structure
   ```python
   from flask import Flask, render_template
   
   app = Flask(__name__)
   
   @app.route('/')
   def home():
       return render_template('index.html')
   
   if __name__ == '__main__':
       app.run(debug=True)
   ```

3. **HTML Templates**
   - Creating a base template
   - Template inheritance
   - Passing variables to templates
   ```html
   <!-- base.html -->
   <!DOCTYPE html>
   <html>
   <head>
       <title>{% block title %}{% endblock %}</title>
       <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
   </head>
   <body>
       <header>
           <h1>My Portfolio</h1>
       </header>
       <main>
           {% block content %}{% endblock %}
       </main>
       <footer>
           <p>&copy; 2025 My Portfolio</p>
       </footer>
   </body>
   </html>
   ```

4. **Static Files and CSS**
   - Organizing static files
   - Creating a basic stylesheet
   - Responsive design principles

5. **Deployment**
   - Running the application locally
   - Basic debugging techniques

**Final Deliverable:** A simple portfolio website with a home page, about page, and projects page using Flask routes and templates with CSS styling.

---

## Tutorial 2: Flask with Form Handling and Data Storage

**Title: "Interactive Flask: Forms and Data Persistence"**

**Learning Objectives:**
- Handle form submissions in Flask
- Validate user input
- Store data in a simple SQLite database
- Retrieve and display data from a database

**Project: Task Manager Application**

**Project Structure:**
```
task_manager/
├── app.py                 # Main Flask application
├── schema.sql             # SQL schema for database setup
├── instance/              # Instance-specific data
│   └── tasks.db           # SQLite database file (generated)
├── static/                # Static files directory
│   └── css/               # CSS files directory
│       └── style.css      # Main stylesheet
├── templates/             # HTML templates directory
│   ├── base.html          # Base template with common elements
│   ├── index.html         # Task list page
│   └── add_task.html      # Form to add a new task
└── requirements.txt       # Project dependencies
```

**Tutorial Outline:
1. **Form Handling in Flask**
   - Creating HTML forms
   - GET vs POST methods
   - Processing form data with Flask
   ```python
   @app.route('/add_task', methods=['GET', 'POST'])
   def add_task():
       if request.method == 'POST':
           task_title = request.form['title']
           task_description = request.form['description']
           # Process the data...
           return redirect(url_for('tasks'))
       return render_template('add_task.html')
   ```

2. **Introduction to SQLite**
   - What is SQLite?
   - Creating a database schema
   - Basic SQL commands (CREATE, INSERT)
   ```sql
   CREATE TABLE tasks (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       title TEXT NOT NULL,
       description TEXT,
       created_date TEXT DEFAULT CURRENT_TIMESTAMP
   );
   ```

3. **Connecting Flask to SQLite**
   - Database connection in Flask
   - Creating a helper function
   ```python
   def get_db_connection():
       conn = sqlite3.connect('database.db')
       conn.row_factory = sqlite3.Row
       return conn
   ```

4. **CRUD Operations - Create and Read**
   - Inserting data from forms
   - Retrieving and displaying data
   ```python
   @app.route('/')
   def tasks():
       conn = get_db_connection()
       tasks = conn.execute('SELECT * FROM tasks').fetchall()
       conn.close()
       return render_template('tasks.html', tasks=tasks)
   ```

5. **Flash Messages and User Feedback**
   - Implementing flash messages
   - Improving user experience

**Final Deliverable:** A task manager application where users can add tasks that are stored in a SQLite database and displayed on the main page.

---

## Tutorial 3: Advanced Flask with Complete CRUD and Relational Data

**Title: "Full-Stack Flask: Complete CRUD and Relational Databases"**

**Learning Objectives:**
- Implement complete CRUD operations
- Work with relational data
- Improve application structure
- Add user authentication basics

**Project: Blog Platform with Categories**

**Project Structure:**
```
blog_platform/
├── app.py                 # Main Flask application
├── schema.sql             # SQL schema for database setup
├── instance/              # Instance-specific data
│   └── blog.db            # SQLite database file (generated)
├── static/                # Static files directory
│   ├── css/               # CSS files directory
│   │   └── style.css      # Main stylesheet
│   └── js/                # JavaScript files
│       └── script.js      # Client-side functionality
├── templates/             # HTML templates directory
│   ├── base.html          # Base template with common elements
│   ├── index.html         # Blog post list
│   ├── post.html          # Single post view
│   ├── add_post.html      # Form to add a new post
│   ├── edit_post.html     # Form to edit an existing post
│   ├── categories.html    # Category management
│   ├── login.html         # Login form
│   └── register.html      # Registration form
├── auth.py                # Authentication blueprint
├── blog.py                # Blog functionality blueprint
├── config.py              # Configuration settings
└── requirements.txt       # Project dependencies
```

**Tutorial Outline:
1. **Advanced Database Design**
   - Relational database concepts
   - Foreign keys and relationships
   ```sql
   CREATE TABLE categories (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL UNIQUE
   );
   
   CREATE TABLE posts (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       title TEXT NOT NULL,
       content TEXT NOT NULL,
       category_id INTEGER,
       created_date TEXT DEFAULT CURRENT_TIMESTAMP,
       FOREIGN KEY (category_id) REFERENCES categories (id)
   );
   ```

2. **Complete CRUD Operations**
   - Update operations
   - Delete operations with confirmation
   - Error handling
   ```python
   @app.route('/edit/<int:id>', methods=['GET', 'POST'])
   def edit_post(id):
       if request.method == 'POST':
           title = request.form['title']
           content = request.form['content']
           category_id = request.form['category_id']
           
           conn = get_db_connection()
           conn.execute('UPDATE posts SET title = ?, content = ?, category_id = ? WHERE id = ?',
                       (title, content, category_id, id))
           conn.commit()
           conn.close()
           flash('Post updated successfully!')
           return redirect(url_for('index'))
       # GET request handling...
   ```

3. **Working with Related Data**
   - Joins in SQLite
   - Displaying related data
   ```python
   @app.route('/')
   def index():
       conn = get_db_connection()
       posts = conn.execute('''
           SELECT p.id, p.title, p.content, p.created_date, c.name as category_name
           FROM posts p
           LEFT JOIN categories c ON p.category_id = c.id
           ORDER BY p.created_date DESC
       ''').fetchall()
       conn.close()
       return render_template('index.html', posts=posts)
   ```

4. **Improved Application Structure**
   - Organizing code with blueprints
   - Configuration management
   - Error pages

5. **Basic Authentication**
   - Simple user registration and login
   - Protecting routes with login_required
   - Session management

**Final Deliverable:** A blog platform where users can create, read, update, and delete posts, assign categories to posts, and filter posts by category.

---

## Progression to the Contacts App Project

**Final Project Structure:**
```
contacts_app/
├── app.py                 # Main Flask application
├── instance/              # Instance-specific data
│   └── contacts_updated.db # SQLite database file
├── static/                # Static files directory
│   └── css/               # CSS files directory
│       └── style.css      # Main stylesheet
├── templates/             # HTML templates directory
│   ├── base.html          # Base template with common elements
│   ├── index.html         # Contacts list
│   ├── add.html           # Form to add a new contact
│   └── edit.html          # Form to edit an existing contact
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
├── TUTORIALS.md           # Tutorial outlines
└── requirements.txt       # Project dependencies
```

After completing these three tutorials, students will have learned:

1. **From Tutorial 1:**
   - Basic Flask application structure
   - Routes and templates
   - HTML/CSS integration

2. **From Tutorial 2:**
   - Form handling
   - Basic SQLite integration
   - Simple CRUD operations (Create, Read)

3. **From Tutorial 3:**
   - Complete CRUD operations
   - Relational data
   - More advanced application structure

These skills will prepare students for the Contacts App project, which combines all these concepts into a practical application. Each tutorial builds on the previous one, gradually introducing more complex concepts while reinforcing what was learned before.

## Teaching Tips

- Encourage students to experiment with the code
- Provide challenges at the end of each tutorial to reinforce learning
- Have students work in pairs for more complex tasks
- Use code reviews to help students learn from each other
- Emphasize the importance of good documentation and comments
