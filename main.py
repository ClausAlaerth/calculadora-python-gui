import sys
from main_window import MainWindow
from variables import ICON_PATH
from display import Display
from info import Info
# from styles import setupTheme
from buttons import ButtonsGrid
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":

    # Criar a Aplicação:
    app = QApplication(sys.argv)  # App principal.
    # setupTheme(app)
    window = MainWindow()  # Instanciando a janela do arquivo.

    # Definir Ícone:
    icon = QIcon(str(ICON_PATH))
    app.setWindowIcon(icon)
    window.setWindowIcon(icon)

    # Info:
    info = Info("")
    window.addWidgetToVLayout(info)

    # Display:
    display = Display()
    display.setPlaceholderText("Digite algo...")
    window.addWidgetToVLayout(display)

    # Botão - Grid:
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executar Código:
    window.adjustFixedSize()  # Importante adicionar por último sempre.
    window.show()
    app.exec()
