import numpy as np
import sys
import os

'''Sample wat file and execute hadoop streaming code'''

# number of files to sample
n = sys.argv[1]
# hadoop streaming output path
out = sys.argv[2]

f = open('wat.paths')
path_list = f.readlines()


pre = 'hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \\\n-D mapreduce.job.reduces=0 \\\n-files tld_mapper.py \\\n'
input_paths = ''.join(['-input s3://commoncrawl/'+path_list[i][:-1]+' \\\n' for i in \
                       list(np.random.choice(56000, int(n), replace=False))])
end = '-output '+out+' \\\n-mapper tld_mapper.py'


os.system(pre+input_paths+end)
# print(pre+input_paths+end)