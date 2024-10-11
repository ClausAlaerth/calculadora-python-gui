import math

from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT
from styles import qssDark, qssLight
from utils import isNumOrDot, isValidNumber, convertToInteger

from typing import TYPE_CHECKING  # Para impedir erros circulares.

# Vai checar a tipagem sem ativar erros circulares.
if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow


# BOTÔES NORMAIS - Não usados
class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT)
        self.setFont(font)
        self.setMinimumSize(75, 75)


# GRADE DE BOTÕES DA CALCULADORA
class ButtonsGrid(QGridLayout):
    def __init__(
        self, display: "Display",
        info: "Info",
        window: "MainWindow",
        *args,
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ["C", "◀", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["3", "2", "1", "+"],
            ["N", "0", ".", "="],
        ]

        self.display = display  # Área vazia que recebe os valores.
        self.info = info  # Equação que fica em cima do label.
        self.window = window  # Janela principal (Msg Erro)
        self._equation = ""  # Vai receber a conta para enviar para a info.
        self._equationInitialValue = "Sua conta"
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    # Getter e Setter para o display da conta,
    # localizada acima do label de inserção de,
    # valores (Info).
    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    # Criação automática de todos os botões da grade
    # Contém a estilização dos botões.
    def _makeGrid(self):

        # O evento no Display está ignorado, mas a conexão
        # com o sinal pode ser feita em qualquer lugar.
        # Dessa forma, é viável inserir a conexão do pressionar
        # dos botões em "_makeGrid", que compila todos os
        # botões virtuais da calculadora.
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.negativePressed.connect(self._invertNumber)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for rowNumber, rolList in enumerate(self._gridMask):
            for colNumber, colElement in enumerate(rolList):
                button = Button(colElement)

                # BOTÕES NORMAIS
                if isNumOrDot(colElement):

                    # Cor do botão
                    button.setStyleSheet(qssLight)

                # BOTÕES ESPECIAIS
                else:

                    # Cor do botão
                    button.setStyleSheet(qssDark)

                    # Config dos botões especiais.
                    self._configSpecialButtons(button)

                # RESTANTE DOS ELEMENTOS
                self.addWidget(button, rowNumber, colNumber)

                # Slot que vai inserir os elementos digitados
                # no campo correto na calculadora.
                slot = self._makeSlot(self._insertToDisplay, colElement)
                self._connectButtonsClicked(button, slot)

    # CONEXÃO DOS BOTÕES
    # Método conectando as ações aos botões.
    def _connectButtonsClicked(self, button, slot):
        button.clicked.connect(slot)

    # CONFIGURAÇÃO DOS BOTÕES ESPECIAIS
    # Associando funções aos botões azuis.
    def _configSpecialButtons(self, button):
        text = button.text()

        # Limpar tudo.
        # Ação e conexão ao botão.
        if text == "C":
            # slot = self._makeSlot(self._clear, "mensagem")
            self._connectButtonsClicked(button, self._clear)

        # Backspace - Apagar uma casa.
        # Ação e conexão do botão.
        if text == "◀":
            self._connectButtonsClicked(button, self.display.backspace)

        # Conversor Negativo - Torna um número no display, negativo.
        # Ação e conexão do botão.
        if text == "N":
            self._connectButtonsClicked(button, self._invertNumber)

        # Usar operadores.
        # Ações e conexões dos botões.
        if text in "+-*/^":
            self._connectButtonsClicked(
                button,
                self._makeSlot(self._configLeftOp, text)
            )

        # Usar operadores.
        # Ações e conexões dos botões.
        if text == "=":
            self._connectButtonsClicked(button, self._eq)

    # MÉTODO PARA CRIAR SLOTS - Criar as ações dos botões
    # Closure - Vai pausar a execução.
    @Slot()
    def _makeSlot(self, function, *args, **kwargs):

        # Método interior - Vai receber a função real.
        @Slot(bool)
        def realSlot():
            function(*args, **kwargs)
        return realSlot

    # MÉTODO PARA INVERTER NÚMEROS NO DISPLAY - Botão "N"
    # O slot receberá essa função.
    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        number = convertToInteger(displayText) * -1

        self.display.setText(str(number))
        self.display.setFocus()

    # MÉTODO PARA INSERIR O TEXTO NO CAMPO - Todos os botões.
    # O slot receberá essa função.
    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)
        self.display.setFocus()

    # MÉTODO PARA LIMPAR O CAMPO DE DIGITAÇÃO - Botão "C".
    # O slot receberá essa função.
    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue

        self.display.clear()
        self.display.setFocus()

    # MÉTODO PARA USAR OS OPERADORES - Botões "+-*/^".
    # O slot receberá essa função.
    @Slot()
    def _configLeftOp(self, text):  # Receberá o operador (+-*/^)
        displayText = self.display.text()  # Receberá o _left (num + op)
        self.display.clear()  # Limpa o display

        # Se o operador for inserido sem um número na esquerda
        # esta condicional é ativada.
        # Nada será feito aqui, tudo é retornado como None.
        if not isValidNumber(displayText) and self._left is None:
            self._showError("Primeiro valor não informado.")
            return

        # Havendo um número no display, _left receberá este valor.
        # A partir daqui, o número da direta é aguardado.
        if self._left is None:
            self._left = convertToInteger(displayText)

        self._op = text  # Recebe o operador (+-*/^)

        self.equation = f"{self._left} {self._op} ??"

        self.display.setFocus()

    # MÉTODO PARA USAR O SINAL DE IGUAL - Botão "=".
    # O slot receberá essa função.
    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            self._showError("Você não inseriu um valor para a operação.")
            return

        self._right = convertToInteger(displayText)

        self.equation = f"{self._left} {self._op} {self._right}"

        result = "Error"

        # GERAR RESULTADO - Colheita de exceções.
        # Eval vai recolher a string informada e executar o código em Python.
        try:

            # POTENCIAÇÃO - Uso do "^".
            # Utilizando o módulo "math".
            if "^" in self.equation and isinstance(self._left, float | int):
                result = str(math.pow(self._left, self._right))
                result = convertToInteger(result)
                self.display.setFocus()
            else:
                result = eval(self.equation)  # Cuidado com o eval...
                self.display.setFocus()

        except ZeroDivisionError:
            print("Zero Division Error")
            self._showError("Erro: Divisão por Zero.")

        except OverflowError:
            print("Número muito grande.")
            self._showError("O resultado excede os limites do aplicativo.")

        except SyntaxError:
            print("Erro na conta")
            result = "Syntax"

        self.display.clear()
        self.info.setText(f"{self.equation} = {result}")

        # Lógica para continuar a conta.
        self._left = None  # Era result, p/ continuar a partir do resultado.
        self._right = None  # O num direita retorna ao None.

        # Mensagem na info, caso dê overflow:
        if result == "Error":

            # Resetar a conta, já que o resultado
            # não pode ser utilizado.
            self._left = None

        # Mensagem na info, caso dê erro de sintaxe:
        if result == "Syntax":

            self.info.setText(
                f"{convertToInteger(displayText)} = {
                    convertToInteger(displayText)}"
            )

            # Resetar a conta, já que o resultado
            # não pode ser utilizado.
            self._left = None

    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()  # Não tá funfando por alguma razão...

    # GERAR MENSAGENS POP-UPS
    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()  # Gerar a janela.
        msgBox.setText(text)  # Texto na janela.
        return msgBox

    # MENSAGENS DE ERRO
    # Pop-ups informando erros ocorridos na equação.
    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)  # Design da janela.

        # # Modificando o botão da janelinha.
        # msgBox.setStandardButtons(
        #     msgBox.StandardButton.Ok
        # )

        msgBox.exec()  # Execução da janela.

    # MENSAGENS DE INFORMAÇÃO
    # Pop-ups informando erros ocorridos na equação.
    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)  # Design da janela.

        # # Modificando o botão da janelinha.
        # msgBox.setStandardButtons(
        #     msgBox.StandardButton.Ok
        # )

        msgBox.exec()  # Execução da janela.
