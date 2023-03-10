"""RESTfull service"""
from flask import jsonify, request

from service.services import get_user, get_users, get_post, get_posts
from service.services import create_user, create_post
from service.services import update_user, update_post
from service.services import delete_user, delete_post

from config import app


# ==================== Users ====================
@app.route('/api/')
@app.route('/api/users/')
def api_users():
    """
    Endpoint for retrieving a list of users in the application.
    :return:
        list of dict: A list of dictionaries, where each dictionary represents a user.
                      The keys in each dictionary correspond to the fields of a User object.
    """
    app.logger.debug("API. GET. list of users")
    return jsonify(get_users())


@app.route('/api/create_user/', methods=['POST'])
def api_create_user():
    """
    Endpoint for creating a new user in the application.

    Request body:
        JSON object: A dictionary representing the user to be created.
                     The keys in the dictionary correspond to the fields of a User object.

    Raises:
        HTTPException: If the user could not be created due to a conflict or other error.

    :return:
        JSON object: A dictionary with a 'message' key indicating the success
        or failure of the operation.
    """
    data = request.json
    feedback = create_user(data)
    app.logger.debug(f'API. POST. Email = {data.get("email")}. {feedback}')
    if feedback == 'Success':
        return jsonify(message='User ' + data['username'] + ' has been created'), 201
    return jsonify(message=feedback), 409


@app.route('/api/get_user/', methods=['GET'])
def api_get_user():
    """
    Endpoint for retrieving a single user by ID.

    Request body:
        JSON object: A dictionary with a single key 'id' whose value is
        the ID of the user to retrieve.

    Raises:
        HTTPException: If the user ID provided is invalid.
    :return:
        JSON object: A dictionary representing the user, or a 'message' key
        with a 'Not Found' value if the user
                     does not exist.
    """
    user_id = request.json.get('id')
    feedback = get_user(int(user_id))
    app.logger.debug(f"API. GET. GET USER. id = {user_id}. {feedback}")
    if feedback:
        return jsonify(feedback), 200
    return jsonify(message="Not Found"), 204


@app.route('/api/update_user/', methods=['PUT'])
def api_update_user():
    """
    Endpoint for updating a single user by ID.

    Request body:
        JSON object: A dictionary with a single key 'id' whose value is the ID of
        the user to update, and other keys whose values are the updated
        properties of the user.

    Raises:
        HTTPException: If the user ID provided is invalid or the request body is
        malformed.

    :return:
        JSON object: A 'message' key with a 'Success' value if the update was successful,
        or a 'message' key with
                     the error message if the update was unsuccessful.
    """
    data = request.json
    feedback = update_user(data)
    app.logger.debug(f"API. UPDATE USER. id = {request.json.get('id')}. {feedback}")
    if feedback == "Success":
        return jsonify(message='User ' + data['username'] + ' has been updated'), 201
    return jsonify(message=feedback), 409  # check status code


@app.route('/api/delete_user/', methods=['DELETE'])
def api_delete_user():
    """
    Endpoint for deleting a single user by ID.

    Request body:
        JSON object: A dictionary with a single key 'id' whose value is the ID of the
        user to delete.

    Raises:
        HTTPException: If the user ID provided is invalid or the request body is malformed.

    :return:
        JSON object: A 'message' key with a 'Success' value if the deletion was successful,
        or a 'message' key with
                     the error message if the deletion was unsuccessful.
    """
    user_id = request.json.get('id')
    feedback = delete_user(int(user_id))
    app.logger.debug(f"API. DELETE USER. id = {request.json.get('id')}. {feedback}")
    if feedback == 'Success':
        return jsonify(message='User id: ' + user_id + ' has been deleted'), 200
    return jsonify(message=feedback), 409


# ==================== Posts ====================
@app.route('/api/posts/')
def api_posts():
    """
    Endpoint for retrieving a list of all posts.

    Raises:
        HTTPException: If there is an error retrieving the list of posts.

    :return:
        JSON object: A list of dictionaries, where each dictionary represents
        a single post
    """
    app.logger.debug("API. LISTS OF POSTS.")
    return jsonify(get_posts()), 200


@app.route('/api/create_post/', methods=['POST'])
def api_create_post():
    """
     Creates a new post by receiving the post data in JSON format in the request body.

    :return:
        A JSON response indicating whether the operation was successful or not.

    """
    data = request.json
    feedback = create_post(data)
    app.logger.debug(f"API. CREATE POST. id = {request.json.get('id')}. {feedback}")
    if feedback == 'Success':
        return jsonify(message='Post ' + data['title'] + ' has been created'), 201
    return jsonify(message=feedback), 409


@app.route('/api/get_post/', methods=['GET'])
def api_get_post():
    """
    Endpoint for retrieving a single post by ID.

    :return:
        JSON object: A dictionary representing the post, or a 'message' key with a
        'Not Found' value if the user
                     does not exist.
    """
    post_id = request.json.get('id')
    feedback = get_post(int(post_id))
    app.logger.debug(f"API. GET POST. id = {request.json.get('id')}. {feedback}")
    if feedback:
        return jsonify(feedback), 200
    return jsonify(message="Not Found"), 204


@app.route('/api/update_post/', methods=['PUT'])
def api_update_post():
    """
    Updates an existing post in the database.

    Expected request body format:
    {
        "id": <post_id>,
        "title": <new_title>,   # Optional
        "description": <new_description>,   # Optional
        "author_id": <new_author_id>   # Optional
    }

    :return: JSON response with a message indicating whether the update was successful
    or not:
    - If the update was successful, returns a 201 (Created) status code with a message
    like "Post <post_title> has been updated".
    - If the update was not successful, returns a 409 (Conflict) status code with
    a message explaining the reason for the failure.
    """
    data = request.json
    feedback = update_post(data)
    app.logger.debug(f"API. UPDATE POST. id = {request.json.get('id')}. {feedback}")
    if feedback == "Success":
        return jsonify(message='Post ' + data['title'] + ' has been updated'), 201
    return jsonify(message=feedback), 409  # check status code


@app.route('/api/delete_post/', methods=['DELETE'])
def api_delete_post():
    """
    Deletes a post from the database.

    :return:
        A JSON object with a 'message' key indicating the success
        or failure of the operation, and an appropriate HTTP status code.
    """
    post_id = request.json.get('id')
    feedback = delete_post(int(post_id))
    app.logger.debug(f"API. DELETE POST. id = {request.json.get('id')}. {feedback}")
    if feedback == 'Success':
        return jsonify(message='Post id: ' + post_id + ' has been deleted'), 200
    return jsonify(message=feedback), 409
