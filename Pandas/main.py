import pandas as pd

produtos = {
    'data': ['12/23/2333', '16/45/2344'],
    'valor': ['4000', '200'],
}

# produtos_df = pd.DataFrame(produtos)
produtos_df = pd.read_csv("produtos.csv")

print(produtos_df.describe())