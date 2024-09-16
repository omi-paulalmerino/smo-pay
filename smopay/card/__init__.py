import base64
import requests

XENDIT_SECRET_KEY = "xnd_development_Gr6cLvZPOJnjzTaO16BfN3oWfgoJMJxORAIo6ef3RMPqg2redZY37dIIBMdfWO"

authentication_id = "66e65ad786ee6a001a157189"
token = "66e65ad786ee6a001a157188"

def charge(opts):
    ref_no = opts.get("ref_no")
    token = opts.get("token")
    authentication_id = opts.get("authentication_id")
    amount = opts.get("amount")

    auth_pair = f"{XENDIT_SECRET_KEY}:"
    auth_base64 = base64.b64encode(auth_pair.encode())
    auth_token = auth_base64.decode("utf-8")

    header = {
        "Authorization": f"Basic {auth_token}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "external_id": ref_no,
        "token_id": token,
        "authentication_id": authentication_id,
        "amount": amount,
    }

    return {
        "gateway_reference_id": "TEST-0001",
        "raw_json": {},
    }

    response = requests.post(
        "https://api.xendit.co/credit_card_charges",
        headers=header,
        data=data,
    )
    print(f"response: {response.json()}")
    return {
        "gateway_reference_id": "TEST-0001",
        "raw_json": response.json(),
    }
