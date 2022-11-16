"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re
from datetime import datetime


def lower_del_special_chr(df,header):
    for column in header:
        df[column] = df[column].str.lower().apply(lambda x: x.replace('_', ' ') and x.replace('-', ' '))
    
    return df

def fix_format(df):
    df['monto_del_credito'] = df['monto_del_credito'].str.replace("\$[\s*]", "").str.replace(",", "").str.replace("\.00", "")
    df['monto_del_credito'] = df['monto_del_credito'].astype(int)

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)

    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))

    return df

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",  index_col = 0)
    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)

    df = lower_del_special_chr(df,['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio'])

    df = fix_format(df)

    df.drop_duplicates(inplace = True)

    return df
