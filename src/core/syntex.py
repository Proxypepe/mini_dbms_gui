from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QColor


class Formatter:
    STYLES = {
        'keyword': int('FFD300', base=16),
        'braces': int('FFE773', base=16),
        'string': int('A68900', base=16),
        'string2': int('A68900', base=16),
        'numbers': format('brown'),
    }

    @staticmethod
    def format(color, style=''):
        _color = QtGui
        _color = setNamedColor(color)

        _format = QtGui.QTextCharFormat()
        _format.setForeground(_color)

        if 'bold' in style:
            _format.setFontWeight(QtGui.QFont.Bold)
        if 'italic' in style:
            _format.setFontItalic(True)

        return _format


class SQLHighlighter(QtGui.QSyntaxHighlighter):
    keywords = [
        'UPDATE', 'SET', 'ALTER', 'UNION ALL', 'WHERE', 'ALTER COLUMN', 'ALL', 'SELECT INTO', 'ALTER TABLE', 'NOT',
        'NOT NULL', 'CREATE TABLE', 'EXISTS', 'SELECT', 'INDEX', 'OR', 'HAVING', 'AND', 'DATABASE', 'INSERT INTO',
        'TRUNCATE TABLE', 'DROP VIEW', 'DELETE', 'CREATE UNIQUE INDEX', 'IS NOT NULL', 'PRIMARY KEY',
        'INSERT INTO SELECT', 'DISTINCT', 'DROP', 'CHECK', 'ORDER BY', 'PROCEDURE', 'RIGHT JOIN', 'SELECT DISTINCT',
        'CREATE PROCEDURE', 'GROUP BY', 'OUTER JOIN', 'COLUMN', 'DROP COLUMN', 'LEFT JOIN', 'ASC', 'INNER JOIN',
        'LIMIT', 'IS NULL', 'ROWNUM', 'ANY', 'FULL OUTER JOIN', 'JOIN', 'DESC', 'CREATE', 'AS', 'BACKUP DATABASE',
        'CASE', 'CONSTRAINT', 'UNION', 'BETWEEN', 'ADD', 'FOREIGN KEY', 'IN', 'DROP DEFAULT', 'ADD CONSTRAINT', 'FROM',
        'DROP TABLE', 'LIKE', 'CREATE INDEX', 'DEFAULT', 'DROP DATABASE', 'CREATE DATABASE', 'DROP INDEX',
        'CREATE VIEW', 'SELECT TOP', 'UNIQUE', 'REPLACE VIEW', 'VALUES', 'DROP CONSTRAINT', 'EXEC',
    ]

    braces = [
        '\{', '\}', '\(', '\)', '\[', '\]',
    ]

    def __init__(self, parent: QtGui.QTextDocument) -> None:
        super().__init__(parent)

        self.tripleQuoutesWithinStrings = []
        self.tri_single = (QtCore.QRegExp("'''"), 1
                           , Formatter.STYLES['string'])
        self.tri_double = (QtCore.QRegExp('"""'), 2
                           , Formatter.STYLES['string'])
        rules = []

        rules += [(r'\b%s\b' % w, 0, Formatter.STYLES['keyword'])
                  for w in SQLHighlighter.keywords]
        rules += [(r'\b%s\b' % w.lower(), 0, Formatter.STYLES['keyword'])
                  for w in SQLHighlighter.keywords]
        # rules += [(r'%s' % o, 0, Formatter.STYLES['operator'])
        #           for o in SQLHighlighter.operators]
        rules += [(r'%s' % b, 0, Formatter.STYLES['braces'])
                  for b in SQLHighlighter.braces]
        rules += [
            (r'\b[+-]?[-]+[lL]?\b', 0, Formatter.STYLES['numbers']),
            (r'\b[+-]?[xX][-A-Fa-f]+[lL]?\b', 0, Formatter.STYLES['numbers']),
            (r'\b[+-]?[-]+(?:\.[-]+)?(?:[eE][+-]?[-]+)?\b', 0, Formatter.STYLES['numbers']),
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, Formatter.STYLES['string']),
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, Formatter.STYLES['string']),
        ]
        self.rules = [(QtCore.QRegExp(pat), index, fmt)
                      for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, )
            if index >= 0:
                if expression.pattern() in [r'"[^"\\]*(\\.[^"\\]*)*"', r"'[^'\\]*(\\.[^'\\]*)*'"]:
                    innerIndex = self.tri_single[0].indexIn(text, index + 1)

                    if innerIndex == -1:
                        innerIndex = self.tri_double[0].indexIn(text, index + 1)

                    if innerIndex != -1:
                        tripleQuoteIndexes = range(innerIndex, innerIndex + 3)

                        self.tripleQuoutesWithinStrings.extend(tripleQuoteIndexes)
            while index >= 0:
                if index in self.tripleQuoutesWithinStrings:
                    index += 1
                    expression.indexIn(text, index)
                    continue
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, QColor(format))
                index = expression.indexIn(text, index + length)
        self.setCurrentBlockState(0)
        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)

    def match_multiline(self, text, delimiter, in_state, style):
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        else:
            start = delimiter.indexIn(text)
            if start in self.tripleQuoutesWithinStrings:
                return False
            add = delimiter.matchedLength()
        while start >= 0:
            end = delimiter.indexIn(text, start + add)
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
                self.setFormat(start, length, style)
                start = delimiter.indexIn(text, start + length)
        if self.currentBlockState() == in_state:
            return True
        else:
            return False
