import os
import pandas as pd
from typing import List, Dict

class ProductSaver:
    def __init__(self, datapath: str, name: str = "data"):
        """
        Initialize a ProductSaver instance.

        Args:
            datapath (str): The path where the JSON data file will be stored.
            name (str): The name of the JSON data file (default is "data").
        """
        if not os.path.exists(datapath):
            os.makedirs(datapath)

        self.jsonpath = os.path.join(datapath, "{}.json".format(name))

        if os.path.exists(self.jsonpath):
            self.data = pd.read_json(self.jsonpath, orient="records")
        else:
            self.data = pd.DataFrame(columns=["_id"])

    def product(self, product: Dict) -> bool:
        """
        Save a product to the product list.

        Args:
            product (Dict): A dictionary representing the product to be saved.

        Returns:
            bool: True if the product was successfully saved, False if it already exists.
        """
        product_id = product.get("_id")

        if product_id in self.data["_id"].values:
            return False

        self.data = pd.concat([self.data, pd.DataFrame([product])], ignore_index=True)

        self.data.to_json(self.jsonpath, orient="records")

        return True

    def product_list(self, product_list: List[Dict]):
        """
        Save a list of products to the product list.

        Args:
            product_list (List[Dict]): A list of dictionaries representing products.
        """
        products_list_df = pd.DataFrame(product_list)

        self.data = pd.concat(
            [
                products_list_df,
                self.data[~self.data["_id"].isin(products_list_df["_id"])],
            ],
            axis=0,
        )

        self.data.to_json(self.jsonpath, orient="records")
