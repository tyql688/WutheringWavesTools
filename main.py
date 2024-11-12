import app.api
import app.enhance


def main():
    # app.api.download()
    # app.enhance.enhance()
    # app.enhance.enhance_role_skill()
    # app.enhance.enhance_role_chain()
    app.enhance.enhance_weapon()


def new_version():
    app.api.download()
    app.enhance.enhance()
    app.enhance.enhance_weapon()
    app.enhance.enhance_char()


if __name__ == '__main__':
    new_version()
