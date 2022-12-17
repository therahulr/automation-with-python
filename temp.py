from datetime import datetime

data = "PhonePe Dec 15, 2022 Paid to Vicky yadav ₹ 32 Txn. ID : T2212151430404279943304 Txn. status : Successful Debited from : XXXXXX9178 HDFC Bank Bank Ref. No. : 234936229876 Message : Hi Rahul Raj If you"
receive_data = "PhonePe Dec 11, 2022 Received from RANJAN KUMAR THAKUR ₹ 4000 Txn. ID : T2212111726581250157963 Txn. status : Successful Credited to : XXXXXX8996 State Bank Of India Bank Ref. No. : 271148838298"
if "paid to" in data.lower():
    print(data.split("Paid to"))
    date = datetime.strptime(data.split("Paid to")[0].strip().split("PhonePe")[1].strip(), "%b %d, %Y").strftime(
        "%d-%m-%Y")
    name = data.split("Paid to")[1].split("₹")[0].strip()
    amount = data.split("Paid to")[1].split("₹")[1].split("Txn. ID")[0].strip()
    debited_from = data.split("Debited from")[1].split("Bank")[0].split(":")[1].strip() + " Bank"
    print(date, name, amount, debited_from)

if "received from" in receive_data.lower():
    print(receive_data.split("Received from"))
    date = datetime.strptime(receive_data.split("Received from")[0].strip().split("PhonePe")[1].strip(),
                             "%b %d, %Y").strftime("%d-%m-%Y")
    name = receive_data.split("Received from")[1].split("₹")[0].strip()
    amount = receive_data.split("Received from")[1].split("₹")[1].split("Txn. ID")[0].strip()
    credited_to = receive_data.split("Credited to")[1].split("Bank")[0].split(":")[1].strip() + " Bank"
    print(date, name, amount, credited_to)
