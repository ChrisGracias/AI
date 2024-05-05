def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, target, source)

# Example usage:
n_disks = 3
source_peg = "A"
target_peg = "C"
auxiliary_peg = "B"
print(f"Solving Towers of Hanoi with {n_disks} disks:")
hanoi(n_disks, source_peg, target_peg, auxiliary_peg)
