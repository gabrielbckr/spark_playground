import findspark
import os

spark_path = "/home/gabriel/dev/spark/spark-2.4.5-bin-hadoop2.7"
findspark.init(spark_path)
os.environ['JAVA_HOME'] = "/usr/java/jdk1.8.0_241/"

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

conf = SparkConf().setAppName('hello').setMaster('spark://localhost:7077')
sc = SparkContext(conf=conf)
spark = SparkSession.builder.config(conf=conf).getOrCreate()

# sc = SparkContext("local[*]")
# spark = SparkSession.builder.master("local[*]").getOrCreate()
