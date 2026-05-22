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

            before_value = normalize(
                before_group.get(topic, "")
            )

            after_value = normalize(
                after_group.get(topic, "")
            )

            status = (
                "MATCH"
                if before_value == after_value
                else "MISMATCH"
            )

            if status == "MATCH":
                matched += 1
            else:
                mismatched += 1

            results.append({

                "group_name": "",
                "topic": topic,
                "before_value": before_value,
                "after_value": after_value,
                "status": status

            })

    return results, matched, mismatched