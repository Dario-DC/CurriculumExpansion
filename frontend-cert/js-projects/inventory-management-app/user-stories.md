1. You should declare an empty array named `inventory`, that will store product objects having a key `name` with the value of a string, and a key `quantity` with the value of an integer number.
1. You should create a function named `findProductIndex` that takes the product name as its argument and returns the index of the corresponding product object inside the `inventory` array. If the product is not found, the function should return `-1`.
1. You should create a function named `addProduct` that takes a product object as its argument.
1. If the product is already present in the inventory, the `addProduct` function should update its `quantity` value and log to the console the product name followed by a space and `quantity updated`.
1. If the product is not present in the inventory, the `addProduct` function should push the product to the `inventory` array and log to the console the product name followed by a space and `added to inventory`. 
1. You should create a function named `removeProduct` that takes the product name and quantity as its arguments.
1. The `removeProduct` function should subtract the passed quantity from the corresponding product object inside the inventory and log the string `Remaining <product-name> pieces: <product-quantity>` to the console, where `<product-name>` should be replaced by the product name, and `<product-quantity>` should be replaced by the product quantity.
1. If the quantity after the subtraction is zero, `removeProduct` should remove the product object from the inventory. Instead, if the quantity in the inventory is not enough to perform the subtraction, the `removeProduct` function should log the string `Not enough <product-name> available, remaining pieces: <product-quantity>` to the console.