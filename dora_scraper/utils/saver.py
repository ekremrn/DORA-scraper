import pandas as pd
import os

class ProductSaver:
    def __init__(self, data_path: str):
        self.data_path = data_path
        
        if os.path.exists(self.data_path):
            self.data = pd.read_json(self.data_path, orient="records")
        else:
            self.data = pd.DataFrame(columns=["id"])
    
    def save_product(self, product: dict) -> bool:
        """
        Save a product to the product list.
        """
        product_id = product.get("id")
        
        # Check if the product already exists in the DataFrame
        if product_id in self.data['id'].values:
            return False
        
        # Append the product to the DataFrame
        self.data = pd.concat([self.data, pd.DataFrame([product])], ignore_index=True)

        # Save the DataFrame to a JSON file
        self.data.to_json(self.data_path, orient="records")
        
        return True
