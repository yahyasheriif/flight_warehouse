import pandas as pd
from pyopensky.rest import REST

rest = REST()
df = rest.states()
file_name = f"data/load/{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
date_load = df.to_csv(file_name, index=False)
