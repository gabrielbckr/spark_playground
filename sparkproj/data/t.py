from pathlib import Path
from sparkproj import spark

import pandas as pd
import pyspark.sql.functions as sf
import pyspark.sql.types as stype
from pyspark.sql.functions import udf


def main():
    path = Path(__file__).resolve().parents[2].joinpath('data', 'raw')
    df = spark.read.csv(str(path / "appl_stock.csv"), inferSchema=True, header=True)
    def myFunc(x, y):
        return x - y
    my_udf = sf.udf(myFunc,  stype.FloatType())
    df = df.withColumn('new', my_udf('Open', 'Close'))
    x = df.toPandas()
    pass


if __name__ == '__main__':
    main()
