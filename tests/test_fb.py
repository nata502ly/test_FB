
from models.params import Data

#TC 1
def test_sign_up_fb(app):
    app.fill_sign_up_form(params=Data())
    app.login(params=Data())
