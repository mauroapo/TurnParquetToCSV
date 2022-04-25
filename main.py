import pandas as pd

pd.read_parquet('part-00000-4870f14e-c508-41aa-94c1-49bb8b03d3ec-c000.gz.parquet').to_csv('BNB-USDT.csv')