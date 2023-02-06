import test_example
machine = test_example.machine()
first_order = test_example.first_order(machine)
second_order = test_example.second_order(first_order, machine)
test_example.test_production_line(second_order)
