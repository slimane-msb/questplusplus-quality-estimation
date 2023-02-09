filename = "output/test/output.txt"
file_rank = "input/training/tgt1/target.sent-level_rank.sp"

train_len = 0.8

def fet_to_learning():
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

# fet_to_learning()

import pandas as pd 

df = pd.read_csv("learning/data/features/dataset/test.qe.tsv", sep="\t", header=None)
df.fillna(0, inplace=True)
df.to_csv('learning/data/features/dataset/test.qe.nona.tsv', index=False, header=None, sep="\t")
print(df)

df = pd.read_csv("learning/data/features/dataset/training.qe.tsv", sep="\t", header=None)
df.fillna(0, inplace=True)
df.to_csv('learning/data/features/dataset/training.qe.nona.tsv', index=False, header=None, sep="\t")
print(df)