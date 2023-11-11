from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        self.categories.append(category) if category not in self.categories else None

    def add_topic(self, topic: Topic):
        self.topics.append(topic) if topic not in self.topics else None

    def add_document(self, document: Document):
        self.documents.append(document) if document not in self.documents else None

    def __object_grep(self, provided_id, class_name):
        object_grep = next((obj for obj in getattr(self, class_name) if obj.id == provided_id), None)
        return object_grep

    def edit_category(self, category_id: int, new_name: str):
        CTE = self.__object_grep(category_id, 'categories')
        CTE.edit(new_name) if CTE is not None else None

    def edit_document(self, document_id: int, new_file_name: str):
        DTE = self.__object_grep(document_id, 'documents')
        DTE.edit(new_file_name) if DTE is not None else None

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        TTE = self.__object_grep(topic_id, 'topics')
        TTE.edit(new_topic, new_storage_folder) if TTE is not None else None

    def delete_category(self, category_id):
        CTD = self.__object_grep(category_id, 'categories')
        self.categories.remove(CTD) if CTD is not None else None

    def delete_topic(self, topic_id):
        TTD = self.__object_grep(topic_id, 'topics')
        self.topics.remove(TTD) if TTD is not None else None

    def delete_document(self, document_id):
        DTD = self.__object_grep(document_id, 'documents')
        self.documents.remove(DTD) if DTD is not None else None

    def get_document(self, document_id):
        FD = self.__object_grep(document_id, 'documents')
        return repr(FD) if FD is not None else None

    def __repr__(self):
        return '\n'.join([repr(doc) for doc in self.documents])
