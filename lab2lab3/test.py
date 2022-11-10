from SymbolTable import SymbolTable
symbol_table = SymbolTable()

symbol_table.add_item('a', 5)
value = symbol_table.find_item('a')
assert value == 5

removed_value = symbol_table.delete_item('a')
assert removed_value == 5

found_value = symbol_table.find_item('a')
assert found_value == None

symbol_table.add_item('a', 7)
symbol_table.add_item('b', 8) 

found_a = symbol_table.find_item('a')
assert found_a == 7
found_b = symbol_table.find_item('b')
assert found_b == 8

removed_a = symbol_table.delete_item('a')
assert removed_a == 7
removed_b = symbol_table.delete_item('a')
assert removed_b is None
found_value_b = symbol_table.find_item('b')
assert found_value_b == 8