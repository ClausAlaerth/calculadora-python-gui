from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from variables import BIG_FONT, TEXT_MARGIN, MINIMUM_WIDTH
from utils import isEmpty, isNumOrDot


# DISPLAY DA CALCULADORA - Área para inserir os números.
class Display(QLineEdit):

    # Instanciando uma classe para receber os
    # sinais do acionamento do teclado.
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    negativePressed = Signal()
    inputPressed = Signal(str)  # Especificar o recebimento do arg.
    operatorPressed = Signal(str)  # Especificar o recebimento do arg.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margin = [TEXT_MARGIN for _ in range(4)]

        self.setStyleSheet(f"font-size: {BIG_FONT}px")
        self.setMinimumHeight(BIG_FONT * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margin)
        self.setMinimumWidth(MINIMUM_WIDTH)

    # CONFIGURANDO O PRESSIONAR DE TECLAS DO TECLADO
    def keyPressEvent(self, event: QKeyEvent) -> None:

        text = event.text().strip()  # Texto da tecla, sem espaços.
        key = event.key()  # O ativar de uma tecla.
        KEYS = Qt.Key  # Instanciando a classe Key.

        # Verificando o pressionar das teclas:
        # Retorna True ou False.
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isEscape = key in [KEYS.Key_Escape]
        isNegative = key in [KEYS.Key_N]
        isOperator = key in [
            KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk,
            KEYS.Key_P
        ]

        if isEnter or text == "=":
            self.eqPressed.emit()  # Emitir o sinal.
            return event.ignore()  # Vai ignorar qualquer ação.

        if isDelete or text.lower() == "c":
            self.delPressed.emit()  # Emitir o sinal.
            return event.ignore()  # Vai ignorar qualquer ação.

        if isEscape:
            self.clearPressed.emit()  # Emitir o sinal.
            return event.ignore()  # Vai ignorar qualquer ação.

        if isNegative or text.lower() == "n":
            self.negativePressed.emit()  # Emitir o sinal.
            return event.ignore()  # Vai ignorar qualquer ação.

        if isOperator:

            if text.lower() == "p":
                text = "^"

            self.operatorPressed.emit(text)  # Emitir o sinal.
            return event.ignore()  # Vai ignorar qualquer ação.

        # Não passar daqui se não houver um texto:
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)  # Emitir o sinal.
            return event.ignore()  # Vai ignorar qualquer ação.
