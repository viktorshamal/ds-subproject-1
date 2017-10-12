from sys import argv
from csv import DictReader

def consolidate_transactions(inputname, outputname):
    with open(inputname, "r") as infile, open(outputname, "w") as outfile:
        reader = DictReader(infile)
        
        # We start with the first transaction
        working_trans = next(reader)

        for transaction in reader:
            if(transaction["msno"] == working_trans["msno"]):
                # This is still the same user, so we add the values from this transaction
                working_trans["count"] += 1
                working_trans["plan_list_price"] += int(transaction["plan_list_price"])
                working_trans["actual_amount_paid"] += int(working_trans["actual_amount_paid"])

                # Always update so we get the latest date and renewal choice in the end
                working_trans["transaction_date"] = transaction["transaction_date"]
                working_trans["is_auto_renew"] = int(transaction["is_auto_renew"])

                # Have they cancelled at any point?
                if(int(working_trans["is_cancel"])):
                    working_trans["is_cancel"] = 1
            else:
                working_trans["discount"] = int(working_trans["plan_list_price"]) - int(working_trans["actual_amount_paid"])
                if(working_trans["discount"] < 0):
                    working_trans["discount"] = 0 

                # We've reached another user, so we convert to a string and write it to the file
                values = [str(value) for value in working_trans.values()]
                outfile.write(",".join(values) + "\n")

                # Now we look at the next transaction and format it for later use
                working_trans = transaction
                working_trans["count"] = 1
                working_trans["plan_list_price"] = int(working_trans["plan_list_price"])
                working_trans["actual_amount_paid"] = int(working_trans["actual_amount_paid"])


infilename = argv[1]
outfilename = argv[2]

consolidate_transactions(infilename, outfilename)