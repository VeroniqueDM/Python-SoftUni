class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if self.name != new_name:
            self.name = new_name
            return self.name
        return "Name cannot be the same."
    def change_due_date(self, new_due_date):
        if new_due_date != self.due_date:
            self.due_date = new_due_date
            return self.due_date
        return "Date cannot be the same."

    def add_comment(self, comment):
        self.comments.append(comment)


    def edit_comment(self, comment_number, new_comment):
        try:
            self.comments[comment_number] = new_comment
            result = ", ".join(self.comments)
            return result
        except IndexError:
            return "Cannot find comment."
    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
