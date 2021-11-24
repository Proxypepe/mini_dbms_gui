from src.views.delete_page import DeletePage
from src.db.repository import Repository


class DeleteFrameController:

    def __init__(self, view: DeletePage, repository: Repository):
        self.view = view
        self.repository = repository
        self.current_table = ""

        self.view.delete_btn.clicked.connect(self.delete)

    def set_condition(self, fields):
        self.view.condition_value_2.clear()
        for field in fields:
            self.view.condition_value_2.addItem(field)

    def delete(self):
        query = f"DELETE FROM {self.current_table}"
        if self.view.condition_value.text() != "":
            query += f" WHERE {self.view.condition_value_2.currentText()} {self.view.comboBox_3.currentText()} " \
                     f"{self.view.condition_value.text()}"
        print(query)
