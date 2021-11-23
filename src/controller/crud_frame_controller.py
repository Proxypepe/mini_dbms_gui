from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject

from src.views.crud_frame import GRUDScreen
from src.db.repository import Repository
from .update_frame_controller import UpdateController


class CRUDFrameController(QObject):

    def __init__(self):
        super(CRUDFrameController, self).__init__()
        self.repository = Repository.create_repository()
        self.__view = None
        self.create_tap = None
        self.update_controller = None
        self.delete_tap = None
        self.read_tap = None

    def init_ui(self, parent):
        self.__view = GRUDScreen(parent)
        self.__view.setup_ui()

    @property
    def view(self):
        return self.__view

    @view.setter
    def view(self, value):
        self.__view = value
        self.create_tap = self.__view.create_page
        self.update_controller = UpdateController(self.__view.update_page, self.repository)
        self.delete_tap = self.__view.delete_page
        self.read_tap = self.__view.read_page
