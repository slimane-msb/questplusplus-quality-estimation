WMT Ranking Data - XML version
Release date: 22.02.2013

For the WMT Shared Task where this data originate from, see: Callison-Burch, Findings of the 2011 Workshop on Statistical Machine Translation (WMT11)

For sample QE experiments with this dataset see: Avramidis, E. Comparative Quality Estimation: Automatic Sentence-Level Ranking of Multiple Machine Translation Outputs (COLING2012)


Judged Corpus Markup Language - File Description
================================================

node tags:
----------
judgedsentence: a ranking instance including one source and 5 target sentences
src: source sentence
tgt: target sentence
ref: reference sentence

attributes:
-----------
segment_id/id: id of the segment for the particular file
langsrc: source language (2-letter ISO code)
langtgt: target language (2-letter ISO code)
judge_id: id of the annotator who performed this judgement
system: the name of the system. Same system names may represent different systems from one year to another
rank: an integer representing the rank assigned to this particular translation alternative

Notice: WMT10 "public" data are also contained. They should be used with caution as explained in Callison-Burch (2010)
