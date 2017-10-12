import pandas as pd
from sys import argv

def merge(outfilename):
    members = pd.read_csv("samples/members_sample.csv")
    transactions = pd.read_csv("samples/consolidated_transactions.csv")
    #user_logs = pd.read_csv("samples/user_logs_sample.csv")
    train = pd.read_csv("samples/train_sample.csv")

    merged = members.merge(transactions, on="msno", how="inner")
    #merged = merged.merge(user_logs, on="msno", how="inner")
    merged = merged.merge(train, on="msno", how="inner")

    merged.to_csv(outfilename)


outfilename = argv[1]

merge(outfilename)