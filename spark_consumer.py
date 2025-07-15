from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, DoubleType, StringType, IntegerType
import pickle
import numpy as np
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

# Load trained model
with open('model/isolation_forest.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("AnomalyDetectionStreaming") \
    .getOrCreate()

# Define schema for incoming JSON messages
schema = StructType() \
    .add("transaction_id", IntegerType()) \
    .add("user_id", IntegerType()) \
    .add("amount", DoubleType()) \
    .add("timestamp", StringType())

# Read streaming data from Kafka topic 'transactions'
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions") \
    .load()

# Parse JSON messages
df_parsed = df_raw.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Define anomaly detection function
def detect_anomaly(amount):
    prediction = model.predict(np.array([[amount]]))
    return int(prediction[0])

# Register UDF for anomaly detection
anomaly_udf = udf(detect_anomaly, IntegerType())

# Apply anomaly detection to the parsed stream
df_anomalies = df_parsed.withColumn("anomaly", anomaly_udf(col("amount")))

# Filter only anomalies (anomaly == 1)
df_only_anomalies = df_anomalies.filter(col("anomaly") == 1)

# Output anomalies to the console
query = df_only_anomalies.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .start()

# Keep the query running
query.awaitTermination()
