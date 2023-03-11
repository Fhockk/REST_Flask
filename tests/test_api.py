import sys
sys.path.append('C:\\Users\\lostd\\Desktop\\epam\\REST_Flask')


from restflask.app import app

class TestApiHome:
    ''' Testing home routes'''

    def test_get_api(self):
        assert app.test_client().get('/api/').status_code == 200


class TestApiUsers:
    ''' Testing Users Api'''

    test_data = dict(
        username='coolguy',
        email='test@gmail.com',
        first_name='John',
        last_name='Smith',
        location='Ukraine'
    )
    update_data = dict(
        username='john321',
        email='test@gmail.com',
        first_name='John',
        last_name='Smith',
        location='Ukraine/Kyiv'
    )
    not_valid_data = dict(
        username='an123',
        email='smth@gmail.com',
        first_name='Mark',
        last_name='Mask',
        location='Germany'
    )

    def test_get_api_users(self):
        response = app.test_client().get('/api/users/')
        assert response.status_code == 200

    def test_api_create_user(self):
        response = app.test_client().post('/api/create_user/', json=self.test_data)
        assert response.status_code == 201
        assert b'has been created' in response.data

    def test_api_create_user_err(self):
        response = app.test_client().post('/api/create_user/', json=self.test_data)
        assert response.status_code == 409
        assert b'Error. Username or email is already exist' in response.data

    def test_api_get_user(self):
        response = app.test_client().get('/api/get_user/?id=' + self.test_data['email'])
        assert response.status_code == 200

    def test_api_get_user_err(self):
        response = app.test_client().get('/api/get_user/?id=0')
        assert response.status_code == 204

    def test_api_update_user(self):
        response = app.test_client().put('/api/update_user/', json=self.update_data)
        assert response.status_code == 201
        assert b'has been updated' in response.data

    def test_api_update_user_err(self):
        response = app.test_client().put('/api/update_user/', json=self.not_valid_data)
        assert response.status_code == 409
        assert b'Error. No such user record in the db' in response.data

    def test_api_delete_user(self):
        response = app.test_client().delete('/api/delete_user/?id=' + self.test_data['email'])
        assert response.status_code == 200
        assert b'has been deleted' in response.data

    def test_api_delete_user_err(self):
        response = app.test_client().delete('/api/delete_user/?id=' + 'somee423432mail@g432mail.com')
        assert response.status_code == 409
        assert b'No such user record in the db' in response.data


class TestApiPosts:
    ''' Testing Posts Api'''
    test_data = dict(
        title='Earth',
        description='Earth is the 3rd planet from the Sun.'
    )
    update_data = dict(
        title='Earth',
        description='Maybe Earth is the 3rd planet from the Sun.'
    )
    not_valid_data = dict(
        title=None,
        description='Not valid Data. Maybe...'
    )

    def test_get_api_posts(self):
        response = app.test_client().get('/api/posts/')
        assert response.status_code == 200

    def test_api_create_post(self):
        response = app.test_client().post('/api/create_post/', json=self.test_data)
        assert response.status_code == 201
        assert b'has been created' in response.data

    def test_api_create_post_err(self):
        response = app.test_client().post('/api/create_post/', json=self.not_valid_data)
        assert response.status_code == 409

    def test_api_get_post(self):
        response = app.test_client().get('/api/get_post/?id=' + self.test_data['title'])
        assert response.status_code == 200

    def test_api_get_post_err(self):
        response = app.test_client().get('/api/get_post/?id=0')
        assert response.status_code == 204

    def test_api_update_post(self):
        response = app.test_client().put('/api/update_post/', json=self.update_data)
        assert response.status_code == 201
        assert b'has been updated' in response.data

    def test_api_update_post_err(self):
        response = app.test_client().put('/api/update_post/', json=self.not_valid_data)
        assert response.status_code == 409
        assert b'Error. No such post record in the db' in response.data

    def test_api_delete_post(self):
        response = app.test_client().delete('/api/delete_post/?id=' + self.test_data['title'])
        assert response.status_code == 200
        assert b'has been deleted' in response.data

    def test_api_delete_post_err(self):
        response = app.test_client().delete('/api/delete_post/?id=' + 'JSKFbnkmfnSLFKJknmfksnMFKFSFSFSFS')
        assert response.status_code == 409
        assert b'Error. No such post record in the db' in response.data
