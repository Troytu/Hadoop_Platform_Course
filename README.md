# Hadoop_Platform_Course

Codes of Hadoop_Platform_Course.

# Commands:

hdfs dfs -mkdir /user

hdfs dfs -mkdir /user/cloudera

hdfs dfs -mkdir /user/cloudera/input

hdfs dfs -put join1_FileA.txt /user/cloudera/input

hdfs dfs -put join1_FileB.txt /user/cloudera/input

hdfs dfs -ls /user/cloudera/input

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.3.jar -input /user/cloudera/input -output /user/cloudera/output_join -mapper ./join1_mapper.py -reducer ./join1_reducer.py

hdfs dfs -ls /user/cloudera/output_join/part-00000

hdfs dfs -cat /user/cloudera/output_join/part-00000


## Part 2

hdfs dfs -mkdir /user/cloudera/input_join2

sh make_data_join2.txt

hdfs dfs -put join2*.txt /user/cloudera/input_join2

hdfs dfs -ls /user/cloudera/input_join2

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.3.jar -input /user/cloudera/input_join3 -output /user/cloudera/output_join2 -mapper ./join2_mapper.py -reducer ./join2_reducer.py

hdfs dfs -ls /user/cloudera/output_join2/part-00000

hdfs dfs -cat /user/cloudera/output_join2/part-00000

hadoop fs -get /user/cloudera/output_join2/part-00000 ./total_viewers_count.txt

# Problems founded:

* Hdfs does not starting. Error **connection refused localhost:9000**


Follow the steps of:
[http://stackoverflow.com/questions/8076439/namenode-not-getting-started](http://stackoverflow.com/questions/8076439/namenode-not-getting-started)

Change the value of core-site.xml

```xml
<property>
<name>hadoop.tmp.dir</name>
<value>/home/marcelo/Ambiente/hadoop-2.6.3/tmp/</value>
</property>
```

For default the temp folder is set for **/tmp** folder. This folder is cleanup by SO on each reboot.



hadoop fs -rm -r -f user/cloudera/output_join2 

