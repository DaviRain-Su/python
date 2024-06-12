from typing import List

def print_models(unprinted_designs: List[str], completed_models: List[str]):
    # Simulate printing each design, until none are left.
    # Move each design to completed_models after printing.
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models: List[str]):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# This program demonstrates how to pass a list to a function and modify it within the function.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# use [:] to pass a copy of the list to the function
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
