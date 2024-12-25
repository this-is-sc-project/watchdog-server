#기존 데이터 불러오기
import pandas as pd

path = '/content/drive/MyDrive/Colab Notebooks/0. 창업템/'
tickers = ['NVDA', 'TSLA']

dfs = {}
for t in tickers:
  df = pd.read_csv(path+f'news_{t}.csv')
  dfs[t] = df


#새로운 뉴스 추가
for t in tickers:
  df = get_news(t)
  combined_df = pd.concat([dfs[t], df], ignore_index=True)
  combined_df = combined_df.dropna() #데이터 없으면 제거
  combined_df = combined_df.drop_duplicates() #중복 행 제거
  combined_df.to_csv(path+f'news_{t}.csv', index=False)

print('\n Finished scrapping, your news got saved as "news.csv"')
