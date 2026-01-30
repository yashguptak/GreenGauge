import pandas as pd
import os

def save_data(filename, record):
    if not os.path.exists(filename):
        df = pd.DataFrame([record])
    else:
        df = pd.read_csv(filename)
        df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)
    df.to_csv(filename, index=False)

def load_user_data(filename):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return pd.DataFrame()
