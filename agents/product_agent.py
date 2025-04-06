from database.schema import get_product_info

class ProductAgent:
    def __init__(self):
        pass

    def get_product_info(self, product_id):
        return get_product_info(product_id)
