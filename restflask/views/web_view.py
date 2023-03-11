"""WEB controllers"""
from datetime import datetime

from ..config import app
from flask import render_template, redirect, request, flash

from ..models.model import User, Post

from ..service.validate import date_format
from ..service.services import get_user, get_users, get_post, get_posts
from ..service.services import create_user, create_post
from ..service.services import update_user, update_post
from ..service.services import delete_user, delete_post


# ==================== Users ====================
@app.route('/')
@app.route('/users/')
def view_users():
    """
    Displays a list of users on the webpage, including the number of posts they have
    and their registration date.

    :return:
        rendered template: the list of users and their details.
    """
    data = get_users()
    for item in data:
        item['num_post'] = len(item['posts'])
        item['registered_at'] = date_format(item['registered_at'])
    app.logger.debug("GET. list of users")
    return render_template("user_list.html", data=data)


@app.route('/new_user/', methods=['GET', 'POST'])
def view_new_user():
    """
    Renders a template for creating a new user, and processes the form data if submitted.

    :return:
        rendered template: for creating a new user, with appropriate feedback messages.
    """
    if request.method == "POST":
        data = {
            'username': request.form.get('username'),
            'email': request.form.get('email'),
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'location': request.form.get('location')
        }
        feedback = create_user(data)
        app.logger.debug(f'POST. email = {data.get("email")}. {feedback}')
        if feedback == 'success':
            flash('New user record created!', category='message')
        else:
            flash(feedback, category='error')
        return redirect("/")
    app.logger.debug("GET. Rendering new_user.html")
    return render_template("new_user.html")


@app.route('/users/<int:id>/', methods=['GET'])
def view_get_user(id: int):  # pylint: disable=C0103,W0622
    """
    Displays the details of a specific user, including the number of posts they have and
    their registration date.

    :param id:
        id (int): The ID of the user to display.

    :return:
        rendered template: the details of the specified user.
    """
    user_id = id
    user = get_user(int(user_id))
    user['num_post'] = len(user['posts'])
    user['registered_at'] = date_format(user['registered_at'])
    app.logger.debug(f"GET USER. id = {user_id}")
    return render_template("user.html", data=user)


@app.route('/edit_user/<int:id>/', methods=['GET', 'POST'])
def view_edit_user(id: int):  # pylint: disable=C0103,W0622,R1710
    """
    View function for editing a user record.

    :param id:
        id (int): The user ID for the record to be edited.

    :return:
        If a GET request, renders the edit_user.html template with the user's data.
        If a POST request, updates the user record with the submitted data and redirects
        to the home page.
    """
    if request.method == "POST":
        data = {
            'id': id,
            'username': request.form.get('username'),
            'email': request.form.get('email'),
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'location': request.form.get('location')
        }
        feedback = update_user(data)
        app.logger.debug(f"POST. EDIT USER {data.get('email')}: {feedback}")
        if feedback == 'Success':
            flash('User record updated!', category='message')
            return redirect('/')
    else:
        user = get_user(id)
        app.logger.debug(f"GET. EDIT USER. id = {id}")
        return render_template("edit_user.html", data=user)


@app.route('/delete_user/<int:id>/', methods=['GET'])
def view_delete_user(id: int):  # pylint: disable=C0103,W0622
    """
    View function for deleting a user record.

    :param id:
        id (int): The user ID for the record to be deleted.

    :return:
        Redirects to the home page with a success or error message flashed to
        the user.
    """
    feedback = delete_user(id)
    if feedback == 'Success':
        app.logger.debug("GET. DELETING USER. flash SUCCESS MESSAGE ")
        flash('User record deleted!',  category='message')
    else:
        app.logger.debug("GET. DELETING USER. flash ERROR MESSAGE ")
        flash(feedback, category='error')
    return redirect("/")


