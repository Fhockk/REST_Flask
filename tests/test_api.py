from restflask.app import app

class TestApiHome():
    ''' Testing home routes'''
    def test_get_api(self):
        assert app.test_client().get('/api/').status_code == 200


class TestApiUsers():
    ''' Testing Users Api'''

    test_data = dict(
        username='coolguy',
        email='test@gmail.com',
        first_name='John',
        last_name='Smith',
        location='Ukraine'
    )
    update_data = dict(
        id=1,
        username='john321',
        email='test@gmail.com',
        first_name='John',
        last_name='Smith',
        location='Ukraine/Kyiv'
    )
    not_valid_data = dict(
        id=0,
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
        response = app.test_client().post('/api/create_user/',json=self.test_data)
        assert response.status_code == 409
        assert b'Error. Username or email is already exist' in response.data

    def test_api_get_user(self):
        response = app.test_client().get('/api/get_user/?id=1')
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
        responce = app.test_client().get('/api/get_user/?id=', self.test_data['email'])
        id = responce.json.get('id')
        response = app.test_client().delete('/api/delete_user/', json={'id': id})
        assert response.status_code == 200
        assert b'has been deleted' in response.data

    def test_api_delete_user_err(self):
        response = app.test_client().delete('/api/delete_user/', json={'id': '0'})
        assert response.status_code == 409
        assert b'No such user record in the db' in response.data