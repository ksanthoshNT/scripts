data = {
  "original_number_map": {
    "BOL": "bol_original_number",
    "AWB": "carrier_country",
    "COO": "carrier_country",
    "IC": "carrier_country",
    "RR": "carrier_country",
    "LR": "carrier_country",
    "CI": "remitter_country",
    "BOE": "drawee_country",
    "PL":"carrier_country",
    "CS": "drawee_country"
  },
  "applicant_country": {
    "BOL": "carrier_country",
    "AWB": "carrier_country",
    "COO": "carrier_country",
    "IC": "carrier_country",
    "RR": "carrier_country",
    "LR": "carrier_country",
    "CI": "remitter_country",
    "BOE": "drawee_country",
    "PL":"carrier_country",
    "CS": "drawee_country"
  },
  "beneficiary_country": {
     "BOL": "carrier_country",
    "AWB": "carrier_country",
    "COO": "carrier_country",
    "IC": "carrier_country",
    "RR": "carrier_country",
    "LR": "carrier_country",
    "CI": "remitter_country",
    "BOE": "drawer_country",
    "PL":"carrier_country",
    "CS": "drawer_country"
  },
  "issue_date_map": {
    "BOL": "bill_of_lading_issue_date",
    "AWB": "awb_bill_issue_date",
    "COO": "issue_date",
    "IC": "issue_date",
    "RR": "issue_date",
    "LR": "issue_date",
    "CI": "date_of_invoice",
    "BOE": "bill_exchange_date",
    "PL":"bill_of_lading_date",
    "CS": "csh_presentation_date"
  },
  "stamped_onboard_date_map": {
    "AWB": "stamped_onboard_date",
    "BOL": "stamped_onboard_date",
    "RR": "stamped_onboard_date",
    "LR": "stamped_onboard_date"
  },
  "shipped_onboard_date_map": {
    "AWB": "shipped_onboard_date",
    "BOL": "shipped_onboard_date",
    "RR": "shipped_onboard_date",
    "LR": "shipped_onboard_date"
  },
"issuer_name": {
  "IC":"insurance_issuer_name"
},
  "signed_verified_stamp_map": {
    "BOL": "is_sign,is_stamp",
    "AWB": "is_sign,is_stamp",
    "COO": "is_sign,is_stamp",
    "IC": "is_sign,is_stamp",
    "RR": "is_sign,is_stamp",
    "LR": "is_sign,is_stamp",
    "CI": "is_sign,is_stamp",
    "BOE": "is_sign,is_stamp",
    "PL":"is_sign,is_stamp",
    "CS": "is_sign,is_stamp"
  }}

json_final = {}
for x,y in data.items():
    for