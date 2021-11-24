from typing import Optional

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject

from src.views.crud_frame import CRUDScreen
from src.db.repository import Repository
from .update_frame_controller import UpdateController
from .read_frame_controller import ReadFrameController
from .delete_frame_controller import DeleteFrameController
from .create_frame_controller import CreateFrameController
from src.core.config import DATABASE_NAME


class CRUDFrameController(QObject):
    """
    Controller for CRUD screen
    """
    def __init__(self):
        super(CRUDFrameController, self).__init__()
        self.repository = Repository.create_repository()
        self.tables = self.__get_table_names()
        self.table_headers = self.set_table_fields()
        self.__view: CRUDScreen = None
        self.create_controller: CreateFrameController = None
        self.update_controller: UpdateController = None
        self.delete_controller: DeleteFrameController = None
        self.read_controller: ReadFrameController = None

    def init_ui(self, parent):
        self.__view = CRUDScreen(parent)
        self.__view.setup_ui()

    def __get_table_names(self) -> Optional[list[str]]:
        """

        :return: Optional[list[str]]
        """
        if DATABASE_NAME == '':
            return
        query = f"select TABLE_NAME from information_schema.tables where information_schema.tables.TABLE_SCHEMA = '{DATABASE_NAME}'"

        res = self.repository.execute(query)
        return [x[0] for x in res]

    def __get_datatypes(self, table_name) -> Optional[list[tuple[str, str]]]:
        if DATABASE_NAME == '':
            return
        query = f"select COLUMN_NAME, DATA_TYPE from information_schema.columns where table_schema = '{DATABASE_NAME}' " \
                f"and TABLE_NAME = '{table_name}';"
        res = self.repository.execute(query)
        return [x for x in res]

    def set_table_names(self):
        for table_name in self.tables:
            self.__view.current_table_box.addItem(table_name)

    def set_table_fields(self, table_name=None):
        if self.tables:
            if table_name is None:
                table_name = self.tables[0]
            query = f"select * from {table_name};"
            rows = self.repository.execute(query)
            descriptions = rows.cursor.description
            headers = [description[0] for description in descriptions]
            return headers

    def update_fields(self):
        table_name = self.__view.current_table_box.currentText()
        data_types = self.__get_datatypes(table_name)
        self.table_headers = self.set_table_fields(table_name)

        self.update_controller.current_table = table_name
        self.update_controller.validate_data = data_types
        self.update_controller.set_boxes(self.table_headers)
        self.update_controller.set_conditions(self.table_headers)

        self.read_controller.current_table = table_name
        self.read_controller.show_current_table()

        self.delete_controller.current_table = table_name
        self.delete_controller.set_condition(self.table_headers)

        self.create_controller.current_table = table_name
        self.create_controller.validate_data = data_types
        self.create_controller.add_fields(data_types)

    @property
    def view(self):
        return self.__view

    # TODO move to constructor
    @view.setter
    def view(self, value):
        self.__view = value

        self.set_table_names()
        self.create_controller = CreateFrameController(self.__view.create_page, self.repository)
        self.update_controller = UpdateController(self.__view.update_page, self.repository)
        self.delete_controller = DeleteFrameController(self.__view.delete_page, self.repository)
        self.read_controller = ReadFrameController(self.__view.read_page, self.repository)

        self.__view.current_table_box.currentTextChanged.connect(self.update_fields)
        self.update_fields()

