import pandas as pd


def generate_report(
    detailed_rows,
    summary_rows
):

    detailed_df = pd.DataFrame(
        detailed_rows
    )

    summary_df = pd.DataFrame(
        summary_rows
    )

    output_file = (
        "reports/regression_report.xlsx"
    )

    with pd.ExcelWriter(
        output_file,
        engine="openpyxl"
    ) as writer:

        detailed_df.to_excel(
            writer,
            sheet_name="Detailed_Report",
            index=False
        )

        summary_df.to_excel(
            writer,
            sheet_name="Summary_Report",
            index=False
        )

    print(
        f"\n✅ Report Generated: {output_file}"
    )