# dark mode class
class ColorTheme:
    #Basic Color Variables
    BG = '#EAEAEA'
    FWG = '#2C332C'
    FG = '#458448'
    BTN = '#4C78EB'
    Theme = 'Light'

    def setDarkColorScheme(self):
        self.BG = '#283328'
        self.FWG = '#FFFFFF'
        self.FG = '#EAEAEA'
        self.BTN = '#458448'
        self.Theme = 'Dark'

    def setLightColorScheme(self):
        self.BG = '#EAEAEA'
        self.FWG = '#2C332C'
        self.FG = '#458448'
        self.BTN = '#4C78EB'
        self.Theme = 'Light'

    def __init__(self, colorTheme):
        self.Theme = colorTheme
        if(colorTheme=='Dark'):
            self.setDarkColorScheme()
            print(colorTheme)
        else:
            self.setLightColorScheme()
    