# ==================== Posts ====================
@app.route('/posts/', methods=['GET', 'POST'])
def view_posts():
    """
    Renders a list of posts filtered by a date range and author ID, or all posts
    if no filter is applied. GET requests render the default list of all posts,
    and POST requests filter by the provided form data.

    :return:
        rendered template: "post_list.html" template with a list of post records
        and associated user details.
    """
    users = get_users()
    if request.method == "POST":
        form = {
            'date_from': datetime.strptime(request.form.get('date_from'), '%Y-%m-%d')
                         or "0001-01-01",
            'date_to': datetime.strptime(request.form.get('date_to'), '%Y-%m-%d')
                       or "9999-12-31",
            'author_id': request.form.get('author_id')
        }
        posts = Post.query.filter(Post.created_at >= form['date_from'],
                                  Post.created_at <= form['date_to'],
                                  Post.author_id == form['author_id']).all()
        for post in posts:
            post.created_at = post.created_at.strftime("%Y-%m-%d")
        app.logger.debug(
            f"""Filtered list of Posts:
                date_from = {form.get('date_from')}, 
                date_to = {form.get('date_to')},
                author_id = {form.get('author_id')}""")
    else:
        posts = get_posts()
        for post in posts:
            post['created_at'] = date_format(post['created_at'])
        app.logger.debug("GET. List of posts")
    return render_template("post_list.html", posts=posts, users=users)


@app.route('/new_post/', methods=['GET', 'POST'])
def view_new_post():
    """
    View function that handles requests to create a new post. If the request
    method is GET, retrieves a list of users from the database to display in
    the post creation form. If the request method is POST, retrieves the form data,
    creates a new post using the data, and redirects to the post list page.
    If there was an error creating the post, an error message is displayed
    using a flash message.

    :return:
        The rendered HTML template for the new post creation page with
        a form to create a new post.
    """
    if request.method == "POST":  # pylint: disable=R1705
        data = {
            'title': request.form.get('title'),
            'description': request.form.get('description'),
            'author_id': request.form.get('author_id')
        }
        feedback = create_post(data)
        app.logger.debug(f'POST. NEW POST {feedback}')
        if feedback == 'success':
            flash('New post record created!', category='message')
        else:
            flash(feedback, category='error')
        return redirect("/posts/")
    else:
        data = User.query.all()
        app.logger.debug(f'GET NEW POST. USER id ={request.form.get("author_id")}')
        return render_template("new_post.html", data=data)


@app.route('/posts/<int:id>/', methods=['GET'])
def view_get_posts(id: int):   # pylint: disable=C0103,W0622
    """
    Renders a view to display a single post identified by the given ID.

    :param id:
        id (int): The ID of the post to display.

    :return:
        If a post with the given ID is found, renders the "post.html" template with
        data dictionary.
    """
    post = get_post(id)
    if post:  # pylint: disable=R1705
        author = post['user']
        data = {
            'id': post['id'],
            'title': post['title'],
            'description': post['description'],
            'created_at': date_format(post['created_at']),
            'author_id': post['author_id'],
            'first_name': author.first_name,
            'last_name': author.last_name
        }
        app.logger.debug(f'GET. POST VIEW. id ={post["id"]}')
        return render_template("post.html", data=data)
    else:
        app.logger.debug('GET. POST VIEW. UNKNOWN ID')
        return redirect('/')


@app.route('/edit_post/<int:id>/', methods=['GET', 'POST'])
def view_edit_post(id: int):   # pylint: disable=C0103,W0622,R1710
    """
    View function to edit an existing post.

    :param id:
        id (int): The ID of the post to edit.

    :return:
    If the request method is POST and the update is successful, the function will
    redirect to the post view page for the edited post with a success message.
    If the update fails, the function will redirect to the post edit page with
    an error message. If the request method is GET, the function will render
    the post edit page with the post data populated in the form fields.
    """
    if request.method == "POST":
        data = {
            'id': id,
            'title': request.form.get('title'),
            'description': request.form.get('description'),
        }
        feedback = update_post(data)
        app.logger.debug(f"POST. EDIT POST {data.get('id')}: {feedback}")
        if feedback == 'Success':
            flash('Post record updated!', category='message')
            return redirect('/posts/' + str(id))
    else:
        post = get_post(id)
        app.logger.debug(f"GET. EDIT USER. id = {id}")
        return render_template("edit_post.html", data=post)


@app.route('/delete_post/<int:id>/', methods=['GET'])
def view_delete_post(id: int):   # pylint: disable=C0103,W0622
    """
    This view function deletes a post record with the given ID from the database.

    :param id:
        id (int): The ID of the post record to be deleted.

    :return:
        A redirect response to the '/posts/' URL.
    """
    feedback = delete_post(id)
    if feedback == 'Success':
        app.logger.debug("GET. DELETING USER. flash SUCCESS MESSAGE ")
        flash('Post record deleted!',  category='message')
    else:
        app.logger.debug("GET. DELETING USER. flash ERROR MESSAGE ")
        flash(feedback, category='error')
    return redirect("/posts/")
