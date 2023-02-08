filename = "output/test/output.txt"
file_rank = "input/training/tgt1/target.sent-level_rank.sp"

train_len = 0.8

with open(filename) as file, open(file_rank) as file_rank:
    lines = file.readlines()
    split_index = int(len(lines) * train_len)
    with open("learning/data/features/dataset/training.qe.tsv", "w") as file1:
        for line in lines[:split_index]:
            file1.write(line)
    with open("learning/data/features/dataset/test.qe.tsv", "w") as file2:
        for line in lines[split_index:]:
            file2.write(line)

    # rank
    lines = file_rank.readlines()
    with open("learning/data/features/dataset/training.effort", "w") as file1:
        for line in lines[:split_index]:
            file1.write(line)
    with open("learning/data/features/dataset/test.effort", "w") as file2:
        for line in lines[split_index:]:
            file2.write(line)