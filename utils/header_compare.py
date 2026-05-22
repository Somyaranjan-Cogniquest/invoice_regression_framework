from utils.normalizer import normalize

# FIXED HEADER ORDER
HEADER_TOPICS = [

    "InvoiceHeader",
    "SupplierName",
    "SupplierAddress",
    "SupplierTaxNumber",
    "BuyerName",
    "BuyerAddress",
    "BuyerTaxNumber",
    "InvoiceNumber",
    "InvoiceIssueDate",
    "InvoiceDueDate",
    "PurchaseOrderNumber",
    "EWayBillNumber",
    "TotalAmountBeforeTax",
    "TotalTax",
    "TotalAmountAfterTax",
    "GRNSeal",
    "IRNSticker",
    "IRNStickerWHDocumentID",
    "IRNStickerInvoiceQty",
    "AuthorisedSignature",
    "HSNCodePresence"

]


def compare_headers(before_data, after_data):

    results = []

    matched = 0
    mismatched = 0

    # SERIAL ORDER
    for topic in HEADER_TOPICS:

        before_value = normalize(
            before_data.get(topic, "")
        )

        after_value = normalize(
            after_data.get(topic, "")
        )

        if before_value == after_value:

            status = "MATCH"
            matched += 1

        else:

            status = "MISMATCH"
            mismatched += 1

        results.append({

            "topic": topic,
            "before_value": before_value,
            "after_value": after_value,
            "status": status

        })

    return results, matched, mismatched