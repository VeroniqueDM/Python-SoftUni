from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []


    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for category in self.categories:
            if category.id == category_id:
                category.edit(new_name)
                
    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        for document in self.documents:
            if document.id == document_id:
                document.edit(new_file_name)

    def delete_category(self, category_id):
        category = [cat for cat in self.categories if category_id == cat.id][0]
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [top for top in self.topics if topic_id == top.id][0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [doc for doc in self.documents if doc.id == document_id][0]
        self.documents.remove(document)

    def get_document(self, document_id):
        document = [doc for doc in self.documents if doc.id == document_id][0]
        return document

    def __repr__(self):
        return '\n'.join([repr(doc) for doc in self.documents])


