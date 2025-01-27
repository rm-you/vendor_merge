import excel_handler
import logic
import models

ICON_ORIGINAL_OPR = "ICON_original_OPR.xlsx"
ICON_COMMENT = "ICON comment.xlsx"
IQVIA_ORIGINAL_OPR = "IQVIA_original_OPR.xlsx"
IQVIA_COMMENT = "IQVIA comment.xlsx"
OUTPUT_FILENAME = "merged_comments.xlsx"

if __name__ == "__main__":
    # Load the original OPR and comment files
    icon_opr = excel_handler.load_excel_opr(ICON_ORIGINAL_OPR)
    icon_comments = excel_handler.load_excel_comment_file(
        ICON_COMMENT, models.ExcelICON)
    iqvia_opr = excel_handler.load_excel_opr(IQVIA_ORIGINAL_OPR)
    iqvia_comments = excel_handler.load_excel_comment_file(IQVIA_COMMENT, models.ExcelIQVIA)

    # Compare the original OPR to the comment files
    missing_icon_data = logic.compare_icon_opr(icon_opr, icon_comments)
    if missing_icon_data:
        print(f"Missing ICON data: {missing_icon_data}")
    else:
        print("No missing ICON data.")
    missing_iqvia_data = logic.compare_iqvia_opr(iqvia_opr, iqvia_comments)
    if missing_iqvia_data:
        print(f"Missing IQVIA data: {missing_iqvia_data}")
    else:
        print("No missing IQVIA data.")

    # If no data is missing, merge the comment files
    if missing_icon_data or missing_iqvia_data:
        print("Missing data, exiting...")
    else:
        merged_data = logic.merge_comment_files(icon_comments, iqvia_comments)
        excel_handler.write_merged_comments(merged_data, OUTPUT_FILENAME)
        print("Merged comments written to file.")
