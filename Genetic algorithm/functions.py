import numpy as np
import pandas as pd


def readData(data_file):
    column_names = ["ID", "NAME", "WEIGHT", "VALUE"]
    df = pd.read_csv(data_file, names=column_names)

    idArray = np.array(df.ID.values.tolist())
    nameArray = np.array(df.NAME.values.tolist())
    weightArray = np.array(df.WEIGHT.values.tolist())
    valueArray = np.array(df.VALUE.values.tolist())

    return [idArray, nameArray, weightArray, valueArray]
