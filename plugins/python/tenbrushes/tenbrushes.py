'''
This script is licensed CC 0 1.0, so that you can learn from it.

------ CC 0 1.0 ---------------

The person who associated a work with this deed has dedicated the work to the public domain by waiving all of his or her rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law.

You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.

https://creativecommons.org/publicdomain/zero/1.0/legalcode
'''
import krita
from . import uitenbrushes


class TenBrushesExtension(krita.Extension):

    def __init__(self, parent):
        super(TenBrushesExtension, self).__init__(parent)

        self.actions = []
        self.buttons = []
        self.selectedPresets = []
        self.oldPreset = None

    def setup(self):
        self.readSettings()

    def createActions(self, window):
        action = window.createAction("ten_brushes", i18n("Ten Brushes"))
        action.setToolTip(i18n("Assign ten brush presets to ten shortcuts."))
        action.triggered.connect(self.initialize)
        self.loadActions(window)

    def initialize(self):
        self.uitenbrushes = uitenbrushes.UITenBrushes()
        self.uitenbrushes.initialize(self)

    def readSettings(self):
        self.selectedPresets = Application.readSetting("", "tenbrushes", "").split(',')

    def writeSettings(self):
        presets = []

        for index, button in enumerate(self.buttons):
            self.actions[index].preset = button.preset
            presets.append(button.preset)
        Application.writeSetting("", "tenbrushes", ','.join(map(str, presets)))

    def loadActions(self, window):
        allPresets = Application.resources("preset")

        for index, item in enumerate(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']):
            action = window.createAction("activate_preset_" + item, str(i18n("Activate Brush Preset {num}")).format(num=item), "")
            action.triggered.connect(self.activatePreset)

            if index < len(self.selectedPresets) and self.selectedPresets[index] in allPresets:
                action.preset = self.selectedPresets[index]
            else:
                action.preset = None

            self.actions.append(action)

    def activatePreset(self):
        allPresets = Application.resources("preset")
        if Application.activeWindow() and len(Application.activeWindow().views()) > 0 and self.sender().preset in allPresets:
            currentPreset = Application.activeWindow().views()[0].currentBrushPreset()
            if self.sender().preset == currentPreset.name():
                Application.activeWindow().views()[0].activateResource(self.oldPreset)
            else:
                self.oldPreset = Application.activeWindow().views()[0].currentBrushPreset()
                Application.activeWindow().views()[0].activateResource(allPresets[self.sender().preset])


Scripter.addExtension(TenBrushesExtension(Application))
