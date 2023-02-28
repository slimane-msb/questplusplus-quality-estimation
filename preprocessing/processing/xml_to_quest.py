import xml.etree.ElementTree as ET
import os

train_or_test = ["training", "test"]
tree = ET.parse('data/training_data/en-es/wmt2010-public.en-es.jcml.rank.jcml')
root = tree.getroot()

folders = ["src","tgt1","tgt2","tgt3","tgt4","ref"]

data_input = train_or_test[0]
for folder in folders:
    os.makedirs(f"output_data/{data_input}/{folder}", exist_ok=True)



with    open(F"output_data/{data_input}/src/source.sent-level.en", "w") as source_file,  \
        open(F"output_data/{data_input}/tgt1/target.sent-level.sp", "w") as target1_file,  \
        open(F"output_data/{data_input}/tgt2/target.sent-level.sp", "w") as target2_file,  \
        open(F"output_data/{data_input}/tgt3/target.sent-level.sp", "w") as target3_file,  \
        open(F"output_data/{data_input}/tgt4/target.sent-level.sp", "w") as target4_file,  \
        open(F"output_data/{data_input}/tgt1/target.sent-level_rank.sp", "w") as target1_rank,  \
        open(F"output_data/{data_input}/tgt2/target.sent-level_rank.sp", "w") as target2_rank,  \
        open(F"output_data/{data_input}/tgt3/target.sent-level_rank.sp", "w") as target3_rank,  \
        open(F"output_data/{data_input}/tgt4/target.sent-level_rank.sp", "w") as target4_rank,  \
        open(F"output_data/{data_input}/ref/ref.sent-level.sp", "w") as ref_file : 
    
    buffers = [ source_file, target1_file, target2_file, target3_file, target4_file, ref_file]
    rank_buffers = [target1_rank, target2_rank, target3_rank, target4_rank]
    for sentence in root.iter("judgedsentence"):
        for i in range(6):
            buffers[i].write((sentence[i].text) + "\n")
        for i in range(4):
            rank_buffers[i].write((sentence[i+1].get('rank')) + "\n")
        


# asset all files have the same number of lines 
with    open(F"output_data/{data_input}/src/source.sent-level.en", "r") as source_file,  \
        open(F"output_data/{data_input}/tgt1/target.sent-level.sp", "r") as target1_file,  \
        open(F"output_data/{data_input}/tgt2/target.sent-level.sp", "r") as target2_file,  \
        open(F"output_data/{data_input}/tgt3/target.sent-level.sp", "r") as target3_file,  \
        open(F"output_data/{data_input}/tgt4/target.sent-level.sp", "r") as target4_file,  \
        open(F"output_data/{data_input}/tgt1/target.sent-level_rank.sp", "r") as target1_rank,  \
        open(F"output_data/{data_input}/tgt2/target.sent-level_rank.sp", "r") as target2_rank,  \
        open(F"output_data/{data_input}/tgt3/target.sent-level_rank.sp", "r") as target3_rank,  \
        open(F"output_data/{data_input}/tgt4/target.sent-level_rank.sp", "r") as target4_rank,  \
        open(F"output_data/{data_input}/ref/ref.sent-level.sp", "r") as ref_file : 

    assert  len( source_file.readlines()) == len( target1_file.readlines()) == \
            len( target2_file.readlines()) == len( target3_file.readlines()) == \
            len( target4_file.readlines()) == len( target1_rank.readlines()) == \
            len( target2_rank.readlines()) == len( target3_rank.readlines()) == \
            len( target4_rank.readlines()) == len( ref_file.readlines()) 
