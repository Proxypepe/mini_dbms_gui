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


class TextEdit(QtWidgets.QTextEdit):
    def __init__(self, *args):
        super(TextEdit, self).__init__(*args)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.completer = None

    def setCompleter(self, completer):
        if self.completer:
            self.disconnect(self.completer, 0, self, 0)
        if not completer:
            return

        completer.setWidget(self)
        completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer = completer
        self.completer.insertText.connect(self.insertCompletion)

    def insertCompletion(self, completion):
        tc = self.textCursor()
        extra = (len(completion) -
                 len(self.completer.completionPrefix()))
        cased_text = ""

        if all([ex.isupper() for ex in completion]):
            cased_text = self.completer.completionPrefix().upper()
        elif all([ex.islower() for ex in completion]):
            cased_text = self.completer.completionPrefix().lower()

        full_text = cased_text + completion[-extra:]
        self.completer.setCompletionPrefix(cased_text)
        tc.movePosition(QtGui.QTextCursor.Left)
        tc.movePosition(QtGui.QTextCursor.EndOfWord)
        for _ in range(len(cased_text)):
            tc.deletePreviousChar()
        tc.insertText(full_text)
        self.setTextCursor(tc)

    def textUnderCursor(self):
        tc = self.textCursor()
        tc.select(QtGui.QTextCursor.WordUnderCursor)
        return tc.selectedText()

    def focusInEvent(self, event):
        if self.completer:
            self.completer.setWidget(self)
        QtWidgets.QTextEdit.focusInEvent(self, event)

    def keyPressEvent(self, event):
        if self.completer and self.completer.popup() and self.completer.popup().isVisible():
            if event.key() in (
                    QtCore.Qt.Key_Enter,
                    QtCore.Qt.Key_Return,
                    QtCore.Qt.Key_Escape,
                    QtCore.Qt.Key_Tab,
                    QtCore.Qt.Key_Backtab):
                event.ignore()
                return

        isShortcut = (event.modifiers() == QtCore.Qt.ControlModifier and
                      event.key() == QtCore.Qt.Key_Space)

        if not self.completer or not isShortcut:
            QtWidgets.QTextEdit.keyPressEvent(self, event)

        ctrlOrShift = event.modifiers() in (QtCore.Qt.ControlModifier,
                                            QtCore.Qt.ShiftModifier)
        if ctrlOrShift and event.text() == '':
            return

        completionPrefix = self.textUnderCursor()

        if not isShortcut:
            if self.completer.popup():
                self.completer.popup().hide()
            return

        self.completer.setCompletionPrefix(completionPrefix)
        popup = self.completer.popup()
        popup.setCurrentIndex(
            self.completer.completionModel().index(0, 0))
        cr = self.cursorRect()
        cr.setWidth(self.completer.popup().sizeHintForColumn(0)
                    + self.completer.popup().verticalScrollBar().sizeHint().width())
        self.completer.complete(cr)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    completer = SQLDictionaryCompleter()
    te = TextEdit()
    te.setCompleter(completer)
    te.show()
    app.exec_()
