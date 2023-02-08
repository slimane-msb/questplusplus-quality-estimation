#!/bin/bash

# source="source.sent-level.en"
# target="target.sent-level.es"


source="training/src/source.sent-level.en"
target="training/tgt1/target.sent-level.sp"

echo  input/$source input/$target


java -cp QuEst++.jar shef.mt.SentenceLevelFeatureExtractor -tok -case true -lang english spanish -input input/$source input/$target -config config/config.sentence-level.properties