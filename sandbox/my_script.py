from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)

lines = sc.textFile("/opt/spark/README.md")
pythonLines = lines.filter(lambda line: "Python" in line)
print(pythonLines.first())
print(pythonLines.count())