import app.api
import app.enhance

url_list = {
    "1304.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_24_a_UI.webp"
}


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


def generate():
    import app.generate
    app.generate.generate_weapon()
    app.generate.generate_echo()
    app.generate.generate_char()


if __name__ == '__main__':
    # new_version()
    # generate()
    app.api.download_url(url_list)
