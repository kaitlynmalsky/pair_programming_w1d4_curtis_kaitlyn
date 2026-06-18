"""
Main Program — Product Inventory System
Week 1, Thursday | Pair Programming Exercise

Wire everything together here. Complete each numbered section.
Run with:  python main.py

References:
    written/4-Thursday/lists.md
    written/4-Thursday/tuples.md
    written/4-Thursday/sets.md
    written/4-Thursday/exception-handling-custom-exceptions.md
    written/4-Thursday/try-except.md
"""

from week1_day4.starter_code.product import Product
from week1_day4.starter_code.inventory import Inventory
from week1_day4.starter_code.exceptions import ProductNotFoundError, InsufficientStockError, InventoryError


def section(title: str) -> None:
    print(f"\n{'─' * 55}")
    print(f"  {title}")
    print(f"{'─' * 55}")


def main():
    inv = Inventory()

    # ── 1. Add at least 8 products across 3+ categories ───────────────────
    section("1. Loading Inventory")

    # TODO: Create and add at least 8 Product instances.
    # Use at least 3 different categories (e.g., "electronics", "accessories", "software").
    # Example:
    #   p = Product("Laptop", 999.99, stock=15, category="electronics")
    #   product_id = inv.add_product(p)
    #   print(f"  Added: {p} → ID={product_id}")
    p1 = Product("Laptop no ram", 199.99, stock=15, category="electronics")
    product_id = inv.add_product(p1)
    print(f"  Added: {p1} → ID={product_id}")

    p2 = Product("bracelet", 9.99, stock=3, category="accessories")
    product_id = inv.add_product(p2)
    print(f"  Added: {p2} → ID={product_id}")

    p3 = Product("openai", 1.99, stock=17, category="software")
    product_id = inv.add_product(p3)
    print(f"  Added: {p3} → ID={product_id}")

    p4 = Product("necklace", 9999.99, stock=87, category="accessories")
    product_id = inv.add_product(p4)
    print(f"  Added: {p4} → ID={product_id}")

    p5 = Product("charger", 99.99, stock=16, category="electronics")
    product_id = inv.add_product(p5)
    print(f"  Added: {p5} → ID={product_id}")

    p6 = Product("bill gates", 100.00, stock=65, category="software")
    product_id = inv.add_product(p6)
    print(f"  Added: {p6} → ID={product_id}")

    p7 = Product("ram", 9990.99, stock=99, category="electronics")
    product_id = inv.add_product(p7)
    print(f"  Added: {p7} → ID={product_id}")

    p8 = Product("twitter", 1.00, stock=9999, category="software")
    product_id = inv.add_product(p8)
    print(f"  Added: {p8} → ID={product_id}")

    p9 = Product("intel processor", 1.00, stock=9999, category="eletronics")
    product_id = inv.add_product(p9)
    print(f"  Added: {p9} → ID={product_id}")

    # ── 2. Display all products sorted by price ────────────────────────────
    section("2. All Products (sorted by price)")

    # TODO: Use sorted() with the __lt__ dunder to sort inv.products.values().
    # Print each product using its __str__ representation.

    organizedInventory = sorted(inv.products.values())

    for item in organizedInventory:
        print (item)

    # ── 3. Search products by keyword ─────────────────────────────────────
    section("3. Search: 'pro'")

    # TODO: Call inv.search("pro") and print the results.
    # This uses the __contains__ dunder on Product.
    resultSearch = inv.search("pro")
    for output in resultSearch:
        print(f"{output}")


    # ── 4. Filter by category ─────────────────────────────────────────────
    section("4. Category: 'electronics'")

    # TODO: Call inv.by_category("electronics") and print the results.
    resultCategory = inv.by_category("electronics")
    for output in resultCategory:
        print(f"{output}")


    # ── 5. Sell products — one should succeed, one should fail ────────────
    section("5. Sell Operations")

    # TODO: Attempt to sell a quantity that succeeds, then one that exceeds stock.
    # Use try/except to catch InsufficientStockError and print the error details.
    # Access e.requested and e.available from the exception object.
    try:
        inv.sell(1, 2)
        inv.sell(1, 100)
    except InsufficientStockError as e:
        print(e)
        print(f"requested: {e.requested}")
        print(f"available:{e.available}")


    # ── 6. Access a non-existent product ID ───────────────────────────────
    section("6. Non-Existent Product Lookup")

    # TODO: Try inv.get_product(9999) and catch ProductNotFoundError.
    try:
        inv.get_product(9999)
    except ProductNotFoundError as p:
        print(p)
    

    # ── 7. Transaction history ────────────────────────────────────────────
    section("7. Recent Transaction History")

    # TODO: Print each entry in inv.history.
    # Remember: history is a deque — you can iterate over it directly.

    for item in inv.history:
        print(item)



    # ── 8. Inventory summary ──────────────────────────────────────────────
    section("8. Inventory Summary")

    # TODO: Call inv.summary() and print each key-value pair neatly.
    summaryDict = inv.summary()

    print(f"{'Total Products: ':>20} {summaryDict['total_products']}")
    print(f"{'Total Value: ':>20} {summaryDict['total_value']}")
    print(f"{'categories: ':>20} {str(summaryDict['categories'])} ")
    print(f"{'out of stock count: ':>20} {summaryDict['out_of_stock_count']} ")


    # ── 9. Set operations on categories ───────────────────────────────────
    section("9. Set Operations on Categories")

    my_wishlist = {"electronics", "gaming", "software"}

    # TODO: Use inv.categories (a set) and my_wishlist to show:
    #   - Union:        All categories across both sets
    #   - Intersection: Categories in BOTH my_wishlist and the inventory
    #   - Difference:   Categories in my_wishlist but NOT in the inventory
    # Use the |, &, - operators (ref: written/4-Thursday/sets.md)

    allCategories = inv.categories | my_wishlist
    sameCategories  = inv.categories & my_wishlist
    onlyWishlist = my_wishlist - inv.categories
    print(f"Union: {allCategories}")
    print(f"Intersection: {sameCategories}")
    print(f"Difference: {onlyWishlist}")


    # ── 10. Tuple-based product configurations ────────────────────────────
    section("10. Product Configs as Tuples")

    # TODO: Define at least 3 product configurations as tuples:
    #   configs = [
    #       ("Monitor", 349.99, 8, "electronics"),
    #       ("USB Hub",  24.99, 30, "accessories"),
    #       ...
    #   ]
    # Iterate over configs and add each as a Product to the inventory.
    # Print the updated total using len(inv).
    # This demonstrates tuples as immutable, structured data records.
    # (ref: written/4-Thursday/tuples.md — "Tuples as Fixed Records")
    
    productConfig = [
          ("Monitor", 349.99, 8, "electronics"),
          ("USB Hub",  24.99, 30, "accessories"),
          ("Chrome", 19.99, 100, "software")
    ]

    for name, stock, price, category in productConfig:
        product = Product(name, price, stock, category)
        inv.add_product(product)
        
    print(f"total inventory: {len(inv)}")

    # ── 11. Sell exactly all remaining stock (stock → 0) ────────────────────────────
    section("11. Sell exactly all remaining stock (stock → 0)")

    try:
        inv.sell(2, 3)
        product = inv.get_product(2)
        if product.stock == 0:
            print("stock is 0")
    except InsufficientStockError as e:
        print(e)
        print(f"requested: {e.requested}")
        print(f"available:{e.available}")

    # ── 12. Remove a product and try to sell it. ────────────────────────────
    section("12. Remove a product and try to sell it.")
    
    inv.remove_product(9)
    print("removed: 9")
    try:
        inv.sell(9, 1)

    except ProductNotFoundError as e:
        print(e)


    # ── 13. Add duplicate products (same name, same category) — what happens? ────────────────────────────
    section("13. Add duplicate products (same name, same category) — what happens?")

    try:
        inv.add_product(p1)
        print(f"  Added: {p1} → ID={product_id}")
        print("it dupped the add product we do not have check condiition for addproduct() in inventory class therefore it accepts")
    except InventoryError as e:
        print(e)


    # ── 14. selling a negative quantity ────────────────────────────
    section("14. selling a negative quantity")

    try:
        inv.sell(1,-5)
        print("sold a negative quantity not possible")
    except InventoryError as e:
        print(e)

    # print(inv.products)

    # ── 15. Sell product with insufficient stock (should fail) and attempt to sell again (should succeed) after restock ──────────────────────────── 
    section("15. Sell product with insufficient stock (should fail) and attempt to sell again (should succeed) after restock")

    try:
        # product 1 should have a stock of 18
        inv.sell(1, 19)
        print("Sold more of product 1 than inventory has in stock")
    except InsufficientStockError as e:
        print(e)

    try:
        inv.restock(1, 1) # stock: 18 -> 19
        inv.sell(1, 19)
    except InsufficientStockError as e:
        print(e)

if __name__ == "__main__":
    main()