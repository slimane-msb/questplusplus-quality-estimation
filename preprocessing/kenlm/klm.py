import kenlm

model = kenlm.Model('../input_data/language/en.arpa')
sentence = "my sentence exemple ."
score = model.score(sentence)
print("Log probability:", score)

# english
with open('../output_data/training/src/source.sent-level.en', 'r') as input_file, open('../output_data/training/src/source.sent-level_score.en', 'w') as output_file:
    for line in input_file:
        line = line.strip()
        log_prob = model.score(line)
        # normalisation
        log_prob_per_length = log_prob/len(line)
        # print(F"prob={log_prob} ==> prob/length = {log_prob_per_length} ==> line = {line}")
        output_file.write(str(log_prob_per_length) + '\n')


# spanish 
model = kenlm.Model('../input_data/language/sp.arpa')

with open('../output_data/training/tgt1/target.sent-level.sp', 'r') as input_file, open('../output_data/training/tgt1/target.sent-level_score.sp', 'w') as output_file:
    for line in input_file:
        line = line.strip()
        log_prob = model.score(line)
        # normalisation
        log_prob_per_length = log_prob/len(line)
        # print(F"prob={log_prob} ==> prob/length = {log_prob_per_length} ==> line = {line}")
        output_file.write(str(log_prob_per_length) + '\n')


# combine with output from quest++
with open('../output_data/training/tgt1/output.txt', 'r') as file1, \
     open('../output_data/training/src/source.sent-level_score.en', 'r') as file2, \
     open('../output_data/training/tgt1/target.sent-level_score.sp', 'r') as file3, \
     open('../output_data/training/tgt1/output_lm.txt', 'w') as output:
    for line1, line2, line3 in zip(file1, file2, file3):
        output.write(line1.strip() + '\t' + line2.strip() + '\t' + line3.strip() + '\n')
