from uiUtils import GUIComponents
from uiUtils.guiBackend import GUIBackend

class commonUI:

    def show_confirm_box(Self, title, massage, buttons):
        cmb = GUIComponents.confirmMessageBox(title, massage, buttons = buttons)
        return cmb.render()
    
    def change_cursure(self, name):
        GUIBackend.cursor_changer(name)