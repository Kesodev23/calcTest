from kivy.config import Config
Config.set('kivy','window_icon','SGN_10_25_2023_1698219205385.ico')
import kivy
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import Screen
from math import *
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.button import MDFlatButton

Window.size = (320,600)

class ScreenManagement(ScreenManager):
    pass

class MainGui(MDScreen):
    pass
    

class MyGui(MDScreen):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        global sent, disp ,symp 
        sent=''
        disp=''
        symp=''

        

    def Display(self,arg,obj):
        match arg:
            case '=':
                return ''
            case '3.142':
                return ''
            case 'sqrt':
                return '('
            case '^':
                return ''
            case '%':
                return ''
            case 'sin':
                return '('
            case 'cos':
                return '('
            case 'tan':
                return '('
            case 'log':
                return '('
            case 'asin':
                return '('
            case 'acos':
                return '('
            case 'atan':
                return '('
            case 'exp':
                return '('
            case 'log10':
                return '('

    def set_arg(self,*arg):
        self.disp = arg[0]
        self.sent = arg[1]

        if arg[1] != '=' and arg[1] != 'Del' and arg[1] != 'cls' :
            self.combin = arg[2] + arg[1]
        else:
            self.combin = arg[2]
        try:
            #POWER CHECK
            val=''
            if '^' in self.combin:
                val = self.combin.replace('^','**')
            elif '!' in self.combin:
                val = self.factorial(self.combin.replace('!',''))
                return val
            else:
                val = self.combin
                
            return eval(val)
        except SyntaxError:
            pass
        except TypeError:
            pass
        except NameError:
            pass
        except ZeroDivisionError:
            return 'Div/0'
        except ValueError:
            return 'Value Error!'

    def set_symb(self,*arg):
        self.symb = arg[0]
        self.combin =self.combin + self.symb

    def factorial(self,arg):
        val = 1
        num = 1
        num = int(arg)
        if num <= 0:
            return 1
        else:
            for i in range(1,num +1):
                val = val*i
            return val

class about_dialog(OneLineAvatarListItem):
    divider = None
    

class MainApp(MDApp):

    dialog = None

    def build (self):
        self.title = 'CALCULATOR'
        global combin, cursor_pos
        combin=''
        cursor_pos = ''
        return MyGui()
        
    def fill_display(self,arg):
        #SHOW RESULTS
        self.show_results(arg)
        #DISPLAY EXPRESSION
        val=(MyGui().Display(arg,self.root.ids['display_txt']))
        if val:
            val = arg+val
        else:
            val = arg

        self.root.ids['display_txt'].insert_text(val)
        
    def enter_value_in_curent_cursor_pos(self,pos):
        val = self.root.ids['display_txt'].text
        print(val[0:pos])

    def show_results(self,arg):
        rslt=MyGui().set_arg(self.root.ids['results_lbl'].text,arg,self.root.ids['display_txt'].text)
        try:
            rslt=f"{rslt:,}"
        except TypeError:
            pass
        self.root.ids['results_lbl'].text = str(rslt) if rslt else ' '
    
    def del_from_display(self):
        val = self.root.ids['display_txt'].text
        self.root.ids['display_txt'].text = val[0:len(val)-1]
        
        self.show_results('Del')
        
        
    def cls_display(self):
        self.root.ids['display_txt'].text = ''
        self.show_results('cls')

    def results_display(self):
        self.show_results('=')
    
    def about_func(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = 'About Us',
                text = 'Contact Us On:.\n\nkesodevinfodesk@gmail.com.',
                type = 'confirmation',
                buttons = [
                    MDFlatButton(
                        text = 'Ok',
                        theme_text_color = 'Custom',
                        text_color = self.theme_cls.primary_color,
                        on_release = self.cancel_dialog
                    ),
                ]
                
            )
        self.dialog.open()

    def cancel_dialog(self,obj):
        self.dialog.dismiss()

 
if __name__=='__main__':
    app = MainApp()
    app.run()