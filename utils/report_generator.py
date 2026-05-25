import pandas as pd

from openpyxl.styles import Font


def generate_report(
    detailed_rows,
    summary_rows
):

    # =========================
    # CREATE DATAFRAMES
    # =========================

    detailed_df = pd.DataFrame(
        detailed_rows
    )

    summary_df = pd.DataFrame(
        summary_rows
    )

    # =========================
    # HEADER FORMAT
    # FIRST LETTER CAPITAL
    # =========================

    detailed_df.columns = [

        column.capitalize()

        for column in detailed_df.columns
    ]

    summary_df.columns = [

        column.capitalize()

        for column in summary_df.columns
    ]

    # =========================
    # OUTPUT FILE
    # =========================

    output_file = (
        "reports/Validation_PR_Report.xlsx"
    )

    # =========================
    # WRITE EXCEL
    # =========================

    with pd.ExcelWriter(
        output_file,
        engine="openpyxl"
    ) as writer:

        # =========================
        # DETAILED REPORT
        # =========================

        detailed_df.to_excel(

            writer,

            sheet_name="Detailed_Report",

            index=False

        )

        # =========================
        # SUMMARY REPORT
        # =========================

        summary_df.to_excel(

            writer,

            sheet_name="Summary_Report",

            index=False

        )

        # =========================
        # FORMAT SHEETS
        # =========================

        for sheet_name in writer.sheets:

            worksheet = writer.sheets[
                sheet_name
            ]

            # =========================
            # BOLD HEADER
            # =========================

            for cell in worksheet[1]:

                cell.font = Font(
                    bold=True
                )

            # =========================
            # FILTER ONLY IN
            # DETAILED REPORT
            # =========================

            max_row = worksheet.max_row

            if sheet_name == "Detailed_Report":

                worksheet.auto_filter.ref = (
                    f"A1:G{max_row}"
                )

    print(
        f"\n✅ Report Generated: {output_file}"
    )