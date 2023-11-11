from typing import List

from project.category import Category
from project.topic import Topic


class Document:
    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags: List = []

    @classmethod
    def from_instances(cls, id: int, category: Category, topic: Topic, file_name: str):
        return cls(id, category.id if category else None, topic.id if topic else None, file_name)

    def add_tag(self, tag_content: str):
        self.tags.append(tag_content) if tag_content not in self.tags else None

    def remove_tag(self, tag_content: str):
        self.tags.remove(tag_content) if tag_content in self.tags else None

    # edit filename
    def edit(self, file_name: str):
        self.file_name = file_name

    def __repr__(self):
        return (f"Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, "
                f"tags: {', '.join(self.tags)}")

