import pandas as pd

from db.db_helper import (
    get_header_data,
    get_lineitem_data
)

from utils.header_compare import (
    compare_headers
)

from utils.lineitem_compare import (
    compare_lineitems
)

from utils.report_generator import (
    generate_report
)

# =========================
# DB CONFIG
# =========================

dbconfig = {
    "host": "35.244.41.206",
    "user": "root",
    "password": "~0g-\"&~[>DAY]p|&",
    "database": "eval_2_db2",
    "port": 3306
}

# =========================
# READ MAPPING FILE
# =========================

mapping_df = pd.read_excel(
    "mapping/doc_mapping.xlsx"
)

detailed_rows = []

summary_rows = []

# =========================
# LOOP ALL DOC IDS
# =========================

for _, row in mapping_df.iterrows():

    before_doc_id = int(
        row["before_doc_id"]
    )

    after_doc_id = int(
        row["after_doc_id"]
    )

    print(
        f"Comparing {before_doc_id} ↔ {after_doc_id}"
    )

    # =========================
    # HEADER DATA
    # =========================

    before_header = get_header_data(
        before_doc_id,
        dbconfig
    )

    after_header = get_header_data(
        after_doc_id,
        dbconfig
    )

    header_results, hm, hmis = compare_headers(
        before_header,
        after_header
    )

    # =========================
    # LINE ITEM DATA
    # =========================

    before_lines = get_lineitem_data(
        before_doc_id,
        dbconfig
    )

    after_lines = get_lineitem_data(
        after_doc_id,
        dbconfig
    )

    line_results, lm, lmis, group_summary = compare_lineitems(
        before_lines,
        after_lines
    )

    # =========================
    # STORE HEADER RESULTS
    # =========================

    for item in header_results:

        detailed_rows.append({

            "before_doc_id": before_doc_id,
            "after_doc_id": after_doc_id,
            "section": "HEADER",
            **item

        })

    # =========================
    # STORE LINE ITEM RESULTS
    # =========================

    for item in line_results:

        detailed_rows.append({

            "before_doc_id": before_doc_id,
            "after_doc_id": after_doc_id,
            "section": "LINEITEM",
            **item

        })

    # =========================
    # TOTALS
    # =========================

    total_header_topics = hm + hmis

    total_match = hm + lm

    total_mismatch = hmis + lmis

    # =========================
    # ACCURACY
    # =========================

    accuracy = (
        (
            total_match /
            (
                total_match +
                total_mismatch
            )
        ) * 100
        if (
            total_match +
            total_mismatch
        ) > 0
        else 0
    )

    # =========================
    # GROUP PASS / FAIL
    # =========================

    group_pass = 0
    group_fail = 0

    for group in group_summary:

        if group["status"] == "PASS":
            group_pass += 1
        else:
            group_fail += 1

    # =========================
    # STORE SUMMARY
    # =========================

    summary_rows.append({

        "before_doc_id": before_doc_id,
        "after_doc_id": after_doc_id,

        # HEADER
        "total_header_topics": total_header_topics,
        "header_pass": hm,
        "header_fail": hmis,

        # LINE ITEM
        "total_lineitem_groups": len(group_summary),
        "lineitem_groups_pass": group_pass,
        "lineitem_groups_fail": group_fail,

        # ACCURACY
        "accuracy": round(
            accuracy, 2
        )

    })

# =========================
# GENERATE FINAL REPORT
# =========================

generate_report(
    detailed_rows,
    summary_rows
)

print(
    "\n✅ Comparison Completed Successfully"
)

print(
    "✅ Report Generated"
)

# python main.py