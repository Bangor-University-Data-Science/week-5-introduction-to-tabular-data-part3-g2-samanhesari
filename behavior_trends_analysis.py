import pandas as pd

data_path = "Online Retail.xlsx"


#--exercise_1--------------------------------------------------------------

def import_data(filename: str) -> pd.DataFrame:
    return pd.read_excel(data_path)

#--exercise_2--------------------------------------------------------------

def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    filter1 = df['CustomerID'].isna()
    filter2 = df['Quantity'] < 0
    filter3 = df['UnitPrice'] < 0
    filtered_df = df[~filter2  & ~filter2 & ~filter3]
    return filtered_df

#--exercise_3--------------------------------------------------------------

def loyalty_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame:
    cleaned_data  = filter_data(df)
    cusomer_n_purchues = cleaned_data.groupby('CustomerID')['InvoiceNo'].nunique().reset_index()
    filter1 = cusomer_n_purchues['InvoiceNo'] < min_purchases
    filtered_data = cusomer_n_purchues[~filter1]
    return filtered_data

#--exercise_4--------------------------------------------------------------

def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    df['quarter'] = df['InvoiceDate'].dt.to_period('Q')
    df['total_revenue'] = df['UnitPrice']*df['Quantity'] 
    return df.groupby('quarter')['total_revenue'].sum().reset_index()

#--exercise_5--------------------------------------------------------------

def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    cleaned_data  = filter_data(df)
    cleaned_data = cleaned_data.groupby('StockCode')['Quantity'].sum().reset_index()
    return cleaned_data.nlargest(top_n, 'Quantity')

#--exercise_6--------------------------------------------------------------

def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame:
    summary = df.groupby('StockCode').agg(
        avg_quantity=('Quantity', 'mean'),
        avg_unit_price=('UnitPrice', 'mean')
    ).reset_index()
    
    # Rename 'StockCode' to 'product'
    summary.rename(columns={'StockCode': 'product'}, inplace=True)
    
    return summary

#--exercise_7--------------------------------------------------------------

def answer_conceptual_questions():
    return {'Q1': {'A', 'D'}, 'Q2' : {'B'}, 'Q3' : {'B', 'C'}, 'Q4': {'C', 'D'}, 'Q5': {'A'}}