print("Choinka pierwszych krokow.")
def print_case(n):
    for size in range(1, n+1, 4):
        print((size * "*").center(n))

def print_segment(n):
    for size in range(1, n+1, 2):
        print((size * "*").center(n))

print_case(5)
print_segment(5)
print_case(5)
print_segment(5)