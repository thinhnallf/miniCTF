import os
import uuid
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

# UUIDs for a normal user and an admin
normal_user_uuid = str(uuid.uuid4())
admin_uuid = str(uuid.uuid4())

#Get user's UUID
def get_user_uuid(): 
    return normal_user_uuid
# Variable to check if user is admin
# Set admin status in the session
def set_admin_status():
    session['is_admin'] = True

# Check admin status
def is_admin():
    return session.get('is_admin', False)
# Sample blogs data
blogs = [
    {
        'title': 'Tech News',
        'content': 'Stay updated with the latest tech news!',
    },
    {
        'title': 'Travel Adventures',
        'content': 'Explore the world through amazing travel stories.',
    },
    {
        'title': 'Coding Tips',
        'content': 'Improve your coding skills with these helpful tips.',
    },
    {
        'title': 'Admin Corner',
        'content': f'Admin UUID: {admin_uuid}',
    },
]

@app.route('/')
def index():
    return render_template('index.html', blogs=blogs, user_uuid=normal_user_uuid,  get_user_uuid=get_user_uuid)

@app.route('/admin_panel', methods=['GET', 'POST'])
def admin_panel():
    # Get the provided admin UUID from the URL
    provided_user_uuid = request.args.get('uuid')

    # Check if the provided admin UUID is valid
    if provided_user_uuid == admin_uuid:
        # Set admin status in the session
        set_admin_status()

        return render_template('admin_panel.html', is_admin=is_admin())  # Replace 'admin_panel.html' with your actual template name
    else:
        # If the provided admin UUID is not valid, abort with a 403 Forbidden status
        return "Access Denied: Admins only!"

   
@app.route('/blog/<int:index>')
def blog_detail(index):
    blog = blogs[index - 1]  # Adjusting for 1-based index
    return render_template('blog_detail.html', blog=blog)

@app.route('/flag', methods=['GET', 'POST'])
def flag():
    # Check if the user is an admin
    if is_admin():
        return "Congratulations! Here is the flag: CTF{your_flag_here}"
    else:
        return "Access Denied: Admins only!"

if __name__ == '__main__':
    app.run(debug=True)
