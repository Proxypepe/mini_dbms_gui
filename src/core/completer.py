from PyQt5 import QtGui, QtCore, QtWidgets
from src.core.dictionary import keywords


class SQLDictionaryCompleter(QtWidgets.QCompleter):

    insertText = QtCore.pyqtSignal(str)

    def __init__(self, _keywords=None, parent=None):
        if _keywords is None:
            _keywords = keywords
            low_case_keywords = [keyword.lower() for keyword in _keywords]
            _keywords += low_case_keywords
        super(SQLDictionaryCompleter, self).__init__(_keywords, parent)

        self.activated.connect(self.changeCompletion)

    def changeCompletion(self, completion):
        if completion.find("(") != -1:
            completion = completion[:completion.find("(")]
        self.insertText.emit(completion)

