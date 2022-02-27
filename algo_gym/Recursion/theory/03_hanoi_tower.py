def hanoi(from_peg, to_peg, temp_peg, disks):
    # move n - 1 disks to temp_peg
    if disks > 1:
        hanoi(from_peg, temp_peg, to_peg, disks - 1)

    print(from_peg, '->', to_peg)

    # move n - 1 disks from temp_peg to to_peg
    if disks > 1:
        hanoi(temp_peg, to_peg, from_peg, disks - 1)


if __name__ == '__main__':
    hanoi('A', 'C', 'B', 4)
