from typing import List, Optional
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        # return next((pr for pr in self.products if pr.name == product_name), None)
        for pr in self.products:
            if pr.name == product_name:
                return pr

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join([f"{pr.name}: {pr.quantity}" for pr in self.products])
