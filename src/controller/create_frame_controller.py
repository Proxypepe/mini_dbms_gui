from src.views.create_page import CreatePage
from src.db.repository import Repository

from src.views.create_field import CreateField


class CreateFrameController:
    def __init__(self, view: CreatePage, repository: Repository):
        self.view = view
        self.repository = repository
        self.current_table = ""
        self.fields: list[CreateField] = []

    def add_fields(self, fields, types=None):
        for field in self.fields:
            self.view.verticalLayout.removeWidget(field)
        self.fields.clear()

        for field in fields:
            create_field = CreateField()
            create_field.field_name_lbl.setText(field)
            self.view.verticalLayout.addWidget(create_field)
            self.fields.append(create_field)
