
import os,shutil
name = "0041FLC210044"
def main():
	path = "/media/ntlpt59/HI/D/DATA_LAKE/TradeFinanceFinalDelivery/ExtractionResultPDF2/pdf_1_2/pdf_2/document"
	path_dest = "/media/ntlpt59/HI/D/DATA_LAKE/TradeFinanceFinalDelivery/ExtractionResultPDF2/pdf_1_2/pdf_2/document_latest"
	
	for x in os.listdir(path):
		if x.endswith("png"):
			y = int(x.split(".")[0])
			src = os.path.join(path,x)
			dest = os.path.join(path_dest,name+"_"+str(y+1)+".png")
			shutil.copy(src,dest)


def OCR():
	path = "/media/ntlpt59/HI/D/DATA_LAKE/TradeFinanceFinalDelivery/ExtractionResultPDF2/pdf_1_2/pdf_2/document/OCR"
	path_dest = "/media/ntlpt59/HI/D/DATA_LAKE/TradeFinanceFinalDelivery/ExtractionResultPDF2/pdf_1_2/pdf_2/document_latest/OCR"
	for x in os.listdir(path):
		y = int(x.split("_")[0])
		src = os.path.join(path,x)
		dest = os.path.join(path_dest,name+str(y+1)+"_"+x.split("_")[1])
		shutil.copy(src,dest)

