import pandas as pd
import random
df=pd.read_csv(r"D:\Allen Stuff/Project/1 - Football Sim/players_raw.csv",encoding='utf8')
def gen_name(self):
    f=random.randint(0,623)
    s=random.randint(0,623)
    name=df['first_name'][f]+' '+df['second_name'][s]
    return name.strip()