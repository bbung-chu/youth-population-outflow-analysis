import pandas as pd

def load_data(file_path, **kwargs):
    return pd.read_csv(file_path, **kwargs)

def normalize_column_names(df):
    df.columns = df.columns.str.strip().str.lower()
    return df

def filter_youth_age(df, age_col, min_age=19, max_age=34):
    return df[(df[age_col] >= min_age) & (df[age_col] <= max_age)]

def convert_numeric_columns(df, columns):
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

def clean_region_name(df, region_col):
    df[region_col] = df[region_col].astype(str).str.strip()
    return df

def compute_net_migration(df, in_col, out_col, result_col="net_migration"):
    df[result_col] = df[in_col] - df[out_col]
    return df