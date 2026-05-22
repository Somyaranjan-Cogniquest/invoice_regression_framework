import mysql.connector

try:

    conn = mysql.connector.connect(
        host="35.244.41.206",
        user="root",
        password='~0g-"&~[>DAY]p|&',
        database="eval_2_db2",
        port=3306
    )

    print("✅ DB Connected Successfully")

except Exception as e:

    print("❌ Error:", e)   