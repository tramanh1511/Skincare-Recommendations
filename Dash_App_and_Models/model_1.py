import dash
import pandas as pd
import numpy as np
from dash import html

df = pd.read_csv('skindataall.csv', index_col=[0])

def Table(df):
    rows = []
    for i in range(len(df)):
        row = []
        for col in df.columns:
            value = df.iloc[i][col]
            # update this depending on which
            # columns you want to show links for
            # and what you want those links to be
            if col == 'Product':
                cell = html.Td(html.A(href=df.iloc[i]['Product_Url'], children=value))
            elif col == 'Product_Url':
                continue
            else:
                cell = html.Td(children=value)
            row.append(cell)
        rows.append(html.Tr(row))
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in ['V', 'V']])] + rows
        )


def recommend_products_by_user_features(skintone, skintype, eyecolor, haircolor):
    ddf = df[(df['Skin_Tone'] == skintone) & (df['Hair_Color'] == haircolor) & (df['Skin_Type'] == skintype) & (df['Eye_Color'] == eyecolor)]
    recommendations = ddf[(ddf['Rating_Stars'].notnull())]
    data = recommendations[['Rating_Stars', 'Product_Url', 'Product']]

    data = data.sort_values('Rating_Stars', ascending=False).head()

    return Table(data)