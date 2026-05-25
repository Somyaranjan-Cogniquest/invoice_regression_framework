from utils.normalizer import normalize

# FIXED HEADER ORDER
HEADER_TOPICS = [

    "InvoiceIssueDate",

    "BuyerAddress",

    "BuyerName",

    "InvoiceNumber",

    "SupplierAddress",

    "IRNStickerInvoiceQty",

    "SupplierTaxNumber",

    "TotalAmountBeforeTax",

    "TotalTax",

    "SupplierName",

    "PurchaseOrderNumber",

    "TotalAmountAfterTax"

]


def compare_headers(before_data, after_data):

    results = []

    matched = 0
    mismatched = 0

    # SERIAL ORDER
    for topic in HEADER_TOPICS:

        # =========================
        # ORIGINAL VALUES
        # =========================

        before_value = str(
            before_data.get(topic, "")
        )

        after_value = str(
            after_data.get(topic, "")
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

        if normalized_before == normalized_after:

            status = "MATCH"
            matched += 1

        else:

            status = "MISMATCH"
            mismatched += 1

        # =========================
        # STORE ORIGINAL VALUES
        # =========================

        results.append({

            "topic": topic,
            "before_value": before_value,
            "after_value": after_value,
            "status": status

        })

    return results, matched, mismatched