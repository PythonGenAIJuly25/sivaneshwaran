import pandas as pd


orders = pd.read_excel('project/train_with_detailed_return.xlsx', sheet_name='train')
returns = pd.read_excel('project/train_with_detailed_return.xlsx', sheet_name='Return')
people=pd.read_excel('project/train_with_detailed_return.xlsx', sheet_name='People')
# Sample data exploration
print(f"Total orders: {len(orders)}")
print(f"Date range: {orders['Order Date'].min()} to {orders['Order Date'].max()}")
print(f"Product categories: {orders['Category'].unique()}")
print(orders.head())
print(returns.head())
print(people.head())
