import zoof
from zoof import ui

def keep_alive():
    __iep__.process_commands()
    ui.call_later(0.1, keep_alive)



class MyApp(ui.App):
    
    _config = ui.App.Config(title='Zoof test app', size=(400, 300),
                            icon='https://assets-cdn.github.com/favicon.ico')
               
    def init(self):
        
        #self.b0 = ui.Button(self, 'This is behind the box layout')
        
        TEST = 2
        
        if TEST == 1:
            with ui.HBox(self, flex=1) as self.hbox1:
                self.b1 = ui.Button(text='Hola', flex=1)
                self.b2 = ui.Button(text='Hello world', flex=0)
                self.b3 = ui.Button(text='Foo bar', flex=3)
        
        if TEST == 2:
            with ui.VBox(self) as self.vbox:
                
                ui.Label(text='Flex 0 0 0', flex=0)
                with ui.HBox(flex=0) as self.hbox2:
                    self.b1 = ui.Button(text='Hola', flex=0)
                    self.b2 = ui.Button(text='Hello world', flex=0)
                    self.b3 = ui.Button(text='Foo bar', flex=0)
                
                ui.Label(text='Flex 1 0 3', flex=0)
                with ui.HBox(flex=0) as self.hbox1:
                    self.b1 = ui.Button(text='Hola', flex=1)
                    self.b2 = ui.Button(text='Hello world', flex=0)
                    self.b3 = ui.Button(text='Foo bar', flex=3)
                
                ui.Label(text='margin 10 (around layout)', flex=0)
                with ui.HBox(flex=0, margin=10) as self.hbox2:
                    self.b1 = ui.Button(text='Hola', flex=0)
                    self.b2 = ui.Button(text='Hello world', flex=0)
                    self.b3 = ui.Button(text='Foo bar', flex=0)
                
                ui.Label(text='spacing 10 (inter-widget)', flex=0)
                with ui.HBox(flex=0, spacing=10) as self.hbox2:
                    self.b1 = ui.Button(text='Hola', flex=0)
                    self.b2 = ui.Button(text='Hello world', flex=0)
                    self.b3 = ui.Button(text='Foo bar', flex=0)
                
                ui.Widget(flex=1)
                ui.Label(text='Note the spacer Widget above', flex=0)
        
        if TEST == 3:
            with ui.HBox(self, spacing=20):
                with ui.Form() as self.form:
                    # todo: can this be written with one line per row?
                    # e.g. self.b1 = ui.Button(label='Name', text='Hola')
                    ui.Label(text='Name:')
                    self.b1 = ui.Button(text='Hola')
                    ui.Label(text='Age:')
                    self.b2 = ui.Button(text='Hello world')
                    ui.Label(text='Favorite color:')
                    self.b3 = ui.Button(text='Foo bar')
                with ui.Form() as self.form:
                    # e.g. self.b1 = ui.Button(label='Name', text='Hola')
                    ui.Widget(flex=1)  # Add a flexer
                    ui.Widget()
                    ui.Label(text='Pet name:')
                    self.b1 = ui.Button(text='Hola')
                    ui.Label(text='Pet Age:')
                    self.b2 = ui.Button(text='Hello world')
                    ui.Label(text='Pet\'s Favorite color:')
                    self.b3 = ui.Button(text='Foo bar')
                    ui.Widget(flex=1)
        if TEST == 4:
            with ui.Grid(self) as self.grid:
                self.b1 = ui.Button(text='Nostretch', pos=(0, 0))
                self.b2 = ui.Button(text='Hola', pos=(1, 1), flex=(1,1))
                self.b3 = ui.Button(text='Hello world', pos=(2, 2), flex=(2, 1))
                self.b4 = ui.Button(text='Foo bar', pos=(4, 4), flex=(1, 2))
        
        if TEST == 5:
            with ui.PinBoard(self) as self.grid:
                self.b1 = ui.Button(text='Stuck at (20, 20)', pos=(20, 30))
                self.b2 = ui.Button(text='Dynamic at (20%, 20%)', pos=(0.2, 0.2))
                self.b3 = ui.Button(text='Dynamic at (50%, 70%)', pos=(0.5, 0.7))
            
        #self.win = ui.Window(self, 'A new window!')
        
# class MyApp2(ui.App):
#     def init(self):
#         self.b = ui.Button(self, 'Hello world')

app = MyApp()
keep_alive()
ui.run(runtime='xul')
