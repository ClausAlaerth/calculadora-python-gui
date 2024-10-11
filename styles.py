# NOT USED - READ DOCUMENTATION TO IMPLEMENT

# import qdarkstyle
from variables import (
    PRIMARY_BUTTON_COLOR,
    DARKER_BUTTON_COLOR,
    DARKEST_BUTTON_COLOR,
    SECONDARY_BUTTON_COLOR,
    LIGHTER_BUTTON_COLOR,
    BRIGHTEST_BUTTON_COLOR
)

qssDark = f"""
        Button {{
        color: #fff;
        background-color: {PRIMARY_BUTTON_COLOR};
        border-radius: 5px;
        }}
        Button:hover {{
        color: #fff;
        background-color: {DARKER_BUTTON_COLOR};
        }}
        Button:pressed {{
        color: #fff;
        background-color: {DARKEST_BUTTON_COLOR};
        }}
        """

qssLight = f"""
        Button {{
        color: #fff;
        background-color: {SECONDARY_BUTTON_COLOR};
        border-radius: 5px;
        }}
        Button:hover {{
        color: #fff;
        background-color: {LIGHTER_BUTTON_COLOR};
        }}
        Button:pressed {{
        color: #fff;
        background-color: {BRIGHTEST_BUTTON_COLOR};
        }}
        """


# def setupTheme(app):
#     # Aplicar o estilo escuro do qdarkstyle
#     app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

#     # Sobrepor com o QSS personalizado para estilização adicional
#     app.setStyleSheet(app.styleSheet() + qss)