def necessary_keys_in_extraction():
	DOC_Wise_Primary_Key_name: dict = {
	"BOL": ["bill_of_lading_number","bill_of_lading_issue_date","vessel_name","voyage_number","stamped_shipped_onboard_date","shipped_onboard_date"],
	"CI": ["invoice_no","transaction_date","transaction_amount_value","invoice_amount_in_words"],
	"PL": [],
	"COO": ["certificate_no","ref_no","issue_date","country_of_origin_of_goods"],
	"IC": ["certificate_no","issue_date","expiry_date","vessel_or_flight_name","vessel_or_flight_number","premium","policy_no"],
	"CS": [],
	"PI": [],
	"ELB": [],
	"AWB": ["awb_bill_no","master_awb_bill_no","house_awb_bill_no","awb_bill_issue_date","transaction_date","flight_no","flight_date"],
	"PO": [],
	"BOE":["bill_exchange_no","boe_amount"],
	"COA":[]}
	Doc_Org_key_map: dict = {
	"BOL": ["bol_original_or_copy"],
	"CI": ["original_or_copy"],
	"PL": ["original_copy"],
	"COO": ["original_or_copy"],
	"IC": ["original_copy"],
	"CS": [],
	"PI": [],
	"ELB": [],
	"AWB": ["awb_original_or_copy"],
	"PO": [],
	"BOE":["original_or_copy"],
	"COA":[]}	
	extraction_results = {"extraction_result": {
            "1609flc230614_1.png": {
                "docClass": "LC",
                "keys_extraction": {}
            },
            "1609flc230614_2.png": {
                "docClass": "LC",
                "keys_extraction": {}
            },
            "1609flc230614_3.png": {
                "docClass": "LC",
                "keys_extraction": {}
            },
            "1609flc230614_4.png": {
                "docClass": "LC",
                "keys_extraction": {}
            },
            "1609flc230614_5.png": {
                "docClass": "ELB",
                "keys_extraction": {}
            },
            "1609flc230614_6.png": {
                "docClass": "CI",
                "keys_extraction": {
                    "beneficiary_address": {
                        "value": "UM YU3 9R WAR KIMDB 13UI KUWA BUNU AVI",
                        "coordinate": [
                            [
                                179,
                                104,
                                364,
                                120
                            ]
                        ],
                        "model_confidence": [
                            93.3336520700716
                        ]
                    },
                    "consignee_address": {
                        "value": "COMMERCIAL DSM SHIVAJI 321 MARG 3RD FLOOR NEW DELHI DLF TOWERS 110015 ",
                        "coordinate": [
                            [
                                124,
                                140,
                                308,
                                204
                            ]
                        ],
                        "model_confidence": [
                            82.98843007401636
                        ]
                    },
                    "cosignee_name": {
                        "value": "RESOL VINYLS AND CHLORIDES LIMITED",
                        "coordinate": [
                            [
                                123,
                                169,
                                285,
                                177
                            ]
                        ],
                        "model_confidence": [
                            99.28345679012345
                        ]
                    },
                    "invoice_no": {
                        "value": "SSIPL - 23146 23073",
                        "coordinate": [
                            [
                                124,
                                208,
                                170,
                                238
                            ]
                        ],
                        "model_confidence": [
                            94.70253731343283
                        ]
                    },
                    "date_of_invoice": {
                        "value": "05-07-2023",
                        "coordinate": [
                            [
                                125,
                                221,
                                175,
                                227
                            ]
                        ],
                        "model_confidence": [
                            98.64166666666668
                        ]
                    },
                    "port_of_loading": {
                        "value": "XINGANG PORT ",
                        "coordinate": [
                            [
                                124,
                                245,
                                218,
                                253
                            ]
                        ],
                        "model_confidence": [
                            99.49857142857142
                        ]
                    },
                    "port_of_discharge": {
                        "value": "MUNDRA PORT , INDIA",
                        "coordinate": [
                            [
                                126,
                                257,
                                213,
                                265
                            ]
                        ],
                        "model_confidence": [
                            99.38564705882354
                        ]
                    },
                    "goods_description": {
                        "value": "PVC SUSPENSION RESIN",
                        "coordinate": [
                            [
                                128,
                                318,
                                222,
                                325
                            ]
                        ],
                        "model_confidence": [
                            99.78173913043477
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": " 280.00 ",
                        "coordinate": [
                            [
                                148,
                                317,
                                360,
                                361
                            ]
                        ],
                        "model_confidence": [
                            97.745
                        ]
                    },
                    "rate_per_unit": {
                        "value": "USD 770.00 770.00",
                        "coordinate": [
                            [
                                219,
                                316,
                                428,
                                361
                            ]
                        ],
                        "model_confidence": [
                            86.2078787878788
                        ]
                    },
                    "vessel_flight_no": {
                        "value": "327W",
                        "coordinate": [
                            [
                                195,
                                492,
                                216,
                                499
                            ]
                        ],
                        "model_confidence": [
                            25.51
                        ]
                    },
                    "declaration_by_issuer": {
                        "value": "TIANJIN BOHUA CHEMICAL DEVELOPMENT CO . , LTD .",
                        "coordinate": [
                            [
                                131,
                                441,
                                338,
                                447
                            ]
                        ],
                        "model_confidence": [
                            98.67943611565974
                        ]
                    },
                    "country_of_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                211,
                                453,
                                236,
                                460
                            ]
                        ],
                        "model_confidence": [
                            96.79
                        ]
                    },
                    "lc_ref_no": {
                        "value": "1609FLC230614",
                        "coordinate": [
                            [
                                206,
                                592,
                                262,
                                601
                            ]
                        ],
                        "model_confidence": [
                            93.58
                        ]
                    },
                    "signature_of_the_issuer": {
                        "value": "ORIGINAL FOR AND ALL OF ATHARTOND SIGNAT",
                        "coordinate": [
                            [
                                441,
                                98,
                                519,
                                123
                            ],
                            [
                                364,
                                607,
                                457,
                                650
                            ]
                        ],
                        "model_confidence": [
                            92.53,
                            85.73526898495295
                        ]
                    },
                    "invoice_currency": {
                        "value": "",
                        "coordinate": [
                            [
                                455,
                                516,
                                472,
                                524
                            ]
                        ],
                        "model_confidence": [
                            98.84
                        ]
                    },
                    "invoice_amount": {
                        "value": "215,600.00",
                        "coordinate": [
                            [
                                480,
                                517,
                                518,
                                525
                            ]
                        ],
                        "model_confidence": [
                            75.72
                        ]
                    },
                    "invoice_amount_in_words": {
                        "value": "TWO HUNDRED FIFTEEN THOUSAND AND SIX HUNDRED ONLY .",
                        "coordinate": [
                            [
                                237,
                                555,
                                486,
                                564
                            ]
                        ],
                        "model_confidence": [
                            97.63441417978675
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE TRUE",
                        "coordinate": [
                            [
                                53,
                                87,
                                101,
                                116
                            ],
                            [
                                417,
                                629,
                                464,
                                647
                            ]
                        ],
                        "model_confidence": [
                            0.6178504228591919,
                            0.6794661283493042
                        ]
                    },
                    "is_stamp": {},
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                124,
                                140,
                                308,
                                204
                            ]
                        ],
                        "model_confidence": [
                            82.98843007401636
                        ]
                    },
                    "port_of_loading_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                124,
                                245,
                                218,
                                253
                            ]
                        ],
                        "model_confidence": [
                            99.49857142857142
                        ]
                    },
                    "incoterm": {},
                    "consignor_name": {},
                    "beneficiary_bank_country": {},
                    "transaction_currency": {},
                    "transaction_amonunt_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin": {},
                    "bill_of_lading_date": {},
                    "invoice_tax_ccy": {},
                    "consignee_country": {},
                    "tenor_indicator": {},
                    "net_weight": {},
                    "notify_party_country": {},
                    "indicator_type": {},
                    "hs_code_no": {},
                    "invoice_due_date": {},
                    "country_of_final_destination": {},
                    "indicator_date": {},
                    "invoice_discount_amount": {},
                    "shipper_address": {},
                    "consignor_country": {},
                    "invoice_discount_ccy": {},
                    "usance_tenor": {},
                    "tenor_type": {},
                    "awb_date": {},
                    "delivery_terms": {},
                    "gross_weight": {},
                    "consignor_address": {},
                    "beneficiary_iban_number": {},
                    "transaction_date": {},
                    "beneficiary_account_number": {},
                    "pre-carriage-by": {},
                    "bill_of_lading_no": {},
                    "lc_date": {},
                    "invoice_tax_amount": {},
                    "notify_party_name": {},
                    "original_or_copy": {},
                    "beneficiary_drawer_exporter_seller_supplier_name": {},
                    "notify_party_address": {},
                    "beneficiary_bank_identifier": {},
                    "awb_number": {},
                    "page_no": {},
                    "remitter_address": {},
                    "shipper_name": {},
                    "beneficiary_bank_name": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "1609flc230614_7.png": {
                "docClass": "PL",
                "keys_extraction": {
                    "invoice_no": {
                        "value": "SSIPL - 23146 23073",
                        "coordinate": [
                            [
                                139,
                                166,
                                185,
                                197
                            ]
                        ],
                        "model_confidence": [
                            68.65506849315068
                        ]
                    },
                    "beneficiary_address": {
                        "value": "ROOM 903 TSIM 9 F SHA KIMBERLEY TSUI KOWLOON HOUSE 35 HONG KIMBERLEY KONG ROAD",
                        "coordinate": [
                            [
                                163,
                                97,
                                398,
                                115
                            ]
                        ],
                        "model_confidence": [
                            98.84949599001916
                        ]
                    },
                    "date_of_invoice": {
                        "value": "05 JULY 2023 05 JULY 2023",
                        "coordinate": [
                            [
                                139,
                                178,
                                484,
                                185
                            ]
                        ],
                        "model_confidence": [
                            99.89373265494913
                        ]
                    },
                    "description_of_goods": {
                        "value": "RESOL VINYLS AND CHLORIDES LIMITED~SUSPENSION RESIN~",
                        "coordinate": [
                            [
                                140,
                                203,
                                300,
                                210
                            ]
                        ],
                        "model_confidence": [
                            76.96685302390999
                        ]
                    },
                    "consignor_address": {
                        "value": "DSM SHIVAJI 321 MARG 3RD FLOOR NEW DELHI DLF TOWERS 110015 ",
                        "coordinate": [
                            [
                                140,
                                214,
                                300,
                                235
                            ]
                        ],
                        "model_confidence": [
                            83.16
                        ]
                    },
                    "port_of_loading": {
                        "value": "XINGANG PORT ",
                        "coordinate": [
                            [
                                140,
                                240,
                                231,
                                248
                            ]
                        ],
                        "model_confidence": [
                            99.94
                        ]
                    },
                    "port_of_discharge": {
                        "value": "MUNDRA PORT , INDIA",
                        "coordinate": [
                            [
                                140,
                                252,
                                226,
                                260
                            ]
                        ],
                        "model_confidence": [
                            99.94000000000001
                        ]
                    },
                    "vessel_flight_no": {
                        "value": "327W",
                        "coordinate": [
                            [
                                204,
                                493,
                                224,
                                500
                            ]
                        ],
                        "model_confidence": [
                            34.46
                        ]
                    },
                    "country_of_origin_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                221,
                                455,
                                245,
                                462
                            ]
                        ],
                        "model_confidence": [
                            95.11
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "11200 ",
                        "coordinate": [
                            [
                                143,
                                519,
                                186,
                                526
                            ]
                        ],
                        "model_confidence": [
                            98.74
                        ]
                    },
                    "net_weight": {
                        "value": "280,000 ",
                        "coordinate": [
                            [
                                160,
                                557,
                                203,
                                564
                            ]
                        ],
                        "model_confidence": [
                            99.93
                        ]
                    },
                    "gross_weight": {
                        "value": "282,240 ",
                        "coordinate": [
                            [
                                160,
                                568,
                                203,
                                576
                            ]
                        ],
                        "model_confidence": [
                            99.9
                        ]
                    },
                    "dimension": {
                        "value": "CBM",
                        "coordinate": [
                            [
                                188,
                                582,
                                205,
                                587
                            ]
                        ],
                        "model_confidence": [
                            25.06
                        ]
                    },
                    "original_copy": {
                        "value": "ORIGINAL",
                        "coordinate": [
                            [
                                419,
                                96,
                                496,
                                119
                            ]
                        ],
                        "model_confidence": [
                            99.82
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                382,
                                618,
                                445,
                                642
                            ]
                        ],
                        "model_confidence": [
                            0.5146036744117737
                        ]
                    },
                    "is_stamp": {},
                    "consignor_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                140,
                                214,
                                300,
                                235
                            ]
                        ],
                        "model_confidence": [
                            83.16
                        ]
                    },
                    "port_of_loading_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                140,
                                240,
                                231,
                                248
                            ]
                        ],
                        "model_confidence": [
                            99.94
                        ]
                    },
                    "shipper_address": {},
                    "lc_date": {},
                    "notify_party_address": {},
                    "awb_number": {},
                    "track_reference": {},
                    "declaration": {},
                    "notify_party_name": {},
                    "bill_of_lading_date": {},
                    "transaction_currency": {},
                    "transaction_date": {},
                    "lc_ref_no": {},
                    "country_of_final_destination": {},
                    "consignee_name": {},
                    "invoice_amount": {},
                    "shipper_name": {},
                    "transaction_amount_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_name": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin_no": {},
                    "remitter_address": {},
                    "consignee_address": {},
                    "bill_of_lading_number": {},
                    "rate_per_unit": {},
                    "consignor_name": {},
                    "invoice_currency": {},
                    "pre_carriage_by": {},
                    "payment_terms_terms_of_delivery_&_payment": {},
                    "incoterm": {},
                    "awb_date": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "1609flc230614_8.png": {
                "docClass": "BOL",
                "keys_extraction": {
                    "shipper_address": {
                        "value": "ROOM TSUI KOWLOON 903 UN 9 T KIMBERLEY  HOUSE 35 KIMBERLEY ROAD TSIM SHA",
                        "coordinate": [
                            [
                                71,
                                116,
                                276,
                                136
                            ]
                        ],
                        "model_confidence": [
                            92.65414259715394
                        ]
                    },
                    "carrier_name": {
                        "value": "MAERSK",
                        "coordinate": [
                            [
                                129,
                                64,
                                230,
                                82
                            ]
                        ],
                        "model_confidence": [
                            91.76
                        ]
                    },
                    "consignee_name": {
                        "value": "AXIS BANK LIMITED",
                        "coordinate": [
                            [
                                129,
                                176,
                                188,
                                181
                            ]
                        ],
                        "model_confidence": [
                            99.79818181818182
                        ]
                    },
                    "vessel_name": {
                        "value": "ALS CLIVIA",
                        "coordinate": [
                            [
                                72,
                                238,
                                105,
                                243
                            ]
                        ],
                        "model_confidence": [
                            99.96266666666666
                        ]
                    },
                    "port_of_loading": {
                        "value": "XINGANG PORT ",
                        "coordinate": [
                            [
                                72,
                                262,
                                138,
                                268
                            ]
                        ],
                        "model_confidence": [
                            69.84
                        ]
                    },
                    "voyage_number": {
                        "value": "327W WW",
                        "coordinate": [
                            [
                                178,
                                237,
                                193,
                                258
                            ]
                        ],
                        "model_confidence": [
                            99.90391304347827
                        ]
                    },
                    "port_of_discharge": {
                        "value": "MUNDRA PORT INDIA",
                        "coordinate": [
                            [
                                178,
                                261,
                                226,
                                266
                            ]
                        ],
                        "model_confidence": [
                            99.93586956521739
                        ]
                    },
                    "freight_collect_or_prepaid": {
                        "value": "FREIGHT PREPAID",
                        "coordinate": [
                            [
                                76,
                                431,
                                138,
                                441
                            ]
                        ],
                        "model_confidence": [
                            69.41
                        ]
                    },
                    "goods_description": {
                        "value": "PVC GRADE SUSPENSION DG - 1000K RESIN",
                        "coordinate": [
                            [
                                75,
                                317,
                                161,
                                333
                            ]
                        ],
                        "model_confidence": [
                            99.36589473684211
                        ]
                    },
                    "bol_original_number": {
                        "value": " THREE",
                        "coordinate": [
                            [
                                79,
                                638,
                                104,
                                645
                            ]
                        ],
                        "model_confidence": [
                            99.62
                        ]
                    },
                    "country_of_origin": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                148,
                                414,
                                169,
                                421
                            ]
                        ],
                        "model_confidence": [
                            84.54
                        ]
                    },
                    "place_of_issue": {
                        "value": "QINGDAO",
                        "coordinate": [
                            [
                                184,
                                609,
                                210,
                                616
                            ]
                        ],
                        "model_confidence": [
                            40.8
                        ]
                    },
                    "bill_of_lading_issue_date": {
                        "value": "20230709",
                        "coordinate": [
                            [
                                184,
                                655,
                                223,
                                662
                            ]
                        ],
                        "model_confidence": [
                            65.93
                        ]
                    },
                    "container_number": {
                        "value": "GCXU5787118 CAAU6508744 MRSU4549398 CN1472909 CN1472857 TCKU7571234 TRHU4867750 CN1472858 CN1472880 CN1474922 TAY",
                        "coordinate": [
                            [
                                75,
                                467,
                                182,
                                532
                            ]
                        ],
                        "model_confidence": [
                            93.31612903225806
                        ]
                    },
                    "notify_party_address": {
                        "value": "SURVEY MUNDRA NO DIST 169 KUTCH SECTOR GUJARAT VILLAGE 370421 DHRUVE ",
                        "coordinate": [
                            [
                                297,
                                179,
                                437,
                                197
                            ]
                        ],
                        "model_confidence": [
                            68.37
                        ]
                    },
                    "gross_weight": {
                        "value": "282240.000 ",
                        "coordinate": [
                            [
                                391,
                                287,
                                449,
                                295
                            ]
                        ],
                        "model_confidence": [
                            99.93
                        ]
                    },
                    "signed_by_carrier": {
                        "value": "CARD",
                        "coordinate": [
                            [
                                342,
                                690,
                                431,
                                730
                            ]
                        ],
                        "model_confidence": [
                            98.65
                        ]
                    },
                    "bill_of_lading_number": {
                        "value": "228712853",
                        "coordinate": [
                            [
                                474,
                                93,
                                512,
                                98
                            ]
                        ],
                        "model_confidence": [
                            99.19
                        ]
                    },
                    "measurement_or_dimension": {
                        "value": "470 : 0000 CBM",
                        "coordinate": [
                            [
                                466,
                                284,
                                515,
                                293
                            ]
                        ],
                        "model_confidence": [
                            99.76238341968912
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                344,
                                688,
                                464,
                                734
                            ]
                        ],
                        "model_confidence": [
                            0.8154541850090027
                        ]
                    },
                    "is_stamp": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                462,
                                677,
                                527,
                                739
                            ]
                        ],
                        "model_confidence": [
                            0.8292888402938843
                        ]
                    },
                    "shipper_address_country": {
                        "value": "HONG KONG",
                        "coordinate": [
                            [
                                71,
                                116,
                                276,
                                136
                            ]
                        ],
                        "model_confidence": [
                            92.65414259715394
                        ]
                    },
                    "port_of_loading_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                72,
                                262,
                                138,
                                268
                            ]
                        ],
                        "model_confidence": [
                            69.84
                        ]
                    },
                    "notify_party_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                297,
                                179,
                                437,
                                197
                            ]
                        ],
                        "model_confidence": [
                            68.37
                        ]
                    },
                    "net_weight": {},
                    "shipper_name": {},
                    "bol_original_or_copy": {},
                    "page_no": {},
                    "lc_date": {},
                    "signed_By_agent": {},
                    "goods_marks_and_nos": {},
                    "transaction_date": {},
                    "stamp": {},
                    "goods_quantity": {},
                    "signature": {},
                    "final_destination": {},
                    "lc_ref_number": {},
                    "notify_party_name": {},
                    "place_of_receipt": {},
                    "carrier_country": {},
                    "agent_country": {},
                    "pre_carriage_by": {},
                    "freight_collect_at": {},
                    "agent_name": {},
                    "consignee_address": {},
                    "shipped_onboard_date": {}
                },
                "status_code": "200"
            },
            "1609flc230614_9.png": {
                "docClass": "OTHERS",
                "keys_extraction": {}
            },
            "1609flc230614_10.png": {
                "docClass": "OTHERS",
                "keys_extraction": {}
            },
            "1609flc230614_11.png": {
                "docClass": "COO",
                "keys_extraction": {
                    "consignor_name": {
                        "value": "QUANGZHOU SHINE BAYU INTERNATIONAL TRADING CO PVT . LTD LOITED QUARBEHOU",
                        "coordinate": [
                            [
                                62,
                                66,
                                218,
                                78
                            ]
                        ],
                        "model_confidence": [
                            85.7
                        ]
                    },
                    "consignor_address": {
                        "value": "MA BOOM TSUL SUN KOWLOON 908 95 KIMBERLEY KONG HOUSE SEXMBERLEY OAD  HONG TSM SHA",
                        "coordinate": [
                            [
                                61,
                                66,
                                259,
                                92
                            ]
                        ],
                        "model_confidence": [
                            92.70914781153053
                        ]
                    },
                    "consignee_name": {
                        "value": "RESOLVING AND CHLORIDES LIMITED",
                        "coordinate": [
                            [
                                64,
                                132,
                                183,
                                139
                            ]
                        ],
                        "model_confidence": [
                            99.60199999999999
                        ]
                    },
                    "consignee_address": {
                        "value": "2018 OEM  3213RD FLOOR DLF TOWERS KINJI MARG NEW DELHI 11",
                        "coordinate": [
                            [
                                63,
                                139,
                                264,
                                152
                            ]
                        ],
                        "model_confidence": [
                            99.6966973975758
                        ]
                    },
                    "from_place": {
                        "value": "KINGANG PORTCHINA",
                        "coordinate": [
                            [
                                84,
                                198,
                                150,
                                204
                            ]
                        ],
                        "model_confidence": [
                            99.7
                        ]
                    },
                    "to_place": {
                        "value": "TOMUUTAPORT INDIA",
                        "coordinate": [
                            [
                                152,
                                198,
                                224,
                                206
                            ]
                        ],
                        "model_confidence": [
                            88.3
                        ]
                    },
                    "means_of_transport": {
                        "value": "SEA",
                        "coordinate": [
                            [
                                235,
                                199,
                                247,
                                205
                            ]
                        ],
                        "model_confidence": [
                            99.14
                        ]
                    },
                    "certificate_stamped": {
                        "value": "海 [UNK] [UNK]明 CHINA - [UNK][UNK] [UNK] COUNCIL ( 1 ) OF INTERNATIONAL FOR THE PROMOTION TRADE ADORE GUANGZHOUA GUANGZHO 020-84008424 PA FAXC020-84883431 TEL : BAIYU TRADING GUANGZHOU #W F * ** COLTO",
                        "coordinate": [
                            [
                                104,
                                646,
                                432,
                                738
                            ]
                        ],
                        "model_confidence": [
                            99.18113146293135
                        ]
                    },
                    "original_or_copy": {
                        "value": "ORIGINAL",
                        "coordinate": [
                            [
                                252,
                                34,
                                304,
                                44
                            ]
                        ],
                        "model_confidence": [
                            98.68
                        ]
                    },
                    "description_of_goods": {
                        "value": "ELEVED TROUSAND PVC GRADE SUSPENSION GO - LOOK RESIM",
                        "coordinate": [
                            [
                                151,
                                347,
                                222,
                                385
                            ]
                        ],
                        "model_confidence": [
                            85.07179894179895
                        ]
                    },
                    "marks_and_no_of_packages": {
                        "value": "AND TWO HUNDRED ( 11200 ) BAGS",
                        "coordinate": [
                            [
                                210,
                                347,
                                309,
                                354
                            ]
                        ],
                        "model_confidence": [
                            71.11972073039743
                        ]
                    },
                    "certificate_no": {
                        "value": "23C4401A1501 / 02016",
                        "coordinate": [
                            [
                                334,
                                63,
                                403,
                                72
                            ]
                        ],
                        "model_confidence": [
                            98.61266897746967
                        ]
                    },
                    "issue_date": {
                        "value": "JU , 2003",
                        "coordinate": [
                            [
                                173,
                                745,
                                207,
                                750
                            ]
                        ],
                        "model_confidence": [
                            96.18321428571429
                        ]
                    },
                    "page_no": {
                        "value": "1",
                        "coordinate": [
                            [
                                283,
                                772,
                                297,
                                777
                            ]
                        ],
                        "model_confidence": [
                            99.01
                        ]
                    },
                    "coo_issuer_address": {
                        "value": "THE PEOPLES REPUBLIC OF ",
                        "coordinate": [
                            [
                                357,
                                137,
                                495,
                                149
                            ]
                        ],
                        "model_confidence": [
                            99.7908768898488
                        ]
                    },
                    "net_weight": {
                        "value": "2",
                        "coordinate": [
                            [
                                386,
                                379,
                                420,
                                384
                            ]
                        ],
                        "model_confidence": [
                            97.37
                        ]
                    },
                    "invoice_no": {
                        "value": "SRIPT - 23146",
                        "coordinate": [
                            [
                                445,
                                346,
                                481,
                                352
                            ]
                        ],
                        "model_confidence": [
                            99.43
                        ]
                    },
                    "invoice_date": {
                        "value": "JUL 05.2023",
                        "coordinate": [
                            [
                                444,
                                352,
                                478,
                                359
                            ]
                        ],
                        "model_confidence": [
                            99.53
                        ]
                    },
                    "is_signed": {},
                    "is_stamp": {
                        "value": "TRUE TRUE",
                        "coordinate": [
                            [
                                98,
                                655,
                                191,
                                750
                            ],
                            [
                                284,
                                623,
                                439,
                                733
                            ]
                        ],
                        "model_confidence": [
                            0.8691757321357727,
                            0.8890966176986694
                        ]
                    },
                    "consignor_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                61,
                                66,
                                259,
                                92
                            ]
                        ],
                        "model_confidence": [
                            92.70914781153053
                        ]
                    },
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                63,
                                139,
                                264,
                                152
                            ]
                        ],
                        "model_confidence": [
                            99.6966973975758
                        ]
                    },
                    "coo_issuer_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                357,
                                137,
                                495,
                                149
                            ]
                        ],
                        "model_confidence": [
                            99.7908768898488
                        ]
                    },
                    "vessel_details": {},
                    "country_of_origin_of_goods": {},
                    "declaration_by_exporter": {},
                    "original_number": {},
                    "lc_date": {},
                    "declaration_by_certification": {},
                    "ref_no": {},
                    "coo_issuer_name": {},
                    "lc_ref_no": {},
                    "signature": {},
                    "gross_weight": {},
                    "final_destination": {}
                },
                "status_code": "200"
            },
            "1609flc230614_12.png": {
                "docClass": "IC",
                "keys_extraction": {}
            },
            "1609flc230614_13.png": {
                "docClass": "COA",
                "keys_extraction": {}
            },
            "1609flc230614_14.png": {
                "docClass": "PL",
                "keys_extraction": {
                    "invoice_no": {
                        "value": "SSIPL - 23147",
                        "coordinate": [
                            [
                                138,
                                164,
                                184,
                                170
                            ]
                        ],
                        "model_confidence": [
                            99.87
                        ]
                    },
                    "date_of_invoice": {
                        "value": "05 JULY 2023 05 JULY 2023",
                        "coordinate": [
                            [
                                137,
                                176,
                                485,
                                185
                            ]
                        ],
                        "model_confidence": [
                            99.51314950980392
                        ]
                    },
                    "beneficiary_address": {
                        "value": "ROOM 903 TSIM 9 F SHA KIMBERLEY TSUI KOWLOON HOUSE 35 HONG KIMBERLEY KONG ROAD",
                        "coordinate": [
                            [
                                161,
                                96,
                                395,
                                115
                            ]
                        ],
                        "model_confidence": [
                            99.93639046495595
                        ]
                    },
                    "description_of_goods": {
                        "value": "RESOL VINYLS AND CHLORIDES~PVC SUSPENSION RESIN~",
                        "coordinate": [
                            [
                                139,
                                202,
                                265,
                                209
                            ]
                        ],
                        "model_confidence": [
                            98.89687115180107
                        ]
                    },
                    "remitter_drawee_applicant_importer_buyer_name": {
                        "value": "LIMITED",
                        "coordinate": [
                            [
                                267,
                                202,
                                301,
                                209
                            ]
                        ],
                        "model_confidence": [
                            54.36
                        ]
                    },
                    "consignor_address": {
                        "value": "DSM 321 MARO 3RD FLOOR NEW DELHI DLP TOWERS 110015 ",
                        "coordinate": [
                            [
                                140,
                                214,
                                302,
                                234
                            ]
                        ],
                        "model_confidence": [
                            73.35
                        ]
                    },
                    "remitter_address": {
                        "value": "SHIVAJI",
                        "coordinate": [
                            [
                                140,
                                227,
                                171,
                                234
                            ]
                        ],
                        "model_confidence": [
                            43.01
                        ]
                    },
                    "port_of_loading": {
                        "value": "XINGANG PORT ",
                        "coordinate": [
                            [
                                140,
                                239,
                                232,
                                247
                            ]
                        ],
                        "model_confidence": [
                            99.94555555555556
                        ]
                    },
                    "port_of_discharge": {
                        "value": "MUNDRA PORT , INDIA",
                        "coordinate": [
                            [
                                140,
                                252,
                                227,
                                259
                            ]
                        ],
                        "model_confidence": [
                            99.91305882352943
                        ]
                    },
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "PVT",
                        "coordinate": [
                            [
                                352,
                                77,
                                383,
                                90
                            ]
                        ],
                        "model_confidence": [
                            78.61
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "11200 ",
                        "coordinate": [
                            [
                                147,
                                517,
                                191,
                                524
                            ]
                        ],
                        "model_confidence": [
                            99.94
                        ]
                    },
                    "country_of_origin_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                224,
                                454,
                                249,
                                462
                            ]
                        ],
                        "model_confidence": [
                            98.97
                        ]
                    },
                    "net_weight": {
                        "value": " 280,000 282,240470 280,000 ",
                        "coordinate": [
                            [
                                165,
                                517,
                                456,
                                563
                            ]
                        ],
                        "model_confidence": [
                            72.45260074186479
                        ]
                    },
                    "gross_weight": {
                        "value": "282,240 ",
                        "coordinate": [
                            [
                                165,
                                567,
                                210,
                                576
                            ]
                        ],
                        "model_confidence": [
                            98.84
                        ]
                    },
                    "original_copy": {
                        "value": "ORIGINAL",
                        "coordinate": [
                            [
                                412,
                                97,
                                488,
                                117
                            ]
                        ],
                        "model_confidence": [
                            99.83
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE TRUE",
                        "coordinate": [
                            [
                                334,
                                622,
                                450,
                                646
                            ],
                            [
                                384,
                                625,
                                436,
                                650
                            ]
                        ],
                        "model_confidence": [
                            0.5793284773826599,
                            0.6693568229675293
                        ]
                    },
                    "is_stamp": {},
                    "consignor_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                140,
                                214,
                                302,
                                234
                            ]
                        ],
                        "model_confidence": [
                            73.35
                        ]
                    },
                    "port_of_loading_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                140,
                                239,
                                232,
                                247
                            ]
                        ],
                        "model_confidence": [
                            99.94555555555556
                        ]
                    },
                    "shipper_address": {},
                    "lc_date": {},
                    "notify_party_address": {},
                    "awb_number": {},
                    "vessel_flight_no": {},
                    "track_reference": {},
                    "declaration": {},
                    "notify_party_name": {},
                    "bill_of_lading_date": {},
                    "dimension": {},
                    "transaction_currency": {},
                    "transaction_date": {},
                    "lc_ref_no": {},
                    "country_of_final_destination": {},
                    "consignee_name": {},
                    "invoice_amount": {},
                    "shipper_name": {},
                    "transaction_amount_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin_no": {},
                    "consignee_address": {},
                    "bill_of_lading_number": {},
                    "rate_per_unit": {},
                    "consignor_name": {},
                    "invoice_currency": {},
                    "pre_carriage_by": {},
                    "payment_terms_terms_of_delivery_&_payment": {},
                    "incoterm": {},
                    "awb_date": {}
                },
                "status_code": "200"
            },
            "1609flc230614_15.png": {
                "docClass": "CI",
                "keys_extraction": {
                    "beneficiary_address": {
                        "value": "ROOM 903 TSIM 9 F SHA KIMBERLEY TSUI KOWLOON HOUSE 35 HONG KIMBERLEY KONG ROAD COMMERCIAL",
                        "coordinate": [
                            [
                                172,
                                94,
                                404,
                                147
                            ]
                        ],
                        "model_confidence": [
                            86.04434890498116
                        ]
                    },
                    "cosignee_name": {
                        "value": "RESOL VINYLS AND CHLORIDES LIMITED",
                        "coordinate": [
                            [
                                125,
                                161,
                                286,
                                169
                            ]
                        ],
                        "model_confidence": [
                            99.7037814558321
                        ]
                    },
                    "consignee_address": {
                        "value": "SHIVAJI DSM 321 MARG 3RD FLOOR NEW DELHI DLP TOWERS 110013 ",
                        "coordinate": [
                            [
                                126,
                                173,
                                287,
                                196
                            ]
                        ],
                        "model_confidence": [
                            99.76
                        ]
                    },
                    "invoice_no": {
                        "value": "SSIPL - 23147 23073",
                        "coordinate": [
                            [
                                126,
                                197,
                                172,
                                226
                            ]
                        ],
                        "model_confidence": [
                            97.36963855421685
                        ]
                    },
                    "date_of_invoice": {
                        "value": "05-07-2023",
                        "coordinate": [
                            [
                                126,
                                209,
                                176,
                                216
                            ]
                        ],
                        "model_confidence": [
                            98.50249999999998
                        ]
                    },
                    "port_of_loading": {
                        "value": "XINGANG PORT ",
                        "coordinate": [
                            [
                                126,
                                233,
                                217,
                                241
                            ]
                        ],
                        "model_confidence": [
                            99.34932584269663
                        ]
                    },
                    "port_of_discharge": {
                        "value": "MUNDRA PORT , INDIA",
                        "coordinate": [
                            [
                                125,
                                245,
                                213,
                                254
                            ]
                        ],
                        "model_confidence": [
                            99.39103448275861
                        ]
                    },
                    "goods_description": {
                        "value": "PVC SUSPENSION RESIN",
                        "coordinate": [
                            [
                                126,
                                305,
                                220,
                                313
                            ]
                        ],
                        "model_confidence": [
                            99.79217391304347
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": " 280.00 ",
                        "coordinate": [
                            [
                                143,
                                306,
                                355,
                                346
                            ]
                        ],
                        "model_confidence": [
                            96.50999999999999
                        ]
                    },
                    "rate_per_unit": {
                        "value": "USD 770.00 770.00",
                        "coordinate": [
                            [
                                214,
                                306,
                                419,
                                346
                            ]
                        ],
                        "model_confidence": [
                            86.44723684210527
                        ]
                    },
                    "bill_of_lading_no": {
                        "value": "327W",
                        "coordinate": [
                            [
                                186,
                                476,
                                207,
                                485
                            ]
                        ],
                        "model_confidence": [
                            63.64
                        ]
                    },
                    "declaration_by_issuer": {
                        "value": "TIANJIN BOHUA CHEMICAL DEVELOPMENT CO . , LTD . FOR",
                        "coordinate": [
                            [
                                126,
                                427,
                                331,
                                435
                            ],
                            [
                                336,
                                600,
                                343,
                                607
                            ]
                        ],
                        "model_confidence": [
                            87.77508726161079,
                            79.55
                        ]
                    },
                    "country_of_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                204,
                                440,
                                230,
                                447
                            ]
                        ],
                        "model_confidence": [
                            96.94
                        ]
                    },
                    "lc_ref_no": {
                        "value": "1609FL.C230614",
                        "coordinate": [
                            [
                                195,
                                580,
                                250,
                                590
                            ]
                        ],
                        "model_confidence": [
                            98.24
                        ]
                    },
                    "signature_of_the_issuer": {
                        "value": "ORIGINAL AND HALF OFSH",
                        "coordinate": [
                            [
                                426,
                                95,
                                506,
                                121
                            ],
                            [
                                346,
                                600,
                                389,
                                606
                            ]
                        ],
                        "model_confidence": [
                            96.09,
                            88.55
                        ]
                    },
                    "invoice_currency": {
                        "value": "",
                        "coordinate": [
                            [
                                443,
                                503,
                                460,
                                512
                            ]
                        ],
                        "model_confidence": [
                            98.49
                        ]
                    },
                    "invoice_amount": {
                        "value": "215,600.00",
                        "coordinate": [
                            [
                                466,
                                504,
                                504,
                                513
                            ]
                        ],
                        "model_confidence": [
                            74.88
                        ]
                    },
                    "invoice_amount_in_words": {
                        "value": "TWO HUNDRED FIFTEEN THOUSAND AND SIX HUNDRED ONLY .",
                        "coordinate": [
                            [
                                228,
                                543,
                                473,
                                552
                            ]
                        ],
                        "model_confidence": [
                            99.45380115862332
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                380,
                                619,
                                443,
                                644
                            ]
                        ],
                        "model_confidence": [
                            0.6815761923789978
                        ]
                    },
                    "is_stamp": {},
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                126,
                                173,
                                287,
                                196
                            ]
                        ],
                        "model_confidence": [
                            99.76
                        ]
                    },
                    "port_of_loading_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                126,
                                233,
                                217,
                                241
                            ]
                        ],
                        "model_confidence": [
                            99.34932584269663
                        ]
                    },
                    "incoterm": {},
                    "vessel_flight_no": {},
                    "consignor_name": {},
                    "beneficiary_bank_country": {},
                    "transaction_currency": {},
                    "transaction_amonunt_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin": {},
                    "bill_of_lading_date": {},
                    "invoice_tax_ccy": {},
                    "consignee_country": {},
                    "tenor_indicator": {},
                    "net_weight": {},
                    "notify_party_country": {},
                    "indicator_type": {},
                    "hs_code_no": {},
                    "invoice_due_date": {},
                    "country_of_final_destination": {},
                    "indicator_date": {},
                    "invoice_discount_amount": {},
                    "shipper_address": {},
                    "consignor_country": {},
                    "invoice_discount_ccy": {},
                    "usance_tenor": {},
                    "tenor_type": {},
                    "awb_date": {},
                    "delivery_terms": {},
                    "gross_weight": {},
                    "consignor_address": {},
                    "beneficiary_iban_number": {},
                    "transaction_date": {},
                    "beneficiary_account_number": {},
                    "pre-carriage-by": {},
                    "lc_date": {},
                    "invoice_tax_amount": {},
                    "notify_party_name": {},
                    "original_or_copy": {},
                    "beneficiary_drawer_exporter_seller_supplier_name": {},
                    "notify_party_address": {},
                    "beneficiary_bank_identifier": {},
                    "awb_number": {},
                    "page_no": {},
                    "remitter_address": {},
                    "shipper_name": {},
                    "beneficiary_bank_name": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "1609flc230614_16.png": {
                "docClass": "BOL",
                "keys_extraction": {
                    "shipper_address": {
                        "value": "ROOM TSUI KOWLOON 903 9 KIMBERLEY  HOUSE 35 KIMBERLEY ROAD TSIM SHA",
                        "coordinate": [
                            [
                                65,
                                136,
                                261,
                                153
                            ]
                        ],
                        "model_confidence": [
                            97.90638485622887
                        ]
                    },
                    "carrier_name": {
                        "value": "MAERSK",
                        "coordinate": [
                            [
                                120,
                                83,
                                216,
                                101
                            ]
                        ],
                        "model_confidence": [
                            97.54
                        ]
                    },
                    "consignee_name": {
                        "value": "THE AXIS BANK LIMITED INDIA",
                        "coordinate": [
                            [
                                74,
                                190,
                                197,
                                197
                            ]
                        ],
                        "model_confidence": [
                            85.07631563964438
                        ]
                    },
                    "vessel_name": {
                        "value": "ALS CLIVIA LADY",
                        "coordinate": [
                            [
                                66,
                                252,
                                98,
                                273
                            ]
                        ],
                        "model_confidence": [
                            99.06356347438754
                        ]
                    },
                    "port_of_loading": {
                        "value": "XINGANG PORTCHINA",
                        "coordinate": [
                            [
                                66,
                                274,
                                127,
                                281
                            ]
                        ],
                        "model_confidence": [
                            97.98
                        ]
                    },
                    "goods_description": {
                        "value": "PVC GRADE SUSPENSION DG - 100OK RESIN",
                        "coordinate": [
                            [
                                69,
                                329,
                                149,
                                345
                            ]
                        ],
                        "model_confidence": [
                            63.289007633587794
                        ]
                    },
                    "voyage_number": {
                        "value": "327W",
                        "coordinate": [
                            [
                                167,
                                251,
                                181,
                                256
                            ]
                        ],
                        "model_confidence": [
                            99.96
                        ]
                    },
                    "port_of_discharge": {
                        "value": "MUNDRA PART INDIA",
                        "coordinate": [
                            [
                                167,
                                275,
                                212,
                                280
                            ]
                        ],
                        "model_confidence": [
                            97.16
                        ]
                    },
                    "bol_original_number": {
                        "value": "THREE",
                        "coordinate": [
                            [
                                76,
                                643,
                                98,
                                649
                            ]
                        ],
                        "model_confidence": [
                            99.85
                        ]
                    },
                    "country_of_origin": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                138,
                                424,
                                159,
                                431
                            ]
                        ],
                        "model_confidence": [
                            96.69
                        ]
                    },
                    "freight_collect_or_prepaid": {
                        "value": "FREIGHT PREPAID",
                        "coordinate": [
                            [
                                71,
                                443,
                                128,
                                450
                            ]
                        ],
                        "model_confidence": [
                            99.74
                        ]
                    },
                    "container_number": {
                        "value": "MRSU4678327 MRKU6266943 ML - ML - CN1474771 TCNU7577406 MRKU3881580 - CN1474911 CN1474783 MRKU2029136 - - CN1474784 CN1474930",
                        "coordinate": [
                            [
                                70,
                                475,
                                171,
                                521
                            ]
                        ],
                        "model_confidence": [
                            89.88714285714285
                        ]
                    },
                    "place_of_issue": {
                        "value": "QINGDAO",
                        "coordinate": [
                            [
                                174,
                                613,
                                199,
                                622
                            ]
                        ],
                        "model_confidence": [
                            97.44
                        ]
                    },
                    "shipped_onboard_date": {
                        "value": "20230709",
                        "coordinate": [
                            [
                                174,
                                660,
                                211,
                                667
                            ]
                        ],
                        "model_confidence": [
                            25.48
                        ]
                    },
                    "gross_weight": {
                        "value": "282240.000 ",
                        "coordinate": [
                            [
                                368,
                                298,
                                422,
                                306
                            ]
                        ],
                        "model_confidence": [
                            99.93000000000002
                        ]
                    },
                    "signed_by_carrier": {
                        "value": "CARD",
                        "coordinate": [
                            [
                                324,
                                693,
                                414,
                                730
                            ]
                        ],
                        "model_confidence": [
                            83.74
                        ]
                    },
                    "bill_of_lading_number": {
                        "value": "228712862",
                        "coordinate": [
                            [
                                446,
                                110,
                                481,
                                116
                            ]
                        ],
                        "model_confidence": [
                            98.83
                        ]
                    },
                    "measurement_or_dimension": {
                        "value": "470.0000 CBM",
                        "coordinate": [
                            [
                                439,
                                297,
                                486,
                                305
                            ]
                        ],
                        "model_confidence": [
                            99.96
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                326,
                                690,
                                441,
                                736
                            ]
                        ],
                        "model_confidence": [
                            0.8058339953422546
                        ]
                    },
                    "is_stamp": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                441,
                                679,
                                498,
                                737
                            ]
                        ],
                        "model_confidence": [
                            0.8116793632507324
                        ]
                    },
                    "shipper_address_country": {
                        "value": "HONG KONG",
                        "coordinate": [
                            [
                                65,
                                136,
                                261,
                                153
                            ]
                        ],
                        "model_confidence": [
                            97.90638485622887
                        ]
                    },
                    "net_weight": {},
                    "shipper_name": {},
                    "bill_of_lading_issue_date": {},
                    "bol_original_or_copy": {},
                    "page_no": {},
                    "lc_date": {},
                    "signed_By_agent": {},
                    "goods_marks_and_nos": {},
                    "transaction_date": {},
                    "stamp": {},
                    "goods_quantity": {},
                    "signature": {},
                    "final_destination": {},
                    "lc_ref_number": {},
                    "notify_party_name": {},
                    "place_of_receipt": {},
                    "carrier_country": {},
                    "agent_country": {},
                    "notify_party_address": {},
                    "pre_carriage_by": {},
                    "freight_collect_at": {},
                    "agent_name": {},
                    "consignee_address": {}
                },
                "status_code": "200"
            },
            "1609flc230614_17.png": {
                "docClass": "OTHERS",
                "keys_extraction": {}
            },
            "1609flc230614_18.png": {
                "docClass": "OTHERS",
                "keys_extraction": {}
            },
            "1609flc230614_19.png": {
                "docClass": "COO",
                "keys_extraction": {
                    "consignor_name": {
                        "value": "GUANGZHOU VIASUN SHINE BAN INTERNATIONAL / TRADING QUANDEHOU",
                        "coordinate": [
                            [
                                65,
                                67,
                                221,
                                82
                            ]
                        ],
                        "model_confidence": [
                            88.38904999999998
                        ]
                    },
                    "consignor_address": {
                        "value": "ROAD CHINA TSUE ROOM KOWLOON 80 KMILEY HONG KONG HOUSE MKWERLEY",
                        "coordinate": [
                            [
                                64,
                                68,
                                242,
                                95
                            ]
                        ],
                        "model_confidence": [
                            92.01246533127889
                        ]
                    },
                    "consignee_name": {
                        "value": "RESOL VINYLAND CHLORIDES",
                        "coordinate": [
                            [
                                66,
                                134,
                                159,
                                141
                            ]
                        ],
                        "model_confidence": [
                            64.08716417910448
                        ]
                    },
                    "consignee_address": {
                        "value": "DEM 0018 SE  ARD FLOOR OF TOW MARG NEW DELHI",
                        "coordinate": [
                            [
                                65,
                                141,
                                257,
                                154
                            ]
                        ],
                        "model_confidence": [
                            99.3715350268868
                        ]
                    },
                    "marks_and_no_of_packages": {
                        "value": "ELEVEN THOUSAND AND TWO HUNDRED ( 11200 ) BAGS",
                        "coordinate": [
                            [
                                152,
                                349,
                                315,
                                356
                            ]
                        ],
                        "model_confidence": [
                            99.4197639409072
                        ]
                    },
                    "description_of_goods": {
                        "value": "NSION REBIN",
                        "coordinate": [
                            [
                                188,
                                370,
                                226,
                                376
                            ]
                        ],
                        "model_confidence": [
                            92.38909090909092
                        ]
                    },
                    "signature": {
                        "value": "BOHUA L.08.2003",
                        "coordinate": [
                            [
                                233,
                                442,
                                255,
                                451
                            ],
                            [
                                185,
                                748,
                                213,
                                757
                            ]
                        ],
                        "model_confidence": [
                            51.12,
                            73.5
                        ]
                    },
                    "original_or_copy": {
                        "value": "ORIGINAL",
                        "coordinate": [
                            [
                                257,
                                38,
                                311,
                                48
                            ]
                        ],
                        "model_confidence": [
                            98.72
                        ]
                    },
                    "certificate_no": {
                        "value": "2304401A1501 / 2016",
                        "coordinate": [
                            [
                                341,
                                70,
                                411,
                                77
                            ]
                        ],
                        "model_confidence": [
                            98.27943661971831
                        ]
                    },
                    "coo_issuer_address": {
                        "value": "THE PEOPLES REPUBLIC OF ",
                        "coordinate": [
                            [
                                365,
                                142,
                                505,
                                150
                            ]
                        ],
                        "model_confidence": [
                            99.8016509696956
                        ]
                    },
                    "certificate_stamped": {
                        "value": "中国 国[UNK] [UNK] , [UNK] [UNK] [UNK]明 [UNK][UNK] [UNK][UNK] [UNK][UNK] CHINA OF COUNCIL INTERNATIONAL FOR THE PROMOTION GUANGZHOU TRADE -64003431 TEL : 020421",
                        "coordinate": [
                            [
                                307,
                                637,
                                445,
                                740
                            ]
                        ],
                        "model_confidence": [
                            99.80404692081999
                        ]
                    },
                    "invoice_no": {
                        "value": "SSIPL - 23147",
                        "coordinate": [
                            [
                                455,
                                347,
                                492,
                                353
                            ]
                        ],
                        "model_confidence": [
                            99.63
                        ]
                    },
                    "invoice_date": {
                        "value": "JUL 05 , 2023",
                        "coordinate": [
                            [
                                455,
                                355,
                                490,
                                360
                            ]
                        ],
                        "model_confidence": [
                            99.46
                        ]
                    },
                    "page_no": {
                        "value": "1",
                        "coordinate": [
                            [
                                291,
                                779,
                                301,
                                785
                            ]
                        ],
                        "model_confidence": [
                            98.97
                        ]
                    },
                    "is_signed": {},
                    "is_stamp": {
                        "value": "TRUE TRUE",
                        "coordinate": [
                            [
                                102,
                                658,
                                198,
                                758
                            ],
                            [
                                293,
                                628,
                                452,
                                737
                            ]
                        ],
                        "model_confidence": [
                            0.8651102185249329,
                            0.9201538562774658
                        ]
                    },
                    "consignor_address_country": {
                        "value": "CHINA HONG KONG",
                        "coordinate": [
                            [
                                64,
                                68,
                                242,
                                95
                            ]
                        ],
                        "model_confidence": [
                            92.01246533127889
                        ]
                    },
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                65,
                                141,
                                257,
                                154
                            ]
                        ],
                        "model_confidence": [
                            99.3715350268868
                        ]
                    },
                    "coo_issuer_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                365,
                                142,
                                505,
                                150
                            ]
                        ],
                        "model_confidence": [
                            99.8016509696956
                        ]
                    },
                    "vessel_details": {},
                    "country_of_origin_of_goods": {},
                    "declaration_by_exporter": {},
                    "original_number": {},
                    "lc_date": {},
                    "declaration_by_certification": {},
                    "ref_no": {},
                    "coo_issuer_name": {},
                    "means_of_transport": {},
                    "lc_ref_no": {},
                    "from_place": {},
                    "issue_date": {},
                    "gross_weight": {},
                    "net_weight": {},
                    "final_destination": {},
                    "to_place": {}
                },
                "status_code": "200"
            },
            "1609flc230614_20.png": {
                "docClass": "IC",
                "keys_extraction": {
                    "policy_no": {
                        "value": "11153003902094769645 37020018804",
                        "coordinate": [
                            [
                                118,
                                227,
                                196,
                                233
                            ],
                            [
                                427,
                                711,
                                505,
                                715
                            ]
                        ],
                        "model_confidence": [
                            99.74,
                            99.62
                        ]
                    },
                    "vessel_or_flight_name": {
                        "value": "SCLIVIA",
                        "coordinate": [
                            [
                                125,
                                262,
                                157,
                                274
                            ]
                        ],
                        "model_confidence": [
                            50.01
                        ]
                    },
                    "subject_matter_insured": {
                        "value": "PPC GRADE SUSPENSION DG - 1000K RESIN CHEMICAL THE GOODS ARE OF CHINA ORIGIN",
                        "coordinate": [
                            [
                                77,
                                356,
                                221,
                                450
                            ]
                        ],
                        "model_confidence": [
                            95.24878904696018
                        ]
                    },
                    "sum_insured_amount": {
                        "value": "USD237,160.00",
                        "coordinate": [
                            [
                                117,
                                324,
                                170,
                                332
                            ]
                        ],
                        "model_confidence": [
                            99.37
                        ]
                    },
                    "issue_date": {
                        "value": "JUL 05 , 2023",
                        "coordinate": [
                            [
                                103,
                                597,
                                150,
                                605
                            ]
                        ],
                        "model_confidence": [
                            99.76774901929065
                        ]
                    },
                    "from_place": {
                        "value": "XINGANG PORT , CHINA",
                        "coordinate": [
                            [
                                211,
                                284,
                                288,
                                290
                            ]
                        ],
                        "model_confidence": [
                            99.7960810810811
                        ]
                    },
                    "to_place": {
                        "value": "MUNDRA PORT , INDIA",
                        "coordinate": [
                            [
                                210,
                                303,
                                282,
                                312
                            ]
                        ],
                        "model_confidence": [
                            99.88335570469798
                        ]
                    },
                    "claim_payable_in": {
                        "value": "ATIN INDIA IN USD",
                        "coordinate": [
                            [
                                335,
                                221,
                                399,
                                234
                            ]
                        ],
                        "model_confidence": [
                            99.66260040160644
                        ]
                    },
                    "conditions_of_coverage": {
                        "value": "IRRESPECTIVERERCENTAGE WAREHOUST",
                        "coordinate": [
                            [
                                292,
                                404,
                                499,
                                421
                            ]
                        ],
                        "model_confidence": [
                            17.55496402877698
                        ]
                    },
                    "address_of_assured": {
                        "value": "KOLKATA JANKI 700022 SHAH , INDIA RD , EMAILS HASTINGS",
                        "coordinate": [
                            [
                                341,
                                248,
                                464,
                                266
                            ]
                        ],
                        "model_confidence": [
                            96.7343642611684
                        ]
                    },
                    "original_Number": {
                        "value": "2 2",
                        "coordinate": [
                            [
                                458,
                                580,
                                497,
                                605
                            ]
                        ],
                        "model_confidence": [
                            97.78965811965811
                        ]
                    },
                    "declaration_by": {
                        "value": "中国 平安 [UNK][UNK] PROPERTY 保 UNK",
                        "coordinate": [
                            [
                                411,
                                648,
                                472,
                                667
                            ]
                        ],
                        "model_confidence": [
                            69.00646884272997
                        ]
                    },
                    "insurance_issuer_name_bottom": {
                        "value": "PING COMPANY & CASUALTY BRANCH , LTD",
                        "coordinate": [
                            [
                                412,
                                659,
                                512,
                                686
                            ]
                        ],
                        "model_confidence": [
                            43.2022684562343
                        ]
                    },
                    "signature": {
                        "value": "INSURANCE AN QINGDAO CHINA",
                        "coordinate": [
                            [
                                412,
                                659,
                                498,
                                686
                            ]
                        ],
                        "model_confidence": [
                            39.966686390532544
                        ]
                    },
                    "insurance_issuer_address_bottom": {
                        "value": "ROOM DISTRICT 1401-1402 , QINGDAO BUILING , SHANDONG , CHINA . 28 , MIAOLING 0086-532-80903999 RD , LAN",
                        "coordinate": [
                            [
                                261,
                                720,
                                473,
                                738
                            ]
                        ],
                        "model_confidence": [
                            78.94859879645435
                        ]
                    },
                    "is_signed": {
                        "value": "",
                        "coordinate": [],
                        "model_confidence": []
                    },
                    "is_stamp": {
                        "value": "",
                        "coordinate": [],
                        "model_confidence": []
                    },
                    "start_date": {},
                    "vessel_or_flight_number": {},
                    "certificate_Stamped": {},
                    "sail_on_or_about_to_date": {},
                    "insurance_issuer_address": {},
                    "country_of_origin_origin_of_goods": {},
                    "original_copy": {},
                    "name_of_assured": {},
                    "expiry_date": {},
                    "premium": {},
                    "claim_payable_by_address": {},
                    "lc_date": {},
                    "page_no": {},
                    "insurance_issuer_name": {},
                    "certificate_no": {},
                    "lc_ref_no": {},
                    "claim payable_by_name": {},
                    "mode_of_transport": {},
                    "sum_insured_currency": {}
                },
                "status_code": "200"
            },
            "1609flc230614_21.png": {
                "docClass": "COA",
                "keys_extraction": {}
            },
            "1609flc230614_22.png": {
                "docClass": "CI",
                "keys_extraction": {
                    "invoice_no": {
                        "value": " 23148 23073",
                        "coordinate": [
                            [
                                121,
                                215,
                                165,
                                244
                            ]
                        ],
                        "model_confidence": [
                            91.65142857142855
                        ]
                    },
                    "beneficiary_address": {
                        "value": "ROOM 903 TSIM 9 F SHA KIMBERLEY TSUI KOWLOON HOUSE 35 HONG KIMBERLEY KONG ROAD COMMERCIAL",
                        "coordinate": [
                            [
                                168,
                                114,
                                396,
                                166
                            ]
                        ],
                        "model_confidence": [
                            86.3440525804931
                        ]
                    },
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "INTERNATIONAL PVT LIMITED",
                        "coordinate": [
                            [
                                219,
                                94,
                                453,
                                109
                            ]
                        ],
                        "model_confidence": [
                            99.89164179104478
                        ]
                    },
                    "cosignee_name": {
                        "value": "RESOL VINYLS AND CHLORIDES LIMITED",
                        "coordinate": [
                            [
                                123,
                                180,
                                278,
                                187
                            ]
                        ],
                        "model_confidence": [
                            99.67139802813782
                        ]
                    },
                    "consignee_address": {
                        "value": "DSM SHIVAJI 321 SSIPL MARG 3RD FLOOR NEW DELHI DLF TOWERS 110015 ",
                        "coordinate": [
                            [
                                122,
                                192,
                                279,
                                222
                            ]
                        ],
                        "model_confidence": [
                            95.93
                        ]
                    },
                    "date_of_invoice": {
                        "value": "05-07-2023",
                        "coordinate": [
                            [
                                122,
                                227,
                                170,
                                234
                            ]
                        ],
                        "model_confidence": [
                            97.90659574468084
                        ]
                    },
                    "port_of_loading": {
                        "value": "XINGANG PORT ",
                        "coordinate": [
                            [
                                121,
                                252,
                                211,
                                259
                            ]
                        ],
                        "model_confidence": [
                            99.43159090909091
                        ]
                    },
                    "port_of_discharge": {
                        "value": "MUNDRA PORT , INDIA",
                        "coordinate": [
                            [
                                122,
                                263,
                                207,
                                272
                            ]
                        ],
                        "model_confidence": [
                            99.29285714285716
                        ]
                    },
                    "goods_description": {
                        "value": "PVC SUSPENSION RESIN",
                        "coordinate": [
                            [
                                121,
                                322,
                                210,
                                328
                            ]
                        ],
                        "model_confidence": [
                            99.80050588235295
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "280  280.00 ",
                        "coordinate": [
                            [
                                139,
                                323,
                                343,
                                364
                            ]
                        ],
                        "model_confidence": [
                            95.96970588235294
                        ]
                    },
                    "rate_per_unit": {
                        "value": "USD 770.00 770.00",
                        "coordinate": [
                            [
                                208,
                                323,
                                406,
                                364
                            ]
                        ],
                        "model_confidence": [
                            86.92200000000001
                        ]
                    },
                    "bill_of_lading_no": {
                        "value": "327W",
                        "coordinate": [
                            [
                                178,
                                492,
                                198,
                                500
                            ]
                        ],
                        "model_confidence": [
                            64.57
                        ]
                    },
                    "declaration_by_issuer": {
                        "value": "TIANJIN BOHUA CHEMICAL DEVELOPMENT CO . , LTD .",
                        "coordinate": [
                            [
                                119,
                                442,
                                318,
                                451
                            ]
                        ],
                        "model_confidence": [
                            95.73000936707068
                        ]
                    },
                    "country_of_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                196,
                                456,
                                220,
                                464
                            ]
                        ],
                        "model_confidence": [
                            95.5
                        ]
                    },
                    "lc_ref_no": {
                        "value": "1609FLC230614",
                        "coordinate": [
                            [
                                186,
                                594,
                                241,
                                603
                            ]
                        ],
                        "model_confidence": [
                            94.15
                        ]
                    },
                    "invoice_currency": {
                        "value": "",
                        "coordinate": [
                            [
                                427,
                                518,
                                444,
                                527
                            ]
                        ],
                        "model_confidence": [
                            99.0
                        ]
                    },
                    "invoice_amount": {
                        "value": "215,600.00",
                        "coordinate": [
                            [
                                451,
                                519,
                                488,
                                528
                            ]
                        ],
                        "model_confidence": [
                            77.6
                        ]
                    },
                    "invoice_amount_in_words": {
                        "value": "TWO HUNDRED FIFTEEN THOUSAND AND SIX HUNDRED ONLY",
                        "coordinate": [
                            [
                                218,
                                554,
                                453,
                                565
                            ]
                        ],
                        "model_confidence": [
                            96.67851918393231
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                345,
                                632,
                                403,
                                651
                            ]
                        ],
                        "model_confidence": [
                            0.5424861311912537
                        ]
                    },
                    "is_stamp": {},
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                122,
                                192,
                                279,
                                222
                            ]
                        ],
                        "model_confidence": [
                            95.93
                        ]
                    },
                    "port_of_loading_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                121,
                                252,
                                211,
                                259
                            ]
                        ],
                        "model_confidence": [
                            99.43159090909091
                        ]
                    },
                    "incoterm": {},
                    "vessel_flight_no": {},
                    "consignor_name": {},
                    "beneficiary_bank_country": {},
                    "transaction_currency": {},
                    "transaction_amonunt_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin": {},
                    "bill_of_lading_date": {},
                    "invoice_tax_ccy": {},
                    "consignee_country": {},
                    "tenor_indicator": {},
                    "net_weight": {},
                    "notify_party_country": {},
                    "indicator_type": {},
                    "hs_code_no": {},
                    "invoice_due_date": {},
                    "country_of_final_destination": {},
                    "indicator_date": {},
                    "invoice_discount_amount": {},
                    "shipper_address": {},
                    "consignor_country": {},
                    "invoice_discount_ccy": {},
                    "usance_tenor": {},
                    "tenor_type": {},
                    "awb_date": {},
                    "delivery_terms": {},
                    "gross_weight": {},
                    "consignor_address": {},
                    "beneficiary_iban_number": {},
                    "transaction_date": {},
                    "beneficiary_account_number": {},
                    "pre-carriage-by": {},
                    "signature_of_the_issuer": {},
                    "lc_date": {},
                    "invoice_tax_amount": {},
                    "notify_party_name": {},
                    "original_or_copy": {},
                    "notify_party_address": {},
                    "beneficiary_bank_identifier": {},
                    "awb_number": {},
                    "page_no": {},
                    "remitter_address": {},
                    "shipper_name": {},
                    "beneficiary_bank_name": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "1609flc230614_23.png": {
                "docClass": "PL",
                "keys_extraction": {
                    "invoice_no": {
                        "value": "SSIPL - 23148",
                        "coordinate": [
                            [
                                139,
                                154,
                                184,
                                161
                            ]
                        ],
                        "model_confidence": [
                            98.44
                        ]
                    },
                    "date_of_invoice": {
                        "value": "05 JULY 2023 05 JULY 2023",
                        "coordinate": [
                            [
                                139,
                                166,
                                482,
                                174
                            ]
                        ],
                        "model_confidence": [
                            95.86687326549492
                        ]
                    },
                    "description_of_goods": {
                        "value": "RESOL VINYLS AND CHLORIDES LIMITED~PVC GRADE SUSPENSION DG - 1000K RESIN~",
                        "coordinate": [
                            [
                                140,
                                191,
                                300,
                                198
                            ]
                        ],
                        "model_confidence": [
                            92.76906661133015
                        ]
                    },
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "INTERNATIONAL PVT LIMITED",
                        "coordinate": [
                            [
                                218,
                                69,
                                455,
                                81
                            ]
                        ],
                        "model_confidence": [
                            79.50474137931035
                        ]
                    },
                    "beneficiary_address": {
                        "value": "ROOM 903 TSIM 9 F SHA KIMBERLEY TSUI KOWLOON HOUSE 35 HONG KIMBERLEY KONG ROAD",
                        "coordinate": [
                            [
                                163,
                                88,
                                396,
                                107
                            ]
                        ],
                        "model_confidence": [
                            99.88873907654168
                        ]
                    },
                    "port_of_loading": {
                        "value": "XINGANG PORT ",
                        "coordinate": [
                            [
                                141,
                                228,
                                232,
                                236
                            ]
                        ],
                        "model_confidence": [
                            99.85613636363637
                        ]
                    },
                    "port_of_discharge": {
                        "value": "MUNDRA PORT , INDIA",
                        "coordinate": [
                            [
                                140,
                                240,
                                227,
                                247
                            ]
                        ],
                        "model_confidence": [
                            99.94
                        ]
                    },
                    "consignor_address": {
                        "value": "DSM SHIVAJI 321 MARG 3RD FLOOR NEW DELHI DLF TOWERS 110015 ",
                        "coordinate": [
                            [
                                141,
                                204,
                                302,
                                224
                            ]
                        ],
                        "model_confidence": [
                            83.49
                        ]
                    },
                    "incoterm": {
                        "value": "CIF",
                        "coordinate": [
                            [
                                144,
                                379,
                                155,
                                387
                            ]
                        ],
                        "model_confidence": [
                            25.83
                        ]
                    },
                    "declaration": {
                        "value": "TIANJIN BOHUA CHEMICAL DEVELOPMENT CO . , LTD .",
                        "coordinate": [
                            [
                                144,
                                427,
                                349,
                                437
                            ]
                        ],
                        "model_confidence": [
                            86.79341596122359
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "11200 ",
                        "coordinate": [
                            [
                                144,
                                507,
                                188,
                                514
                            ]
                        ],
                        "model_confidence": [
                            96.36
                        ]
                    },
                    "original_copy": {
                        "value": "ORIGINAL",
                        "coordinate": [
                            [
                                413,
                                85,
                                489,
                                110
                            ]
                        ],
                        "model_confidence": [
                            99.84
                        ]
                    },
                    "net_weight": {
                        "value": "280,000 ",
                        "coordinate": [
                            [
                                161,
                                544,
                                206,
                                553
                            ]
                        ],
                        "model_confidence": [
                            99.93
                        ]
                    },
                    "gross_weight": {
                        "value": "282,240 ",
                        "coordinate": [
                            [
                                161,
                                556,
                                206,
                                566
                            ]
                        ],
                        "model_confidence": [
                            99.92
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                407,
                                606,
                                458,
                                625
                            ]
                        ],
                        "model_confidence": [
                            0.5947839021682739
                        ]
                    },
                    "is_stamp": {},
                    "port_of_loading_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                141,
                                228,
                                232,
                                236
                            ]
                        ],
                        "model_confidence": [
                            99.85613636363637
                        ]
                    },
                    "consignor_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                141,
                                204,
                                302,
                                224
                            ]
                        ],
                        "model_confidence": [
                            83.49
                        ]
                    },
                    "shipper_address": {},
                    "lc_date": {},
                    "notify_party_address": {},
                    "awb_number": {},
                    "vessel_flight_no": {},
                    "track_reference": {},
                    "country_of_origin_origin_of_goods": {},
                    "notify_party_name": {},
                    "bill_of_lading_date": {},
                    "dimension": {},
                    "transaction_currency": {},
                    "transaction_date": {},
                    "lc_ref_no": {},
                    "country_of_final_destination": {},
                    "consignee_name": {},
                    "invoice_amount": {},
                    "shipper_name": {},
                    "transaction_amount_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin_no": {},
                    "remitter_address": {},
                    "consignee_address": {},
                    "bill_of_lading_number": {},
                    "rate_per_unit": {},
                    "consignor_name": {},
                    "invoice_currency": {},
                    "pre_carriage_by": {},
                    "payment_terms_terms_of_delivery_&_payment": {},
                    "awb_date": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "1609flc230614_24.png": {
                "docClass": "BOL",
                "keys_extraction": {
                    "shipper_name": {
                        "value": "NT LIMITED",
                        "coordinate": [
                            [
                                152,
                                119,
                                186,
                                126
                            ]
                        ],
                        "model_confidence": [
                            99.9304
                        ]
                    },
                    "shipper_address": {
                        "value": "ROOM TSUL KOWLOON 903 95 KIMBERLEY  HOUSE 35 KIMBERLEY ROAD TSIM SHA",
                        "coordinate": [
                            [
                                65,
                                126,
                                267,
                                144
                            ]
                        ],
                        "model_confidence": [
                            99.94942061028263
                        ]
                    },
                    "consignee_name": {
                        "value": "THE AXIS BANK LIMITED , INDIA",
                        "coordinate": [
                            [
                                75,
                                180,
                                201,
                                187
                            ]
                        ],
                        "model_confidence": [
                            78.58239717851329
                        ]
                    },
                    "vessel_name": {
                        "value": "ALS CLIVIA IKE",
                        "coordinate": [
                            [
                                67,
                                244,
                                99,
                                250
                            ],
                            [
                                167,
                                378,
                                179,
                                384
                            ]
                        ],
                        "model_confidence": [
                            89.78709677419354,
                            97.29
                        ]
                    },
                    "carrier_name": {
                        "value": "MAERSK",
                        "coordinate": [
                            [
                                121,
                                71,
                                221,
                                89
                            ]
                        ],
                        "model_confidence": [
                            99.81
                        ]
                    },
                    "port_of_loading": {
                        "value": "XINGANG PORTCHINA",
                        "coordinate": [
                            [
                                66,
                                268,
                                130,
                                274
                            ]
                        ],
                        "model_confidence": [
                            89.02
                        ]
                    },
                    "goods_description": {
                        "value": "PVC GRADE SUSPENSION DG - 1000K RESIN",
                        "coordinate": [
                            [
                                70,
                                325,
                                154,
                                341
                            ]
                        ],
                        "model_confidence": [
                            95.7081932021467
                        ]
                    },
                    "freight_collect_or_prepaid": {
                        "value": "FREIGHT PREPAID",
                        "coordinate": [
                            [
                                73,
                                440,
                                133,
                                448
                            ]
                        ],
                        "model_confidence": [
                            99.78
                        ]
                    },
                    "voyage_number": {
                        "value": "327W",
                        "coordinate": [
                            [
                                170,
                                244,
                                187,
                                249
                            ]
                        ],
                        "model_confidence": [
                            99.97
                        ]
                    },
                    "port_of_discharge": {
                        "value": "MUNDRE PORT , INDIA",
                        "coordinate": [
                            [
                                171,
                                268,
                                218,
                                273
                            ]
                        ],
                        "model_confidence": [
                            99.72282608695652
                        ]
                    },
                    "bol_original_number": {
                        "value": "THREE",
                        "coordinate": [
                            [
                                81,
                                645,
                                103,
                                650
                            ]
                        ],
                        "model_confidence": [
                            99.92
                        ]
                    },
                    "country_of_origin": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                143,
                                423,
                                164,
                                429
                            ]
                        ],
                        "model_confidence": [
                            97.88
                        ]
                    },
                    "container_number": {
                        "value": "MRKU2596130 TRHU4828076 MRSUS880749 ML ML - - ML - CN1467971 CN1467976 MRKU6243130 MRSU3086581 ML - CN1468786 - CN1468845 CN1468838",
                        "coordinate": [
                            [
                                73,
                                475,
                                177,
                                519
                            ]
                        ],
                        "model_confidence": [
                            91.79770771682222
                        ]
                    },
                    "bill_of_lading_issue_date": {
                        "value": "20230712",
                        "coordinate": [
                            [
                                181,
                                636,
                                219,
                                645
                            ]
                        ],
                        "model_confidence": [
                            98.61
                        ]
                    },
                    "shipped_onboard_date": {
                        "value": "20230709",
                        "coordinate": [
                            [
                                181,
                                660,
                                219,
                                669
                            ]
                        ],
                        "model_confidence": [
                            99.95
                        ]
                    },
                    "gross_weight": {
                        "value": "282240.000 ",
                        "coordinate": [
                            [
                                381,
                                295,
                                437,
                                303
                            ]
                        ],
                        "model_confidence": [
                            99.92999999999999
                        ]
                    },
                    "bill_of_lading_number": {
                        "value": "228712925",
                        "coordinate": [
                            [
                                461,
                                101,
                                499,
                                107
                            ]
                        ],
                        "model_confidence": [
                            99.54
                        ]
                    },
                    "measurement_or_dimension": {
                        "value": "470.0000 CBM",
                        "coordinate": [
                            [
                                454,
                                294,
                                502,
                                302
                            ]
                        ],
                        "model_confidence": [
                            99.96
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                337,
                                693,
                                454,
                                739
                            ]
                        ],
                        "model_confidence": [
                            0.8094532489776611
                        ]
                    },
                    "is_stamp": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                456,
                                685,
                                517,
                                744
                            ]
                        ],
                        "model_confidence": [
                            0.7703148722648621
                        ]
                    },
                    "shipper_address_country": {
                        "value": "HONG KONG",
                        "coordinate": [
                            [
                                65,
                                126,
                                267,
                                144
                            ]
                        ],
                        "model_confidence": [
                            99.94942061028263
                        ]
                    },
                    "net_weight": {},
                    "bol_original_or_copy": {},
                    "page_no": {},
                    "lc_date": {},
                    "signed_By_agent": {},
                    "goods_marks_and_nos": {},
                    "transaction_date": {},
                    "signed_by_carrier": {},
                    "stamp": {},
                    "goods_quantity": {},
                    "signature": {},
                    "final_destination": {},
                    "lc_ref_number": {},
                    "notify_party_name": {},
                    "place_of_receipt": {},
                    "carrier_country": {},
                    "place_of_issue": {},
                    "agent_country": {},
                    "notify_party_address": {},
                    "pre_carriage_by": {},
                    "freight_collect_at": {},
                    "agent_name": {},
                    "consignee_address": {}
                },
                "status_code": "200"
            },
            "1609flc230614_25.png": {
                "docClass": "OTHERS",
                "keys_extraction": {}
            },
            "1609flc230614_26.png": {
                "docClass": "OTHERS",
                "keys_extraction": {}
            },
            "1609flc230614_27.png": {
                "docClass": "COO",
                "keys_extraction": {
                    "consignor_name": {
                        "value": "QUANGZHOU EXER BAYU TRADING CO .",
                        "coordinate": [
                            [
                                76,
                                59,
                                174,
                                74
                            ]
                        ],
                        "model_confidence": [
                            77.31278215491662
                        ]
                    },
                    "consignor_address": {
                        "value": "VIRSUNSHINE ROOM TSUE KOWLOON 10 KMBCHLEY INTERNATIONACENT  ROUSSEREY LEATED ROAD 18M SHA",
                        "coordinate": [
                            [
                                75,
                                72,
                                269,
                                94
                            ]
                        ],
                        "model_confidence": [
                            99.72120763485073
                        ]
                    },
                    "consignee_name": {
                        "value": "RESOLVINYLSAND CHLOROES LETED",
                        "coordinate": [
                            [
                                77,
                                131,
                                193,
                                140
                            ]
                        ],
                        "model_confidence": [
                            50.57008771929824
                        ]
                    },
                    "consignee_address": {
                        "value": "DEMAS FLOOR DUE TOWERS SY MARG",
                        "coordinate": [
                            [
                                76,
                                138,
                                231,
                                148
                            ]
                        ],
                        "model_confidence": [
                            82.22746605581557
                        ]
                    },
                    "from_place": {
                        "value": "PROM XINGANG PORT CHINA",
                        "coordinate": [
                            [
                                76,
                                197,
                                160,
                                205
                            ]
                        ],
                        "model_confidence": [
                            94.77397708674305
                        ]
                    },
                    "to_place": {
                        "value": "EW DELH TOMURORAPORTINDIA",
                        "coordinate": [
                            [
                                161,
                                137,
                                266,
                                204
                            ]
                        ],
                        "model_confidence": [
                            77.56356750823271
                        ]
                    },
                    "means_of_transport": {
                        "value": "BY SEA",
                        "coordinate": [
                            [
                                233,
                                196,
                                254,
                                203
                            ]
                        ],
                        "model_confidence": [
                            90.6
                        ]
                    },
                    "original_or_copy": {
                        "value": "ORIGINAL",
                        "coordinate": [
                            [
                                264,
                                31,
                                314,
                                41
                            ]
                        ],
                        "model_confidence": [
                            98.76
                        ]
                    },
                    "country_of_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                216,
                                459,
                                234,
                                466
                            ]
                        ],
                        "model_confidence": [
                            60.22
                        ]
                    },
                    "marks_and_no_of_packages": {
                        "value": "ELEVEN THOUSAND AND TWO HUNDRED 1200 ) BAGS",
                        "coordinate": [
                            [
                                158,
                                343,
                                315,
                                352
                            ]
                        ],
                        "model_confidence": [
                            98.8729602459589
                        ]
                    },
                    "description_of_goods": {
                        "value": "PV GRADE SUSPENSION DO RESP",
                        "coordinate": [
                            [
                                157,
                                364,
                                227,
                                384
                            ]
                        ],
                        "model_confidence": [
                            99.55668989547038
                        ]
                    },
                    "signature": {
                        "value": "FINA , AGTIFUNE ANC AMP JUL 05.2005 HOTTED",
                        "coordinate": [
                            [
                                117,
                                692,
                                248,
                                763
                            ]
                        ],
                        "model_confidence": [
                            72.14333333333333
                        ]
                    },
                    "certificate_no": {
                        "value": "2304401A150102017",
                        "coordinate": [
                            [
                                345,
                                59,
                                413,
                                71
                            ]
                        ],
                        "model_confidence": [
                            97.41
                        ]
                    },
                    "coo_issuer_address": {
                        "value": "THE PEOPLES REPUBLIC OF ",
                        "coordinate": [
                            [
                                367,
                                133,
                                504,
                                147
                            ]
                        ],
                        "model_confidence": [
                            99.79423769507804
                        ]
                    },
                    "certificate_stamped": {
                        "value": "HEREBY COM DECLARATION RES CHINA OF COUNCIL INTERNATIONAL FOR THE PROMOTION GUANGZHOU TRADE ADDRE FAX GUANGZHO : 020-04803431 TEL : 00064000421",
                        "coordinate": [
                            [
                                291,
                                616,
                                431,
                                731
                            ]
                        ],
                        "model_confidence": [
                            94.73425932188853
                        ]
                    },
                    "invoice_no": {
                        "value": "SSIPL - 23148",
                        "coordinate": [
                            [
                                450,
                                341,
                                485,
                                348
                            ]
                        ],
                        "model_confidence": [
                            99.68
                        ]
                    },
                    "invoice_date": {
                        "value": "JUL 05.2023",
                        "coordinate": [
                            [
                                450,
                                348,
                                483,
                                354
                            ]
                        ],
                        "model_confidence": [
                            99.57
                        ]
                    },
                    "is_signed": {},
                    "is_stamp": {
                        "value": "TRUE TRUE",
                        "coordinate": [
                            [
                                100,
                                654,
                                190,
                                748
                            ],
                            [
                                291,
                                619,
                                437,
                                728
                            ]
                        ],
                        "model_confidence": [
                            0.8470067381858826,
                            0.8834928274154663
                        ]
                    },
                    "consignor_address_country": {
                        "value": "HONG KONG",
                        "coordinate": [
                            [
                                75,
                                72,
                                269,
                                94
                            ]
                        ],
                        "model_confidence": [
                            99.72120763485073
                        ]
                    },
                    "coo_issuer_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                367,
                                133,
                                504,
                                147
                            ]
                        ],
                        "model_confidence": [
                            99.79423769507804
                        ]
                    },
                    "vessel_details": {},
                    "declaration_by_exporter": {},
                    "original_number": {},
                    "lc_date": {},
                    "declaration_by_certification": {},
                    "ref_no": {},
                    "coo_issuer_name": {},
                    "lc_ref_no": {},
                    "issue_date": {},
                    "page_no": {},
                    "gross_weight": {},
                    "net_weight": {},
                    "final_destination": {}
                },
                "status_code": "200"
            },
            "1609flc230614_28.png": {
                "docClass": "COA",
                "keys_extraction": {}
            },
            "1609flc230614_29.png": {
                "docClass": "IC",
                "keys_extraction": {
                    "policy_no": {
                        "value": "PCB020001231100001135 11153009902094770747 3703001000004",
                        "coordinate": [
                            [
                                74,
                                114,
                                183,
                                122
                            ],
                            [
                                113,
                                228,
                                190,
                                237
                            ],
                            [
                                413,
                                710,
                                486,
                                715
                            ]
                        ],
                        "model_confidence": [
                            25.27,
                            99.64,
                            99.05
                        ]
                    },
                    "vessel_or_flight_name": {
                        "value": "QIVIA",
                        "coordinate": [
                            [
                                128,
                                266,
                                153,
                                278
                            ]
                        ],
                        "model_confidence": [
                            73.1
                        ]
                    },
                    "vessel_or_flight_number": {
                        "value": "327",
                        "coordinate": [
                            [
                                155,
                                265,
                                169,
                                275
                            ]
                        ],
                        "model_confidence": [
                            97.83
                        ]
                    },
                    "subject_matter_insured": {
                        "value": "PIC SUSPENSION RESIN ARE OF CHINA ORIGIN",
                        "coordinate": [
                            [
                                74,
                                358,
                                187,
                                453
                            ]
                        ],
                        "model_confidence": [
                            89.53604060820571
                        ]
                    },
                    "from_place": {
                        "value": "XINGANG PORT , CHINA",
                        "coordinate": [
                            [
                                204,
                                285,
                                276,
                                293
                            ]
                        ],
                        "model_confidence": [
                            99.8760294117647
                        ]
                    },
                    "to_place": {
                        "value": "MUNDRA PORT , INDIA",
                        "coordinate": [
                            [
                                204,
                                305,
                                273,
                                313
                            ]
                        ],
                        "model_confidence": [
                            99.89883578214432
                        ]
                    },
                    "sum_insured_amount": {
                        "value": "USD237,160.00",
                        "coordinate": [
                            [
                                114,
                                327,
                                164,
                                336
                            ]
                        ],
                        "model_confidence": [
                            99.08
                        ]
                    },
                    "claim payable_by_name": {
                        "value": "A IN VANWAY - GLADSTONE BOHUA CHEMICAL DEVELOPMENT",
                        "coordinate": [
                            [
                                317,
                                225,
                                390,
                                248
                            ],
                            [
                                160,
                                425,
                                261,
                                434
                            ]
                        ],
                        "model_confidence": [
                            79.99918367346939,
                            64.87183281733746
                        ]
                    },
                    "issue_date": {
                        "value": "JUL 05 , 2023",
                        "coordinate": [
                            [
                                102,
                                601,
                                148,
                                608
                            ]
                        ],
                        "model_confidence": [
                            95.31313497822931
                        ]
                    },
                    "claim_payable_in": {
                        "value": "INDIA IN USD",
                        "coordinate": [
                            [
                                342,
                                225,
                                388,
                                233
                            ]
                        ],
                        "model_confidence": [
                            70.29285714285713
                        ]
                    },
                    "signature": {
                        "value": "DENGAN",
                        "coordinate": [
                            [
                                296,
                                681,
                                318,
                                686
                            ]
                        ],
                        "model_confidence": [
                            35.96
                        ]
                    },
                    "insurance_issuer_address": {
                        "value": "PINAN INSURANCE PROPERTY DENT & CABALTY",
                        "coordinate": [
                            [
                                412,
                                71,
                                482,
                                87
                            ]
                        ],
                        "model_confidence": [
                            81.17
                        ]
                    },
                    "claim_payable_by_address": {
                        "value": "KOLKATA 1A JANKI 700022 SHAH RD , HASTINGS",
                        "coordinate": [
                            [
                                330,
                                248,
                                450,
                                268
                            ]
                        ],
                        "model_confidence": [
                            69.31121784840094
                        ]
                    },
                    "address_of_assured": {
                        "value": ", INDIA",
                        "coordinate": [
                            [
                                382,
                                259,
                                409,
                                267
                            ]
                        ],
                        "model_confidence": [
                            65.07499999999999
                        ]
                    },
                    "original_Number": {
                        "value": "2",
                        "coordinate": [
                            [
                                476,
                                598,
                                483,
                                608
                            ]
                        ],
                        "model_confidence": [
                            98.64
                        ]
                    },
                    "insurance_issuer_address_bottom": {
                        "value": "DISTRICT RODI 1401 , QINGDAO 1402 , BUILINGO.28 , SHANDONG , CHINA , MINOLING RUU , 12 STUNDA",
                        "coordinate": [
                            [
                                256,
                                719,
                                452,
                                737
                            ]
                        ],
                        "model_confidence": [
                            85.27753731856284
                        ]
                    },
                    "is_signed": {
                        "value": "",
                        "coordinate": [],
                        "model_confidence": []
                    },
                    "is_stamp": {
                        "value": "",
                        "coordinate": [],
                        "model_confidence": []
                    },
                    "start_date": {},
                    "certificate_Stamped": {},
                    "sail_on_or_about_to_date": {},
                    "declaration_by": {},
                    "country_of_origin_origin_of_goods": {},
                    "original_copy": {},
                    "name_of_assured": {},
                    "conditions_of_coverage": {},
                    "expiry_date": {},
                    "premium": {},
                    "lc_date": {},
                    "page_no": {},
                    "insurance_issuer_name": {},
                    "certificate_no": {},
                    "lc_ref_no": {},
                    "insurance_issuer_name_bottom": {},
                    "mode_of_transport": {},
                    "sum_insured_currency": {}
                },
                "status_code": "200"
            },
            "1609flc230614_30.png": {
                "docClass": "PL",
                "keys_extraction": {
                    "invoice_no": {
                        "value": "SSIPL - 23149 23073",
                        "coordinate": [
                            [
                                137,
                                182,
                                181,
                                213
                            ]
                        ],
                        "model_confidence": [
                            85.02242990654207
                        ]
                    },
                    "date_of_invoice": {
                        "value": "05 JULY 2023 05 JULY 2023",
                        "coordinate": [
                            [
                                137,
                                195,
                                471,
                                205
                            ]
                        ],
                        "model_confidence": [
                            99.5970652173913
                        ]
                    },
                    "shipper_name": {
                        "value": "INTERNATIONAL",
                        "coordinate": [
                            [
                                214,
                                98,
                                342,
                                113
                            ]
                        ],
                        "model_confidence": [
                            53.95
                        ]
                    },
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "PVT LIMITED",
                        "coordinate": [
                            [
                                347,
                                100,
                                446,
                                114
                            ]
                        ],
                        "model_confidence": [
                            82.49733333333333
                        ]
                    },
                    "beneficiary_address": {
                        "value": "ROOM 903 TSIM 9 F SHA KIMBERLEY TSUI KOWLOON HOUSE 35 HONG KIMBERLEY KONG ROAD",
                        "coordinate": [
                            [
                                161,
                                116,
                                389,
                                136
                            ]
                        ],
                        "model_confidence": [
                            99.82917450728844
                        ]
                    },
                    "original_copy": {
                        "value": "ORIGINAL",
                        "coordinate": [
                            [
                                412,
                                117,
                                485,
                                136
                            ]
                        ],
                        "model_confidence": [
                            99.61
                        ]
                    },
                    "description_of_goods": {
                        "value": "RESOL VINYLS AND CHLORIDES LIMITED PVC GRADE SUSPENSION SG5 RESIN",
                        "coordinate": [
                            [
                                137,
                                219,
                                293,
                                347
                            ]
                        ],
                        "model_confidence": [
                            93.94063643911437
                        ]
                    },
                    "consignor_address": {
                        "value": "DSM SHIVAJI 321 MARG 3RD FLOOR NEW DELHI DLF TOWERS 110015 ",
                        "coordinate": [
                            [
                                138,
                                231,
                                295,
                                254
                            ]
                        ],
                        "model_confidence": [
                            92.99
                        ]
                    },
                    "port_of_loading": {
                        "value": "QINGDAO PORT ",
                        "coordinate": [
                            [
                                137,
                                256,
                                228,
                                263
                            ]
                        ],
                        "model_confidence": [
                            99.72295454545454
                        ]
                    },
                    "port_of_discharge": {
                        "value": "MUNDRA PORT , INDIA",
                        "coordinate": [
                            [
                                137,
                                267,
                                222,
                                275
                            ]
                        ],
                        "model_confidence": [
                            99.944578313253
                        ]
                    },
                    "country_of_origin_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                215,
                                465,
                                239,
                                472
                            ]
                        ],
                        "model_confidence": [
                            98.89
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "11200 ",
                        "coordinate": [
                            [
                                139,
                                528,
                                182,
                                535
                            ]
                        ],
                        "model_confidence": [
                            99.7
                        ]
                    },
                    "net_weight": {
                        "value": "280,000 282,240 280,000 ",
                        "coordinate": [
                            [
                                154,
                                527,
                                437,
                                574
                            ]
                        ],
                        "model_confidence": [
                            77.5775
                        ]
                    },
                    "gross_weight": {
                        "value": "282,240 ",
                        "coordinate": [
                            [
                                155,
                                578,
                                198,
                                587
                            ]
                        ],
                        "model_confidence": [
                            99.67
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                401,
                                616,
                                452,
                                637
                            ]
                        ],
                        "model_confidence": [
                            0.6284654140472412
                        ]
                    },
                    "is_stamp": {},
                    "consignor_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                138,
                                231,
                                295,
                                254
                            ]
                        ],
                        "model_confidence": [
                            92.99
                        ]
                    },
                    "port_of_loading_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                137,
                                256,
                                228,
                                263
                            ]
                        ],
                        "model_confidence": [
                            99.72295454545454
                        ]
                    },
                    "shipper_address": {},
                    "lc_date": {},
                    "notify_party_address": {},
                    "awb_number": {},
                    "vessel_flight_no": {},
                    "track_reference": {},
                    "declaration": {},
                    "notify_party_name": {},
                    "bill_of_lading_date": {},
                    "dimension": {},
                    "transaction_currency": {},
                    "transaction_date": {},
                    "lc_ref_no": {},
                    "country_of_final_destination": {},
                    "consignee_name": {},
                    "invoice_amount": {},
                    "transaction_amount_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin_no": {},
                    "remitter_address": {},
                    "consignee_address": {},
                    "bill_of_lading_number": {},
                    "rate_per_unit": {},
                    "consignor_name": {},
                    "invoice_currency": {},
                    "pre_carriage_by": {},
                    "payment_terms_terms_of_delivery_&_payment": {},
                    "incoterm": {},
                    "awb_date": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "1609flc230614_31.png": {
                "docClass": "CI",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "INTERNATIONAL PVT LIMITED",
                        "coordinate": [
                            [
                                229,
                                81,
                                471,
                                96
                            ]
                        ],
                        "model_confidence": [
                            99.90000000000002
                        ]
                    },
                    "beneficiary_address": {
                        "value": "ROOM 903 TSIM 9 F SHA KIMBERLEY TSUI KOWLOON HOUSE 35 HONG KIMBERLEY KONG ROAD COMMERCIAL",
                        "coordinate": [
                            [
                                175,
                                101,
                                410,
                                155
                            ]
                        ],
                        "model_confidence": [
                            85.73465879653082
                        ]
                    },
                    "signature_of_the_issuer": {
                        "value": "ORIGINAL DRINKIN",
                        "coordinate": [
                            [
                                438,
                                99,
                                513,
                                122
                            ],
                            [
                                416,
                                616,
                                457,
                                629
                            ]
                        ],
                        "model_confidence": [
                            94.23,
                            94.59
                        ]
                    },
                    "cosignee_name": {
                        "value": "RESOL VINYLS AND CHLORIDES LIMITED",
                        "coordinate": [
                            [
                                130,
                                171,
                                291,
                                178
                            ]
                        ],
                        "model_confidence": [
                            99.64470325793732
                        ]
                    },
                    "consignee_address": {
                        "value": "DSM SHIVAJI 321 MARG 3RD FLOOR NEW DELHI DLF TOWERS 110015 ",
                        "coordinate": [
                            [
                                130,
                                183,
                                292,
                                204
                            ]
                        ],
                        "model_confidence": [
                            99.75
                        ]
                    },
                    "invoice_no": {
                        "value": "SSIPL - 23149 23073",
                        "coordinate": [
                            [
                                129,
                                208,
                                174,
                                239
                            ]
                        ],
                        "model_confidence": [
                            94.08872483221478
                        ]
                    },
                    "date_of_invoice": {
                        "value": "05-07-2023",
                        "coordinate": [
                            [
                                130,
                                221,
                                180,
                                227
                            ]
                        ],
                        "model_confidence": [
                            94.13562499999999
                        ]
                    },
                    "port_of_loading": {
                        "value": "QINGDAO PORT ",
                        "coordinate": [
                            [
                                130,
                                245,
                                223,
                                253
                            ]
                        ],
                        "model_confidence": [
                            99.36428571428573
                        ]
                    },
                    "port_of_discharge": {
                        "value": "MUNDRA PORT , INDIA",
                        "coordinate": [
                            [
                                130,
                                258,
                                218,
                                265
                            ]
                        ],
                        "model_confidence": [
                            99.39689655172413
                        ]
                    },
                    "goods_description": {
                        "value": "PVC SUSPENSION RESIN",
                        "coordinate": [
                            [
                                131,
                                316,
                                224,
                                323
                            ]
                        ],
                        "model_confidence": [
                            99.78807858807859
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "280   280.00 ",
                        "coordinate": [
                            [
                                150,
                                315,
                                384,
                                360
                            ]
                        ],
                        "model_confidence": [
                            87.55093793273986
                        ]
                    },
                    "rate_per_unit": {
                        "value": "770.00 770.00",
                        "coordinate": [
                            [
                                221,
                                315,
                                427,
                                360
                            ]
                        ],
                        "model_confidence": [
                            80.58500000000001
                        ]
                    },
                    "country_of_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                211,
                                452,
                                235,
                                460
                            ]
                        ],
                        "model_confidence": [
                            94.76
                        ]
                    },
                    "incoterm": {
                        "value": "ZHONG GU JI NAN ",
                        "coordinate": [
                            [
                                130,
                                490,
                                204,
                                500
                            ]
                        ],
                        "model_confidence": [
                            57.166666666666664
                        ]
                    },
                    "vessel_flight_no": {
                        "value": "23002W",
                        "coordinate": [
                            [
                                203,
                                489,
                                231,
                                500
                            ]
                        ],
                        "model_confidence": [
                            71.98
                        ]
                    },
                    "lc_ref_no": {
                        "value": "1609FLC230614",
                        "coordinate": [
                            [
                                202,
                                592,
                                258,
                                602
                            ]
                        ],
                        "model_confidence": [
                            94.53
                        ]
                    },
                    "invoice_currency": {
                        "value": "",
                        "coordinate": [
                            [
                                451,
                                515,
                                469,
                                524
                            ]
                        ],
                        "model_confidence": [
                            98.78
                        ]
                    },
                    "invoice_amount": {
                        "value": "215,600.00",
                        "coordinate": [
                            [
                                475,
                                515,
                                515,
                                524
                            ]
                        ],
                        "model_confidence": [
                            76.94
                        ]
                    },
                    "invoice_amount_in_words": {
                        "value": "TWO HUNDRED FIFTEEN THOUSAND AND SIX HUNDRED ONLY .",
                        "coordinate": [
                            [
                                234,
                                553,
                                481,
                                564
                            ]
                        ],
                        "model_confidence": [
                            99.55219933769011
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                415,
                                615,
                                479,
                                636
                            ]
                        ],
                        "model_confidence": [
                            0.7165550589561462
                        ]
                    },
                    "is_stamp": {},
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                130,
                                183,
                                292,
                                204
                            ]
                        ],
                        "model_confidence": [
                            99.75
                        ]
                    },
                    "port_of_loading_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                130,
                                245,
                                223,
                                253
                            ]
                        ],
                        "model_confidence": [
                            99.36428571428573
                        ]
                    },
                    "consignor_name": {},
                    "beneficiary_bank_country": {},
                    "transaction_currency": {},
                    "transaction_amonunt_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin": {},
                    "bill_of_lading_date": {},
                    "invoice_tax_ccy": {},
                    "consignee_country": {},
                    "tenor_indicator": {},
                    "net_weight": {},
                    "notify_party_country": {},
                    "indicator_type": {},
                    "hs_code_no": {},
                    "declaration_by_issuer": {},
                    "invoice_due_date": {},
                    "country_of_final_destination": {},
                    "indicator_date": {},
                    "invoice_discount_amount": {},
                    "shipper_address": {},
                    "consignor_country": {},
                    "invoice_discount_ccy": {},
                    "usance_tenor": {},
                    "tenor_type": {},
                    "awb_date": {},
                    "delivery_terms": {},
                    "gross_weight": {},
                    "consignor_address": {},
                    "beneficiary_iban_number": {},
                    "transaction_date": {},
                    "beneficiary_account_number": {},
                    "pre-carriage-by": {},
                    "bill_of_lading_no": {},
                    "lc_date": {},
                    "invoice_tax_amount": {},
                    "notify_party_name": {},
                    "original_or_copy": {},
                    "notify_party_address": {},
                    "beneficiary_bank_identifier": {},
                    "awb_number": {},
                    "page_no": {},
                    "remitter_address": {},
                    "shipper_name": {},
                    "beneficiary_bank_name": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "1609flc230614_32.png": {
                "docClass": "BOL",
                "keys_extraction": {
                    "carrier_name": {
                        "value": "TT.S. LINES",
                        "coordinate": [
                            [
                                97,
                                82,
                                205,
                                102
                            ]
                        ],
                        "model_confidence": [
                            98.76
                        ]
                    },
                    "shipper_name": {
                        "value": "INTERNATIONAL PVT LIMITED",
                        "coordinate": [
                            [
                                126,
                                127,
                                217,
                                135
                            ]
                        ],
                        "model_confidence": [
                            99.20493392070485
                        ]
                    },
                    "shipper_address": {
                        "value": "ROOM KIMBERLEY 903 SF ROAD KIMBERLEY  TSIM SHA HOUSE TSU 35 KOWLOON",
                        "coordinate": [
                            [
                                89,
                                137,
                                210,
                                162
                            ]
                        ],
                        "model_confidence": [
                            99.98
                        ]
                    },
                    "consignee_name": {
                        "value": "AXIS BANK LIMITED",
                        "coordinate": [
                            [
                                151,
                                182,
                                212,
                                188
                            ]
                        ],
                        "model_confidence": [
                            99.91666666666667
                        ]
                    },
                    "consignee_address": {
                        "value": "",
                        "coordinate": [
                            [
                                90,
                                190,
                                107,
                                199
                            ]
                        ],
                        "model_confidence": [
                            99.35
                        ]
                    },
                    "notify_party_name": {
                        "value": "1.0WS WAREHOUSE SERVICES LLP",
                        "coordinate": [
                            [
                                90,
                                249,
                                204,
                                256
                            ]
                        ],
                        "model_confidence": [
                            98.77687216553288
                        ]
                    },
                    "notify_party_address": {
                        "value": "SURVEY DHRUVE NO DIST MITAP 160 KUTCH ROAD SECTOR APSEZ VILLAGE GUJARAT 370421 MUNDRA ",
                        "coordinate": [
                            [
                                90,
                                260,
                                214,
                                284
                            ]
                        ],
                        "model_confidence": [
                            99.95
                        ]
                    },
                    "place_of_receipt": {
                        "value": "QINGDAO PORT , INDIA",
                        "coordinate": [
                            [
                                92,
                                330,
                                164,
                                337
                            ]
                        ],
                        "model_confidence": [
                            99.91916478555305
                        ]
                    },
                    "port_of_discharge": {
                        "value": "QINGDAO PORT , INDIA MUNDRA PORT , INDIA",
                        "coordinate": [
                            [
                                92,
                                332,
                                341,
                                357
                            ]
                        ],
                        "model_confidence": [
                            94.3128550420168
                        ]
                    },
                    "freight_collect_at": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                123,
                                691,
                                143,
                                697
                            ]
                        ],
                        "model_confidence": [
                            89.37
                        ]
                    },
                    "vessel_name": {
                        "value": "ZHONG GU JINAN",
                        "coordinate": [
                            [
                                317,
                                219,
                                374,
                                224
                            ]
                        ],
                        "model_confidence": [
                            99.98
                        ]
                    },
                    "final_destination": {
                        "value": "MUNDRA PORT , INDIA",
                        "coordinate": [
                            [
                                270,
                                351,
                                339,
                                357
                            ]
                        ],
                        "model_confidence": [
                            99.93
                        ]
                    },
                    "goods_description": {
                        "value": "11200 BAGS SAID TO CONTAIN",
                        "coordinate": [
                            [
                                227,
                                405,
                                334,
                                414
                            ]
                        ],
                        "model_confidence": [
                            78.32082889703852
                        ]
                    },
                    "agent_country": {
                        "value": "RIDDHI UNIT GANDHIDHAM NO.208 SIDDHI , SECOND ARCADE , FLOOR BUILDING - , SECTOR , GUJARAT 370201 - 8 , PLOT NO . 13",
                        "coordinate": [
                            [
                                318,
                                258,
                                492,
                                284
                            ]
                        ],
                        "model_confidence": [
                            98.74643576668767
                        ]
                    },
                    "bol_original_number": {
                        "value": "THREECH",
                        "coordinate": [
                            [
                                283,
                                713,
                                314,
                                721
                            ]
                        ],
                        "model_confidence": [
                            48.86
                        ]
                    },
                    "bill_of_lading_number": {
                        "value": "709310223512",
                        "coordinate": [
                            [
                                451,
                                129,
                                494,
                                135
                            ]
                        ],
                        "model_confidence": [
                            96.76
                        ]
                    },
                    "voyage_number": {
                        "value": "23002W",
                        "coordinate": [
                            [
                                467,
                                217,
                                490,
                                223
                            ]
                        ],
                        "model_confidence": [
                            99.98
                        ]
                    },
                    "gross_weight": {
                        "value": "2",
                        "coordinate": [
                            [
                                389,
                                378,
                                442,
                                386
                            ]
                        ],
                        "model_confidence": [
                            99.86
                        ]
                    },
                    "measurement_or_dimension": {
                        "value": "400.00000CBM",
                        "coordinate": [
                            [
                                469,
                                377,
                                512,
                                385
                            ]
                        ],
                        "model_confidence": [
                            99.94
                        ]
                    },
                    "bol_original_or_copy": {
                        "value": "ORIGINAL",
                        "coordinate": [
                            [
                                420,
                                520,
                                504,
                                532
                            ]
                        ],
                        "model_confidence": [
                            99.87
                        ]
                    },
                    "place_of_issue": {
                        "value": "QINGDAO , CHINA QINGDAO",
                        "coordinate": [
                            [
                                369,
                                688,
                                453,
                                719
                            ]
                        ],
                        "model_confidence": [
                            79.84267441860464
                        ]
                    },
                    "signed_by_carrier": {
                        "value": "DHR RANCH AGENCY",
                        "coordinate": [
                            [
                                448,
                                701,
                                496,
                                737
                            ]
                        ],
                        "model_confidence": [
                            96.38
                        ]
                    },
                    "is_signed": {
                        "value": "",
                        "coordinate": [],
                        "model_confidence": []
                    },
                    "is_stamp": {
                        "value": "",
                        "coordinate": [],
                        "model_confidence": []
                    },
                    "shipper_address_country": {
                        "value": "HONG KONG",
                        "coordinate": [
                            [
                                89,
                                137,
                                210,
                                162
                            ]
                        ],
                        "model_confidence": [
                            99.98
                        ]
                    },
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                90,
                                190,
                                107,
                                199
                            ]
                        ],
                        "model_confidence": [
                            99.35
                        ]
                    },
                    "notify_party_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                90,
                                260,
                                214,
                                284
                            ]
                        ],
                        "model_confidence": [
                            99.95
                        ]
                    },
                    "country_of_origin": {},
                    "net_weight": {},
                    "freight_collect_or_prepaid": {},
                    "bill_of_lading_issue_date": {},
                    "page_no": {},
                    "lc_date": {},
                    "signed_By_agent": {},
                    "goods_marks_and_nos": {},
                    "transaction_date": {},
                    "stamp": {},
                    "goods_quantity": {},
                    "container_number": {},
                    "signature": {},
                    "lc_ref_number": {},
                    "carrier_country": {},
                    "pre_carriage_by": {},
                    "port_of_loading": {},
                    "agent_name": {},
                    "shipped_onboard_date": {}
                },
                "status_code": "200"
            },
            "1609flc230614_33.png": {
                "docClass": "OTHERS",
                "keys_extraction": {}
            },
            "1609flc230614_34.png": {
                "docClass": "COA",
                "keys_extraction": {}
            },
            "1609flc230614_35.png": {
                "docClass": "COO",
                "keys_extraction": {
                    "consignor_name": {
                        "value": "VASUN GUANGZHOU SHINE BAYU INTERNATIONAL TRADING",
                        "coordinate": [
                            [
                                73,
                                72,
                                167,
                                85
                            ]
                        ],
                        "model_confidence": [
                            99.33
                        ]
                    },
                    "consignor_address": {
                        "value": "ROOMKIMBERLEY QUANGZHOU CHA TSUL KOWLOON  HOUSELEDAD TOM SHA",
                        "coordinate": [
                            [
                                74,
                                69,
                                274,
                                98
                            ]
                        ],
                        "model_confidence": [
                            99.87339608242178
                        ]
                    },
                    "description_of_goods": {
                        "value": "RESOLVINYLS AND CHLORIDE~PVC GRADE SUSPENSION DES RES~",
                        "coordinate": [
                            [
                                75,
                                138,
                                166,
                                144
                            ]
                        ],
                        "model_confidence": [
                            97.39131247591479
                        ]
                    },
                    "consignee_address": {
                        "value": "DSM 15  321 3RD FLOOR DER",
                        "coordinate": [
                            [
                                77,
                                145,
                                154,
                                156
                            ]
                        ],
                        "model_confidence": [
                            95.3925003686337
                        ]
                    },
                    "from_place": {
                        "value": "GINGDAO PORT , CHINA INDIA",
                        "coordinate": [
                            [
                                75,
                                203,
                                165,
                                294
                            ]
                        ],
                        "model_confidence": [
                            98.5243438914027
                        ]
                    },
                    "certificate_stamped": {
                        "value": "CHINA OF COUNCIL INTERNATIONAL FOR THE PROMOTION GUANGZHO TRADE FAX : 020-64003431 ROZON",
                        "coordinate": [
                            [
                                119,
                                672,
                                447,
                                735
                            ]
                        ],
                        "model_confidence": [
                            79.47655159830683
                        ]
                    },
                    "to_place": {
                        "value": "RSPORT , INDIA",
                        "coordinate": [
                            [
                                196,
                                203,
                                242,
                                209
                            ]
                        ],
                        "model_confidence": [
                            99.19652173913043
                        ]
                    },
                    "means_of_transport": {
                        "value": "SEA",
                        "coordinate": [
                            [
                                253,
                                203,
                                264,
                                209
                            ]
                        ],
                        "model_confidence": [
                            99.14
                        ]
                    },
                    "original_or_copy": {
                        "value": "ORIGINAL",
                        "coordinate": [
                            [
                                267,
                                41,
                                320,
                                48
                            ]
                        ],
                        "model_confidence": [
                            98.77
                        ]
                    },
                    "marks_and_no_of_packages": {
                        "value": "ELEVEN THOUSAND AND TWO HUNDRED ( 110 ) BAGS",
                        "coordinate": [
                            [
                                163,
                                348,
                                324,
                                356
                            ]
                        ],
                        "model_confidence": [
                            98.54018637797614
                        ]
                    },
                    "certificate_no": {
                        "value": "2304401A180102016",
                        "coordinate": [
                            [
                                351,
                                67,
                                420,
                                79
                            ]
                        ],
                        "model_confidence": [
                            98.48
                        ]
                    },
                    "signature": {
                        "value": "PENTING AUTHO SAMP OF THORIZED",
                        "coordinate": [
                            [
                                178,
                                760,
                                480,
                                768
                            ]
                        ],
                        "model_confidence": [
                            51.11785166240409
                        ]
                    },
                    "coo_issuer_address": {
                        "value": "THE PEOPLES REPUBLIC OF ",
                        "coordinate": [
                            [
                                375,
                                141,
                                514,
                                152
                            ]
                        ],
                        "model_confidence": [
                            99.77421701803631
                        ]
                    },
                    "page_no": {
                        "value": "1",
                        "coordinate": [
                            [
                                300,
                                774,
                                315,
                                779
                            ]
                        ],
                        "model_confidence": [
                            98.77
                        ]
                    },
                    "gross_weight": {
                        "value": "2",
                        "coordinate": [
                            [
                                404,
                                357,
                                436,
                                366
                            ]
                        ],
                        "model_confidence": [
                            99.4
                        ]
                    },
                    "net_weight": {
                        "value": "2",
                        "coordinate": [
                            [
                                405,
                                378,
                                433,
                                385
                            ]
                        ],
                        "model_confidence": [
                            98.18
                        ]
                    },
                    "invoice_no": {
                        "value": "SSIPL - 2314",
                        "coordinate": [
                            [
                                464,
                                345,
                                495,
                                352
                            ]
                        ],
                        "model_confidence": [
                            99.68
                        ]
                    },
                    "invoice_date": {
                        "value": "JULTS 2023",
                        "coordinate": [
                            [
                                463,
                                351,
                                497,
                                358
                            ]
                        ],
                        "model_confidence": [
                            99.55
                        ]
                    },
                    "issue_date": {
                        "value": "JUL05.2023",
                        "coordinate": [
                            [
                                412,
                                743,
                                448,
                                752
                            ]
                        ],
                        "model_confidence": [
                            62.24
                        ]
                    },
                    "is_signed": {},
                    "is_stamp": {
                        "value": "TRUE TRUE",
                        "coordinate": [
                            [
                                113,
                                656,
                                207,
                                752
                            ],
                            [
                                304,
                                623,
                                459,
                                732
                            ]
                        ],
                        "model_confidence": [
                            0.8679823279380798,
                            0.9208887219429016
                        ]
                    },
                    "consignor_address_country": {
                        "value": "HONG KONG",
                        "coordinate": [
                            [
                                74,
                                69,
                                274,
                                98
                            ]
                        ],
                        "model_confidence": [
                            99.87339608242178
                        ]
                    },
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                77,
                                145,
                                154,
                                156
                            ]
                        ],
                        "model_confidence": [
                            95.3925003686337
                        ]
                    },
                    "coo_issuer_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                375,
                                141,
                                514,
                                152
                            ]
                        ],
                        "model_confidence": [
                            99.77421701803631
                        ]
                    },
                    "vessel_details": {},
                    "country_of_origin_of_goods": {},
                    "declaration_by_exporter": {},
                    "original_number": {},
                    "consignee_name": {},
                    "lc_date": {},
                    "declaration_by_certification": {},
                    "ref_no": {},
                    "coo_issuer_name": {},
                    "lc_ref_no": {},
                    "final_destination": {}
                },
                "status_code": "200"
            }
        }}
    
	PDF_2_EX = {"extraction_result": {"0041FLC210044_1.png": {

                "docClass": "Checklist",
                "keys_extraction": {}
            },
            "0041FLC210044_2.png": {
                "docClass": "LC",
                "keys_extraction": {}
            },
            "0041FLC210044_3.png": {
                "docClass": "LC",
                "keys_extraction": {}
            },
            "0041FLC210044_4.png": {
                "docClass": "OTHERS",
                "keys_extraction": {}
            },
            "0041FLC210044_5.png": {
                "docClass": "CS",
                "keys_extraction": {
                    "drawee_bank_name": {
                        "value": "AXIS BANK LTD",
                        "coordinate": [
                            [
                                48,
                                134,
                                122,
                                141
                            ]
                        ],
                        "model_confidence": [
                            99.9
                        ]
                    },
                    "drawee_bank_address": {
                        "value": "SCO CHANDIGARH 343344 SECTOR 160022 35  B",
                        "coordinate": [
                            [
                                48,
                                146,
                                181,
                                165
                            ]
                        ],
                        "model_confidence": [
                            99.26736867088609
                        ]
                    },
                    "document_enclosed": {
                        "value": "INVOICE 1ST 2ND DOCUMENT 1ST 2ND DOCUMENT 2/2 DRAFT 6 COMMERCIAL INVOICE ISET AIRWAY 1 2C CERTIFICATE BILLS OF ORIGIN PACKING LIST ",
                        "coordinate": [
                            [
                                48,
                                275,
                                496,
                                402
                            ]
                        ],
                        "model_confidence": [
                            98.93540588105435
                        ]
                    },
                    "drawer_bank_name": {
                        "value": "INDUSTRIAL CHINA HANGZHOU AND COMMERCIAL BRANCH BANK OF",
                        "coordinate": [
                            [
                                362,
                                39,
                                524,
                                54
                            ]
                        ],
                        "model_confidence": [
                            93.7224340175953
                        ]
                    },
                    "drawer_bank_address": {
                        "value": "3 F NO4 HUANCHENGBEJ ROAD ZHEJIANG ",
                        "coordinate": [
                            [
                                362,
                                57,
                                525,
                                72
                            ]
                        ],
                        "model_confidence": [
                            89.58721282657453
                        ]
                    },
                    "drawer_bank_bic": {
                        "value": "ICBKCNBIZ.JP",
                        "coordinate": [
                            [
                                389,
                                76,
                                439,
                                82
                            ]
                        ],
                        "model_confidence": [
                            99.29
                        ]
                    },
                    "csh_presentation_date": {
                        "value": "11-01-2022",
                        "coordinate": [
                            [
                                395,
                                121,
                                440,
                                130
                            ]
                        ],
                        "model_confidence": [
                            99.87
                        ]
                    },
                    "csh_ref_no": {
                        "value": "BP33221C10637901",
                        "coordinate": [
                            [
                                289,
                                194,
                                375,
                                205
                            ]
                        ],
                        "model_confidence": [
                            97.61
                        ]
                    },
                    "csh_bill_currency": {
                        "value": "USD,FLC,",
                        "coordinate": [
                            [
                                289,
                                216,
                                307,
                                225
                            ]
                        ],
                        "model_confidence": [
                            76.48
                        ]
                    },
                    "csh_bill_amount": {
                        "value": "42,250,00,0041210044,",
                        "coordinate": [
                            [
                                311,
                                216,
                                351,
                                225
                            ]
                        ],
                        "model_confidence": [
                            75.725
                        ]
                    },
                    "currency_amount": {
                        "value": "0041FLC210044",
                        "coordinate": [
                            [
                                289,
                                227,
                                356,
                                235
                            ]
                        ],
                        "model_confidence": [
                            53.79
                        ]
                    },
                    "usance_tenor": {
                        "value": "90",
                        "coordinate": [
                            [
                                289,
                                241,
                                300,
                                249
                            ]
                        ],
                        "model_confidence": [
                            99.67
                        ]
                    },
                    "tenor_indicator": {
                        "value": "DAYS",
                        "coordinate": [
                            [
                                302,
                                241,
                                329,
                                249
                            ]
                        ],
                        "model_confidence": [
                            98.13
                        ]
                    },
                    "tenor_indicator_type": {
                        "value": "FROM",
                        "coordinate": [
                            [
                                331,
                                241,
                                359,
                                249
                            ]
                        ],
                        "model_confidence": [
                            99.43
                        ]
                    },
                    "tenor_indicator_date": {
                        "value": "AWB DATE",
                        "coordinate": [
                            [
                                363,
                                241,
                                415,
                                249
                            ]
                        ],
                        "model_confidence": [
                            99.52
                        ]
                    },
                    "csh_due_date": {
                        "value": "20211223  20220323",
                        "coordinate": [
                            [
                                417,
                                241,
                                458,
                                249
                            ],
                            [
                                356,
                                422,
                                406,
                                431
                            ]
                        ],
                        "model_confidence": [
                            99.63,
                            77.92
                        ]
                    },
                    "page_no": {
                        "value": "11",
                        "coordinate": [
                            [
                                543,
                                815,
                                557,
                                825
                            ]
                        ],
                        "model_confidence": [
                            99.85
                        ]
                    },
                    "drawee_bank_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                48,
                                146,
                                181,
                                165
                            ]
                        ],
                        "model_confidence": [
                            99.26736867088609
                        ]
                    },
                    "drawer_bank_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                362,
                                57,
                                525,
                                72
                            ]
                        ],
                        "model_confidence": [
                            89.58721282657453
                        ]
                    },
                    "csh_drawn_under_rules": {},
                    "signed_stamp": {},
                    "drawer_address": {},
                    "tenor_type": {},
                    "csh_drawn_under_lc_number": {},
                    "doc_charge_instructions": {},
                    "drawee_address": {},
                    "doc_delivery_instruction": {},
                    "drawer_bank_bottom_bic": {},
                    "nostro_bank_bic": {},
                    "drawee_name": {},
                    "drawee_bank_bic": {},
                    "drawer_bank_bottom_address": {},
                    "drawer_bank_bottom_name": {},
                    "drawer_ref_no": {},
                    "nostro_bank_address": {},
                    "drawer_name": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_6.png": {
                "docClass": "BOE",
                "keys_extraction": {
                    "bill_exchange_no": {
                        "value": "P202130061",
                        "coordinate": [
                            [
                                247,
                                290,
                                296,
                                298
                            ]
                        ],
                        "model_confidence": [
                            45.71
                        ]
                    },
                    "issue_place": {
                        "value": "AST",
                        "coordinate": [
                            [
                                251,
                                340,
                                273,
                                353
                            ]
                        ],
                        "model_confidence": [
                            5.66
                        ]
                    },
                    "drawer_bank_name": {
                        "value": "INDUSTRIAL AND COMMERCIAL BANK OF CHINA",
                        "coordinate": [
                            [
                                349,
                                391,
                                653,
                                405
                            ]
                        ],
                        "model_confidence": [
                            76.67310622394915
                        ]
                    },
                    "amount_in_words": {
                        "value": "PORTY TWO THOUSAND TWO HUNDRED FIFTY",
                        "coordinate": [
                            [
                                344,
                                412,
                                517,
                                422
                            ]
                        ],
                        "model_confidence": [
                            84.09487822177074
                        ]
                    },
                    "invoice_no": {
                        "value": "NO.20213 AXISIN0041",
                        "coordinate": [
                            [
                                241,
                                485,
                                438,
                                515
                            ]
                        ],
                        "model_confidence": [
                            29.564666666666668
                        ]
                    },
                    "usance_tenor": {
                        "value": "90",
                        "coordinate": [
                            [
                                295,
                                335,
                                306,
                                350
                            ]
                        ],
                        "model_confidence": [
                            48.68
                        ]
                    },
                    "tenor_indicator": {
                        "value": "DAYS",
                        "coordinate": [
                            [
                                309,
                                335,
                                330,
                                351
                            ]
                        ],
                        "model_confidence": [
                            48.06
                        ]
                    },
                    "indicator_type": {
                        "value": "FROM",
                        "coordinate": [
                            [
                                334,
                                336,
                                355,
                                352
                            ]
                        ],
                        "model_confidence": [
                            48.55
                        ]
                    },
                    "indicator_date": {
                        "value": "AMB DATE",
                        "coordinate": [
                            [
                                357,
                                337,
                                399,
                                354
                            ]
                        ],
                        "model_confidence": [
                            73.88
                        ]
                    },
                    "invoice_due_date": {
                        "value": "20211223",
                        "coordinate": [
                            [
                                401,
                                338,
                                442,
                                356
                            ]
                        ],
                        "model_confidence": [
                            9.52
                        ]
                    },
                    "bill_exchange_date": {
                        "value": "JANUARY 10 , 2022",
                        "coordinate": [
                            [
                                591,
                                292,
                                663,
                                303
                            ]
                        ],
                        "model_confidence": [
                            68.81970128022759
                        ]
                    },
                    "signature": {
                        "value": "ENDORSEWEHOOVEVE RA MAS T SHIOB MAS OT C. LTD . VIT YMA YAS",
                        "coordinate": [
                            [
                                569,
                                335,
                                679,
                                531
                            ]
                        ],
                        "model_confidence": [
                            64.00056512505022
                        ]
                    },
                    "is_signed": {
                        "value": "",
                        "coordinate": [],
                        "model_confidence": []
                    },
                    "is_stamp": {
                        "value": "",
                        "coordinate": [],
                        "model_confidence": []
                    },
                    "lc_ref_no": {},
                    "drawer_address": {},
                    "boe_currency": {},
                    "original_or_copy": {},
                    "drawer_name": {},
                    "stamp": {},
                    "boe_amount": {},
                    "diclaration_by": {},
                    "invoice_amount": {},
                    "invoice_date": {},
                    "country_of_origin": {},
                    "drawee_name": {},
                    "drawee_address": {},
                    "drawee_bank_address": {},
                    "lc_date": {},
                    "drawee_bank_name": {},
                    "invoice_currency": {},
                    "drawer_bank_address": {},
                    "tenor_type": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_7.png": {
                "docClass": "BOE",
                "keys_extraction": {
                    "bill_exchange_no": {
                        "value": "P202130051",
                        "coordinate": [
                            [
                                545,
                                291,
                                596,
                                303
                            ]
                        ],
                        "model_confidence": [
                            45.83
                        ]
                    },
                    "boe_amount": {
                        "value": "USD42.250.00",
                        "coordinate": [
                            [
                                478,
                                270,
                                535,
                                280
                            ]
                        ],
                        "model_confidence": [
                            46.93
                        ]
                    },
                    "bill_exchange_date": {
                        "value": "2022 , 10 JANUARY",
                        "coordinate": [
                            [
                                179,
                                295,
                                251,
                                305
                            ]
                        ],
                        "model_confidence": [
                            72.35955223880597
                        ]
                    },
                    "usance_tenor": {
                        "value": "90",
                        "coordinate": [
                            [
                                536,
                                245,
                                547,
                                255
                            ]
                        ],
                        "model_confidence": [
                            48.6
                        ]
                    },
                    "tenor_indicator": {
                        "value": "DAYS",
                        "coordinate": [
                            [
                                513,
                                245,
                                532,
                                254
                            ]
                        ],
                        "model_confidence": [
                            47.83
                        ]
                    },
                    "indicator_type": {
                        "value": "FROM",
                        "coordinate": [
                            [
                                487,
                                245,
                                507,
                                254
                            ]
                        ],
                        "model_confidence": [
                            48.29
                        ]
                    },
                    "indicator_date": {
                        "value": "20211223 DATE AMB",
                        "coordinate": [
                            [
                                401,
                                245,
                                483,
                                254
                            ]
                        ],
                        "model_confidence": [
                            42.53999999999999
                        ]
                    },
                    "lc_date": {
                        "value": "01-02-2020",
                        "coordinate": [
                            [
                                176,
                                76,
                                598,
                                160
                            ]
                        ],
                        "model_confidence": [
                            32.265
                        ]
                    },
                    "lc_ref_no": {
                        "value": "CP202130061 CN0041F210044",
                        "coordinate": [
                            [
                                382,
                                100,
                                539,
                                160
                            ]
                        ],
                        "model_confidence": [
                            39.275075301204815
                        ]
                    },
                    "issue_place": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                261,
                                271,
                                286,
                                279
                            ]
                        ],
                        "model_confidence": [
                            27.06
                        ]
                    },
                    "drawer_bank_name": {
                        "value": "CHINA OF BANK COMMERCIAL AND INDUSTRIAL",
                        "coordinate": [
                            [
                                188,
                                190,
                                493,
                                207
                            ]
                        ],
                        "model_confidence": [
                            76.59774032510512
                        ]
                    },
                    "amount_in_words": {
                        "value": "PIFTY HUNDRED NO TYSUSAND TWO PORTY",
                        "coordinate": [
                            [
                                323,
                                174,
                                498,
                                184
                            ]
                        ],
                        "model_confidence": [
                            86.1996195708421
                        ]
                    },
                    "signature": {
                        "value": "BVA MA VIT MON , . CO MEDICINE LO MAS LHE HOMAS ENDOTJENEM ONDEBOL TRUP ENVUVISE MOD",
                        "coordinate": [
                            [
                                164,
                                68,
                                315,
                                262
                            ]
                        ],
                        "model_confidence": [
                            72.32745837630765
                        ]
                    },
                    "is_signed": {
                        "value": "",
                        "coordinate": [],
                        "model_confidence": []
                    },
                    "is_stamp": {
                        "value": "",
                        "coordinate": [],
                        "model_confidence": []
                    },
                    "drawer_address": {},
                    "boe_currency": {},
                    "original_or_copy": {},
                    "invoice_due_date": {},
                    "drawer_name": {},
                    "invoice_no": {},
                    "stamp": {},
                    "diclaration_by": {},
                    "invoice_amount": {},
                    "invoice_date": {},
                    "country_of_origin": {},
                    "drawee_name": {},
                    "drawee_address": {},
                    "drawee_bank_address": {},
                    "drawee_bank_name": {},
                    "invoice_currency": {},
                    "drawer_bank_address": {},
                    "tenor_type": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_8.png": {
                "docClass": "OTHERS",
                "keys_extraction": {}
            },
            "0041FLC210044_9.png": {
                "docClass": "OTHERS",
                "keys_extraction": {}
            },
            "0041FLC210044_10.png": {
                "docClass": "CI",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD",
                        "coordinate": [
                            [
                                187,
                                130,
                                392,
                                141
                            ]
                        ],
                        "model_confidence": [
                            99.90285000000002
                        ]
                    },
                    "beneficiary_address": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                104,
                                151,
                                485,
                                161
                            ]
                        ],
                        "model_confidence": [
                            99.31111060475186
                        ]
                    },
                    "cosignee_name": {
                        "value": "CADCHEM LABORATORIES LTD",
                        "coordinate": [
                            [
                                70,
                                231,
                                233,
                                240
                            ]
                        ],
                        "model_confidence": [
                            99.4154023307436
                        ]
                    },
                    "consignee_address": {
                        "value": "ADD PUNJAB VILLAGE  JAUIA KHURD TEHSIL DERA BASSI",
                        "coordinate": [
                            [
                                53,
                                248,
                                305,
                                270
                            ]
                        ],
                        "model_confidence": [
                            99.34875593913821
                        ]
                    },
                    "usance_tenor": {
                        "value": "90",
                        "coordinate": [
                            [
                                110,
                                324,
                                121,
                                334
                            ]
                        ],
                        "model_confidence": [
                            98.96
                        ]
                    },
                    "tenor_indicator": {
                        "value": "DAYS",
                        "coordinate": [
                            [
                                124,
                                324,
                                152,
                                334
                            ]
                        ],
                        "model_confidence": [
                            99.45
                        ]
                    },
                    "indicator_type": {
                        "value": "AFTER",
                        "coordinate": [
                            [
                                154,
                                324,
                                188,
                                334
                            ]
                        ],
                        "model_confidence": [
                            95.44
                        ]
                    },
                    "indicator_date": {
                        "value": "B / L DATE",
                        "coordinate": [
                            [
                                190,
                                324,
                                238,
                                334
                            ]
                        ],
                        "model_confidence": [
                            98.79434782608696
                        ]
                    },
                    "rate_per_unit": {
                        "value": "USD84.50 / KG",
                        "coordinate": [
                            [
                                265,
                                372,
                                323,
                                382
                            ]
                        ],
                        "model_confidence": [
                            96.38933333333333
                        ]
                    },
                    "goods_description": {
                        "value": "RIFAMYCIN FCA",
                        "coordinate": [
                            [
                                147,
                                385,
                                285,
                                403
                            ]
                        ],
                        "model_confidence": [
                            78.92638709677419
                        ]
                    },
                    "delivery_terms": {
                        "value": "DELHI",
                        "coordinate": [
                            [
                                287,
                                385,
                                319,
                                394
                            ]
                        ],
                        "model_confidence": [
                            45.37
                        ]
                    },
                    "invoice_no": {
                        "value": "CP202130061 ZMCAS22112002",
                        "coordinate": [
                            [
                                435,
                                228,
                                518,
                                261
                            ]
                        ],
                        "model_confidence": [
                            99.18
                        ]
                    },
                    "date_of_invoice": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                402,
                                274,
                                454,
                                284
                            ]
                        ],
                        "model_confidence": [
                            99.16
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "500.00 2",
                        "coordinate": [
                            [
                                153,
                                379,
                                502,
                                407
                            ]
                        ],
                        "model_confidence": [
                            67.725
                        ]
                    },
                    "lc_ref_no": {
                        "value": "0041FLC210044",
                        "coordinate": [
                            [
                                138,
                                418,
                                211,
                                427
                            ]
                        ],
                        "model_confidence": [
                            99.43
                        ]
                    },
                    "lc_date": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                245,
                                418,
                                301,
                                427
                            ]
                        ],
                        "model_confidence": [
                            96.64
                        ]
                    },
                    "country_of_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                181,
                                525,
                                206,
                                536
                            ]
                        ],
                        "model_confidence": [
                            80.5
                        ]
                    },
                    "invoice_amount": {
                        "value": "42,250.00 1202022309814002850",
                        "coordinate": [
                            [
                                346,
                                385,
                                408,
                                393
                            ],
                            [
                                114,
                                639,
                                213,
                                649
                            ]
                        ],
                        "model_confidence": [
                            62.18,
                            19.38
                        ]
                    },
                    "port_of_loading": {
                        "value": "XIACHENG HANGZHOU",
                        "coordinate": [
                            [
                                219,
                                620,
                                385,
                                630
                            ]
                        ],
                        "model_confidence": [
                            33.24464912280702
                        ]
                    },
                    "beneficiary_bank_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                388,
                                620,
                                422,
                                630
                            ]
                        ],
                        "model_confidence": [
                            58.89
                        ]
                    },
                    "declaration_by_issuer": {
                        "value": "ZHEJIANG CO . , LTD.",
                        "coordinate": [
                            [
                                358,
                                707,
                                511,
                                737
                            ]
                        ],
                        "model_confidence": [
                            78.44351893095768
                        ]
                    },
                    "signature_of_the_issuer": {
                        "value": "MEDICINE",
                        "coordinate": [
                            [
                                410,
                                712,
                                461,
                                732
                            ]
                        ],
                        "model_confidence": [
                            41.33
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                369,
                                624,
                                489,
                                676
                            ]
                        ],
                        "model_confidence": [
                            0.7460878491401672
                        ]
                    },
                    "is_stamp": {},
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                53,
                                248,
                                305,
                                270
                            ]
                        ],
                        "model_confidence": [
                            99.34875593913821
                        ]
                    },
                    "incoterm": {},
                    "vessel_flight_no": {},
                    "consignor_name": {},
                    "transaction_currency": {},
                    "transaction_amonunt_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin": {},
                    "bill_of_lading_date": {},
                    "invoice_tax_ccy": {},
                    "consignee_country": {},
                    "net_weight": {},
                    "notify_party_country": {},
                    "hs_code_no": {},
                    "invoice_due_date": {},
                    "country_of_final_destination": {},
                    "invoice_discount_amount": {},
                    "shipper_address": {},
                    "consignor_country": {},
                    "invoice_discount_ccy": {},
                    "tenor_type": {},
                    "awb_date": {},
                    "gross_weight": {},
                    "consignor_address": {},
                    "beneficiary_iban_number": {},
                    "transaction_date": {},
                    "beneficiary_account_number": {},
                    "pre-carriage-by": {},
                    "port_of_discharge": {},
                    "bill_of_lading_no": {},
                    "invoice_tax_amount": {},
                    "invoice_currency": {},
                    "notify_party_name": {},
                    "original_or_copy": {},
                    "notify_party_address": {},
                    "beneficiary_bank_identifier": {},
                    "awb_number": {},
                    "page_no": {},
                    "remitter_address": {},
                    "shipper_name": {},
                    "beneficiary_bank_name": {},
                    "invoice_amount_in_words": {},
                    "beneficiary_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                104,
                                151,
                                485,
                                161
                            ]
                        ],
                        "model_confidence": [
                            99.31111060475186
                        ]
                    },
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_11.png": {
                "docClass": "CI",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD",
                        "coordinate": [
                            [
                                185,
                                130,
                                389,
                                142
                            ]
                        ],
                        "model_confidence": [
                            99.9
                        ]
                    },
                    "beneficiary_address": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                101,
                                152,
                                483,
                                161
                            ]
                        ],
                        "model_confidence": [
                            99.32526922094293
                        ]
                    },
                    "cosignee_name": {
                        "value": "CADCHEM LABORATORIES LTD",
                        "coordinate": [
                            [
                                68,
                                231,
                                231,
                                239
                            ]
                        ],
                        "model_confidence": [
                            99.39501296296297
                        ]
                    },
                    "consignee_address": {
                        "value": "ADD PUNJAB VILLAGE  JAUIA KHURD TEHSIL DERA BASSI",
                        "coordinate": [
                            [
                                50,
                                247,
                                303,
                                270
                            ]
                        ],
                        "model_confidence": [
                            99.32498574929659
                        ]
                    },
                    "usance_tenor": {
                        "value": "90",
                        "coordinate": [
                            [
                                108,
                                324,
                                118,
                                334
                            ]
                        ],
                        "model_confidence": [
                            99.04
                        ]
                    },
                    "tenor_indicator": {
                        "value": "DAYS",
                        "coordinate": [
                            [
                                122,
                                324,
                                149,
                                334
                            ]
                        ],
                        "model_confidence": [
                            99.45
                        ]
                    },
                    "indicator_type": {
                        "value": "AFTER",
                        "coordinate": [
                            [
                                152,
                                324,
                                186,
                                334
                            ]
                        ],
                        "model_confidence": [
                            95.55
                        ]
                    },
                    "indicator_date": {
                        "value": "B / L DATE",
                        "coordinate": [
                            [
                                188,
                                324,
                                235,
                                334
                            ]
                        ],
                        "model_confidence": [
                            98.78288888888889
                        ]
                    },
                    "goods_description": {
                        "value": "RIFAMYCIN 500.00KGS",
                        "coordinate": [
                            [
                                145,
                                379,
                                195,
                                402
                            ]
                        ],
                        "model_confidence": [
                            97.48
                        ]
                    },
                    "rate_per_unit": {
                        "value": "USD84.50 / KG",
                        "coordinate": [
                            [
                                262,
                                372,
                                320,
                                382
                            ]
                        ],
                        "model_confidence": [
                            87.76016949152542
                        ]
                    },
                    "lc_ref_no": {
                        "value": "0041FLC210044",
                        "coordinate": [
                            [
                                135,
                                418,
                                208,
                                427
                            ]
                        ],
                        "model_confidence": [
                            99.32
                        ]
                    },
                    "lc_date": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                244,
                                418,
                                298,
                                427
                            ]
                        ],
                        "model_confidence": [
                            76.72
                        ]
                    },
                    "invoice_no": {
                        "value": "CP202130061 ZMCAS22112002",
                        "coordinate": [
                            [
                                433,
                                228,
                                516,
                                261
                            ]
                        ],
                        "model_confidence": [
                            99.74
                        ]
                    },
                    "date_of_invoice": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                400,
                                274,
                                452,
                                283
                            ]
                        ],
                        "model_confidence": [
                            99.37
                        ]
                    },
                    "invoice_amount": {
                        "value": "42,250.00 1202022309814002850",
                        "coordinate": [
                            [
                                344,
                                386,
                                407,
                                394
                            ],
                            [
                                112,
                                637,
                                210,
                                650
                            ]
                        ],
                        "model_confidence": [
                            41.53,
                            43.3
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "2",
                        "coordinate": [
                            [
                                449,
                                399,
                                499,
                                407
                            ]
                        ],
                        "model_confidence": [
                            98.48
                        ]
                    },
                    "country_of_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                178,
                                526,
                                204,
                                537
                            ]
                        ],
                        "model_confidence": [
                            87.67
                        ]
                    },
                    "port_of_loading": {
                        "value": "XIACHENG HANGZHOU",
                        "coordinate": [
                            [
                                216,
                                620,
                                382,
                                630
                            ]
                        ],
                        "model_confidence": [
                            36.41823008849558
                        ]
                    },
                    "beneficiary_bank_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                386,
                                620,
                                417,
                                630
                            ]
                        ],
                        "model_confidence": [
                            47.64
                        ]
                    },
                    "signature_of_the_issuer": {
                        "value": "ESTI",
                        "coordinate": [
                            [
                                371,
                                629,
                                437,
                                673
                            ]
                        ],
                        "model_confidence": [
                            98.75
                        ]
                    },
                    "declaration_by_issuer": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD.",
                        "coordinate": [
                            [
                                350,
                                710,
                                503,
                                728
                            ]
                        ],
                        "model_confidence": [
                            89.19611321900136
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                368,
                                624,
                                491,
                                680
                            ]
                        ],
                        "model_confidence": [
                            0.7225927710533142
                        ]
                    },
                    "is_stamp": {},
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                50,
                                247,
                                303,
                                270
                            ]
                        ],
                        "model_confidence": [
                            99.32498574929659
                        ]
                    },
                    "incoterm": {},
                    "vessel_flight_no": {},
                    "consignor_name": {},
                    "transaction_currency": {},
                    "transaction_amonunt_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin": {},
                    "bill_of_lading_date": {},
                    "invoice_tax_ccy": {},
                    "consignee_country": {},
                    "net_weight": {},
                    "notify_party_country": {},
                    "hs_code_no": {},
                    "invoice_due_date": {},
                    "country_of_final_destination": {},
                    "invoice_discount_amount": {},
                    "shipper_address": {},
                    "consignor_country": {},
                    "invoice_discount_ccy": {},
                    "tenor_type": {},
                    "awb_date": {},
                    "delivery_terms": {},
                    "gross_weight": {},
                    "consignor_address": {},
                    "beneficiary_iban_number": {},
                    "transaction_date": {},
                    "beneficiary_account_number": {},
                    "pre-carriage-by": {},
                    "port_of_discharge": {},
                    "bill_of_lading_no": {},
                    "invoice_tax_amount": {},
                    "invoice_currency": {},
                    "notify_party_name": {},
                    "original_or_copy": {},
                    "notify_party_address": {},
                    "beneficiary_bank_identifier": {},
                    "awb_number": {},
                    "page_no": {},
                    "remitter_address": {},
                    "shipper_name": {},
                    "beneficiary_bank_name": {},
                    "invoice_amount_in_words": {},
                    "beneficiary_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                101,
                                152,
                                483,
                                161
                            ]
                        ],
                        "model_confidence": [
                            99.32526922094293
                        ]
                    },
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_12.png": {
                "docClass": "CI",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD",
                        "coordinate": [
                            [
                                182,
                                127,
                                385,
                                141
                            ]
                        ],
                        "model_confidence": [
                            99.90280612244898
                        ]
                    },
                    "beneficiary_address": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                99,
                                148,
                                478,
                                160
                            ]
                        ],
                        "model_confidence": [
                            99.34846441961207
                        ]
                    },
                    "cosignee_name": {
                        "value": "CADCHEM LABORATORIES LTD",
                        "coordinate": [
                            [
                                64,
                                229,
                                228,
                                238
                            ]
                        ],
                        "model_confidence": [
                            99.48496323529412
                        ]
                    },
                    "consignee_address": {
                        "value": "PUNJAB VILLAGE  JAUIA KHURD TEHSIL DERA BASSI",
                        "coordinate": [
                            [
                                49,
                                246,
                                300,
                                269
                            ]
                        ],
                        "model_confidence": [
                            99.66725354817311
                        ]
                    },
                    "usance_tenor": {
                        "value": "90",
                        "coordinate": [
                            [
                                105,
                                322,
                                115,
                                332
                            ]
                        ],
                        "model_confidence": [
                            99.05
                        ]
                    },
                    "tenor_indicator": {
                        "value": "DAYS",
                        "coordinate": [
                            [
                                118,
                                321,
                                146,
                                332
                            ]
                        ],
                        "model_confidence": [
                            99.45
                        ]
                    },
                    "indicator_type": {
                        "value": "AFTER",
                        "coordinate": [
                            [
                                150,
                                321,
                                182,
                                331
                            ]
                        ],
                        "model_confidence": [
                            95.24
                        ]
                    },
                    "indicator_date": {
                        "value": "B / L DATE",
                        "coordinate": [
                            [
                                185,
                                320,
                                232,
                                331
                            ]
                        ],
                        "model_confidence": [
                            98.80418803418803
                        ]
                    },
                    "rate_per_unit": {
                        "value": "USD84.50 ",
                        "coordinate": [
                            [
                                260,
                                370,
                                308,
                                379
                            ]
                        ],
                        "model_confidence": [
                            89.09276595744682
                        ]
                    },
                    "goods_description": {
                        "value": "500.00KGS FCA",
                        "coordinate": [
                            [
                                150,
                                376,
                                282,
                                392
                            ]
                        ],
                        "model_confidence": [
                            23.34279069767442
                        ]
                    },
                    "lc_ref_no": {
                        "value": "0041FLC210044",
                        "coordinate": [
                            [
                                133,
                                416,
                                205,
                                426
                            ]
                        ],
                        "model_confidence": [
                            82.99
                        ]
                    },
                    "lc_date": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                241,
                                415,
                                296,
                                426
                            ]
                        ],
                        "model_confidence": [
                            35.4
                        ]
                    },
                    "invoice_no": {
                        "value": "CP202130061 ZMCAS22112002",
                        "coordinate": [
                            [
                                430,
                                226,
                                513,
                                258
                            ]
                        ],
                        "model_confidence": [
                            99.38
                        ]
                    },
                    "date_of_invoice": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                396,
                                271,
                                448,
                                280
                            ]
                        ],
                        "model_confidence": [
                            99.3
                        ]
                    },
                    "invoice_amount": {
                        "value": "42,250.00 1202022309814002850",
                        "coordinate": [
                            [
                                342,
                                384,
                                404,
                                391
                            ],
                            [
                                112,
                                637,
                                210,
                                647
                            ]
                        ],
                        "model_confidence": [
                            44.2,
                            41.9
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "2",
                        "coordinate": [
                            [
                                447,
                                396,
                                496,
                                404
                            ]
                        ],
                        "model_confidence": [
                            98.86
                        ]
                    },
                    "country_of_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                177,
                                525,
                                201,
                                535
                            ]
                        ],
                        "model_confidence": [
                            82.55
                        ]
                    },
                    "port_of_loading": {
                        "value": "HUANCHENG XIACHENG HANGZHOU",
                        "coordinate": [
                            [
                                95,
                                617,
                                381,
                                628
                            ]
                        ],
                        "model_confidence": [
                            52.55332699455441
                        ]
                    },
                    "beneficiary_bank_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                386,
                                617,
                                418,
                                627
                            ]
                        ],
                        "model_confidence": [
                            41.83
                        ]
                    },
                    "signature_of_the_issuer": {
                        "value": "ESTAT",
                        "coordinate": [
                            [
                                382,
                                621,
                                460,
                                673
                            ]
                        ],
                        "model_confidence": [
                            96.34
                        ]
                    },
                    "declaration_by_issuer": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD.",
                        "coordinate": [
                            [
                                356,
                                720,
                                509,
                                740
                            ]
                        ],
                        "model_confidence": [
                            88.27668930112792
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                384,
                                623,
                                505,
                                675
                            ]
                        ],
                        "model_confidence": [
                            0.7173946499824524
                        ]
                    },
                    "is_stamp": {},
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                49,
                                246,
                                300,
                                269
                            ]
                        ],
                        "model_confidence": [
                            99.66725354817311
                        ]
                    },
                    "incoterm": {},
                    "vessel_flight_no": {},
                    "consignor_name": {},
                    "transaction_currency": {},
                    "transaction_amonunt_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin": {},
                    "bill_of_lading_date": {},
                    "invoice_tax_ccy": {},
                    "consignee_country": {},
                    "net_weight": {},
                    "notify_party_country": {},
                    "hs_code_no": {},
                    "invoice_due_date": {},
                    "country_of_final_destination": {},
                    "invoice_discount_amount": {},
                    "shipper_address": {},
                    "consignor_country": {},
                    "invoice_discount_ccy": {},
                    "tenor_type": {},
                    "awb_date": {},
                    "delivery_terms": {},
                    "gross_weight": {},
                    "consignor_address": {},
                    "beneficiary_iban_number": {},
                    "transaction_date": {},
                    "beneficiary_account_number": {},
                    "pre-carriage-by": {},
                    "port_of_discharge": {},
                    "bill_of_lading_no": {},
                    "invoice_tax_amount": {},
                    "invoice_currency": {},
                    "notify_party_name": {},
                    "original_or_copy": {},
                    "notify_party_address": {},
                    "beneficiary_bank_identifier": {},
                    "awb_number": {},
                    "page_no": {},
                    "remitter_address": {},
                    "shipper_name": {},
                    "beneficiary_bank_name": {},
                    "invoice_amount_in_words": {},
                    "beneficiary_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                99,
                                148,
                                478,
                                160
                            ]
                        ],
                        "model_confidence": [
                            99.34846441961207
                        ]
                    },
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_13.png": {
                "docClass": "CI",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD",
                        "coordinate": [
                            [
                                195,
                                129,
                                399,
                                140
                            ]
                        ],
                        "model_confidence": [
                            99.90286432160805
                        ]
                    },
                    "beneficiary_address": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                111,
                                150,
                                492,
                                162
                            ]
                        ],
                        "model_confidence": [
                            99.31607968663303
                        ]
                    },
                    "cosignee_name": {
                        "value": "CADCHEM LABORATORIES LTD",
                        "coordinate": [
                            [
                                77,
                                231,
                                241,
                                240
                            ]
                        ],
                        "model_confidence": [
                            99.49196539605299
                        ]
                    },
                    "consignee_address": {
                        "value": "ADD PUNJAB VILLAGE  JAUIA KHURD TEHSIL DERA BASSI",
                        "coordinate": [
                            [
                                61,
                                247,
                                314,
                                270
                            ]
                        ],
                        "model_confidence": [
                            99.27451457191165
                        ]
                    },
                    "usance_tenor": {
                        "value": "90",
                        "coordinate": [
                            [
                                119,
                                324,
                                129,
                                334
                            ]
                        ],
                        "model_confidence": [
                            99.01
                        ]
                    },
                    "tenor_indicator": {
                        "value": "DAYS",
                        "coordinate": [
                            [
                                132,
                                324,
                                160,
                                334
                            ]
                        ],
                        "model_confidence": [
                            99.45
                        ]
                    },
                    "indicator_type": {
                        "value": "AFTER",
                        "coordinate": [
                            [
                                162,
                                324,
                                196,
                                334
                            ]
                        ],
                        "model_confidence": [
                            95.52
                        ]
                    },
                    "indicator_date": {
                        "value": "B / L DATE",
                        "coordinate": [
                            [
                                199,
                                324,
                                246,
                                334
                            ]
                        ],
                        "model_confidence": [
                            98.81266666666666
                        ]
                    },
                    "rate_per_unit": {
                        "value": "USD84.50 / KG",
                        "coordinate": [
                            [
                                273,
                                371,
                                331,
                                382
                            ]
                        ],
                        "model_confidence": [
                            94.67511041009465
                        ]
                    },
                    "delivery_terms": {
                        "value": "FCA DELHI",
                        "coordinate": [
                            [
                                274,
                                385,
                                329,
                                394
                            ]
                        ],
                        "model_confidence": [
                            58.34
                        ]
                    },
                    "invoice_no": {
                        "value": "CP202130061 ZMCAS22112002",
                        "coordinate": [
                            [
                                443,
                                229,
                                527,
                                261
                            ]
                        ],
                        "model_confidence": [
                            99.64
                        ]
                    },
                    "date_of_invoice": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                409,
                                272,
                                462,
                                283
                            ]
                        ],
                        "model_confidence": [
                            99.33
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "5",
                        "coordinate": [
                            [
                                161,
                                379,
                                206,
                                388
                            ]
                        ],
                        "model_confidence": [
                            97.57
                        ]
                    },
                    "goods_description": {
                        "value": "RIFAMYCIN",
                        "coordinate": [
                            [
                                155,
                                391,
                                201,
                                403
                            ]
                        ],
                        "model_confidence": [
                            98.91
                        ]
                    },
                    "lc_ref_no": {
                        "value": "0041FLC210044",
                        "coordinate": [
                            [
                                146,
                                418,
                                219,
                                427
                            ]
                        ],
                        "model_confidence": [
                            99.39
                        ]
                    },
                    "lc_date": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                254,
                                418,
                                309,
                                427
                            ]
                        ],
                        "model_confidence": [
                            95.1
                        ]
                    },
                    "country_of_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                190,
                                525,
                                215,
                                536
                            ]
                        ],
                        "model_confidence": [
                            86.34
                        ]
                    },
                    "invoice_amount": {
                        "value": "42,250.00 1202022309814002850",
                        "coordinate": [
                            [
                                355,
                                383,
                                417,
                                394
                            ],
                            [
                                124,
                                638,
                                222,
                                647
                            ]
                        ],
                        "model_confidence": [
                            60.09,
                            34.48
                        ]
                    },
                    "port_of_loading": {
                        "value": "XIACHENG",
                        "coordinate": [
                            [
                                228,
                                619,
                                283,
                                628
                            ]
                        ],
                        "model_confidence": [
                            26.59
                        ]
                    },
                    "beneficiary_bank_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                397,
                                619,
                                431,
                                628
                            ]
                        ],
                        "model_confidence": [
                            47.03
                        ]
                    },
                    "signature_of_the_issuer": {
                        "value": "J",
                        "coordinate": [
                            [
                                409,
                                640,
                                443,
                                681
                            ]
                        ],
                        "model_confidence": [
                            98.9
                        ]
                    },
                    "declaration_by_issuer": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD.",
                        "coordinate": [
                            [
                                376,
                                721,
                                528,
                                738
                            ]
                        ],
                        "model_confidence": [
                            95.47552384903263
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                410,
                                632,
                                531,
                                692
                            ]
                        ],
                        "model_confidence": [
                            0.7312248349189758
                        ]
                    },
                    "is_stamp": {},
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                61,
                                247,
                                314,
                                270
                            ]
                        ],
                        "model_confidence": [
                            99.27451457191165
                        ]
                    },
                    "incoterm": {},
                    "vessel_flight_no": {},
                    "consignor_name": {},
                    "transaction_currency": {},
                    "transaction_amonunt_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin": {},
                    "bill_of_lading_date": {},
                    "invoice_tax_ccy": {},
                    "consignee_country": {},
                    "net_weight": {},
                    "notify_party_country": {},
                    "hs_code_no": {},
                    "invoice_due_date": {},
                    "country_of_final_destination": {},
                    "invoice_discount_amount": {},
                    "shipper_address": {},
                    "consignor_country": {},
                    "invoice_discount_ccy": {},
                    "tenor_type": {},
                    "awb_date": {},
                    "gross_weight": {},
                    "consignor_address": {},
                    "beneficiary_iban_number": {},
                    "transaction_date": {},
                    "beneficiary_account_number": {},
                    "pre-carriage-by": {},
                    "port_of_discharge": {},
                    "bill_of_lading_no": {},
                    "invoice_tax_amount": {},
                    "invoice_currency": {},
                    "notify_party_name": {},
                    "original_or_copy": {},
                    "notify_party_address": {},
                    "beneficiary_bank_identifier": {},
                    "awb_number": {},
                    "page_no": {},
                    "remitter_address": {},
                    "shipper_name": {},
                    "beneficiary_bank_name": {},
                    "invoice_amount_in_words": {},
                    "beneficiary_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                111,
                                150,
                                492,
                                162
                            ]
                        ],
                        "model_confidence": [
                            99.31607968663303
                        ]
                    },
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_14.png": {
                "docClass": "CI",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD",
                        "coordinate": [
                            [
                                188,
                                128,
                                392,
                                140
                            ]
                        ],
                        "model_confidence": [
                            99.90286432160805
                        ]
                    },
                    "beneficiary_address": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                104,
                                150,
                                485,
                                160
                            ]
                        ],
                        "model_confidence": [
                            99.31109893766573
                        ]
                    },
                    "cosignee_name": {
                        "value": "CADCHEM LABORATORIES LTD",
                        "coordinate": [
                            [
                                70,
                                229,
                                234,
                                238
                            ]
                        ],
                        "model_confidence": [
                            99.46815054744528
                        ]
                    },
                    "consignee_address": {
                        "value": "ADD PUNJAB VILLAGE  JAUIA KHURD TEHSIL DERA BASSI",
                        "coordinate": [
                            [
                                54,
                                245,
                                306,
                                268
                            ]
                        ],
                        "model_confidence": [
                            98.38993723385228
                        ]
                    },
                    "usance_tenor": {
                        "value": "90",
                        "coordinate": [
                            [
                                110,
                                322,
                                121,
                                332
                            ]
                        ],
                        "model_confidence": [
                            99.01
                        ]
                    },
                    "tenor_indicator": {
                        "value": "DAYS",
                        "coordinate": [
                            [
                                124,
                                322,
                                151,
                                332
                            ]
                        ],
                        "model_confidence": [
                            99.45
                        ]
                    },
                    "indicator_type": {
                        "value": "AFTER",
                        "coordinate": [
                            [
                                155,
                                322,
                                187,
                                332
                            ]
                        ],
                        "model_confidence": [
                            95.4
                        ]
                    },
                    "indicator_date": {
                        "value": "B / L DATE",
                        "coordinate": [
                            [
                                190,
                                322,
                                236,
                                332
                            ]
                        ],
                        "model_confidence": [
                            98.84499999999998
                        ]
                    },
                    "rate_per_unit": {
                        "value": "USD84.50 / KG",
                        "coordinate": [
                            [
                                265,
                                371,
                                323,
                                380
                            ]
                        ],
                        "model_confidence": [
                            94.10066666666667
                        ]
                    },
                    "goods_description": {
                        "value": "RIFAMYCIN O FCA DELHI",
                        "coordinate": [
                            [
                                149,
                                383,
                                321,
                                401
                            ]
                        ],
                        "model_confidence": [
                            68.59109505330873
                        ]
                    },
                    "invoice_no": {
                        "value": "CP202130061 ZMCAS22112002",
                        "coordinate": [
                            [
                                436,
                                228,
                                519,
                                259
                            ]
                        ],
                        "model_confidence": [
                            99.08
                        ]
                    },
                    "date_of_invoice": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                402,
                                272,
                                455,
                                282
                            ]
                        ],
                        "model_confidence": [
                            99.12
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "5",
                        "coordinate": [
                            [
                                154,
                                376,
                                197,
                                387
                            ]
                        ],
                        "model_confidence": [
                            90.97
                        ]
                    },
                    "lc_ref_no": {
                        "value": "0041FLC210044",
                        "coordinate": [
                            [
                                137,
                                416,
                                211,
                                426
                            ]
                        ],
                        "model_confidence": [
                            97.75
                        ]
                    },
                    "lc_date": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                246,
                                416,
                                301,
                                426
                            ]
                        ],
                        "model_confidence": [
                            84.7
                        ]
                    },
                    "country_of_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                181,
                                524,
                                207,
                                534
                            ]
                        ],
                        "model_confidence": [
                            84.42
                        ]
                    },
                    "invoice_amount": {
                        "value": "42,250.00 1202022309814002850",
                        "coordinate": [
                            [
                                347,
                                384,
                                409,
                                393
                            ],
                            [
                                115,
                                637,
                                213,
                                645
                            ]
                        ],
                        "model_confidence": [
                            72.59,
                            25.02
                        ]
                    },
                    "port_of_loading": {
                        "value": "XIACHENG HANGZHOU ",
                        "coordinate": [
                            [
                                220,
                                618,
                                421,
                                627
                            ]
                        ],
                        "model_confidence": [
                            51.658918918918914
                        ]
                    },
                    "signature_of_the_issuer": {
                        "value": "ESTAR",
                        "coordinate": [
                            [
                                378,
                                640,
                                463,
                                685
                            ]
                        ],
                        "model_confidence": [
                            99.47
                        ]
                    },
                    "declaration_by_issuer": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD.",
                        "coordinate": [
                            [
                                348,
                                735,
                                501,
                                748
                            ]
                        ],
                        "model_confidence": [
                            98.26815068493151
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                381,
                                638,
                                502,
                                692
                            ]
                        ],
                        "model_confidence": [
                            0.7159293293952942
                        ]
                    },
                    "is_stamp": {},
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                54,
                                245,
                                306,
                                268
                            ]
                        ],
                        "model_confidence": [
                            98.38993723385228
                        ]
                    },
                    "port_of_loading_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                220,
                                618,
                                421,
                                627
                            ]
                        ],
                        "model_confidence": [
                            51.658918918918914
                        ]
                    },
                    "incoterm": {},
                    "vessel_flight_no": {},
                    "consignor_name": {},
                    "beneficiary_bank_country": {},
                    "transaction_currency": {},
                    "transaction_amonunt_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin": {},
                    "bill_of_lading_date": {},
                    "invoice_tax_ccy": {},
                    "consignee_country": {},
                    "net_weight": {},
                    "notify_party_country": {},
                    "hs_code_no": {},
                    "invoice_due_date": {},
                    "country_of_final_destination": {},
                    "invoice_discount_amount": {},
                    "shipper_address": {},
                    "consignor_country": {},
                    "invoice_discount_ccy": {},
                    "tenor_type": {},
                    "awb_date": {},
                    "delivery_terms": {},
                    "gross_weight": {},
                    "consignor_address": {},
                    "beneficiary_iban_number": {},
                    "transaction_date": {},
                    "beneficiary_account_number": {},
                    "pre-carriage-by": {},
                    "port_of_discharge": {},
                    "bill_of_lading_no": {},
                    "invoice_tax_amount": {},
                    "invoice_currency": {},
                    "notify_party_name": {},
                    "original_or_copy": {},
                    "notify_party_address": {},
                    "beneficiary_bank_identifier": {},
                    "awb_number": {},
                    "page_no": {},
                    "remitter_address": {},
                    "shipper_name": {},
                    "beneficiary_bank_name": {},
                    "invoice_amount_in_words": {},
                    "beneficiary_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                104,
                                150,
                                485,
                                160
                            ]
                        ],
                        "model_confidence": [
                            99.31109893766573
                        ]
                    },
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_15.png": {
                "docClass": "CI",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD",
                        "coordinate": [
                            [
                                188,
                                129,
                                393,
                                140
                            ]
                        ],
                        "model_confidence": [
                            99.9029
                        ]
                    },
                    "beneficiary_address": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                104,
                                150,
                                485,
                                161
                            ]
                        ],
                        "model_confidence": [
                            99.33444831079379
                        ]
                    },
                    "cosignee_name": {
                        "value": "CADCHEM LABORATORIES LTD",
                        "coordinate": [
                            [
                                70,
                                229,
                                233,
                                238
                            ]
                        ],
                        "model_confidence": [
                            99.48733695652172
                        ]
                    },
                    "consignee_address": {
                        "value": "ADD PUNJAB VILLAGE  JAUIA KHURD TEHSIL DERA BASSI",
                        "coordinate": [
                            [
                                54,
                                246,
                                306,
                                269
                            ]
                        ],
                        "model_confidence": [
                            99.38579859848166
                        ]
                    },
                    "usance_tenor": {
                        "value": "90",
                        "coordinate": [
                            [
                                110,
                                322,
                                121,
                                332
                            ]
                        ],
                        "model_confidence": [
                            98.96
                        ]
                    },
                    "tenor_indicator": {
                        "value": "DAYS",
                        "coordinate": [
                            [
                                124,
                                322,
                                151,
                                332
                            ]
                        ],
                        "model_confidence": [
                            99.45
                        ]
                    },
                    "indicator_type": {
                        "value": "AFTER",
                        "coordinate": [
                            [
                                155,
                                322,
                                187,
                                332
                            ]
                        ],
                        "model_confidence": [
                            95.35
                        ]
                    },
                    "indicator_date": {
                        "value": "B / L DATE",
                        "coordinate": [
                            [
                                190,
                                322,
                                236,
                                332
                            ]
                        ],
                        "model_confidence": [
                            98.83348837209303
                        ]
                    },
                    "goods_description": {
                        "value": "RIFAMYCIN 500.00KGS",
                        "coordinate": [
                            [
                                149,
                                375,
                                197,
                                400
                            ]
                        ],
                        "model_confidence": [
                            98.36
                        ]
                    },
                    "rate_per_unit": {
                        "value": "USD84.50 ",
                        "coordinate": [
                            [
                                265,
                                370,
                                313,
                                380
                            ]
                        ],
                        "model_confidence": [
                            93.63040816326532
                        ]
                    },
                    "invoice_no": {
                        "value": "CP202130061 ZMCAS22112002",
                        "coordinate": [
                            [
                                435,
                                228,
                                517,
                                260
                            ]
                        ],
                        "model_confidence": [
                            99.74
                        ]
                    },
                    "date_of_invoice": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                402,
                                272,
                                456,
                                283
                            ]
                        ],
                        "model_confidence": [
                            99.38
                        ]
                    },
                    "invoice_amount": {
                        "value": "42,250.00 1202022309814002850",
                        "coordinate": [
                            [
                                347,
                                384,
                                408,
                                392
                            ],
                            [
                                115,
                                637,
                                213,
                                646
                            ]
                        ],
                        "model_confidence": [
                            20.29,
                            37.55
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "2",
                        "coordinate": [
                            [
                                451,
                                397,
                                502,
                                406
                            ]
                        ],
                        "model_confidence": [
                            76.21
                        ]
                    },
                    "lc_ref_no": {
                        "value": "0041FLC210044",
                        "coordinate": [
                            [
                                138,
                                416,
                                212,
                                426
                            ]
                        ],
                        "model_confidence": [
                            97.01
                        ]
                    },
                    "lc_date": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                246,
                                416,
                                302,
                                426
                            ]
                        ],
                        "model_confidence": [
                            88.43
                        ]
                    },
                    "country_of_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                181,
                                524,
                                206,
                                534
                            ]
                        ],
                        "model_confidence": [
                            82.31
                        ]
                    },
                    "port_of_loading": {
                        "value": "XIACHENG HANGZHOU",
                        "coordinate": [
                            [
                                220,
                                617,
                                386,
                                629
                            ]
                        ],
                        "model_confidence": [
                            45.56132743362832
                        ]
                    },
                    "beneficiary_bank_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                387,
                                617,
                                422,
                                629
                            ]
                        ],
                        "model_confidence": [
                            53.97
                        ]
                    },
                    "signature_of_the_issuer": {
                        "value": "TEX",
                        "coordinate": [
                            [
                                337,
                                622,
                                424,
                                665
                            ]
                        ],
                        "model_confidence": [
                            74.98
                        ]
                    },
                    "declaration_by_issuer": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD.",
                        "coordinate": [
                            [
                                322,
                                716,
                                474,
                                738
                            ]
                        ],
                        "model_confidence": [
                            88.3510468524531
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                338,
                                614,
                                456,
                                670
                            ]
                        ],
                        "model_confidence": [
                            0.7572820782661438
                        ]
                    },
                    "is_stamp": {},
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                54,
                                246,
                                306,
                                269
                            ]
                        ],
                        "model_confidence": [
                            99.38579859848166
                        ]
                    },
                    "incoterm": {},
                    "vessel_flight_no": {},
                    "consignor_name": {},
                    "transaction_currency": {},
                    "transaction_amonunt_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin": {},
                    "bill_of_lading_date": {},
                    "invoice_tax_ccy": {},
                    "consignee_country": {},
                    "net_weight": {},
                    "notify_party_country": {},
                    "hs_code_no": {},
                    "invoice_due_date": {},
                    "country_of_final_destination": {},
                    "invoice_discount_amount": {},
                    "shipper_address": {},
                    "consignor_country": {},
                    "invoice_discount_ccy": {},
                    "tenor_type": {},
                    "awb_date": {},
                    "delivery_terms": {},
                    "gross_weight": {},
                    "consignor_address": {},
                    "beneficiary_iban_number": {},
                    "transaction_date": {},
                    "beneficiary_account_number": {},
                    "pre-carriage-by": {},
                    "port_of_discharge": {},
                    "bill_of_lading_no": {},
                    "invoice_tax_amount": {},
                    "invoice_currency": {},
                    "notify_party_name": {},
                    "original_or_copy": {},
                    "notify_party_address": {},
                    "beneficiary_bank_identifier": {},
                    "awb_number": {},
                    "page_no": {},
                    "remitter_address": {},
                    "shipper_name": {},
                    "beneficiary_bank_name": {},
                    "invoice_amount_in_words": {},
                    "beneficiary_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                104,
                                150,
                                485,
                                161
                            ]
                        ],
                        "model_confidence": [
                            99.33444831079379
                        ]
                    },
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_16.png": {
                "docClass": "PL",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD .",
                        "coordinate": [
                            [
                                184,
                                130,
                                394,
                                141
                            ]
                        ],
                        "model_confidence": [
                            99.93960784313725
                        ]
                    },
                    "beneficiary_address": {
                        "value": "168 MID ZHIYUAN AVENUE BINHAI NEW AREA SHAOXING CITY ZHEJIANG PROVINCE 312366 PRCHINA",
                        "coordinate": [
                            [
                                100,
                                149,
                                480,
                                162
                            ]
                        ],
                        "model_confidence": [
                            99.35429738030989
                        ]
                    },
                    "consignee_name": {
                        "value": "CADCHEM LABORATORIES LTD",
                        "coordinate": [
                            [
                                67,
                                231,
                                230,
                                240
                            ]
                        ],
                        "model_confidence": [
                            99.94000000000001
                        ]
                    },
                    "consignee_address": {
                        "value": "ADD PUNJAB VILLAGE  JAUIA KHURD TEHSIL DERA BASSI",
                        "coordinate": [
                            [
                                51,
                                247,
                                302,
                                269
                            ]
                        ],
                        "model_confidence": [
                            99.90981428442608
                        ]
                    },
                    "payment_terms_terms_of_delivery_&_payment": {
                        "value": "L / C 90 DAYS AFTER B / L DATE",
                        "coordinate": [
                            [
                                89,
                                307,
                                234,
                                319
                            ]
                        ],
                        "model_confidence": [
                            99.94773959173622
                        ]
                    },
                    "description_of_goods": {
                        "value": "RIFAMYCIN O",
                        "coordinate": [
                            [
                                145,
                                377,
                                198,
                                387
                            ]
                        ],
                        "model_confidence": [
                            99.20333333333333
                        ]
                    },
                    "lc_ref_no": {
                        "value": "0041FLC210044",
                        "coordinate": [
                            [
                                127,
                                404,
                                200,
                                413
                            ]
                        ],
                        "model_confidence": [
                            99.4
                        ]
                    },
                    "lc_date": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                235,
                                404,
                                291,
                                413
                            ]
                        ],
                        "model_confidence": [
                            99.74
                        ]
                    },
                    "net_weight": {
                        "value": "",
                        "coordinate": [
                            [
                                96,
                                422,
                                153,
                                432
                            ]
                        ],
                        "model_confidence": [
                            99.88
                        ]
                    },
                    "gross_weight": {
                        "value": "",
                        "coordinate": [
                            [
                                97,
                                441,
                                153,
                                450
                            ]
                        ],
                        "model_confidence": [
                            99.42
                        ]
                    },
                    "invoice_no": {
                        "value": "CP202130061",
                        "coordinate": [
                            [
                                450,
                                229,
                                509,
                                238
                            ]
                        ],
                        "model_confidence": [
                            99.98
                        ]
                    },
                    "date_of_invoice": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                398,
                                257,
                                450,
                                268
                            ]
                        ],
                        "model_confidence": [
                            99.94
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "20 2",
                        "coordinate": [
                            [
                                362,
                                376,
                                500,
                                385
                            ]
                        ],
                        "model_confidence": [
                            99.8742857142857
                        ]
                    },
                    "country_of_origin_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                178,
                                511,
                                204,
                                521
                            ]
                        ],
                        "model_confidence": [
                            99.83
                        ]
                    },
                    "declaration": {
                        "value": "MEDICINE CO . , LTD.",
                        "coordinate": [
                            [
                                334,
                                610,
                                436,
                                636
                            ]
                        ],
                        "model_confidence": [
                            65.35732620320856
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                297,
                                513,
                                410,
                                571
                            ]
                        ],
                        "model_confidence": [
                            0.771777331829071
                        ]
                    },
                    "is_stamp": {},
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                51,
                                247,
                                302,
                                269
                            ]
                        ],
                        "model_confidence": [
                            99.90981428442608
                        ]
                    },
                    "shipper_address": {},
                    "notify_party_address": {},
                    "awb_number": {},
                    "vessel_flight_no": {},
                    "track_reference": {},
                    "notify_party_name": {},
                    "bill_of_lading_date": {},
                    "dimension": {},
                    "transaction_currency": {},
                    "port_of_loading": {},
                    "transaction_date": {},
                    "country_of_final_destination": {},
                    "invoice_amount": {},
                    "shipper_name": {},
                    "transaction_amount_value": {},
                    "consignor_address": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin_no": {},
                    "remitter_address": {},
                    "bill_of_lading_number": {},
                    "rate_per_unit": {},
                    "consignor_name": {},
                    "invoice_currency": {},
                    "pre_carriage_by": {},
                    "incoterm": {},
                    "port_of_discharge": {},
                    "original_copy": {},
                    "awb_date": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_17.png": {
                "docClass": "PL",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD .",
                        "coordinate": [
                            [
                                187,
                                130,
                                396,
                                141
                            ]
                        ],
                        "model_confidence": [
                            99.94896551724138
                        ]
                    },
                    "beneficiary_address": {
                        "value": "168 MID ZHIYUAN AVENUE BINHAI NEW AREA SHAOXING CITY ZHEJIANG PRCHINA",
                        "coordinate": [
                            [
                                103,
                                151,
                                485,
                                161
                            ]
                        ],
                        "model_confidence": [
                            89.9823359480711
                        ]
                    },
                    "consignee_name": {
                        "value": "CADCHEM LABORATORIES LTD",
                        "coordinate": [
                            [
                                69,
                                231,
                                233,
                                239
                            ]
                        ],
                        "model_confidence": [
                            99.94
                        ]
                    },
                    "consignee_address": {
                        "value": "ADD PUNJAB VILLAGE  JAUIA KHURD TEHSIL DERA BASSI",
                        "coordinate": [
                            [
                                52,
                                247,
                                305,
                                270
                            ]
                        ],
                        "model_confidence": [
                            99.5618804522228
                        ]
                    },
                    "payment_terms_terms_of_delivery_&_payment": {
                        "value": "L / C 90 DAYS AFTER B / L DATE",
                        "coordinate": [
                            [
                                91,
                                307,
                                237,
                                318
                            ]
                        ],
                        "model_confidence": [
                            99.94782167935018
                        ]
                    },
                    "description_of_goods": {
                        "value": "RIFAMYCIN O",
                        "coordinate": [
                            [
                                147,
                                377,
                                202,
                                387
                            ]
                        ],
                        "model_confidence": [
                            98.77384615384614
                        ]
                    },
                    "lc_ref_no": {
                        "value": "0041FLC210044",
                        "coordinate": [
                            [
                                129,
                                404,
                                202,
                                414
                            ]
                        ],
                        "model_confidence": [
                            99.21
                        ]
                    },
                    "lc_date": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                238,
                                404,
                                292,
                                414
                            ]
                        ],
                        "model_confidence": [
                            99.73
                        ]
                    },
                    "net_weight": {
                        "value": "",
                        "coordinate": [
                            [
                                99,
                                422,
                                155,
                                432
                            ]
                        ],
                        "model_confidence": [
                            99.21
                        ]
                    },
                    "gross_weight": {
                        "value": "",
                        "coordinate": [
                            [
                                100,
                                440,
                                156,
                                452
                            ]
                        ],
                        "model_confidence": [
                            96.49
                        ]
                    },
                    "invoice_no": {
                        "value": "CP202130061",
                        "coordinate": [
                            [
                                452,
                                229,
                                512,
                                238
                            ]
                        ],
                        "model_confidence": [
                            99.98
                        ]
                    },
                    "bill_of_lading_number": {
                        "value": "ZMCAS22112002",
                        "coordinate": [
                            [
                                436,
                                245,
                                518,
                                254
                            ]
                        ],
                        "model_confidence": [
                            28.85
                        ]
                    },
                    "date_of_invoice": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                400,
                                259,
                                452,
                                268
                            ]
                        ],
                        "model_confidence": [
                            99.94
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "20 2",
                        "coordinate": [
                            [
                                364,
                                376,
                                502,
                                385
                            ]
                        ],
                        "model_confidence": [
                            99.87878787878788
                        ]
                    },
                    "country_of_origin_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                180,
                                510,
                                205,
                                521
                            ]
                        ],
                        "model_confidence": [
                            99.83
                        ]
                    },
                    "declaration": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD.",
                        "coordinate": [
                            [
                                331,
                                620,
                                484,
                                642
                            ]
                        ],
                        "model_confidence": [
                            97.86575006050826
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                341,
                                525,
                                464,
                                583
                            ]
                        ],
                        "model_confidence": [
                            0.7552236318588257
                        ]
                    },
                    "is_stamp": {},
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                52,
                                247,
                                305,
                                270
                            ]
                        ],
                        "model_confidence": [
                            99.5618804522228
                        ]
                    },
                    "shipper_address": {},
                    "notify_party_address": {},
                    "awb_number": {},
                    "vessel_flight_no": {},
                    "track_reference": {},
                    "notify_party_name": {},
                    "bill_of_lading_date": {},
                    "dimension": {},
                    "transaction_currency": {},
                    "port_of_loading": {},
                    "transaction_date": {},
                    "country_of_final_destination": {},
                    "invoice_amount": {},
                    "shipper_name": {},
                    "transaction_amount_value": {},
                    "consignor_address": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin_no": {},
                    "remitter_address": {},
                    "rate_per_unit": {},
                    "consignor_name": {},
                    "invoice_currency": {},
                    "pre_carriage_by": {},
                    "incoterm": {},
                    "port_of_discharge": {},
                    "original_copy": {},
                    "awb_date": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_18.png": {
                "docClass": "PL",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD .",
                        "coordinate": [
                            [
                                189,
                                129,
                                398,
                                140
                            ]
                        ],
                        "model_confidence": [
                            99.9609268292683
                        ]
                    },
                    "beneficiary_address": {
                        "value": "168 MID ZHIYUAN AVENUE BINHAI NEW AREA SHAOXING CITY ZHEJIANG PROVINCE 312366 PR ",
                        "coordinate": [
                            [
                                105,
                                150,
                                487,
                                160
                            ]
                        ],
                        "model_confidence": [
                            99.28833076012303
                        ]
                    },
                    "consignee_name": {
                        "value": "CADCHEM LABORATORIES LTD",
                        "coordinate": [
                            [
                                71,
                                229,
                                235,
                                239
                            ]
                        ],
                        "model_confidence": [
                            99.931969451203
                        ]
                    },
                    "consignee_address": {
                        "value": "ADD PUNJAB VILLAGE  JAUIA KHURD TEHSIL DERA BASSI",
                        "coordinate": [
                            [
                                55,
                                247,
                                307,
                                269
                            ]
                        ],
                        "model_confidence": [
                            99.36849374216416
                        ]
                    },
                    "payment_terms_terms_of_delivery_&_payment": {
                        "value": "L / C 90 DAYS AFTER B / L DATE",
                        "coordinate": [
                            [
                                93,
                                306,
                                239,
                                318
                            ]
                        ],
                        "model_confidence": [
                            99.95
                        ]
                    },
                    "description_of_goods": {
                        "value": "RIFAMYCIN O",
                        "coordinate": [
                            [
                                149,
                                375,
                                204,
                                388
                            ]
                        ],
                        "model_confidence": [
                            99.71430906389303
                        ]
                    },
                    "lc_ref_no": {
                        "value": "0041FLC210044",
                        "coordinate": [
                            [
                                132,
                                404,
                                205,
                                413
                            ]
                        ],
                        "model_confidence": [
                            99.42
                        ]
                    },
                    "lc_date": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                240,
                                404,
                                296,
                                413
                            ]
                        ],
                        "model_confidence": [
                            99.76
                        ]
                    },
                    "net_weight": {
                        "value": "",
                        "coordinate": [
                            [
                                101,
                                421,
                                157,
                                432
                            ]
                        ],
                        "model_confidence": [
                            99.75
                        ]
                    },
                    "gross_weight": {
                        "value": "",
                        "coordinate": [
                            [
                                102,
                                439,
                                158,
                                450
                            ]
                        ],
                        "model_confidence": [
                            99.0
                        ]
                    },
                    "invoice_no": {
                        "value": "CP202130061",
                        "coordinate": [
                            [
                                455,
                                229,
                                515,
                                238
                            ]
                        ],
                        "model_confidence": [
                            99.98
                        ]
                    },
                    "date_of_invoice": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                403,
                                258,
                                457,
                                267
                            ]
                        ],
                        "model_confidence": [
                            99.94
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "20 2",
                        "coordinate": [
                            [
                                367,
                                376,
                                505,
                                385
                            ]
                        ],
                        "model_confidence": [
                            99.87393939393938
                        ]
                    },
                    "country_of_origin_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                182,
                                510,
                                207,
                                521
                            ]
                        ],
                        "model_confidence": [
                            99.83
                        ]
                    },
                    "declaration": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD.",
                        "coordinate": [
                            [
                                354,
                                658,
                                508,
                                672
                            ]
                        ],
                        "model_confidence": [
                            99.67609044688253
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                370,
                                549,
                                489,
                                607
                            ]
                        ],
                        "model_confidence": [
                            0.7046676278114319
                        ]
                    },
                    "is_stamp": {},
                    "beneficiary_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                105,
                                150,
                                487,
                                160
                            ]
                        ],
                        "model_confidence": [
                            99.28833076012303
                        ]
                    },
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                55,
                                247,
                                307,
                                269
                            ]
                        ],
                        "model_confidence": [
                            99.36849374216416
                        ]
                    },
                    "shipper_address": {},
                    "notify_party_address": {},
                    "awb_number": {},
                    "vessel_flight_no": {},
                    "track_reference": {},
                    "notify_party_name": {},
                    "bill_of_lading_date": {},
                    "dimension": {},
                    "transaction_currency": {},
                    "port_of_loading": {},
                    "transaction_date": {},
                    "country_of_final_destination": {},
                    "invoice_amount": {},
                    "shipper_name": {},
                    "transaction_amount_value": {},
                    "consignor_address": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin_no": {},
                    "remitter_address": {},
                    "bill_of_lading_number": {},
                    "rate_per_unit": {},
                    "consignor_name": {},
                    "invoice_currency": {},
                    "pre_carriage_by": {},
                    "incoterm": {},
                    "port_of_discharge": {},
                    "original_copy": {},
                    "awb_date": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_19.png": {
                "docClass": "PL",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD .",
                        "coordinate": [
                            [
                                184,
                                129,
                                392,
                                142
                            ]
                        ],
                        "model_confidence": [
                            99.95012272534913
                        ]
                    },
                    "beneficiary_address": {
                        "value": "MID ZHIYUAN AVENUE BINHAI NEW AREA SHAOXING",
                        "coordinate": [
                            [
                                115,
                                151,
                                310,
                                162
                            ]
                        ],
                        "model_confidence": [
                            82.08125161887008
                        ]
                    },
                    "consignee_name": {
                        "value": "CADCHEM LABORATORIES LTD",
                        "coordinate": [
                            [
                                65,
                                231,
                                229,
                                240
                            ]
                        ],
                        "model_confidence": [
                            99.94
                        ]
                    },
                    "consignee_address": {
                        "value": "ADD PUNJAB VILLAGE  JAUIA KHURD TEHSIL DERA BASSI",
                        "coordinate": [
                            [
                                51,
                                248,
                                301,
                                271
                            ]
                        ],
                        "model_confidence": [
                            99.90402531057495
                        ]
                    },
                    "payment_terms_terms_of_delivery_&_payment": {
                        "value": "L / C 90 DAYS AFTER B / L DATE",
                        "coordinate": [
                            [
                                89,
                                308,
                                234,
                                320
                            ]
                        ],
                        "model_confidence": [
                            99.9543466155468
                        ]
                    },
                    "description_of_goods": {
                        "value": "RIFAMYCIN O",
                        "coordinate": [
                            [
                                146,
                                378,
                                200,
                                388
                            ]
                        ],
                        "model_confidence": [
                            94.23529411764706
                        ]
                    },
                    "lc_ref_no": {
                        "value": "0041FLC210044",
                        "coordinate": [
                            [
                                127,
                                404,
                                199,
                                414
                            ]
                        ],
                        "model_confidence": [
                            99.3
                        ]
                    },
                    "lc_date": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                235,
                                403,
                                291,
                                414
                            ]
                        ],
                        "model_confidence": [
                            99.77
                        ]
                    },
                    "net_weight": {
                        "value": "",
                        "coordinate": [
                            [
                                98,
                                422,
                                154,
                                433
                            ]
                        ],
                        "model_confidence": [
                            99.9
                        ]
                    },
                    "gross_weight": {
                        "value": "",
                        "coordinate": [
                            [
                                99,
                                442,
                                153,
                                452
                            ]
                        ],
                        "model_confidence": [
                            99.45
                        ]
                    },
                    "invoice_no": {
                        "value": "CP202130061",
                        "coordinate": [
                            [
                                450,
                                229,
                                510,
                                238
                            ]
                        ],
                        "model_confidence": [
                            99.98
                        ]
                    },
                    "bill_of_lading_number": {
                        "value": "ZMCAS22112002",
                        "coordinate": [
                            [
                                433,
                                244,
                                516,
                                253
                            ]
                        ],
                        "model_confidence": [
                            6.0
                        ]
                    },
                    "date_of_invoice": {
                        "value": "13-12-2021",
                        "coordinate": [
                            [
                                398,
                                257,
                                451,
                                270
                            ]
                        ],
                        "model_confidence": [
                            99.94
                        ]
                    },
                    "total_quantity_of_goods": {
                        "value": "20 2",
                        "coordinate": [
                            [
                                363,
                                376,
                                499,
                                385
                            ]
                        ],
                        "model_confidence": [
                            99.88633128834356
                        ]
                    },
                    "country_of_origin_origin_of_goods": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                178,
                                511,
                                203,
                                520
                            ]
                        ],
                        "model_confidence": [
                            99.81
                        ]
                    },
                    "declaration": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD.",
                        "coordinate": [
                            [
                                309,
                                649,
                                463,
                                663
                            ]
                        ],
                        "model_confidence": [
                            98.07570810142239
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                324,
                                545,
                                442,
                                603
                            ]
                        ],
                        "model_confidence": [
                            0.6749458312988281
                        ]
                    },
                    "is_stamp": {},
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                51,
                                248,
                                301,
                                271
                            ]
                        ],
                        "model_confidence": [
                            99.90402531057495
                        ]
                    },
                    "shipper_address": {},
                    "notify_party_address": {},
                    "awb_number": {},
                    "vessel_flight_no": {},
                    "track_reference": {},
                    "notify_party_name": {},
                    "bill_of_lading_date": {},
                    "dimension": {},
                    "transaction_currency": {},
                    "port_of_loading": {},
                    "transaction_date": {},
                    "country_of_final_destination": {},
                    "invoice_amount": {},
                    "shipper_name": {},
                    "transaction_amount_value": {},
                    "consignor_address": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin_no": {},
                    "remitter_address": {},
                    "rate_per_unit": {},
                    "consignor_name": {},
                    "invoice_currency": {},
                    "pre_carriage_by": {},
                    "incoterm": {},
                    "port_of_discharge": {},
                    "original_copy": {},
                    "awb_date": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_20.png": {
                "docClass": "COO",
                "keys_extraction": {
                    "consignor_name": {
                        "value": "1. RANG MEDICINE CO . , LTD .",
                        "coordinate": [
                            [
                                61,
                                42,
                                188,
                                49
                            ]
                        ],
                        "model_confidence": [
                            98.26837152516904
                        ]
                    },
                    "consignor_address": {
                        "value": "SHAOXING 168 ZHIYUANZHONG ZHEJIANG AVENUE 312366 BINHAI P R  NEW AREA",
                        "coordinate": [
                            [
                                71,
                                51,
                                250,
                                68
                            ]
                        ],
                        "model_confidence": [
                            98.78799645569934
                        ]
                    },
                    "consignee_name": {
                        "value": "2. CADE LABORATORIES LTD",
                        "coordinate": [
                            [
                                61,
                                114,
                                177,
                                121
                            ]
                        ],
                        "model_confidence": [
                            94.86272727272727
                        ]
                    },
                    "consignee_address": {
                        "value": "VILLAGE PUNJAB 140501 JAULA KHURD  TEHSIL DERA BASSI",
                        "coordinate": [
                            [
                                70,
                                123,
                                233,
                                140
                            ]
                        ],
                        "model_confidence": [
                            98.06508893130928
                        ]
                    },
                    "means_of_transport": {
                        "value": "AIR",
                        "coordinate": [
                            [
                                247,
                                184,
                                260,
                                191
                            ]
                        ],
                        "model_confidence": [
                            96.12
                        ]
                    },
                    "original_or_copy": {
                        "value": "ORIGINAL",
                        "coordinate": [
                            [
                                280,
                                19,
                                342,
                                28
                            ]
                        ],
                        "model_confidence": [
                            98.71
                        ]
                    },
                    "declaration_by_exporter": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD .",
                        "coordinate": [
                            [
                                112,
                                712,
                                266,
                                733
                            ]
                        ],
                        "model_confidence": [
                            99.45810775832707
                        ]
                    },
                    "marks_and_no_of_packages": {
                        "value": "TWENTY ( 20 ) DRUMS",
                        "coordinate": [
                            [
                                167,
                                334,
                                242,
                                341
                            ]
                        ],
                        "model_confidence": [
                            96.65766666666669
                        ]
                    },
                    "description_of_goods": {
                        "value": "RIFAMYCIN O",
                        "coordinate": [
                            [
                                167,
                                344,
                                214,
                                350
                            ]
                        ],
                        "model_confidence": [
                            99.62809523809523
                        ]
                    },
                    "coo_issuer_address": {
                        "value": "THE PEOPLES REPUBLIC OF ",
                        "coordinate": [
                            [
                                330,
                                118,
                                551,
                                128
                            ]
                        ],
                        "model_confidence": [
                            99.79682526078864
                        ]
                    },
                    "certificate_no": {
                        "value": "C211429434690412",
                        "coordinate": [
                            [
                                385,
                                35,
                                456,
                                41
                            ]
                        ],
                        "model_confidence": [
                            97.79
                        ]
                    },
                    "certificate_stamped": {
                        "value": "CUSTOMS [UNK] [UNK]人 AI / THE [UNK]州 PEOPLE ORIGIN CHINA OF MOBL",
                        "coordinate": [
                            [
                                394,
                                657,
                                507,
                                765
                            ]
                        ],
                        "model_confidence": [
                            98.56
                        ]
                    },
                    "signature": {
                        "value": "HANGS",
                        "coordinate": [
                            [
                                394,
                                645,
                                502,
                                743
                            ]
                        ],
                        "model_confidence": [
                            78.27
                        ]
                    },
                    "invoice_no": {
                        "value": "CP202130061",
                        "coordinate": [
                            [
                                522,
                                335,
                                568,
                                343
                            ]
                        ],
                        "model_confidence": [
                            99.66
                        ]
                    },
                    "invoice_date": {
                        "value": "DEC . 20 , 202",
                        "coordinate": [
                            [
                                522,
                                346,
                                570,
                                353
                            ]
                        ],
                        "model_confidence": [
                            99.59928571428573
                        ]
                    },
                    "issue_date": {
                        "value": "D60 , 30 , 2021",
                        "coordinate": [
                            [
                                455,
                                768,
                                509,
                                775
                            ]
                        ],
                        "model_confidence": [
                            85.93333333333334
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE TRUE",
                        "coordinate": [
                            [
                                511,
                                735,
                                574,
                                762
                            ],
                            [
                                257,
                                729,
                                304,
                                766
                            ]
                        ],
                        "model_confidence": [
                            0.5853859782218933,
                            0.6664671897888184
                        ]
                    },
                    "is_stamp": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                390,
                                657,
                                508,
                                774
                            ]
                        ],
                        "model_confidence": [
                            0.8985082507133484
                        ]
                    },
                    "consignor_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                71,
                                51,
                                250,
                                68
                            ]
                        ],
                        "model_confidence": [
                            98.78799645569934
                        ]
                    },
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                70,
                                123,
                                233,
                                140
                            ]
                        ],
                        "model_confidence": [
                            98.06508893130928
                        ]
                    },
                    "coo_issuer_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                330,
                                118,
                                551,
                                128
                            ]
                        ],
                        "model_confidence": [
                            99.79682526078864
                        ]
                    },
                    "vessel_details": {},
                    "country_of_origin_of_goods": {},
                    "original_number": {},
                    "lc_date": {},
                    "declaration_by_certification": {},
                    "ref_no": {},
                    "coo_issuer_name": {},
                    "lc_ref_no": {},
                    "from_place": {},
                    "page_no": {},
                    "gross_weight": {},
                    "net_weight": {},
                    "final_destination": {},
                    "to_place": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_21.png": {
                "docClass": "COO",
                "keys_extraction": {
                    "consignor_name": {
                        "value": "1. ERANG MEDICINE CO . , LTD .",
                        "coordinate": [
                            [
                                75,
                                36,
                                199,
                                46
                            ]
                        ],
                        "model_confidence": [
                            98.51921938026067
                        ]
                    },
                    "consignor_address": {
                        "value": "SHACKING 168 ZHIYUANZHONG ZHEJIANG AVENUE 312366 BINHAI P R  NEW AREA",
                        "coordinate": [
                            [
                                83,
                                47,
                                261,
                                64
                            ]
                        ],
                        "model_confidence": [
                            99.79503398517011
                        ]
                    },
                    "consignee_name": {
                        "value": "CLABORATORIES LTD",
                        "coordinate": [
                            [
                                82,
                                108,
                                189,
                                118
                            ]
                        ],
                        "model_confidence": [
                            94.4806387225549
                        ]
                    },
                    "consignee_address": {
                        "value": "VILLAGE PUNJAB 140501 JAUIA KHURD  TEHSIL DERA BASSI",
                        "coordinate": [
                            [
                                82,
                                120,
                                247,
                                138
                            ]
                        ],
                        "model_confidence": [
                            99.63
                        ]
                    },
                    "means_of_transport": {
                        "value": "AIR",
                        "coordinate": [
                            [
                                260,
                                181,
                                275,
                                188
                            ]
                        ],
                        "model_confidence": [
                            98.88
                        ]
                    },
                    "original_or_copy": {
                        "value": "COPY",
                        "coordinate": [
                            [
                                307,
                                16,
                                343,
                                25
                            ]
                        ],
                        "model_confidence": [
                            97.47
                        ]
                    },
                    "declaration_by_exporter": {
                        "value": "ZHEJIANG MEDICI NE CO . , LTD .",
                        "coordinate": [
                            [
                                131,
                                718,
                                284,
                                735
                            ]
                        ],
                        "model_confidence": [
                            99.26444917909514
                        ]
                    },
                    "marks_and_no_of_packages": {
                        "value": "TWENTY ( 20 ) DRUMS",
                        "coordinate": [
                            [
                                179,
                                331,
                                254,
                                338
                            ]
                        ],
                        "model_confidence": [
                            95.03691511387164
                        ]
                    },
                    "description_of_goods": {
                        "value": "RIFAMYCIN O",
                        "coordinate": [
                            [
                                179,
                                341,
                                228,
                                348
                            ]
                        ],
                        "model_confidence": [
                            99.60333333333332
                        ]
                    },
                    "coo_issuer_address": {
                        "value": "THE PEOPLES REPUBLIC OF ",
                        "coordinate": [
                            [
                                342,
                                117,
                                563,
                                127
                            ]
                        ],
                        "model_confidence": [
                            99.8
                        ]
                    },
                    "certificate_stamped": {
                        "value": "HANGZH CUSTOMS B THE [UNK]州 / PEOP ORIGIN NIHOO HANGZHOU PUBLICOF 2021",
                        "coordinate": [
                            [
                                394,
                                668,
                                521,
                                792
                            ]
                        ],
                        "model_confidence": [
                            99.52957069261592
                        ]
                    },
                    "invoice_no": {
                        "value": "INS130061",
                        "coordinate": [
                            [
                                526,
                                331,
                                579,
                                337
                            ]
                        ],
                        "model_confidence": [
                            99.68
                        ]
                    },
                    "invoice_date": {
                        "value": "DEC . 20 , 202",
                        "coordinate": [
                            [
                                532,
                                340,
                                580,
                                347
                            ]
                        ],
                        "model_confidence": [
                            99.52142857142859
                        ]
                    },
                    "is_signed": {},
                    "is_stamp": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                402,
                                668,
                                526,
                                786
                            ]
                        ],
                        "model_confidence": [
                            0.9098304510116577
                        ]
                    },
                    "consignor_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                83,
                                47,
                                261,
                                64
                            ]
                        ],
                        "model_confidence": [
                            99.79503398517011
                        ]
                    },
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                82,
                                120,
                                247,
                                138
                            ]
                        ],
                        "model_confidence": [
                            99.63
                        ]
                    },
                    "coo_issuer_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                342,
                                117,
                                563,
                                127
                            ]
                        ],
                        "model_confidence": [
                            99.8
                        ]
                    },
                    "certificate_no": {},
                    "vessel_details": {},
                    "country_of_origin_of_goods": {},
                    "original_number": {},
                    "lc_date": {},
                    "declaration_by_certification": {},
                    "ref_no": {},
                    "coo_issuer_name": {},
                    "lc_ref_no": {},
                    "from_place": {},
                    "signature": {},
                    "issue_date": {},
                    "page_no": {},
                    "gross_weight": {},
                    "net_weight": {},
                    "final_destination": {},
                    "to_place": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_22.png": {
                "docClass": "COO",
                "keys_extraction": {
                    "consignor_name": {
                        "value": "1. ENG MEDICINE CO . , LTD .",
                        "coordinate": [
                            [
                                76,
                                37,
                                200,
                                44
                            ]
                        ],
                        "model_confidence": [
                            98.17854536995549
                        ]
                    },
                    "consignor_address": {
                        "value": "SHACKING 168 ZHIYUANZHONG ZHEJIANG AVENUE 312366 BINHAI P R  NEW AREA",
                        "coordinate": [
                            [
                                83,
                                47,
                                263,
                                64
                            ]
                        ],
                        "model_confidence": [
                            99.62782928208027
                        ]
                    },
                    "consignee_name": {
                        "value": "2. CANSIN LABORATORIES LTD",
                        "coordinate": [
                            [
                                75,
                                109,
                                190,
                                116
                            ]
                        ],
                        "model_confidence": [
                            87.67424289960371
                        ]
                    },
                    "consignee_address": {
                        "value": "VILLAGE PUNJAB 140501 JAUTA  KHURD TEHSIL DERA BASSI",
                        "coordinate": [
                            [
                                84,
                                119,
                                248,
                                137
                            ]
                        ],
                        "model_confidence": [
                            99.7135969492755
                        ]
                    },
                    "means_of_transport": {
                        "value": "AIR",
                        "coordinate": [
                            [
                                261,
                                181,
                                275,
                                188
                            ]
                        ],
                        "model_confidence": [
                            98.83
                        ]
                    },
                    "original_or_copy": {
                        "value": "COPY",
                        "coordinate": [
                            [
                                308,
                                15,
                                344,
                                25
                            ]
                        ],
                        "model_confidence": [
                            97.4
                        ]
                    },
                    "declaration_by_exporter": {
                        "value": "UNK江 ZHEJIANG MEDICINE CO . , LTD .",
                        "coordinate": [
                            [
                                116,
                                701,
                                271,
                                740
                            ]
                        ],
                        "model_confidence": [
                            97.41769660985281
                        ]
                    },
                    "marks_and_no_of_packages": {
                        "value": "TWENTY ( 20 ) DRUMS",
                        "coordinate": [
                            [
                                180,
                                331,
                                255,
                                338
                            ]
                        ],
                        "model_confidence": [
                            93.85395818815331
                        ]
                    },
                    "description_of_goods": {
                        "value": "RIFAMYCIN O",
                        "coordinate": [
                            [
                                179,
                                341,
                                228,
                                347
                            ]
                        ],
                        "model_confidence": [
                            99.61045454545453
                        ]
                    },
                    "coo_issuer_address": {
                        "value": "THE PEOPLES REPUBLIC OF ",
                        "coordinate": [
                            [
                                343,
                                116,
                                565,
                                127
                            ]
                        ],
                        "model_confidence": [
                            99.80285593014796
                        ]
                    },
                    "gross_weight": {
                        "value": "5",
                        "coordinate": [
                            [
                                464,
                                330,
                                490,
                                338
                            ]
                        ],
                        "model_confidence": [
                            74.81
                        ]
                    },
                    "certificate_stamped": {
                        "value": "202CHINA HANGZH CUSTOMS THE [UNK]州 V ORIGIN HANGZHOU , CHINA ,",
                        "coordinate": [
                            [
                                569,
                                341,
                                582,
                                348
                            ],
                            [
                                394,
                                671,
                                528,
                                775
                            ]
                        ],
                        "model_confidence": [
                            49.91,
                            97.75315436241611
                        ]
                    },
                    "invoice_no": {
                        "value": "30061",
                        "coordinate": [
                            [
                                560,
                                330,
                                579,
                                337
                            ]
                        ],
                        "model_confidence": [
                            99.64
                        ]
                    },
                    "invoice_date": {
                        "value": "DEC . 20 ,",
                        "coordinate": [
                            [
                                533,
                                341,
                                565,
                                348
                            ]
                        ],
                        "model_confidence": [
                            99.408
                        ]
                    },
                    "is_signed": {},
                    "is_stamp": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                410,
                                671,
                                531,
                                784
                            ]
                        ],
                        "model_confidence": [
                            0.8942466378211975
                        ]
                    },
                    "consignor_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                83,
                                47,
                                263,
                                64
                            ]
                        ],
                        "model_confidence": [
                            99.62782928208027
                        ]
                    },
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                84,
                                119,
                                248,
                                137
                            ]
                        ],
                        "model_confidence": [
                            99.7135969492755
                        ]
                    },
                    "coo_issuer_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                343,
                                116,
                                565,
                                127
                            ]
                        ],
                        "model_confidence": [
                            99.80285593014796
                        ]
                    },
                    "certificate_no": {},
                    "vessel_details": {},
                    "country_of_origin_of_goods": {},
                    "original_number": {},
                    "lc_date": {},
                    "declaration_by_certification": {},
                    "ref_no": {},
                    "coo_issuer_name": {},
                    "lc_ref_no": {},
                    "from_place": {},
                    "signature": {},
                    "issue_date": {},
                    "page_no": {},
                    "net_weight": {},
                    "final_destination": {},
                    "to_place": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_23.png": {
                "docClass": "AWB",
                "keys_extraction": {
                    "house_awb_bill_no": {
                        "value": "13139055402 SHAE21122181",
                        "coordinate": [
                            [
                                65,
                                36,
                                532,
                                48
                            ]
                        ],
                        "model_confidence": [
                            57.519999999999996
                        ]
                    },
                    "shipper_name": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD",
                        "coordinate": [
                            [
                                52,
                                80,
                                192,
                                88
                            ]
                        ],
                        "model_confidence": [
                            97.93462588881708
                        ]
                    },
                    "shipper_address": {
                        "value": "CITY 168 MID ZHEJIANG ZHIYUAN PROVINCE AVENUE BINHAI 312366 NEW PR AREA  SHAOXING",
                        "coordinate": [
                            [
                                52,
                                92,
                                320,
                                112
                            ]
                        ],
                        "model_confidence": [
                            95.396525406295
                        ]
                    },
                    "consignee_name": {
                        "value": "AXIS BANK LTD",
                        "coordinate": [
                            [
                                51,
                                148,
                                122,
                                155
                            ]
                        ],
                        "model_confidence": [
                            98.20617647058823
                        ]
                    },
                    "consignee_address": {
                        "value": "SCO  343344 TELEPHONE SECTOR 35 B CHANDIGARH 160022",
                        "coordinate": [
                            [
                                51,
                                159,
                                290,
                                180
                            ]
                        ],
                        "model_confidence": [
                            85.44380543698065
                        ]
                    },
                    "airport_of_departure": {
                        "value": "PUDONG NEW DELHI",
                        "coordinate": [
                            [
                                49,
                                284,
                                103,
                                344
                            ]
                        ],
                        "model_confidence": [
                            71.21461538461539
                        ]
                    },
                    "notify_party_name": {
                        "value": "CADCHEM LABORATORIES LIMITED",
                        "coordinate": [
                            [
                                51,
                                217,
                                213,
                                224
                            ]
                        ],
                        "model_confidence": [
                            85.56131535498075
                        ]
                    },
                    "notify_party_address": {
                        "value": "VILLAGE SAS NAGAR JAULA PUNJAB KHURD 140501 TEHSIL  DERABASSI DISTRICT",
                        "coordinate": [
                            [
                                50,
                                228,
                                298,
                                246
                            ]
                        ],
                        "model_confidence": [
                            94.13604113110539
                        ]
                    },
                    "gross_weight": {
                        "value": "6 3",
                        "coordinate": [
                            [
                                72,
                                424,
                                98,
                                431
                            ],
                            [
                                430,
                                564,
                                475,
                                571
                            ]
                        ],
                        "model_confidence": [
                            94.31,
                            70.93
                        ]
                    },
                    "flight_details": {
                        "value": "JL086 / 27",
                        "coordinate": [
                            [
                                180,
                                334,
                                223,
                                347
                            ]
                        ],
                        "model_confidence": [
                            81.39
                        ]
                    },
                    "flight_date": {
                        "value": ", DEC 2021",
                        "coordinate": [
                            [
                                221,
                                334,
                                269,
                                346
                            ]
                        ],
                        "model_confidence": [
                            25.795652173913044
                        ]
                    },
                    "awb_bill_issue_date": {
                        "value": " 23 , DEC 2021",
                        "coordinate": [
                            [
                                239,
                                334,
                                245,
                                346
                            ],
                            [
                                243,
                                726,
                                300,
                                734
                            ]
                        ],
                        "model_confidence": [
                            38.18,
                            95.77355329949238
                        ]
                    },
                    "carriage_condition": {
                        "value": "SHIPPER CONSIGNMENT FOR CARRIAGE CERTIFIES CONTAINS THAT PARTICUL BY AIR ACCORDING DANGE AS AND ANY IS PART IN PROPER OF THE CONDITION",
                        "coordinate": [
                            [
                                241,
                                652,
                                552,
                                673
                            ]
                        ],
                        "model_confidence": [
                            85.06664845079291
                        ]
                    },
                    "stamp": {
                        "value": "ABB BEDING SHANGH O OF CABE S DANGERGES INSOFAR PS Y NAME . RE",
                        "coordinate": [
                            [
                                327,
                                635,
                                476,
                                714
                            ]
                        ],
                        "model_confidence": [
                            46.96267990952896
                        ]
                    },
                    "freight_collect_or_prepaid": {
                        "value": "FREIGHT COLLECT",
                        "coordinate": [
                            [
                                385,
                                231,
                                470,
                                237
                            ]
                        ],
                        "model_confidence": [
                            96.55
                        ]
                    },
                    "signature": {
                        "value": "PANDA GLOBAL ( ERING VONA Y PER",
                        "coordinate": [
                            [
                                243,
                                678,
                                522,
                                751
                            ]
                        ],
                        "model_confidence": [
                            36.93957741900595
                        ]
                    },
                    "signed_by_agent": {
                        "value": "CO.LTD ) CO . LTD SHANGHA BRANCH OF SHIPPOTHIS",
                        "coordinate": [
                            [
                                359,
                                638,
                                499,
                                713
                            ]
                        ],
                        "model_confidence": [
                            38.05389110732863
                        ]
                    },
                    "declared_value_of_custom": {
                        "value": "N.V.D N.C.V",
                        "coordinate": [
                            [
                                453,
                                311,
                                551,
                                319
                            ]
                        ],
                        "model_confidence": [
                            58.017699115044245
                        ]
                    },
                    "at_place": {
                        "value": "SHANGHAI",
                        "coordinate": [
                            [
                                361,
                                726,
                                410,
                                733
                            ]
                        ],
                        "model_confidence": [
                            54.31
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                461,
                                670,
                                517,
                                753
                            ]
                        ],
                        "model_confidence": [
                            0.5106271505355835
                        ]
                    },
                    "is_stamp": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                324,
                                630,
                                459,
                                726
                            ]
                        ],
                        "model_confidence": [
                            0.8568122982978821
                        ]
                    },
                    "shipper_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                52,
                                92,
                                320,
                                112
                            ]
                        ],
                        "model_confidence": [
                            95.396525406295
                        ]
                    },
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                51,
                                159,
                                290,
                                180
                            ]
                        ],
                        "model_confidence": [
                            85.44380543698065
                        ]
                    },
                    "notify_party_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                50,
                                228,
                                298,
                                246
                            ]
                        ],
                        "model_confidence": [
                            94.13604113110539
                        ]
                    },
                    "declared_value_of_carriage": {},
                    "dimension": {},
                    "lc_no": {},
                    "carrier_name": {},
                    "agent_name": {},
                    "master_awb_bill_no": {},
                    "airport_of_destination": {},
                    "agent_address": {},
                    "invoice_date": {},
                    "place_of_receipt": {},
                    "signed_by_carrier": {},
                    "transaction_date": {},
                    "final_destination": {},
                    "net_weight": {},
                    "awb_original_or_copy": {},
                    "gross_quantity": {},
                    "invoice_number": {},
                    "lc_date": {},
                    "carrier_address": {},
                    "amount_insurance": {},
                    "flight_no": {},
                    "freight_collected_at": {},
                    "awb_original_number": {},
                    "awb_bill_no": {},
                    "good_marks": {},
                    "goods_description": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_24.png": {
                "docClass": "AWB",
                "keys_extraction": {}
            },
            "0041FLC210044_25.png": {
                "docClass": "AWB",
                "keys_extraction": {
                    "house_awb_bill_no": {
                        "value": "13139055402 SHAE21122181",
                        "coordinate": [
                            [
                                66,
                                32,
                                533,
                                47
                            ]
                        ],
                        "model_confidence": [
                            69.965
                        ]
                    },
                    "shipper_name": {
                        "value": "AXIS BANK LTD",
                        "coordinate": [
                            [
                                51,
                                145,
                                124,
                                153
                            ]
                        ],
                        "model_confidence": [
                            97.111
                        ]
                    },
                    "shipper_address": {
                        "value": "SCO  343344 SECTOR 35 B CHANDIGARH 160022",
                        "coordinate": [
                            [
                                52,
                                157,
                                290,
                                176
                            ]
                        ],
                        "model_confidence": [
                            99.11883076255842
                        ]
                    },
                    "consignee_name": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD",
                        "coordinate": [
                            [
                                52,
                                79,
                                192,
                                86
                            ]
                        ],
                        "model_confidence": [
                            98.12672133836313
                        ]
                    },
                    "consignee_address": {
                        "value": "168 CITY MID ZHEJIANG ZHIYUAN PROVINCE AVENUE BINHAI 312366 NEW PR AREA  SHAOXING",
                        "coordinate": [
                            [
                                53,
                                91,
                                320,
                                111
                            ]
                        ],
                        "model_confidence": [
                            98.46435904957465
                        ]
                    },
                    "notify_party_name": {
                        "value": "CADCHEM LABORATORIES LIMITED",
                        "coordinate": [
                            [
                                51,
                                214,
                                211,
                                223
                            ]
                        ],
                        "model_confidence": [
                            85.44986184477854
                        ]
                    },
                    "notify_party_address": {
                        "value": "VIL SAS NAGAR JAULA PUNJAB KHURD 140501 TEHSIL  DERABASSI DISTRICT",
                        "coordinate": [
                            [
                                50,
                                226,
                                297,
                                245
                            ]
                        ],
                        "model_confidence": [
                            94.89664092664093
                        ]
                    },
                    "airport_of_departure": {
                        "value": "PUDONG",
                        "coordinate": [
                            [
                                50,
                                284,
                                88,
                                291
                            ]
                        ],
                        "model_confidence": [
                            87.5
                        ]
                    },
                    "airport_of_destination": {
                        "value": "NEW DELHI",
                        "coordinate": [
                            [
                                51,
                                335,
                                102,
                                342
                            ]
                        ],
                        "model_confidence": [
                            53.844610169491524
                        ]
                    },
                    "gross_weight": {
                        "value": "6 3",
                        "coordinate": [
                            [
                                72,
                                424,
                                96,
                                430
                            ],
                            [
                                429,
                                562,
                                472,
                                569
                            ]
                        ],
                        "model_confidence": [
                            94.1,
                            66.29
                        ]
                    },
                    "flight_details": {
                        "value": "JL086 / 27",
                        "coordinate": [
                            [
                                180,
                                334,
                                222,
                                346
                            ]
                        ],
                        "model_confidence": [
                            79.91
                        ]
                    },
                    "flight_date": {
                        "value": ", DEC 2021",
                        "coordinate": [
                            [
                                220,
                                333,
                                267,
                                345
                            ]
                        ],
                        "model_confidence": [
                            30.362914979757083
                        ]
                    },
                    "awb_bill_issue_date": {
                        "value": "23 , DEC 2021",
                        "coordinate": [
                            [
                                242,
                                724,
                                298,
                                733
                            ]
                        ],
                        "model_confidence": [
                            95.62326923076922
                        ]
                    },
                    "carriage_condition": {
                        "value": "PART NAME AS AND IN THE ANY IS OF PROPER CONDITION CONSIGNMENT FOR SHIPPER CARRIAGE CERTIFIES BY CONTAINS AIR THAT PARTICULAR",
                        "coordinate": [
                            [
                                241,
                                651,
                                552,
                                672
                            ]
                        ],
                        "model_confidence": [
                            72.249841015238
                        ]
                    },
                    "stamp": {
                        "value": "BELING CO . , LTD . ACCORDING DANGERG 7980 SHANGHA SOFAR PANDA GLOBAL ( BNG T DANGERY VORYA ) SO LA GOD NGHAT BRANCH SHANGHAI MRY",
                        "coordinate": [
                            [
                                243,
                                637,
                                497,
                                732
                            ]
                        ],
                        "model_confidence": [
                            63.779785347117084
                        ]
                    },
                    "declared_value_of_custom": {
                        "value": "N.V.D N.C.V",
                        "coordinate": [
                            [
                                452,
                                311,
                                551,
                                318
                            ]
                        ],
                        "model_confidence": [
                            60.97923076923077
                        ]
                    },
                    "freight_collect_or_prepaid": {
                        "value": "FREIGHT COLLECT",
                        "coordinate": [
                            [
                                385,
                                231,
                                470,
                                237
                            ]
                        ],
                        "model_confidence": [
                            96.5
                        ]
                    },
                    "is_signed": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                458,
                                673,
                                513,
                                757
                            ]
                        ],
                        "model_confidence": [
                            0.5362411141395569
                        ]
                    },
                    "is_stamp": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                327,
                                632,
                                463,
                                726
                            ]
                        ],
                        "model_confidence": [
                            0.864861249923706
                        ]
                    },
                    "shipper_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                52,
                                157,
                                290,
                                176
                            ]
                        ],
                        "model_confidence": [
                            99.11883076255842
                        ]
                    },
                    "consignee_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                53,
                                91,
                                320,
                                111
                            ]
                        ],
                        "model_confidence": [
                            98.46435904957465
                        ]
                    },
                    "notify_party_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                50,
                                226,
                                297,
                                245
                            ]
                        ],
                        "model_confidence": [
                            94.89664092664093
                        ]
                    },
                    "declared_value_of_carriage": {},
                    "dimension": {},
                    "lc_no": {},
                    "carrier_name": {},
                    "agent_name": {},
                    "master_awb_bill_no": {},
                    "signature": {},
                    "agent_address": {},
                    "invoice_date": {},
                    "at_place": {},
                    "place_of_receipt": {},
                    "signed_by_carrier": {},
                    "transaction_date": {},
                    "final_destination": {},
                    "net_weight": {},
                    "awb_original_or_copy": {},
                    "gross_quantity": {},
                    "invoice_number": {},
                    "lc_date": {},
                    "carrier_address": {},
                    "amount_insurance": {},
                    "signed_by_agent": {},
                    "flight_no": {},
                    "freight_collected_at": {},
                    "awb_original_number": {},
                    "awb_bill_no": {},
                    "good_marks": {},
                    "goods_description": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_26.png": {
                "docClass": "AWB",
                "keys_extraction": {
                    "house_awb_bill_no": {
                        "value": "13139055402 SHAE21122181",
                        "coordinate": [
                            [
                                66,
                                33,
                                534,
                                47
                            ]
                        ],
                        "model_confidence": [
                            71.095
                        ]
                    },
                    "shipper_name": {
                        "value": "AXIS BANK LTD",
                        "coordinate": [
                            [
                                51,
                                145,
                                122,
                                152
                            ]
                        ],
                        "model_confidence": [
                            95.35411764705881
                        ]
                    },
                    "shipper_address": {
                        "value": "SCO  343344 SECTOR 35 B CHANDIGARH 160022",
                        "coordinate": [
                            [
                                52,
                                157,
                                290,
                                176
                            ]
                        ],
                        "model_confidence": [
                            99.12880503181299
                        ]
                    },
                    "consignee_name": {
                        "value": "ZHEJIANG MEDICINE CO . , LTD",
                        "coordinate": [
                            [
                                52,
                                79,
                                191,
                                88
                            ]
                        ],
                        "model_confidence": [
                            97.79348237968927
                        ]
                    },
                    "consignee_address": {
                        "value": "CITY 168 MID ZHEJIANG ZHIYUAN PROVINCE AVENUE BINHAI 312366 NEW PR AREA  SHAOXING",
                        "coordinate": [
                            [
                                52,
                                92,
                                320,
                                112
                            ]
                        ],
                        "model_confidence": [
                            98.09760365331837
                        ]
                    },
                    "notify_party_name": {
                        "value": "CADCHEM LABORATORIES LIMITED",
                        "coordinate": [
                            [
                                51,
                                214,
                                213,
                                222
                            ]
                        ],
                        "model_confidence": [
                            85.32698867421719
                        ]
                    },
                    "notify_party_address": {
                        "value": "VILLAGE SAS NAGAR JAULA PUNJAB KHURD 140501 TEHSIL  DERABASSI DISTRICT",
                        "coordinate": [
                            [
                                50,
                                226,
                                297,
                                246
                            ]
                        ],
                        "model_confidence": [
                            95.01357474466108
                        ]
                    },
                    "airport_of_departure": {
                        "value": "PUDONG",
                        "coordinate": [
                            [
                                49,
                                284,
                                88,
                                291
                            ]
                        ],
                        "model_confidence": [
                            85.38
                        ]
                    },
                    "airport_of_destination": {
                        "value": "NEW DELHI",
                        "coordinate": [
                            [
                                51,
                                335,
                                103,
                                342
                            ]
                        ],
                        "model_confidence": [
                            59.240212765957445
                        ]
                    },
                    "gross_weight": {
                        "value": "6 3",
                        "coordinate": [
                            [
                                72,
                                423,
                                98,
                                429
                            ],
                            [
                                428,
                                561,
                                472,
                                570
                            ]
                        ],
                        "model_confidence": [
                            92.78,
                            26.51
                        ]
                    },
                    "flight_details": {
                        "value": "L086 / 27 , 2021",
                        "coordinate": [
                            [
                                184,
                                333,
                                266,
                                344
                            ]
                        ],
                        "model_confidence": [
                            53.14189107413011
                        ]
                    },
                    "flight_date": {
                        "value": "DEC ",
                        "coordinate": [
                            [
                                224,
                                333,
                                244,
                                343
                            ]
                        ],
                        "model_confidence": [
                            31.58
                        ]
                    },
                    "awb_bill_issue_date": {
                        "value": "23 , DEC 2021",
                        "coordinate": [
                            [
                                242,
                                726,
                                299,
                                733
                            ]
                        ],
                        "model_confidence": [
                            95.13716981132076
                        ]
                    },
                    "freight_collect_or_prepaid": {
                        "value": "FREIGHT COLLECT",
                        "coordinate": [
                            [
                                383,
                                231,
                                468,
                                237
                            ]
                        ],
                        "model_confidence": [
                            96.54
                        ]
                    },
                    "carriage_condition": {
                        "value": "SHIPPER CERNES THAT PARTICULARS ON FOR CONSIGNMENT CARRIAGE BY CONTAINS AIR ACCORDING DANGEROUS TO AS AND ANY PART OF THE IS IN PROPER CONDITION",
                        "coordinate": [
                            [
                                239,
                                651,
                                553,
                                674
                            ]
                        ],
                        "model_confidence": [
                            83.9498674929703
                        ]
                    },
                    "stamp": {
                        "value": "MING ) CO.LTD SHAROUA INGERGUS FAR ME [UNK][UNK] [UNK][UNK] [UNK] RA SIGNATE",
                        "coordinate": [
                            [
                                367,
                                639,
                                482,
                                762
                            ]
                        ],
                        "model_confidence": [
                            39.40429058576806
                        ]
                    },
                    "signed_by_agent": {
                        "value": " BENG CO , LTD SHANGHAI GOODS P BRANCH",
                        "coordinate": [
                            [
                                317,
                                666,
                                496,
                                686
                            ]
                        ],
                        "model_confidence": [
                            42.12883646539651
                        ]
                    },
                    "signature": {
                        "value": "WITH SHANGHAI",
                        "coordinate": [
                            [
                                360,
                                697,
                                429,
                                733
                            ]
                        ],
                        "model_confidence": [
                            29.4
                        ]
                    },
                    "declared_value_of_custom": {
                        "value": "N.V.D N.C.V",
                        "coordinate": [
                            [
                                452,
                                311,
                                551,
                                318
                            ]
                        ],
                        "model_confidence": [
                            62.382869565217405
                        ]
                    },
                    "is_signed": {},
                    "is_stamp": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                335,
                                634,
                                472,
                                726
                            ]
                        ],
                        "model_confidence": [
                            0.8981873989105225
                        ]
                    },
                    "shipper_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                52,
                                157,
                                290,
                                176
                            ]
                        ],
                        "model_confidence": [
                            99.12880503181299
                        ]
                    },
                    "consignee_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                52,
                                92,
                                320,
                                112
                            ]
                        ],
                        "model_confidence": [
                            98.09760365331837
                        ]
                    },
                    "notify_party_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                50,
                                226,
                                297,
                                246
                            ]
                        ],
                        "model_confidence": [
                            95.01357474466108
                        ]
                    },
                    "declared_value_of_carriage": {},
                    "dimension": {},
                    "lc_no": {},
                    "carrier_name": {},
                    "agent_name": {},
                    "master_awb_bill_no": {},
                    "agent_address": {},
                    "invoice_date": {},
                    "at_place": {},
                    "place_of_receipt": {},
                    "signed_by_carrier": {},
                    "transaction_date": {},
                    "final_destination": {},
                    "net_weight": {},
                    "awb_original_or_copy": {},
                    "gross_quantity": {},
                    "invoice_number": {},
                    "lc_date": {},
                    "carrier_address": {},
                    "amount_insurance": {},
                    "flight_no": {},
                    "freight_collected_at": {},
                    "awb_original_number": {},
                    "awb_bill_no": {},
                    "good_marks": {},
                    "goods_description": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_27.png": {
                "docClass": "AWB",
                "keys_extraction": {
                    "house_awb_bill_no": {
                        "value": "303130055102 SHAE21122181",
                        "coordinate": [
                            [
                                50,
                                30,
                                533,
                                47
                            ]
                        ],
                        "model_confidence": [
                            32.675
                        ]
                    },
                    "shipper_name": {
                        "value": "AXIS LTD",
                        "coordinate": [
                            [
                                52,
                                145,
                                123,
                                152
                            ]
                        ],
                        "model_confidence": [
                            60.13538461538461
                        ]
                    },
                    "consignee_name": {
                        "value": "ZHEDTANG MEDICINE CO . , LTD BANK",
                        "coordinate": [
                            [
                                52,
                                79,
                                191,
                                152
                            ]
                        ],
                        "model_confidence": [
                            90.58322352756241
                        ]
                    },
                    "shipper_address": {
                        "value": " 900 343344 SECTOR 358 CHANDIGARH 160022",
                        "coordinate": [
                            [
                                52,
                                157,
                                290,
                                175
                            ]
                        ],
                        "model_confidence": [
                            98.73921636882541
                        ]
                    },
                    "consignee_address": {
                        "value": "CITY 165 MID ZHEJIANG ZHIYUAN PROVINCE AVENUE BINHAL 312366 NEW PR AREA  SHAOXING",
                        "coordinate": [
                            [
                                52,
                                91,
                                320,
                                109
                            ]
                        ],
                        "model_confidence": [
                            98.26611171490414
                        ]
                    },
                    "notify_party_name": {
                        "value": "CADCHEN LABORATORIES LIMITED",
                        "coordinate": [
                            [
                                51,
                                214,
                                212,
                                221
                            ]
                        ],
                        "model_confidence": [
                            85.23216560509553
                        ]
                    },
                    "notify_party_address": {
                        "value": "VILLAGE SAS NAGAR JAULA PUNJAB KHURD 140501 TEHSIL  DERABASSI DISTRICT",
                        "coordinate": [
                            [
                                50,
                                225,
                                297,
                                243
                            ]
                        ],
                        "model_confidence": [
                            95.0439588688946
                        ]
                    },
                    "airport_of_destination": {
                        "value": "NEW",
                        "coordinate": [
                            [
                                51,
                                334,
                                71,
                                342
                            ]
                        ],
                        "model_confidence": [
                            57.33
                        ]
                    },
                    "airport_of_departure": {
                        "value": "DELHI",
                        "coordinate": [
                            [
                                74,
                                334,
                                104,
                                342
                            ]
                        ],
                        "model_confidence": [
                            45.23
                        ]
                    },
                    "flight_details": {
                        "value": "10086727 ,",
                        "coordinate": [
                            [
                                180,
                                334,
                                226,
                                343
                            ]
                        ],
                        "model_confidence": [
                            78.1
                        ]
                    },
                    "flight_date": {
                        "value": "DEC",
                        "coordinate": [
                            [
                                225,
                                334,
                                243,
                                343
                            ]
                        ],
                        "model_confidence": [
                            16.55
                        ]
                    },
                    "awb_bill_issue_date": {
                        "value": "23 , DEC 2021",
                        "coordinate": [
                            [
                                243,
                                724,
                                298,
                                732
                            ]
                        ],
                        "model_confidence": [
                            95.2969129287599
                        ]
                    },
                    "carriage_condition": {
                        "value": "AND ANY IS PART IN PROPER OF THE CONDITION SHIPPER CONSIGNMENT FOR CARRIAGE CERTIFIES BY CONTAIN AIR THAT ACCORDING PARTICULARS DANGEROUS TO THE ON GOOG THE",
                        "coordinate": [
                            [
                                242,
                                651,
                                553,
                                672
                            ]
                        ],
                        "model_confidence": [
                            78.68464488750213
                        ]
                    },
                    "stamp": {
                        "value": "BEKING ) CO - O SOFAR AS BELINSO A ME [UNK][UNK] [UNK][UNK]章 NCH SHARSHAL PAR ORHISAN HSAYER PAR ( PLACE ) OF",
                        "coordinate": [
                            [
                                321,
                                637,
                                496,
                                762
                            ]
                        ],
                        "model_confidence": [
                            68.30815505151564
                        ]
                    },
                    "freight_collect_or_prepaid": {
                        "value": "FREIGHT COLLECT",
                        "coordinate": [
                            [
                                384,
                                229,
                                469,
                                236
                            ]
                        ],
                        "model_confidence": [
                            96.51
                        ]
                    },
                    "declared_value_of_custom": {
                        "value": "N.V.D N.C.V",
                        "coordinate": [
                            [
                                452,
                                311,
                                550,
                                317
                            ]
                        ],
                        "model_confidence": [
                            61.63264150943397
                        ]
                    },
                    "gross_weight": {
                        "value": "3",
                        "coordinate": [
                            [
                                429,
                                562,
                                472,
                                569
                            ]
                        ],
                        "model_confidence": [
                            88.03
                        ]
                    },
                    "is_signed": {},
                    "is_stamp": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                344,
                                644,
                                481,
                                733
                            ]
                        ],
                        "model_confidence": [
                            0.9079728722572327
                        ]
                    },
                    "shipper_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                52,
                                157,
                                290,
                                175
                            ]
                        ],
                        "model_confidence": [
                            98.73921636882541
                        ]
                    },
                    "consignee_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                52,
                                91,
                                320,
                                109
                            ]
                        ],
                        "model_confidence": [
                            98.26611171490414
                        ]
                    },
                    "notify_party_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                50,
                                225,
                                297,
                                243
                            ]
                        ],
                        "model_confidence": [
                            95.0439588688946
                        ]
                    },
                    "declared_value_of_carriage": {},
                    "dimension": {},
                    "lc_no": {},
                    "carrier_name": {},
                    "agent_name": {},
                    "master_awb_bill_no": {},
                    "signature": {},
                    "agent_address": {},
                    "invoice_date": {},
                    "at_place": {},
                    "place_of_receipt": {},
                    "signed_by_carrier": {},
                    "transaction_date": {},
                    "final_destination": {},
                    "net_weight": {},
                    "awb_original_or_copy": {},
                    "gross_quantity": {},
                    "invoice_number": {},
                    "lc_date": {},
                    "carrier_address": {},
                    "amount_insurance": {},
                    "signed_by_agent": {},
                    "flight_no": {},
                    "freight_collected_at": {},
                    "awb_original_number": {},
                    "awb_bill_no": {},
                    "good_marks": {},
                    "goods_description": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_28.png": {
                "docClass": "AWB",
                "keys_extraction": {
                    "shipper_name": {
                        "value": "ZHERANG MEDICINE CO . , LTD .",
                        "coordinate": [
                            [
                                52,
                                79,
                                196,
                                87
                            ]
                        ],
                        "model_confidence": [
                            94.96784868879091
                        ]
                    },
                    "shipper_address": {
                        "value": "CITY 168 MED ZHEMANG ZHIYUAN PROVINCE AVENUE BINHAI 312366 NEW PR AREA  SHAOXING",
                        "coordinate": [
                            [
                                52,
                                92,
                                320,
                                111
                            ]
                        ],
                        "model_confidence": [
                            97.01005643518548
                        ]
                    },
                    "consignee_name": {
                        "value": "AXIS BANK LT10",
                        "coordinate": [
                            [
                                51,
                                146,
                                121,
                                153
                            ]
                        ],
                        "model_confidence": [
                            98.11029850746267
                        ]
                    },
                    "consignee_address": {
                        "value": " 900 343 TEREPHONE 344 SECTOR 356 CHANDIGARH 160022",
                        "coordinate": [
                            [
                                51,
                                157,
                                290,
                                177
                            ]
                        ],
                        "model_confidence": [
                            86.01364320483262
                        ]
                    },
                    "notify_party_name": {
                        "value": "CADCHEN LABORATORIES LIMITED",
                        "coordinate": [
                            [
                                51,
                                214,
                                213,
                                222
                            ]
                        ],
                        "model_confidence": [
                            84.17319207484864
                        ]
                    },
                    "notify_party_address": {
                        "value": "VILLAGE SAS NAGAR JAULA PUNJAB KHURD 140501 TEHSIL  DERABASSI DISTRIC",
                        "coordinate": [
                            [
                                51,
                                226,
                                292,
                                246
                            ]
                        ],
                        "model_confidence": [
                            94.30496732026144
                        ]
                    },
                    "airport_of_departure": {
                        "value": "PUDONG",
                        "coordinate": [
                            [
                                49,
                                283,
                                88,
                                292
                            ]
                        ],
                        "model_confidence": [
                            83.32
                        ]
                    },
                    "airport_of_destination": {
                        "value": "NEW DELHI",
                        "coordinate": [
                            [
                                51,
                                335,
                                104,
                                342
                            ]
                        ],
                        "model_confidence": [
                            53.39
                        ]
                    },
                    "gross_weight": {
                        "value": "6",
                        "coordinate": [
                            [
                                73,
                                422,
                                99,
                                430
                            ]
                        ],
                        "model_confidence": [
                            94.5
                        ]
                    },
                    "awb_bill_issue_date": {
                        "value": "23 , DEC 2021",
                        "coordinate": [
                            [
                                243,
                                724,
                                300,
                                733
                            ]
                        ],
                        "model_confidence": [
                            95.46318385650224
                        ]
                    },
                    "freight_collect_or_prepaid": {
                        "value": "FREIGHT COLLECT",
                        "coordinate": [
                            [
                                384,
                                229,
                                468,
                                236
                            ]
                        ],
                        "model_confidence": [
                            96.52
                        ]
                    },
                    "declared_value_of_custom": {
                        "value": "N.V.D N.C.V",
                        "coordinate": [
                            [
                                453,
                                310,
                                549,
                                318
                            ]
                        ],
                        "model_confidence": [
                            62.31
                        ]
                    },
                    "signature": {
                        "value": "BENINGL . PANDA GLOBAL",
                        "coordinate": [
                            [
                                243,
                                644,
                                391,
                                685
                            ]
                        ],
                        "model_confidence": [
                            42.675296183293995
                        ]
                    },
                    "stamp": {
                        "value": "CO . LTD 897 ( BSG TO G CO.LTD.SHANGHAEBRANCH [UNK][UNK] [UNK][UNK]章 」 OF SHIPTAR RB",
                        "coordinate": [
                            [
                                318,
                                645,
                                499,
                                729
                            ]
                        ],
                        "model_confidence": [
                            44.77173618462661
                        ]
                    },
                    "house_awb_bill_no": {
                        "value": "SHAB21122181",
                        "coordinate": [
                            [
                                463,
                                37,
                                533,
                                45
                            ]
                        ],
                        "model_confidence": [
                            74.03
                        ]
                    },
                    "at_place": {
                        "value": "SHANGHAT",
                        "coordinate": [
                            [
                                361,
                                723,
                                411,
                                731
                            ]
                        ],
                        "model_confidence": [
                            33.98
                        ]
                    },
                    "carriage_condition": {
                        "value": "SHIPPER CONSIGNMENT CES CONTAINS THAT PARTICULARS FOR CARRIAGE BY ACCORDING DANGEROU ON AIR SOFAR NAME AS AND ANY PART OF THE IS IN PROPER CONDITION",
                        "coordinate": [
                            [
                                242,
                                651,
                                553,
                                673
                            ]
                        ],
                        "model_confidence": [
                            87.39134114807877
                        ]
                    },
                    "net_weight": {
                        "value": "3",
                        "coordinate": [
                            [
                                429,
                                560,
                                476,
                                569
                            ]
                        ],
                        "model_confidence": [
                            24.83
                        ]
                    },
                    "is_signed": {},
                    "is_stamp": {
                        "value": "TRUE",
                        "coordinate": [
                            [
                                332,
                                639,
                                468,
                                729
                            ]
                        ],
                        "model_confidence": [
                            0.8983758091926575
                        ]
                    },
                    "shipper_address_country": {
                        "value": "CHINA",
                        "coordinate": [
                            [
                                52,
                                92,
                                320,
                                111
                            ]
                        ],
                        "model_confidence": [
                            97.01005643518548
                        ]
                    },
                    "consignee_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                51,
                                157,
                                290,
                                177
                            ]
                        ],
                        "model_confidence": [
                            86.01364320483262
                        ]
                    },
                    "notify_party_address_country": {
                        "value": "INDIA",
                        "coordinate": [
                            [
                                51,
                                226,
                                292,
                                246
                            ]
                        ],
                        "model_confidence": [
                            94.30496732026144
                        ]
                    },
                    "declared_value_of_carriage": {},
                    "flight_details": {},
                    "flight_date": {},
                    "dimension": {},
                    "lc_no": {},
                    "carrier_name": {},
                    "agent_name": {},
                    "master_awb_bill_no": {},
                    "agent_address": {},
                    "invoice_date": {},
                    "place_of_receipt": {},
                    "signed_by_carrier": {},
                    "transaction_date": {},
                    "final_destination": {},
                    "awb_original_or_copy": {},
                    "gross_quantity": {},
                    "invoice_number": {},
                    "lc_date": {},
                    "carrier_address": {},
                    "amount_insurance": {},
                    "signed_by_agent": {},
                    "flight_no": {},
                    "freight_collected_at": {},
                    "awb_original_number": {},
                    "awb_bill_no": {},
                    "good_marks": {},
                    "goods_description": {}
                },
                "status_code": "200"
            },
            "0041FLC210044_29.png": {
                "docClass": "OTHERS",
                "keys_extraction": {}
            },
            "0041FLC210044_30.png": {
                "docClass": "OTHERS",
                "keys_extraction": {}
            },
            "0041FLC210044_31.png": {
                "docClass": "AWB",
                "keys_extraction": {
                    "carriage_condition": {
                        "value": "GOOD THE OF CARRIAGE THE AIRWAYBILL THE OF THE",
                        "coordinate": [
                            [
                                313,
                                418,
                                377,
                                424
                            ],
                            [
                                342,
                                528,
                                407,
                                534
                            ]
                        ],
                        "model_confidence": [
                            68.4235806451613,
                            70.36865800865802
                        ]
                    },
                    "house_awb_bill_no": {
                        "value": "83991H2",
                        "coordinate": [
                            [
                                310,
                                26,
                                355,
                                36
                            ]
                        ],
                        "model_confidence": [
                            83.78
                        ]
                    },
                    "declared_value_of_carriage": {},
                    "flight_details": {},
                    "flight_date": {},
                    "freight_collect_or_prepaid": {},
                    "notify_party_name": {},
                    "airport_of_departure": {},
                    "stamp": {},
                    "dimension": {},
                    "notify_party_address": {},
                    "lc_no": {},
                    "carrier_name": {},
                    "gross_weight": {},
                    "agent_name": {},
                    "master_awb_bill_no": {},
                    "airport_of_destination": {},
                    "signature": {},
                    "agent_address": {},
                    "shipper_name": {},
                    "invoice_date": {},
                    "at_place": {},
                    "place_of_receipt": {},
                    "signed_by_carrier": {},
                    "transaction_date": {},
                    "final_destination": {},
                    "net_weight": {},
                    "awb_original_or_copy": {},
                    "gross_quantity": {},
                    "declared_value_of_custom": {},
                    "invoice_number": {},
                    "lc_date": {},
                    "shipper_address": {},
                    "carrier_address": {},
                    "amount_insurance": {},
                    "signed_by_agent": {},
                    "flight_no": {},
                    "freight_collected_at": {},
                    "awb_original_number": {},
                    "awb_bill_no": {},
                    "good_marks": {},
                    "consignee_address": {},
                    "goods_description": {},
                    "awb_bill_issue_date": {},
                    "consignee_name": {}
                },
                "status_code": "200"
            }
        }
        }

	res = {}
	for doc,keys in DOC_Wise_Primary_Key_name.items():
		res[doc] = {}
		for k in keys:
			for img_name,img_values in PDF_2_EX['extraction_result'].items():
				if img_values['docClass'] == doc:
					res[doc].setdefault(k,[]).append({img_name:img_values['keys_extraction'].get(k,{}).get('value',"")})
	return res

if __name__ == "__main__":
	main()
	OCR()
	# res = necessary_keys_in_extraction()
	# print(res)
