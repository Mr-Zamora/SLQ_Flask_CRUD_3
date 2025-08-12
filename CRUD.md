# Flask Contacts App: Understanding CRUD Operations

This document explains the key files in our Flask Contacts App and how they implement CRUD (Create, Read, Update, Delete) operations.

## Project Structure

```
contacts_app/
├── app.py                 # Main Flask application

├── static/                # Static files directory
│   └── css/               # CSS files directory
│       └── style.css      # Main stylesheet
├── templates/             # HTML templates directory
│   ├── base.html          # Base template with common elements
│   ├── index.html         # Homepage (list all contacts)
│   ├── add.html           # Form to add a new contact
│   └── edit.html          # Form to edit an existing contact
└── contacts.db            # SQLite database file (generated)
```

## Key Files Explained



### app.py

The main Flask application file that handles all routes and database operations:

```python
# Key sections:
# 1. Flask app initialization
# 2. Database connection helper function

# 4. Routes for all CRUD operations
```

#### CRUD Operations in app.py:

1. **Create**: Adding new contacts
   ```python
   @app.route('/add', methods=['POST'])
   def add_contact():
       # Get form data, validate, insert into database
   ```

2. **Read**: Viewing all contacts
   ```python
   @app.route('/')
   def index():
       # Query database, display all contacts
   ```

3. **Update**: Editing existing contacts
   ```python
   @app.route('/edit/<int:id>', methods=['POST'])
   def edit_contact(id):
       # Get form data, validate, update database
   ```

4. **Delete**: Removing contacts
   ```python
   @app.route('/delete/<int:id>')
   def delete_contact(id):
       # Delete contact from database
   ```

### HTML Templates

The app uses four HTML templates to handle different views:

1. **base.html**: The main template that others extend, containing:
   - Header with navigation
   - Flash message display
   - Footer

2. **index.html**: Displays all contacts in a table with options to edit or delete

3. **add.html**: Form for adding new contacts

4. **edit.html**: Form for editing existing contacts, pre-populated with contact data

### style.css

The CSS file provides styling for:
- Overall layout and responsive design
- Tables for displaying contacts
- Forms for adding and editing contacts
- Buttons for different actions
- Flash messages for user feedback

## How CRUD Operations Flow

1. **Create**:
   - User clicks "Add Contact" link
   - Form is displayed (add.html)
   - User submits form
   - Data is validated and inserted into database
   - User is redirected to index with success message

2. **Read**:
   - User visits home page
   - App queries database for all contacts
   - Contacts are displayed in a table

3. **Update**:
   - User clicks "Edit" button for a contact
   - Form is displayed with pre-filled data (edit.html)
   - User modifies data and submits form
   - Data is validated and updated in database
   - User is redirected to index with success message

4. **Delete**:
   - User clicks "Delete" button for a contact
   - Confirmation dialog appears
   - If confirmed, contact is deleted from database
   - User is redirected to index with success message

## Database Connection Pattern

The app uses a consistent pattern for database operations:
1. Get a connection using `get_db_connection()`
2. Execute SQL query with parameters to prevent SQL injection
3. Commit changes (for write operations)
4. Close the connection
5. Redirect or render template

This pattern ensures proper resource management and security.
