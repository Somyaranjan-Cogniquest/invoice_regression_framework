import mysql.connector


def get_connection(dbconfig):
    conn = mysql.connector.connect(**dbconfig)
    curr = conn.cursor(dictionary=True)
    return conn, curr


# HEADER DATA
def get_header_data(doc_id, dbconfig):

    conn, curr = get_connection(dbconfig)

    try:
        sql = """
        SELECT topic, topic_value
        FROM kvextract
        WHERE doc_id = %s
        """

        curr.execute(sql, (int(doc_id),))
        rows = curr.fetchall()

        data = {}

        for row in rows:
            data[row["topic"]] = row["topic_value"]

        return data

    finally:
        curr.close()
        conn.close()

# LINE ITEM DATA
def get_lineitem_data(doc_id, dbconfig):

    conn, curr = get_connection(dbconfig)

    try:
        sql = """
        SELECT header, topic, topic_value
        FROM kv_extract_grid
        WHERE doc_id = %s
        ORDER BY header
        """

        curr.execute(sql, (int(doc_id),))
        rows = curr.fetchall()

        lineitems = []
        current_header = None
        group = {}

        for row in rows:

            header = str(row["header"])
            topic = str(row["topic"])
            value = str(row["topic_value"] or "")

            if current_header != header:
                if group:
                    lineitems.append(group)
                group = {}
                current_header = header

            group[topic] = value

        if group:
            lineitems.append(group)

        return lineitems

    finally:
        curr.close()
        conn.close()