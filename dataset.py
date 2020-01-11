import pandas
import randomdata


def Data_PBL():
    size = 5
    start = 1
    end = 11

    df1 = pandas.DataFrame(list(randomdata.Rand(start, end, size)), columns = ['Technology change', 'Political influence', 'Cost of Education', 'Man Power', 'Money Inflation'])

    df1['Instructional Methodology'] = 'PBL/PrBL'

    df1.to_csv("Dataset_PBLandPrL.csv", header = True, index = False)

