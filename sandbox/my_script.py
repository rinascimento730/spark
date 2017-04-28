from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)

lines = sc.textFile("/opt/spark/README.md")
pythonLines = lines.filter(lambda line: "Python" in line)
print pythonLines.first()
print pythonLines.count()
print pythonLines.take(2)

nums = sc.parallelize([1, 2, 3, 4])
squared = nums.map(lambda x: x * x).collect()
for num in squared:
	print "%i " % (num)

lines = sc.parallelize(["Hello world", "hi"])
words = lines.flatMap(lambda line: line.split(" "))
print words.first()
print words.count()
print words.take(words.count())

a = sc.parallelize([1, 2, 3, 4, 3, 4])
b = sc.parallelize([5, 6, 7, 8])
c = a.distinct()
print c.first()
print c.take(c.count())
d = a.union(b)
print d.take(d.count())

e = a.cartesian(b)
print e.take(e.count())

f = a.reduce(lambda x, y: x + y)
print f


