lines = sc.textFile("/opt/spark/README.md")
pythonLines = lines.filter(lambda line: "Python" in line)
pythonLines.first()