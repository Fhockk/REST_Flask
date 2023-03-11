""""APPLICATION"""
import restflask.views.web_view # pylint: disable=unused-import
import restflask.rest.api_view # pylint: disable=unused-import
from restflask.config import app


if __name__ == '__main__':
    app.run()
