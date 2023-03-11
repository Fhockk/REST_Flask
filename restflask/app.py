""""APPLICATION"""
#import views.web_view # pylint: disable=unused-import
from .views import web_view # pylint: disable=unused-import
from .rest import api_view # pylint: disable=unused-import
#import rest.api_view # pylint: disable=unused-import
from .config import app


if __name__ == '__main__':
    app.run()
