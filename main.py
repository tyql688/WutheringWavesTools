import asyncio

import app.api
import app.enhance

prex = "self_"
url_list = {
    f"{prex}role_head_1304.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_24_a_UI.webp",
    f"{prex}role_pile_1304.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_jinxi2_UI.webp",
}

url_attr = {
    "attr_不绝余音.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriAttack.webp",
    "attr_凝夜白霜.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriIce.webp",
    "attr_啸谷长风.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriWind.webp",
    "attr_彻空冥雷.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriThunder.webp",
    "attr_沉日劫明.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriDark.webp",
    "attr_浮星祛暗.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriLight.webp",
    "attr_熔山裂谷.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriFire.webp",
    "attr_轻云出月.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriCloud.webp",
    "attr_隐世回光.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriCure.webp",
    "attr_凌冽决断之心.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriIceUltimateSkill.webp",
    "attr_幽夜隐匿之帷.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriDarkAssist.webp",
    "attr_无惧浪涛之勇.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriEnergy.webp",
    "attr_此间永驻之光.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriLightError.webp",
    "attr_高天共奏之曲.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriCooperate.webp",
    "attr_流云逝尽之空.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriWindError.webp",
    "attr_奔狼燎原之焰.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriFireUltimateSkill.webp",
    "attr_愿戴荣光之旅.png": "https://api.hakush.in/ww/UI/UIResources/Common/Image/IconElementAttri/T_IconElementAttriWindErrorA.webp",
}


def download_url_attr():
    from app.RESOURCE_PATH import ATTRIBUTE_EFFECT_PATH

    asyncio.run(app.api.async_download_url(url_attr, ATTRIBUTE_EFFECT_PATH))


def new_version():
    asyncio.run(app.api.async_download())
    app.enhance.enhance()
    app.enhance.enhance_weapon()
    app.enhance.enhance_char()
    app.enhance.enhance_echo()
    app.enhance.enhance_material()


def generate():
    import app.generate

    app.generate.generate_weapon()
    app.generate.generate_echo()
    app.generate.generate_char()


if __name__ == "__main__":
    new_version()
    generate()
    # download_url_attr()
    # app.api.download_url(url_list)
