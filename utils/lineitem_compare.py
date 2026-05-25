from utils.normalizer import normalize

# FIXED LINE ITEM ORDER
LINEITEM_TOPICS = [

    "Product Description",
    "FSN Code",
    "Article Code",
    "Unit Price",
    "Quantity",
    "UOM",
    "Currency",
    "Discount",
    "Tax Percentage (%)",
    "Taxable Value",
    "IGST Rate (%)",
    "SGST Rate (%)",
    "CGST Rate (%)",
    "IGST Value",
    "SGST Value",
    "CGST Value",
    "Total Amount",
    "Tax Amount"

]


def compare_lineitems(
    before_lines,
    after_lines
):

    results = []

    matched = 0
    mismatched = 0

    # GROUP SUMMARY
    group_summary = []

    max_groups = max(
        len(before_lines),
        len(after_lines)
    )

    for index in range(max_groups):

        before_group = (
            before_lines[index]
            if index < len(before_lines)
            else {}
        )

        after_group = (
            after_lines[index]
            if index < len(after_lines)
            else {}
        )

        group_name = (
            f"Line Item Group {index + 1}"
        )

        # GROUP COUNTS
        group_match = 0
        group_mismatch = 0

        # GROUP HEADER
        results.append({

            "group_name": group_name,
            "topic": "",
            "before_value": "",
            "after_value": "",
            "status": ""

        })

        # SERIAL ORDER
        for topic in LINEITEM_TOPICS:

            # =========================
            # ORIGINAL VALUES
            # =========================

            before_value = str(
                before_group.get(topic, "")
            )

            after_value = str(
                after_group.get(topic, "")
            )

            # =========================
            # NORMALIZED VALUES
            # =========================

            normalized_before = normalize(
                before_value
            )

            normalized_after = normalize(
                after_value
            )

            # =========================
            # COMPARE NORMALIZED VALUES
            # =========================

            status = (
                "MATCH"
                if normalized_before == normalized_after
                else "MISMATCH"
            )

            if status == "MATCH":

                matched += 1
                group_match += 1

            else:

                mismatched += 1
                group_mismatch += 1

            # =========================
            # STORE ORIGINAL VALUES
            # =========================

            results.append({

                "group_name": "",
                "topic": topic,
                "before_value": before_value,
                "after_value": after_value,
                "status": status

            })

        # =========================
        # GROUP STATUS
        # =========================

        group_status = (
            "PASS"
            if group_mismatch == 0
            else "FAIL"
        )

        # =========================
        # STORE GROUP SUMMARY
        # =========================

        group_summary.append({

            "group_name": group_name,
            "status": group_status

        })

    return (
        results,
        matched,
        mismatched,
        group_summary
    )