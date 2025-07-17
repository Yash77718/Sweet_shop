{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a615cff4-25cc-4d0a-a636-2feab9bb76a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Sweet:\n",
    "    def __init__(self, sweet_id, name, category, price, quantity):\n",
    "        self.sweet_id = sweet_id\n",
    "        self.name = name\n",
    "        self.category = category\n",
    "        self.price = price\n",
    "        self.quantity = quantity\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9bd1bda7-5b78-47b2-996e-6d89b1f5eefe",
   "metadata": {},
   "outputs": [],
   "source": [
    "class SweetShop:\n",
    "    def __init__(self):\n",
    "        self.sweets = {}\n",
    "\n",
    "    def add_sweet(self, sweet):\n",
    "        if sweet.sweet_id in self.sweets:\n",
    "            raise ValueError(\"Sweet with this ID already exists.\")\n",
    "        self.sweets[sweet.sweet_id] = sweet\n",
    "\n",
    "    def delete_sweet(self, sweet_id):\n",
    "        if sweet_id not in self.sweets:\n",
    "            raise KeyError(\"Sweet not found.\")\n",
    "        del self.sweets[sweet_id]\n",
    "\n",
    "    def get_sweet_by_id(self, sweet_id):\n",
    "        return self.sweets.get(sweet_id)\n",
    "\n",
    "    def view_sweets(self):\n",
    "        return list(self.sweets.values())\n",
    "\n",
    "    def purchase_sweet(self, sweet_id, quantity):\n",
    "        sweet = self.get_sweet_by_id(sweet_id)\n",
    "        if not sweet:\n",
    "            raise LookupError(\"Sweet not found.\")\n",
    "        if sweet.quantity < quantity:\n",
    "            raise ValueError(\"Not enough stock.\")\n",
    "        sweet.quantity -= quantity\n",
    "\n",
    "    def restock_sweet(self, sweet_id, quantity):\n",
    "        sweet = self.get_sweet_by_id(sweet_id)\n",
    "        if not sweet:\n",
    "            raise LookupError(\"Sweet not found.\")\n",
    "        sweet.quantity += quantity\n",
    "\n",
    "    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):\n",
    "        results = self.sweets.values()\n",
    "        if name:\n",
    "            results = [s for s in results if name.lower() in s.name.lower()]\n",
    "        if category:\n",
    "            results = [s for s in results if category.lower() in s.category.lower()]\n",
    "        if min_price is not None and max_price is not None:\n",
    "            results = [s for s in results if min_price <= s.price <= max_price]\n",
    "        return results\n",
    "\n",
    "    def sort_sweets(self, by=\"price\"):\n",
    "        if by == \"price\":\n",
    "            return sorted(self.sweets.values(), key=lambda s: s.price)\n",
    "        elif by == \"name\":\n",
    "            return sorted(self.sweets.values(), key=lambda s: s.name.lower())\n",
    "        else:\n",
    "            raise ValueError(\"Invalid sort field. Use 'price' or 'name'.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "72ccc065-e9da-441f-b2b7-41dc9c7a50a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "shop = SweetShop()\n",
    "shop.add_sweet(Sweet(1001, \"Kaju Katli\", \"Nut-Based\", 50, 10))\n",
    "shop.add_sweet(Sweet(1002, \"Gulab Jamun\", \"Milk-Based\", 30, 20))\n",
    "shop.add_sweet(Sweet(1003, \"Rasgulla\", \"Milk-Based\", 20, 15))\n",
    "shop.add_sweet(Sweet(1004, \"Ladoo\", \"Traditional\", 25, 12))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fcda21b9-fc4f-413a-abf5-137d4a8b83e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Search by name passed!\n",
      "✅ Search by category passed!\n",
      "✅ Search by price range passed!\n"
     ]
    }
   ],
   "source": [
    "# Search by name\n",
    "results = shop.search_sweets(name=\"kaju\")\n",
    "assert len(results) == 1 and results[0].name == \"Kaju Katli\"\n",
    "print(\"✅ Search by name passed!\")\n",
    "\n",
    "# Search by category\n",
    "results = shop.search_sweets(category=\"Milk-Based\")\n",
    "assert len(results) == 2\n",
    "print(\"✅ Search by category passed!\")\n",
    "\n",
    "# Search by price range\n",
    "results = shop.search_sweets(min_price=20, max_price=30)\n",
    "assert len(results) == 3\n",
    "print(\"✅ Search by price range passed!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7623487e-c4b5-49ed-9cde-85c03877e2c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Sort by price passed!\n",
      "✅ Sort by name passed!\n",
      "✅ Invalid sort field test passed!\n"
     ]
    }
   ],
   "source": [
    "# Sort by price\n",
    "sorted_by_price = shop.sort_sweets(by=\"price\")\n",
    "assert [s.name for s in sorted_by_price] == [\"Rasgulla\", \"Ladoo\", \"Gulab Jamun\", \"Kaju Katli\"]\n",
    "print(\"✅ Sort by price passed!\")\n",
    "\n",
    "# Sort by name\n",
    "sorted_by_name = shop.sort_sweets(by=\"name\")\n",
    "assert [s.name for s in sorted_by_name] == [\"Gulab Jamun\", \"Kaju Katli\", \"Ladoo\", \"Rasgulla\"]\n",
    "print(\"✅ Sort by name passed!\")\n",
    "\n",
    "# Invalid sort key\n",
    "try:\n",
    "    shop.sort_sweets(by=\"quantity\")\n",
    "    print(\"❌ Invalid sort field failed (should raise)\")\n",
    "except ValueError:\n",
    "    print(\"✅ Invalid sort field test passed!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b0719771-7fdf-49e9-b71f-d44f66d13cb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Sort by price passed!\n",
      "✅ Sort by name passed!\n",
      "✅ Invalid sort field test passed!\n"
     ]
    }
   ],
   "source": [
    "# Sort by price\n",
    "sorted_by_price = shop.sort_sweets(by=\"price\")\n",
    "assert [s.name for s in sorted_by_price] == [\"Rasgulla\", \"Ladoo\", \"Gulab Jamun\", \"Kaju Katli\"]\n",
    "print(\"✅ Sort by price passed!\")\n",
    "\n",
    "# Sort by name\n",
    "sorted_by_name = shop.sort_sweets(by=\"name\")\n",
    "assert [s.name for s in sorted_by_name] == [\"Gulab Jamun\", \"Kaju Katli\", \"Ladoo\", \"Rasgulla\"]\n",
    "print(\"✅ Sort by name passed!\")\n",
    "\n",
    "# Invalid sort key\n",
    "try:\n",
    "    shop.sort_sweets(by=\"quantity\")\n",
    "    print(\"❌ Invalid sort field failed (should raise)\")\n",
    "except ValueError:\n",
    "    print(\"✅ Invalid sort field test passed!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e58f8c19-b7cc-4fac-a1eb-aa6cd59a249e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3ffc4a4-1c95-41c6-9e9d-27d6f7f622b1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
