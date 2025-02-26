import pandas
import numpy
from config import SHEET_NAME, EXCEL_NAME, HEADER


def read_excel():
    work = pandas.read_excel(EXCEL_NAME, sheet_name=SHEET_NAME, header=HEADER)
    work = work.apply(lambda col: col.apply(lambda x: None if isinstance(x, float) and numpy.isnan(x) else x))
    dict_data = work.to_dict("records")
    case_data = [record for record in dict_data if record.get("is_true")]
    return case_data



