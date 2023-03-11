import sys
sys.path.append('C:\\Users\\lostd\\Desktop\\epam\\REST_Flask')


from restflask.app import app


class TestWebHome:
    def test_web_get(self):
        response = app.test_client().get('/')
        assert response.status_code == 200
        assert b'Username' in response.data
        assert b'First_name' in response.data


class TestWebUser:
    test_data = dict(
        username='notcoolgu1y',
        email='tes221t@gmail.com',
        first_name='John',
        last_name='Smith',
        location='Ukraine'
    )

    def test_web_get_users(self):
        response = app.test_client().get('/users/')
        assert b'Username' in response.data
        assert b'First_name' in response.data

    def test_web_new_user_get(self):
        response = app.test_client().get('/new_user/')
        assert response.status_code == 200
        assert b'New User' in response.data

    def test_web_new_user_post(self):
        response = app.test_client().post('/new_user/', data=self.test_data)
        assert response.status_code == 302
        assert b'redirected automatically to the target URL: <a href="/">' in response.data

    def test_web_get_user(self):
        response = app.test_client().get('/users/1/')
        assert response.status_code == 200
        assert b'List of posts' in response.data

    def test_web_edit_user(self):
        response = app.test_client().get('/edit_user/1/')
        assert response.status_code == 200
        assert b'<input type="text" id="first_name" name="first_name"' in response.data

    def test_web_edit_user_post(self):
        response = app.test_client().post('/edit_user/1/', data=self.test_data)
        assert response.status_code == 302
        assert b'redirected automatically to the target URL: <a href="/">' in response.data

    def test_web_delete_user(self):
        response = app.test_client().get('/delete_user/1/')
        assert response.status_code == 302
        assert b'redirected' in response.data


class TestWebPost:
    test_data = dict(
        title='Mars',
        description='Mars is the 4th planet'
    )

    def test_web_get_posts(self):
        response = app.test_client().get('/posts/')
        assert b'Title' in response.data
        assert b'SEARCH' in response.data

    def test_web_new_post_get(self):
        response = app.test_client().get('/new_post/')
        assert response.status_code == 200
        assert b'New Post' in response.data

    def test_web_new_post_post(self):
        response = app.test_client().post('/new_post/', data=self.test_data)
        assert response.status_code == 302
        assert b'Redirecting...' in response.data

    def test_web_get_post(self):
        response = app.test_client().get('/posts/2/')
        assert response.status_code == 200
        assert b'Title' in response.data

    def test_web_edit_post(self):
        response = app.test_client().get('/edit_post/2/')
        assert response.status_code == 200
        assert b'<input type="text" id="title" name="title"' in response.data

    def test_web_edit_post_post(self):
        response = app.test_client().post('/edit_post/8/', data=self.test_data)
        assert response.status_code == 302
        assert b'Redirecting...' in response.data

    def test_web_delete_user(self):
        response = app.test_client().get('/delete_user/1/')
        assert response.status_code == 302
        assert b'redirected' in response.data
