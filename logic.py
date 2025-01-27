import models


def compare_icon_opr(opr_data, icon_data):
    """Compare the ICON comments file to the original OPR to ensure no missing rows"""
    icon_pos_nums = [icon_row.pos_num for icon_row in icon_data]
    missing_rows = [row.pos_num for row in opr_data if row.pos_num not in icon_pos_nums]
    return missing_rows


def compare_iqvia_opr(opr_data, iqvia_data):
    """Compare the IQVIA comments file to the original OPR to ensure no missing rows"""
    iqvia_pos_nums = [iqvia_row.pos_num for iqvia_row in iqvia_data]
    missing_rows = [row.pos_num for row in opr_data if row.pos_num not in iqvia_pos_nums]
    return missing_rows


def merge_comment_files(icon_data, iqvia_data):
    """Merge ICON and IQVIA comment files together"""
    merged_data_dict: dict[str, models.ExcelComments] = {}
    for row in icon_data:
        merged_data_dict[row.pos_num] = row
    for row in iqvia_data:
        if row.pos_num in merged_data_dict:
            merged_data_dict[row.pos_num].iqvia_comments = row.iqvia_comments
        else:
            merged_data_dict[row.pos_num] = row
    return list(merged_data_dict.values())
