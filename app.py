import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Database connection helper function
def get_db_connection():
    import os
    # Get the absolute path to the instance folder
    base_dir = os.path.dirname(os.path.abspath(__file__))
    instance_dir = os.path.join(base_dir, 'instance')
    
    # Create the instance directory if it doesn't exist
    if not os.path.exists(instance_dir):
        os.makedirs(instance_dir)
    
    db_path = os.path.join(instance_dir, 'contacts_updated.db')
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn



# Home route - display all contacts
@app.route('/')
def index():
    conn = get_db_connection()
    contacts = conn.execute('SELECT * FROM contacts').fetchall()
    conn.close()
    return render_template('index.html', contacts=contacts)

# Route to display the add contact form
@app.route('/add', methods=['GET'])
def add_form():
    return render_template('add.html')

# Route to handle the form submission for adding a contact
@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    
    if not name or not phone:
        flash('Name and phone are required!')
        return redirect(url_for('add_form'))
    
    conn = get_db_connection()
    conn.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))
    conn.commit()
    conn.close()
    flash('Contact added successfully!')
    return redirect(url_for('index'))

# Route to display the edit contact form
@app.route('/edit/<int:id>', methods=['GET'])
def edit_form(id):
    conn = get_db_connection()
    contact = conn.execute('SELECT * FROM contacts WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('edit.html', contact=contact)

# Route to handle the form submission for editing a contact
@app.route('/edit/<int:id>', methods=['POST'])
def edit_contact(id):
    name = request.form['name']
    phone = request.form['phone']
    
    if not name or not phone:
        flash('Name and phone are required!')
        return redirect(url_for('edit_form', id=id))
    
    conn = get_db_connection()
    conn.execute('UPDATE contacts SET name = ?, phone = ? WHERE id = ?', (name, phone, id))
    conn.commit()
    conn.close()
    flash('Contact updated successfully!')
    return redirect(url_for('index'))

# Route to delete a contact
@app.route('/delete/<int:id>')
def delete_contact(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM contacts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Contact deleted successfully!')
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
