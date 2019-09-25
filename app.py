import kivy
from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
import math

#todo auto focus text input

class CalculatorLayout(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(CalculatorLayout, self).__init__(*args, **kwargs)

class Calculator(App):
    action = 'none'
    val = 0
    textinput = TextInput(text = '', multiline = False)

    plus = Button(text = '+', font_size = 70)
    minus = Button(text = '-', font_size = 70)
    multiple = Button(text = '*', font_size = 70)
    divide = Button(text = '/', font_size = 70)
    equal = Button(text = '=', font_size = 70)
    c = Button(text = 'c', font_size = 70)
    power = Button(text = 'x**', font_size = 70)
    power3 = Button(text = 'x***', font_size = 70)
    squareRoot = Button(text = '√', font_size = 70)

    buttons = [plus, minus, multiple, divide, power, power3, squareRoot]

    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        
        layout.add_widget(self.textinput)
        layout.add_widget(self.plus)
        layout.add_widget(self.minus)
        layout.add_widget(self.multiple)
        layout.add_widget(self.divide)
        layout.add_widget(self.power)
        layout.add_widget(self.power3)
        layout.add_widget(self.squareRoot)
        layout.add_widget(self.equal)
        layout.add_widget(self.c)

        self.plus.bind(on_press = self.actionPlus) 
        self.minus.bind(on_press = self.actionMinus) 
        self.multiple.bind(on_press = self.actionMultiple) 
        self.divide.bind(on_press = self.actionDivide) 
        self.power.bind(on_press = self.actionPower) 
        self.power3.bind(on_press = self.actionPower3) 
        self.squareRoot.bind(on_press = self.actionSqrt)
        self.equal.bind(on_press = self.result) 
        self.c.bind(on_press = self.clear) 

        return layout

    def checkInput(self):
        try:
            fl = float(self.textinput.text)
            print(fl)
            return True
        except ValueError as e:
            print(e)
            return False

    def getInput(self):
        return float(self.textinput.text)

    def changeColor(self, button):
        button.background_color = (0, 0, 1, .1)

    def clearColors(self):
        for button in self.buttons:
            button.background_color = (1, 1, 1, 1)

    def actionPlus(self, button):
        self.clearColors()
        self.changeColor(button)

        if self.checkInput() == True:
            if self.action != 'equal':
                self.val += self.getInput()
            self.textinput.text = ''
        self.action = 'plus'

    def actionMinus(self, button):
        self.clearColors()
        self.changeColor(button)

        if self.checkInput() == True:
            if  self.action == 'none':
                self.val = self.getInput()
            elif self.action != 'equal':
                self.val = self.val - self.getInput()
            self.textinput.text = ''
        self.action = 'minus'

    def actionMultiple(self, button):
        self.clearColors()
        self.changeColor(button)

        if self.checkInput() == True:
            if  self.action == 'none':
                self.val = self.getInput()
            elif self.action != 'equal':
                self.val *= self.getInput()

            self.textinput.text = ''
        self.action = 'multiple'

    def actionDivide(self, button):
        self.clearColors()
        self.changeColor(button)

        if self.checkInput() == True:

            if  self.action == 'none':
                self.val = self.getInput()
            elif self.action != 'equal':
                self.val = self.val / self.getInput()
            self.textinput.text = ''
        self.action = 'divide'

    def actionPower(self, button):
        self.clearColors()
        if self.checkInput() == True:
            result = self.getInput()
            result *= result
            
            self.textinput.text = str(result)
            self.action = 'none'

    def actionPower3(self, button):
        self.clearColors()
        if self.checkInput() == True:
            result = self.getInput()
            result *= result * result
            
            self.textinput.text = str(result)
            self.action = 'none'

    def actionSqrt (self, button):
        self.clearColors()
        if self.checkInput() == True:
            result = math.sqrt(self.getInput())
            
            self.textinput.text = str(result)
            self.action = 'none'

    def clear(self, button):
        self.clearColors()
        self.val = 0
        self.action = 'none'
        self.textinput.text = ''

    def result(self, button):
        self.clearColors()
        if self.checkInput() == True:
            result = self.getInput()
        else:
            result = self.val

        if self.checkInput():
            if self.action == 'plus':
                result = self.val + self.getInput()
            elif self.action == 'minus':
                result = self.val - self.getInput()
            elif self.action == 'multiple':
                result = self.val * self.getInput()
            elif self.action == 'divide':
                result = self.val / self.getInput()

        self.val = result
        self.action = 'equal'
        self.textinput.text = str(result)
        return print(result)

c = Calculator()
c.run()