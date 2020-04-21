hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-D mapreduce.job.reduces=0 \
-files tld_mapper.py \
-input s3://commoncrawl/crawl-data/CC-MAIN-2020-10/segments/1581875141396.22/wat/CC-MAIN-20200216182139-20200216212139-00000.warc.wat.gz \
-input s3://commoncrawl/crawl-data/CC-MAIN-2020-10/segments/1581875141396.22/wat/CC-MAIN-20200216182139-20200216212139-00001.warc.wat.gz \
-output test \
-mapper tld_mapper.py