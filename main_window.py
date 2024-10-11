from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QMessageBox
)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Layout Básico da Janela:
        self.cWidget = QWidget()  # Espaço Principal da Janela.

        self.vLayout = QVBoxLayout()  # Layout para receber Widgets.

        self.cWidget.setLayout(self.vLayout)  # Anexando Layout.

        self.setCentralWidget(self.cWidget)  # Anexando Central Widget.

        # Título da Janela:
        self.setWindowTitle("Calculadora")

    # Definir um tamanho fixo:
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # Adicionar Widgets ao Layout:
    def addWidgetToVLayout(self, widget):
        self.vLayout.addWidget(widget)

    # Adicionar mensagens de erro:
    def makeMsgBox(self):
        return QMessageBox(self)
