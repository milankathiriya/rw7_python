import pandas as pd
from datetime import datetime, timedelta

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)
date_list = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

df = pd.DataFrame({'Date': date_list})
df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')

df.to_excel('UK_dates.xlsx', index=False, columns=['Date'])