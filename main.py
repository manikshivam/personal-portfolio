# main.py

from flask import Flask, render_template, request, redirect, url_for
from model import create_table, insert_message, get_all_messages, delete_message

app = Flask(__name__)

create_table()

@app.route('/')
def index():
    messages = get_all_messages()
    return render_template('index.html', messages=messages)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        message = request.form['message']

        insert_message(name, email, mobile, message)
        return redirect(url_for('index'))

    # If it's a GET request, render the contact form
    return render_template('contact.html')

@app.route('/admin')
def admin():
    messages = get_all_messages()
    return render_template('admin.html', messages=messages)

@app.route('/delete_message/<int:message_id>')
def delete_message_route(message_id):
    delete_message(message_id)
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
