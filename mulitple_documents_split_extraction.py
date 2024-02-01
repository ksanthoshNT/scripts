import datetime
import json
import os

from fuzzywuzzy import fuzz

extraction_results = {"results":
    {

        "page9": {
            "docClass": "CI",
            "keys_extraction": {
                "beneficiary_drawer_exporter_seller_supplier_name": {
                    "value": "ZHEJIANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            771,
                            543,
                            1636,
                            596
                        ]
                    ],
                    "model_confidence": [
                        99.36705843943847
                    ]
                },
                "beneficiary_address": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            426,
                            627,
                            2008,
                            683
                        ]
                    ],
                    "model_confidence": [
                        99.29581752977384
                    ]
                },
                "cosignee_name": {
                    "value": "CADCHEM LABORATORIES LTD.",
                    "coordinate": [
                        [
                            310,
                            974,
                            979,
                            1013
                        ]
                    ],
                    "model_confidence": [
                        99.43891058859161
                    ]
                },
                "invoice_no": {
                    "value": "NUMBERCP202130061 NUMBERZMCAS22112002",
                    "coordinate": [
                        [
                            1649,
                            953,
                            2152,
                            1083
                        ]
                    ],
                    "model_confidence": [
                        79.01
                    ]
                },
                "consignee_address": {
                    "value": "ADDVILLAGE JAUIA KHURD TEHSIL DERA BASSI PUNJABINDIA",
                    "coordinate": [
                        [
                            220,
                            1034,
                            1267,
                            1139
                        ]
                    ],
                    "model_confidence": [
                        99.82940799620359
                    ]
                },
                "date_of_invoice": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1569,
                            1139,
                            1889,
                            1178
                        ]
                    ],
                    "model_confidence": [
                        70.97
                    ]
                },
                "usance_tenor": {
                    "value": "90",
                    "coordinate": [
                        [
                            466,
                            1367,
                            505,
                            1399
                        ]
                    ],
                    "model_confidence": [
                        99.06
                    ]
                },
                "tenor_indicator": {
                    "value": "DAYS",
                    "coordinate": [
                        [
                            518,
                            1367,
                            632,
                            1399
                        ]
                    ],
                    "model_confidence": [
                        99.44
                    ]
                },
                "indicator_type": {
                    "value": "AFTER",
                    "coordinate": [
                        [
                            647,
                            1364,
                            783,
                            1395
                        ]
                    ],
                    "model_confidence": [
                        94.33
                    ]
                },
                "indicator_date": {
                    "value": "BL DATE",
                    "coordinate": [
                        [
                            796,
                            1360,
                            987,
                            1395
                        ]
                    ],
                    "model_confidence": [
                        98.9
                    ]
                },
                "rate_per_unit": {
                    "value": "USD84.50KG",
                    "coordinate": [
                        [
                            1103,
                            1550,
                            1341,
                            1602
                        ]
                    ],
                    "model_confidence": [
                        79.53
                    ]
                },
                "goods_description": {
                    "value": "20DRUMS FCA N/M RIFAMYCIN",
                    "coordinate": [
                        [
                            282,
                            1599,
                            2006,
                            1686
                        ]
                    ],
                    "model_confidence": [
                        40.894999999999996
                    ]
                },
                "invoice_amount": {
                    "value": "42,250,00",
                    "coordinate": [
                        [
                            1450,
                            1599,
                            1708,
                            1651
                        ]
                    ],
                    "model_confidence": [
                        9.61
                    ]
                },
                "total_quantity_of_goods": {
                    "value": "500.00 2",
                    "coordinate": [
                        [
                            644,
                            1588,
                            2090,
                            1686
                        ]
                    ],
                    "model_confidence": [
                        90.32499999999999
                    ]
                },
                "lc_ref_no": {
                    "value": "0041FLC210044",
                    "coordinate": [
                        [
                            582,
                            1753,
                            885,
                            1792
                        ]
                    ],
                    "model_confidence": [
                        99.5
                    ]
                },
                "lc_date": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1031,
                            1749,
                            1257,
                            1785
                        ]
                    ],
                    "model_confidence": [
                        96.34
                    ]
                },
                "country_of_origin_of_goods": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            768,
                            2205,
                            870,
                            2233
                        ]
                    ],
                    "model_confidence": [
                        88.82
                    ]
                },
                "port_of_loading": {
                    "value": "XIACHENG",
                    "coordinate": [
                        [
                            934,
                            2588,
                            1160,
                            2623
                        ]
                    ],
                    "model_confidence": [
                        15.84
                    ]
                },
                "signature_of_the_issuer": {
                    "value": "ER TES MING ..{0. MEDICINE.",
                    "coordinate": [
                        [
                            1507,
                            2872,
                            2162,
                            3075
                        ]
                    ],
                    "model_confidence": [
                        45.22
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1552,
                            2580,
                            2069,
                            2819
                        ]
                    ],
                    "model_confidence": [
                        0.7605540752410889
                    ]
                },
                "is_stamp": {},
                "invoice_currency": {
                    "value": "USD",
                    "coordinate": [
                        [
                            1450,
                            1599,
                            1708,
                            1651
                        ]
                    ],
                    "model_confidence": [
                        9.61
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
                "declaration_by_issuer": {},
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
                            426,
                            627,
                            2008,
                            683
                        ]
                    ],
                    "model_confidence": [
                        99.29581752977384
                    ]
                },
                "remitter_drawee_applicant_importer_buyer_name": {}
            }
        },
        "page26": {
            "docClass": "AWB",
            "keys_extraction": {
                "consignee_name": {
                    "value": "ZHEJIANG MEDICINE CO. LTD,",
                    "coordinate": [
                        [
                            224,
                            333,
                            816,
                            363
                        ]
                    ],
                    "model_confidence": [
                        86.03841155234656
                    ]
                },
                "consignee_address": {
                    "value": "AVENUE 11D ZHIYUAN BINHALNEW AREA SI PROVINCE ZHEJIANG 212285 PR ",
                    "coordinate": [
                        [
                            323,
                            359,
                            1167,
                            462
                        ]
                    ],
                    "model_confidence": [
                        88.7816979992674
                    ]
                },
                "freight_collect_or_prepaid": {
                    "value": "FREIGHT COLLECT",
                    "coordinate": [
                        [
                            1606,
                            963,
                            1955,
                            990
                        ]
                    ],
                    "model_confidence": [
                        96.52
                    ]
                },
                "airport_of_departure": {
                    "value": "PUDONG",
                    "coordinate": [
                        [
                            214,
                            1188,
                            374,
                            1217
                        ]
                    ],
                    "model_confidence": [
                        77.87
                    ]
                },
                "carriage_condition": {
                    "value": "PORES ANY PART OF THE",
                    "coordinate": [
                        [
                            1927,
                            2715,
                            2187,
                            2765
                        ]
                    ],
                    "model_confidence": [
                        91.297826767545
                    ]
                },
                "signature": {
                    "value": " R",
                    "coordinate": [
                        [
                            153,
                            2966,
                            438,
                            3210
                        ]
                    ],
                    "model_confidence": [
                        53.55
                    ]
                },
                "is_signed": {},
                "is_stamp": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1438,
                            2685,
                            2008,
                            3054
                        ]
                    ],
                    "model_confidence": [
                        0.9017217755317688
                    ]
                },
                "consignee_address_country": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            323,
                            359,
                            1167,
                            462
                        ]
                    ],
                    "model_confidence": [
                        88.7816979992674
                    ]
                },
                "declared_value_of_carriage": {},
                "flight_details": {},
                "flight_date": {},
                "notify_party_name": {},
                "stamp": {},
                "dimension": {},
                "notify_party_address": {},
                "lc_no": {},
                "carrier_name": {},
                "gross_weight": {},
                "agent_name": {},
                "master_awb_bill_no": {},
                "airport_of_destination": {},
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
                "house_awb_bill_no": {},
                "flight_no": {},
                "freight_collected_at": {},
                "awb_original_number": {},
                "awb_bill_no": {},
                "good_marks": {},
                "goods_description": {},
                "awb_bill_issue_date": {}
            }
        },
        "page14": {
            "docClass": "CI",
            "keys_extraction": {
                "beneficiary_drawer_exporter_seller_supplier_name": {
                    "value": "ZHEJIANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            771,
                            536,
                            1636,
                            592
                        ]
                    ],
                    "model_confidence": [
                        99.20149143863017
                    ]
                },
                "beneficiary_address": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            426,
                            620,
                            2008,
                            680
                        ]
                    ],
                    "model_confidence": [
                        99.32163572343583
                    ]
                },
                "cosignee_name": {
                    "value": "TOCADCHEM LABORATORIES LTD. BENEFICIARYZHEJIANG MEDICINE",
                    "coordinate": [
                        [
                            223,
                            967,
                            979,
                            1010
                        ],
                        [
                            243,
                            2353,
                            885,
                            2398
                        ]
                    ],
                    "model_confidence": [
                        91.67682458386682,
                        50.229066241352164
                    ]
                },
                "invoice_no": {
                    "value": "NUMBERCP202130061 NUMBERZMCAS22112002",
                    "coordinate": [
                        [
                            1649,
                            950,
                            2152,
                            1076
                        ]
                    ],
                    "model_confidence": [
                        86.48
                    ]
                },
                "consignee_address": {
                    "value": "ADDVILLAGE JAUIA KHURD TEHSIL DERA BASSI PUNJABINDIA",
                    "coordinate": [
                        [
                            223,
                            1031,
                            1267,
                            1136
                        ]
                    ],
                    "model_confidence": [
                        99.76292413197616
                    ]
                },
                "date_of_invoice": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1572,
                            1132,
                            1889,
                            1171
                        ]
                    ],
                    "model_confidence": [
                        70.89
                    ]
                },
                "usance_tenor": {
                    "value": "90",
                    "coordinate": [
                        [
                            468,
                            1360,
                            508,
                            1392
                        ]
                    ],
                    "model_confidence": [
                        99.03
                    ]
                },
                "tenor_indicator": {
                    "value": "DAYS",
                    "coordinate": [
                        [
                            520,
                            1360,
                            634,
                            1392
                        ]
                    ],
                    "model_confidence": [
                        99.44
                    ]
                },
                "indicator_type": {
                    "value": "AFTER",
                    "coordinate": [
                        [
                            649,
                            1357,
                            786,
                            1388
                        ]
                    ],
                    "model_confidence": [
                        94.67
                    ]
                },
                "indicator_date": {
                    "value": "BL DATE",
                    "coordinate": [
                        [
                            796,
                            1353,
                            989,
                            1388
                        ]
                    ],
                    "model_confidence": [
                        98.93
                    ]
                },
                "goods_description": {
                    "value": "500.00KGS RIFAMYCIN O",
                    "coordinate": [
                        [
                            624,
                            1581,
                            845,
                            1679
                        ]
                    ],
                    "model_confidence": [
                        84.0
                    ]
                },
                "rate_per_unit": {
                    "value": "USD84.50KG USD42,250.00",
                    "coordinate": [
                        [
                            1106,
                            1546,
                            1708,
                            1637
                        ]
                    ],
                    "model_confidence": [
                        46.69
                    ]
                },
                "total_quantity_of_goods": {
                    "value": "20 2",
                    "coordinate": [
                        [
                            1812,
                            1588,
                            2090,
                            1679
                        ]
                    ],
                    "model_confidence": [
                        71.78
                    ]
                },
                "lc_ref_no": {
                    "value": "NO0041FLC210044",
                    "coordinate": [
                        [
                            510,
                            1746,
                            885,
                            1788
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
                            1034,
                            1742,
                            1259,
                            1778
                        ]
                    ],
                    "model_confidence": [
                        96.52
                    ]
                },
                "country_of_origin_of_goods": {
                    "value": "CHINA P.R.CHINA",
                    "coordinate": [
                        [
                            771,
                            2198,
                            872,
                            2230
                        ],
                        [
                            1790,
                            2412,
                            1969,
                            2444
                        ]
                    ],
                    "model_confidence": [
                        89.58,
                        5.46
                    ]
                },
                "declaration_by_issuer": {
                    "value": "CO., LTD. A CO., LTD.",
                    "coordinate": [
                        [
                            897,
                            2349,
                            1083,
                            2388
                        ],
                        [
                            1368,
                            2931,
                            2016,
                            3047
                        ]
                    ],
                    "model_confidence": [
                        77.66,
                        80.1428813559322
                    ]
                },
                "signature_of_the_issuer": {
                    "value": "SM TE RA",
                    "coordinate": [
                        [
                            1445,
                            2889,
                            1951,
                            3012
                        ]
                    ],
                    "model_confidence": [
                        80.52000000000001
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1427,
                            2575,
                            1941,
                            2791
                        ]
                    ],
                    "model_confidence": [
                        0.7462582588195801
                    ]
                },
                "is_stamp": {},
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
                "port_of_loading": {},
                "bill_of_lading_no": {},
                "invoice_tax_amount": {},
                "invoice_currency": {},
                "notify_party_name": {},
                "original_or_copy": {},
                "invoice_amount": {},
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
                            426,
                            620,
                            2008,
                            680
                        ]
                    ],
                    "model_confidence": [
                        99.32163572343583
                    ]
                },
                "remitter_drawee_applicant_importer_buyer_name": {}
            }
        },
        "page13": {
            "docClass": "CI",
            "keys_extraction": {
                "beneficiary_drawer_exporter_seller_supplier_name": {
                    "value": "ZHEJIANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            771,
                            536,
                            1636,
                            592
                        ]
                    ],
                    "model_confidence": [
                        99.4114911180973
                    ]
                },
                "beneficiary_address": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            424,
                            620,
                            2008,
                            680
                        ]
                    ],
                    "model_confidence": [
                        99.31605541986926
                    ]
                },
                "cosignee_name": {
                    "value": "CADCHEM LABORATORIES LTD.",
                    "coordinate": [
                        [
                            317,
                            950,
                            979,
                            1024
                        ]
                    ],
                    "model_confidence": [
                        97.90518293660266
                    ]
                },
                "invoice_no": {
                    "value": "NUMBERCP202130061 NUMBERZMCAS22112002",
                    "coordinate": [
                        [
                            1649,
                            946,
                            2152,
                            1076
                        ]
                    ],
                    "model_confidence": [
                        53.92
                    ]
                },
                "consignee_address": {
                    "value": "ADDVILLAGE JAUIA KHURD TEHSIL DERA BASSI PUNJABINDIA",
                    "coordinate": [
                        [
                            223,
                            1027,
                            1267,
                            1136
                        ]
                    ],
                    "model_confidence": [
                        99.801921352958
                    ]
                },
                "usance_tenor": {
                    "value": "90",
                    "coordinate": [
                        [
                            466,
                            1360,
                            505,
                            1392
                        ]
                    ],
                    "model_confidence": [
                        99.12
                    ]
                },
                "tenor_indicator": {
                    "value": "DAYS",
                    "coordinate": [
                        [
                            520,
                            1360,
                            634,
                            1392
                        ]
                    ],
                    "model_confidence": [
                        99.44
                    ]
                },
                "indicator_type": {
                    "value": "AFTER",
                    "coordinate": [
                        [
                            647,
                            1357,
                            783,
                            1388
                        ]
                    ],
                    "model_confidence": [
                        94.78
                    ]
                },
                "indicator_date": {
                    "value": "BL DATE",
                    "coordinate": [
                        [
                            796,
                            1353,
                            989,
                            1388
                        ]
                    ],
                    "model_confidence": [
                        98.92
                    ]
                },
                "rate_per_unit": {
                    "value": "USD84.50KG",
                    "coordinate": [
                        [
                            1106,
                            1546,
                            1341,
                            1588
                        ]
                    ],
                    "model_confidence": [
                        93.59
                    ]
                },
                "goods_description": {
                    "value": "20DRUMS FCA DELHI RIFAMYCIN",
                    "coordinate": [
                        [
                            624,
                            1588,
                            2006,
                            1679
                        ]
                    ],
                    "model_confidence": [
                        67.54333333333334
                    ]
                },
                "total_quantity_of_goods": {
                    "value": "500.00 2",
                    "coordinate": [
                        [
                            647,
                            1581,
                            2093,
                            1676
                        ]
                    ],
                    "model_confidence": [
                        77.32
                    ]
                },
                "invoice_amount": {
                    "value": "42,250.00",
                    "coordinate": [
                        [
                            1450,
                            1595,
                            1708,
                            1634
                        ]
                    ],
                    "model_confidence": [
                        40.81
                    ]
                },
                "lc_ref_no": {
                    "value": "NO0041FLC210044",
                    "coordinate": [
                        [
                            510,
                            1746,
                            885,
                            1785
                        ]
                    ],
                    "model_confidence": [
                        99.1
                    ]
                },
                "lc_date": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1034,
                            1739,
                            1259,
                            1778
                        ]
                    ],
                    "model_confidence": [
                        85.91
                    ]
                },
                "country_of_origin_of_goods": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            771,
                            2195,
                            872,
                            2226
                        ]
                    ],
                    "model_confidence": [
                        88.56
                    ]
                },
                "port_of_loading": {
                    "value": "XIACHENG",
                    "coordinate": [
                        [
                            937,
                            2581,
                            1160,
                            2616
                        ]
                    ],
                    "model_confidence": [
                        23.18
                    ]
                },
                "beneficiary_bank_country": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            1636,
                            2570,
                            1773,
                            2605
                        ]
                    ],
                    "model_confidence": [
                        78.46
                    ]
                },
                "signature_of_the_issuer": {
                    "value": "I HL EE 25 A RS",
                    "coordinate": [
                        [
                            1795,
                            2738,
                            2046,
                            2858
                        ],
                        [
                            1552,
                            2959,
                            2058,
                            3058
                        ]
                    ],
                    "model_confidence": [
                        96.95,
                        94.85666666666668
                    ]
                },
                "declaration_by_issuer": {
                    "value": "HH ZHEJIANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            1480,
                            2959,
                            2127,
                            3117
                        ]
                    ],
                    "model_confidence": [
                        52.90747848799099
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1564,
                            2644,
                            1956,
                            2872
                        ]
                    ],
                    "model_confidence": [
                        0.6214232444763184
                    ]
                },
                "is_stamp": {},
                "invoice_currency": {
                    "value": "USD",
                    "coordinate": [
                        [
                            1450,
                            1595,
                            1708,
                            1634
                        ]
                    ],
                    "model_confidence": [
                        40.81
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
                "date_of_invoice": {},
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
                "invoice_amount_in_words": {},
                "beneficiary_country": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            424,
                            620,
                            2008,
                            680
                        ]
                    ],
                    "model_confidence": [
                        99.31605541986926
                    ]
                },
                "remitter_drawee_applicant_importer_buyer_name": {}
            }
        },
        "page22": {
            "docClass": "AWB",
            "keys_extraction": {
                "house_awb_bill_no": {
                    "value": "13139055402 SHAE21122181",
                    "coordinate": [
                        [
                            280,
                            155,
                            2221,
                            214
                        ]
                    ],
                    "model_confidence": [
                        45.715
                    ]
                },
                "shipper_name": {
                    "value": "ZHEJIANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            224,
                            343,
                            816,
                            379
                        ]
                    ],
                    "model_confidence": [
                        87.3844735379894
                    ]
                },
                "consignee_address": {
                    "value": "168 MID ZHTYUAN AVENUE NEW SHADXING CITY ZHEJIANG PROVINCE 312366 PR CHINA 224 386 1341 475 7604772125399069 960 930 860 930 960 890 960 950 950 930 920 950 880 880 920 910 960~168 MID ZHTYUAN AVENUE NEW SHADXING CITY ZHEJIANG PROVINCE 312366 PR CHINA 224 386 1341 475 7604772125399069 960 930 860 930 960 890 960 950 950 930 920 950 880 880 920 910 960 224 386 1341 475 7604772125399069 960 930 860 930 960 890 960 950 950 930 920 950 880 880 920 910 960~",
                    "coordinate": [
                        [
                            224,
                            386,
                            1341,
                            475
                        ]
                    ],
                    "model_confidence": [
                        86.15188585942178
                    ]
                },
                "shipper_address": {
                    "value": "AREA BINHAI",
                    "coordinate": [
                        [
                            759,
                            386,
                            1122,
                            429
                        ]
                    ],
                    "model_confidence": [
                        81.585
                    ]
                },
                "consignee_name": {
                    "value": "AXIS BANK LTD",
                    "coordinate": [
                        [
                            221,
                            617,
                            520,
                            650
                        ]
                    ],
                    "model_confidence": [
                        98.2143661971831
                    ]
                },
                "notify_party_name": {
                    "value": "CADCHEM LABORATORIES LIMITED",
                    "coordinate": [
                        [
                            219,
                            904,
                            892,
                            937
                        ]
                    ],
                    "model_confidence": [
                        85.23269069193528
                    ]
                },
                "notify_party_address": {
                    "value": "VILLAGE JAULA KHURD TEHSIL DERABASSI DISTRIC SAS NAGAR PUNJAB140501 ",
                    "coordinate": [
                        [
                            216,
                            953,
                            1221,
                            1032
                        ]
                    ],
                    "model_confidence": [
                        94.61313149699235
                    ]
                },
                "freight_collect_or_prepaid": {
                    "value": "FREIGHT COLLECT",
                    "coordinate": [
                        [
                            1606,
                            966,
                            1960,
                            996
                        ]
                    ],
                    "model_confidence": [
                        96.51
                    ]
                },
                "airport_of_departure": {
                    "value": "PUDONG",
                    "coordinate": [
                        [
                            216,
                            1194,
                            379,
                            1257
                        ]
                    ],
                    "model_confidence": [
                        73.14
                    ]
                },
                "carrier_name": {
                    "value": "SECRE PARROT",
                    "coordinate": [
                        [
                            1680,
                            1395,
                            2338,
                            1452
                        ]
                    ],
                    "model_confidence": [
                        79.52
                    ]
                },
                "gross_weight": {
                    "value": "6",
                    "coordinate": [
                        [
                            308,
                            1772,
                            415,
                            1801
                        ]
                    ],
                    "model_confidence": [
                        93.11
                    ]
                },
                "signature": {
                    "value": "AL EEE ARE  ARE = BONE — — —",
                    "coordinate": [
                        [
                            147,
                            2356,
                            512,
                            2468
                        ],
                        [
                            724,
                            2356,
                            874,
                            2468
                        ],
                        [
                            685,
                            2666,
                            869,
                            2887
                        ],
                        [
                            142,
                            2676,
                            1259,
                            3065
                        ]
                    ],
                    "model_confidence": [
                        56.79,
                        51.6,
                        41.74,
                        47.79
                    ]
                },
                "carriage_condition": {
                    "value": "CONSIGNMENT CONTAINS DANGG FOR CARRIAGE BY AIR ACCORDINGH",
                    "coordinate": [
                        [
                            1012,
                            2752,
                            1397,
                            2814
                        ]
                    ],
                    "model_confidence": [
                        78.7
                    ]
                },
                "is_signed": {},
                "is_stamp": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1350,
                            2639,
                            1915,
                            3021
                        ]
                    ],
                    "model_confidence": [
                        0.8872972726821899
                    ]
                },
                "notify_party_address_country": {
                    "value": "INDIA",
                    "coordinate": [
                        [
                            216,
                            953,
                            1221,
                            1032
                        ]
                    ],
                    "model_confidence": [
                        94.61313149699235
                    ]
                },
                "declared_value_of_carriage": {},
                "flight_details": {},
                "flight_date": {},
                "stamp": {},
                "dimension": {},
                "lc_no": {},
                "agent_name": {},
                "master_awb_bill_no": {},
                "airport_of_destination": {},
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
                "declared_value_of_custom": {},
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
                "goods_description": {},
                "awb_bill_issue_date": {}
            }
        },
        "page5": {
            "docClass": "BOE",
            "keys_extraction": {
                "bill_exchange_no": {
                    "value": "0061",
                    "coordinate": [
                        [
                            1157,
                            1215,
                            1230,
                            1249
                        ]
                    ],
                    "model_confidence": [
                        20.77
                    ]
                },
                "bill_exchange_date": {
                    "value": "JANUARY 10, 2022",
                    "coordinate": [
                        [
                            2461,
                            1207,
                            2756,
                            1247
                        ]
                    ],
                    "model_confidence": [
                        73.62946963134085
                    ]
                },
                "usance_tenor": {
                    "value": "8",
                    "coordinate": [
                        [
                            1237,
                            1416,
                            1269,
                            1450
                        ]
                    ],
                    "model_confidence": [
                        47.61
                    ]
                },
                "tenor_indicator": {
                    "value": "DAYS",
                    "coordinate": [
                        [
                            1297,
                            1413,
                            1374,
                            1450
                        ]
                    ],
                    "model_confidence": [
                        47.76
                    ]
                },
                "indicator_type": {
                    "value": "FROM",
                    "coordinate": [
                        [
                            1395,
                            1413,
                            1476,
                            1448
                        ]
                    ],
                    "model_confidence": [
                        47.86
                    ]
                },
                "indicator_date": {
                    "value": "AWB DATE",
                    "coordinate": [
                        [
                            1497,
                            1413,
                            1655,
                            1448
                        ]
                    ],
                    "model_confidence": [
                        73.39263157894736
                    ]
                },
                "drawer_bank_name": {
                    "value": "OF BANK CHINA- NDUSTRIAL",
                    "coordinate": [
                        [
                            1458,
                            1597,
                            2752,
                            1696
                        ]
                    ],
                    "model_confidence": [
                        40.92
                    ]
                },
                "signature": {
                    "value": "SHAUN UNDE BENG VIHE A ",
                    "coordinate": [
                        [
                            824,
                            1765,
                            1578,
                            2189
                        ]
                    ],
                    "model_confidence": [
                        66.60111647867409
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            821,
                            1920,
                            1090,
                            1994
                        ]
                    ],
                    "model_confidence": [
                        0.5484554767608643
                    ]
                },
                "is_stamp": {},
                "lc_ref_no": {},
                "drawer_address": {},
                "boe_currency": {},
                "original_or_copy": {},
                "invoice_due_date": {},
                "issue_place": {},
                "drawer_name": {},
                "invoice_no": {},
                "stamp": {},
                "boe_amount": {},
                "diclaration_by": {},
                "amount_in_words": {},
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
            }
        },
        "page12": {
            "docClass": "CI",
            "keys_extraction": {
                "beneficiary_drawer_exporter_seller_supplier_name": {
                    "value": "ZHEJIANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            838,
                            543,
                            1703,
                            603
                        ]
                    ],
                    "model_confidence": [
                        99.4937476092233
                    ]
                },
                "beneficiary_address": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            488,
                            631,
                            2075,
                            680
                        ]
                    ],
                    "model_confidence": [
                        99.32556263810329
                    ]
                },
                "cosignee_name": {
                    "value": "TOCADCHEM LABORATORIES LTD. CO.,",
                    "coordinate": [
                        [
                            277,
                            957,
                            1034,
                            999
                        ],
                        [
                            915,
                            2349,
                            992,
                            2384
                        ]
                    ],
                    "model_confidence": [
                        91.12864847495263,
                        27.78
                    ]
                },
                "invoice_no": {
                    "value": "NUMBERCP202130061 NUMBERZMCAS22112002",
                    "coordinate": [
                        [
                            1701,
                            974,
                            2207,
                            1104
                        ]
                    ],
                    "model_confidence": [
                        87.21
                    ]
                },
                "consignee_address": {
                    "value": "ADDVILLAGE JAUIA KHURD TEHSIL DERA BASSI PUNJABINDIA",
                    "coordinate": [
                        [
                            275,
                            1024,
                            1319,
                            1118
                        ]
                    ],
                    "model_confidence": [
                        99.78856127171507
                    ]
                },
                "date_of_invoice": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1621,
                            1153,
                            1941,
                            1192
                        ]
                    ],
                    "model_confidence": [
                        70.99
                    ]
                },
                "usance_tenor": {
                    "value": "90",
                    "coordinate": [
                        [
                            510,
                            1346,
                            550,
                            1378
                        ]
                    ],
                    "model_confidence": [
                        98.94
                    ]
                },
                "tenor_indicator": {
                    "value": "DAYS",
                    "coordinate": [
                        [
                            562,
                            1346,
                            677,
                            1378
                        ]
                    ],
                    "model_confidence": [
                        99.44
                    ]
                },
                "indicator_type": {
                    "value": "AFTER",
                    "coordinate": [
                        [
                            691,
                            1350,
                            828,
                            1381
                        ]
                    ],
                    "model_confidence": [
                        94.46
                    ]
                },
                "indicator_date": {
                    "value": "BL DATE",
                    "coordinate": [
                        [
                            840,
                            1350,
                            1031,
                            1385
                        ]
                    ],
                    "model_confidence": [
                        98.92
                    ]
                },
                "total_quantity_of_goods": {
                    "value": "25.00 20 2 500.00",
                    "coordinate": [
                        [
                            684,
                            1564,
                            2251,
                            1704
                        ]
                    ],
                    "model_confidence": [
                        42.785
                    ]
                },
                "rate_per_unit": {
                    "value": "USD84,50KG",
                    "coordinate": [
                        [
                            1145,
                            1553,
                            1381,
                            1595
                        ]
                    ],
                    "model_confidence": [
                        95.09
                    ]
                },
                "goods_description": {
                    "value": "PACKED RICE AO “EN FCA DELHI",
                    "coordinate": [
                        [
                            659,
                            1560,
                            1931,
                            1672
                        ]
                    ],
                    "model_confidence": [
                        80.32666666666667
                    ]
                },
                "lc_ref_no": {
                    "value": "NO0041FLC210044",
                    "coordinate": [
                        [
                            543,
                            1739,
                            917,
                            1778
                        ]
                    ],
                    "model_confidence": [
                        99.03
                    ]
                },
                "lc_date": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1066,
                            1746,
                            1289,
                            1781
                        ]
                    ],
                    "model_confidence": [
                        88.23
                    ]
                },
                "country_of_origin_of_goods": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            791,
                            2188,
                            892,
                            2219
                        ]
                    ],
                    "model_confidence": [
                        80.19
                    ]
                },
                "declaration_by_issuer": {
                    "value": "LTD. CO., LTD. LHECIANG",
                    "coordinate": [
                        [
                            1006,
                            2349,
                            1098,
                            2381
                        ],
                        [
                            1554,
                            3026,
                            2202,
                            3086
                        ]
                    ],
                    "model_confidence": [
                        54.88,
                        60.83666666666667
                    ]
                },
                "port_of_loading": {
                    "value": "XIACHENG",
                    "coordinate": [
                        [
                            944,
                            2581,
                            1170,
                            2616
                        ]
                    ],
                    "model_confidence": [
                        27.42
                    ]
                },
                "beneficiary_bank_country": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            1646,
                            2591,
                            1780,
                            2623
                        ]
                    ],
                    "model_confidence": [
                        69.66
                    ]
                },
                "signature_of_the_issuer": {
                    "value": "BE AR A A RS MEDICINE",
                    "coordinate": [
                        [
                            1696,
                            2931,
                            2145,
                            3082
                        ]
                    ],
                    "model_confidence": [
                        90.4
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1671,
                            2643,
                            2191,
                            2887
                        ]
                    ],
                    "model_confidence": [
                        0.6706926822662354
                    ]
                },
                "is_stamp": {},
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
                "invoice_amount": {},
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
                            488,
                            631,
                            2075,
                            680
                        ]
                    ],
                    "model_confidence": [
                        99.32556263810329
                    ]
                },
                "remitter_drawee_applicant_importer_buyer_name": {}
            }
        },
        "page15": {
            "docClass": "PL",
            "keys_extraction": {
                "beneficiary_drawer_exporter_seller_supplier_name": {
                    "value": "ZHEJIANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            776,
                            547,
                            1641,
                            599
                        ]
                    ],
                    "model_confidence": [
                        99.96016484068751
                    ]
                },
                "beneficiary_address": {
                    "value": "168 MID ZHIYUAN AVENUE BINHAI NEW AREA",
                    "coordinate": [
                        [
                            429,
                            638,
                            1143,
                            676
                        ]
                    ],
                    "model_confidence": [
                        81.88520773918064
                    ]
                },
                "consignee_name": {
                    "value": "TOCADCHEM LABORATORIES LTD.",
                    "coordinate": [
                        [
                            223,
                            967,
                            979,
                            1003
                        ]
                    ],
                    "model_confidence": [
                        78.5233785680861
                    ]
                },
                "invoice_no": {
                    "value": "NUMBERCP202130061",
                    "coordinate": [
                        [
                            1713,
                            964,
                            2132,
                            995
                        ]
                    ],
                    "model_confidence": [
                        99.33
                    ]
                },
                "consignee_address": {
                    "value": "VILLAGE JAUIA KHURD TEHSIL DERA BASSI PUNJABINDIA",
                    "coordinate": [
                        [
                            223,
                            1024,
                            1264,
                            1129
                        ]
                    ],
                    "model_confidence": [
                        99.89
                    ]
                },
                "date_of_invoice": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1567,
                            1083,
                            1887,
                            1122
                        ]
                    ],
                    "model_confidence": [
                        71.36
                    ]
                },
                "payment_terms_terms_of_delivery_&_payment": {
                    "value": "PAYMENTLC 90 DAYS AFTER B/L DATE",
                    "coordinate": [
                        [
                            220,
                            1294,
                            982,
                            1336
                        ]
                    ],
                    "model_confidence": [
                        84.06991177283791
                    ]
                },
                "lc_ref_no": {
                    "value": "NO0041FLC210044",
                    "coordinate": [
                        [
                            468,
                            1690,
                            843,
                            1725
                        ]
                    ],
                    "model_confidence": [
                        99.06
                    ]
                },
                "lc_date": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            992,
                            1690,
                            1215,
                            1725
                        ]
                    ],
                    "model_confidence": [
                        99.63
                    ]
                },
                "net_weight": {
                    "value": "5 ",
                    "coordinate": [
                        [
                            637,
                            1522,
                            815,
                            1560
                        ],
                        [
                            414,
                            1760,
                            642,
                            1802
                        ]
                    ],
                    "model_confidence": [
                        9.14,
                        98.27
                    ]
                },
                "gross_weight": {
                    "value": "",
                    "coordinate": [
                        [
                            416,
                            1841,
                            642,
                            1879
                        ]
                    ],
                    "model_confidence": [
                        95.62
                    ]
                },
                "total_quantity_of_goods": {
                    "value": "20 2",
                    "coordinate": [
                        [
                            1517,
                            1571,
                            2085,
                            1602
                        ]
                    ],
                    "model_confidence": [
                        78.58
                    ]
                },
                "country_of_origin_origin_of_goods": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            751,
                            2132,
                            855,
                            2163
                        ]
                    ],
                    "model_confidence": [
                        99.81
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1234,
                            2139,
                            1706,
                            2378
                        ]
                    ],
                    "model_confidence": [
                        0.7615744471549988
                    ]
                },
                "is_stamp": {},
                "shipper_address": {},
                "notify_party_address": {},
                "awb_number": {},
                "vessel_flight_no": {},
                "track_reference": {},
                "declaration": {},
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
                "description_of_goods": {},
                "awb_date": {},
                "remitter_drawee_applicant_importer_buyer_name": {}
            }
        },
        "page8": {
            "docClass": "BOE",
            "keys_extraction": {
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
                "indicator_date": {},
                "lc_ref_no": {},
                "drawer_address": {},
                "boe_currency": {},
                "original_or_copy": {},
                "invoice_due_date": {},
                "bill_exchange_date": {},
                "drawer_bank_name": {},
                "issue_place": {},
                "drawer_name": {},
                "invoice_no": {},
                "indicator_type": {},
                "stamp": {},
                "boe_amount": {},
                "diclaration_by": {},
                "amount_in_words": {},
                "invoice_amount": {},
                "invoice_date": {},
                "country_of_origin": {},
                "drawee_name": {},
                "drawee_address": {},
                "bill_exchange_no": {},
                "usance_tenor": {},
                "signature": {},
                "drawee_bank_address": {},
                "lc_date": {},
                "drawee_bank_name": {},
                "tenor_indicator": {},
                "invoice_currency": {},
                "drawer_bank_address": {},
                "tenor_type": {}
            }
        },
        "page11": {
            "docClass": "CI",
            "keys_extraction": {
                "beneficiary_drawer_exporter_seller_supplier_name": {
                    "value": "ZHEJIANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            768,
                            540,
                            1631,
                            589
                        ]
                    ],
                    "model_confidence": [
                        99.12337650736936
                    ]
                },
                "beneficiary_address": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            421,
                            627,
                            2003,
                            673
                        ]
                    ],
                    "model_confidence": [
                        99.3481577281508
                    ]
                },
                "cosignee_name": {
                    "value": "TOCADCHEM LABORATORIES LTD.",
                    "coordinate": [
                        [
                            215,
                            964,
                            972,
                            999
                        ]
                    ],
                    "model_confidence": [
                        90.96068793747585
                    ]
                },
                "invoice_no": {
                    "value": "NUMBERCP202130061",
                    "coordinate": [
                        [
                            1706,
                            957,
                            2122,
                            992
                        ]
                    ],
                    "model_confidence": [
                        86.02
                    ]
                },
                "consignee_address": {
                    "value": "ADDVILLAGE JAUIA KHURD TEHSIL DERA BASSI",
                    "coordinate": [
                        [
                            215,
                            1031,
                            1259,
                            1066
                        ]
                    ],
                    "model_confidence": [
                        99.78740614334471
                    ]
                },
                "date_of_invoice": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1559,
                            1139,
                            1879,
                            1174
                        ]
                    ],
                    "model_confidence": [
                        70.84
                    ]
                },
                "usance_tenor": {
                    "value": "90",
                    "coordinate": [
                        [
                            453,
                            1353,
                            496,
                            1385
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
                            508,
                            1353,
                            622,
                            1381
                        ]
                    ],
                    "model_confidence": [
                        99.44
                    ]
                },
                "indicator_type": {
                    "value": "AFTER",
                    "coordinate": [
                        [
                            637,
                            1353,
                            773,
                            1381
                        ]
                    ],
                    "model_confidence": [
                        94.94
                    ]
                },
                "indicator_date": {
                    "value": "BL DATE",
                    "coordinate": [
                        [
                            783,
                            1350,
                            977,
                            1385
                        ]
                    ],
                    "model_confidence": [
                        98.81
                    ]
                },
                "rate_per_unit": {
                    "value": "USD84.50KG",
                    "coordinate": [
                        [
                            1088,
                            1543,
                            1329,
                            1595
                        ]
                    ],
                    "model_confidence": [
                        44.53
                    ]
                },
                "total_quantity_of_goods": {
                    "value": "500.00 2",
                    "coordinate": [
                        [
                            634,
                            1578,
                            2075,
                            1686
                        ]
                    ],
                    "model_confidence": [
                        76.42500000000001
                    ]
                },
                "goods_description": {
                    "value": "RIFAMYCIN",
                    "coordinate": [
                        [
                            607,
                            1630,
                            791,
                            1672
                        ]
                    ],
                    "model_confidence": [
                        83.88
                    ]
                },
                "lc_ref_no": {
                    "value": "0041FLC210044",
                    "coordinate": [
                        [
                            565,
                            1742,
                            868,
                            1778
                        ]
                    ],
                    "model_confidence": [
                        99.51
                    ]
                },
                "lc_date": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1016,
                            1742,
                            1240,
                            1774
                        ]
                    ],
                    "model_confidence": [
                        97.8
                    ]
                },
                "country_of_origin_of_goods": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            748,
                            2191,
                            850,
                            2223
                        ]
                    ],
                    "model_confidence": [
                        86.21
                    ]
                },
                "signature_of_the_issuer": {
                    "value": "IH TL BE 2 RS -THEOLANG MEDICINE",
                    "coordinate": [
                        [
                            1475,
                            2917,
                            2070,
                            3100
                        ]
                    ],
                    "model_confidence": [
                        84.04121895988831
                    ]
                },
                "declaration_by_issuer": {
                    "value": "CO. LTD.",
                    "coordinate": [
                        [
                            1946,
                            3012,
                            2142,
                            3075
                        ]
                    ],
                    "model_confidence": [
                        67.28
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1571,
                            2626,
                            2106,
                            2811
                        ]
                    ],
                    "model_confidence": [
                        0.7128076553344727
                    ]
                },
                "is_stamp": {},
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
                "port_of_loading": {},
                "bill_of_lading_no": {},
                "invoice_tax_amount": {},
                "invoice_currency": {},
                "notify_party_name": {},
                "original_or_copy": {},
                "invoice_amount": {},
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
                            421,
                            627,
                            2003,
                            673
                        ]
                    ],
                    "model_confidence": [
                        99.3481577281508
                    ]
                },
                "remitter_drawee_applicant_importer_buyer_name": {}
            }
        },
        "page24": {
            "docClass": "AWB",
            "keys_extraction": {
                "house_awb_bill_no": {
                    "value": "SHAE21122181",
                    "coordinate": [
                        [
                            1938,
                            165,
                            2223,
                            198
                        ]
                    ],
                    "model_confidence": [
                        50.94
                    ]
                },
                "shipper_name": {
                    "value": "ZHEJIANG MEDICINE COO., LTD.",
                    "coordinate": [
                        [
                            224,
                            336,
                            816,
                            372
                        ]
                    ],
                    "model_confidence": [
                        96.39996745309246
                    ]
                },
                "shipper_address": {
                    "value": "168 MID ZHIYUAN AVENUE BINHAI NEW AREA CITY ZHEJIANG PROVINCE 312366 ",
                    "coordinate": [
                        [
                            224,
                            386,
                            1139,
                            468
                        ]
                    ],
                    "model_confidence": [
                        95.75280094953908
                    ]
                },
                "consignee_address": {
                    "value": "PR 930 432 999 465 4402 910 920 910 920 960~PR 930 432 999 465 4402 910 920 910 920 960 930 432 999 465 4402 910 920 910 920 960~",
                    "coordinate": [
                        [
                            930,
                            432,
                            999,
                            465
                        ]
                    ],
                    "model_confidence": [
                        67.19791527508586
                    ]
                },
                "consignee_name": {
                    "value": "AXIS BANK LTD",
                    "coordinate": [
                        [
                            221,
                            610,
                            520,
                            643
                        ]
                    ],
                    "model_confidence": [
                        98.21572559366754
                    ]
                },
                "notify_party_name": {
                    "value": "CADCHEM LABORATORIES LIMITED",
                    "coordinate": [
                        [
                            216,
                            897,
                            892,
                            930
                        ]
                    ],
                    "model_confidence": [
                        85.14450928477251
                    ]
                },
                "notify_party_address": {
                    "value": "VILLAGE JAULA KHURD TEHSIL DERABASSI DISTRI SAS NAGAR PUNIJAB140501 ",
                    "coordinate": [
                        [
                            216,
                            943,
                            1193,
                            1026
                        ]
                    ],
                    "model_confidence": [
                        94.6318907684872
                    ]
                },
                "airport_of_departure": {
                    "value": "PUDONG",
                    "coordinate": [
                        [
                            211,
                            1188,
                            377,
                            1221
                        ]
                    ],
                    "model_confidence": [
                        85.97
                    ]
                },
                "at_place": {
                    "value": "NEW DELHI PANDA",
                    "coordinate": [
                        [
                            219,
                            1395,
                            436,
                            1452
                        ],
                        [
                            1020,
                            2831,
                            1147,
                            2861
                        ]
                    ],
                    "model_confidence": [
                        52.85,
                        65.88
                    ]
                },
                "stamp": {
                    "value": "ES",
                    "coordinate": [
                        [
                            961,
                            1349,
                            1063,
                            1452
                        ]
                    ],
                    "model_confidence": [
                        54.7
                    ]
                },
                "gross_weight": {
                    "value": "6",
                    "coordinate": [
                        [
                            306,
                            1768,
                            413,
                            1798
                        ]
                    ],
                    "model_confidence": [
                        84.61
                    ]
                },
                "carriage_condition": {
                    "value": "SHIPPER CERTIFIES THAT PARTICULARS CONSIGNMENT CONTAINS FOR CARRIAGE BY AIR ACCORDING AE ATS : PMSOFARAS ANY PART OF THE AILS 20 NAME ANDISIN PROPER CONDITION ; OR PET 20",
                    "coordinate": [
                        [
                            1014,
                            2715,
                            2312,
                            2805
                        ]
                    ],
                    "model_confidence": [
                        93.73827082318753
                    ]
                },
                "awb_bill_issue_date": {
                    "value": "23,DEC 2021",
                    "coordinate": [
                        [
                            1017,
                            3026,
                            1254,
                            3059
                        ]
                    ],
                    "model_confidence": [
                        95.92
                    ]
                },
                "is_signed": {},
                "is_stamp": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1366,
                            2640,
                            1930,
                            3024
                        ]
                    ],
                    "model_confidence": [
                        0.8385535478591919
                    ]
                },
                "shipper_address_country": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            224,
                            386,
                            1139,
                            468
                        ]
                    ],
                    "model_confidence": [
                        95.75280094953908
                    ]
                },
                "notify_party_address_country": {
                    "value": "INDIA",
                    "coordinate": [
                        [
                            216,
                            943,
                            1193,
                            1026
                        ]
                    ],
                    "model_confidence": [
                        94.6318907684872
                    ]
                },
                "declared_value_of_carriage": {},
                "flight_details": {},
                "flight_date": {},
                "freight_collect_or_prepaid": {},
                "dimension": {},
                "lc_no": {},
                "carrier_name": {},
                "agent_name": {},
                "master_awb_bill_no": {},
                "airport_of_destination": {},
                "signature": {},
                "agent_address": {},
                "invoice_date": {},
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
                "carrier_address": {},
                "amount_insurance": {},
                "signed_by_agent": {},
                "flight_no": {},
                "freight_collected_at": {},
                "awb_original_number": {},
                "awb_bill_no": {},
                "good_marks": {},
                "goods_description": {}
            }
        },
        "page20": {
            "docClass": "COO",
            "keys_extraction": {
                "original_or_copy": {
                    "value": "COPY",
                    "coordinate": [
                        [
                            1282,
                            72,
                            1435,
                            112
                        ]
                    ],
                    "model_confidence": [
                        97.47
                    ]
                },
                "consignor_name": {
                    "value": "CINE CO., MED LTD. 1.",
                    "coordinate": [
                        [
                            316,
                            141,
                            838,
                            207
                        ]
                    ],
                    "model_confidence": [
                        99.25273501760563
                    ]
                },
                "consignor_address": {
                    "value": "EPS A AVENUE BINHAI NEW AREA SHAOXING ZHEJIANG 312366 P R ",
                    "coordinate": [
                        [
                            193,
                            158,
                            1093,
                            277
                        ]
                    ],
                    "model_confidence": [
                        88.87707578006797
                    ]
                },
                "consignee_name": {
                    "value": "LTD",
                    "coordinate": [
                        [
                            739,
                            462,
                            795,
                            491
                        ]
                    ],
                    "model_confidence": [
                        92.32
                    ]
                },
                "consignee_address": {
                    "value": "VILLAGE JAUIA KHURD TEHSIL DERA BASSI PUNJAB140501 ",
                    "coordinate": [
                        [
                            351,
                            504,
                            1027,
                            577
                        ]
                    ],
                    "model_confidence": [
                        99.6
                    ]
                },
                "coo_issuer_address": {
                    "value": "THE PEOPLE S REPUBLIC OF ",
                    "coordinate": [
                        [
                            1430,
                            495,
                            2353,
                            534
                        ]
                    ],
                    "model_confidence": [
                        99.16033800334435
                    ]
                },
                "means_of_transport": {
                    "value": "AIR",
                    "coordinate": [
                        [
                            1088,
                            759,
                            1142,
                            788
                        ]
                    ],
                    "model_confidence": [
                        98.95
                    ]
                },
                "marks_and_no_of_packages": {
                    "value": "TWENTY (20) DRUMS",
                    "coordinate": [
                        [
                            754,
                            1382,
                            1063,
                            1415
                        ]
                    ],
                    "model_confidence": [
                        99.13177664974619
                    ]
                },
                "gross_weight": {
                    "value": "29, 41",
                    "coordinate": [
                        [
                            1649,
                            1382,
                            1739,
                            1412
                        ]
                    ],
                    "model_confidence": [
                        87.42
                    ]
                },
                "description_of_goods": {
                    "value": "RIFAMYCIN 0",
                    "coordinate": [
                        [
                            754,
                            1425,
                            956,
                            1452
                        ]
                    ],
                    "model_confidence": [
                        97.21108695652175
                    ]
                },
                "declaration_by_exporter": {
                    "value": "ZHEJIANG MEDICINE CO.,LTD. ,",
                    "coordinate": [
                        [
                            558,
                            3003,
                            1292,
                            3065
                        ]
                    ],
                    "model_confidence": [
                        99.46236337624123
                    ]
                },
                "issue_date": {
                    "value": "30,",
                    "coordinate": [
                        [
                            935,
                            3201,
                            979,
                            3230
                        ]
                    ],
                    "model_confidence": [
                        28.46
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1134,
                            3038,
                            1355,
                            3188
                        ]
                    ],
                    "model_confidence": [
                        0.6229955554008484
                    ]
                },
                "is_stamp": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1673,
                            2780,
                            2193,
                            3277
                        ]
                    ],
                    "model_confidence": [
                        0.9182443618774414
                    ]
                },
                "consignor_address_country": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            193,
                            158,
                            1093,
                            277
                        ]
                    ],
                    "model_confidence": [
                        88.87707578006797
                    ]
                },
                "consignee_address_country": {
                    "value": "INDIA",
                    "coordinate": [
                        [
                            351,
                            504,
                            1027,
                            577
                        ]
                    ],
                    "model_confidence": [
                        99.6
                    ]
                },
                "coo_issuer_address_country": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            1430,
                            495,
                            2353,
                            534
                        ]
                    ],
                    "model_confidence": [
                        99.16033800334435
                    ]
                },
                "certificate_no": {},
                "vessel_details": {},
                "country_of_origin_of_goods": {},
                "original_number": {},
                "invoice_date": {},
                "invoice_no": {},
                "lc_date": {},
                "declaration_by_certification": {},
                "ref_no": {},
                "coo_issuer_name": {},
                "lc_ref_no": {},
                "from_place": {},
                "signature": {},
                "certificate_stamped": {},
                "page_no": {},
                "net_weight": {},
                "final_destination": {},
                "to_place": {}
            }
        },
        "page17": {
            "docClass": "PL",
            "keys_extraction": {
                "beneficiary_drawer_exporter_seller_supplier_name": {
                    "value": "ZHEJIANG MEDICINE COO., LTD.",
                    "coordinate": [
                        [
                            778,
                            540,
                            1644,
                            592
                        ]
                    ],
                    "model_confidence": [
                        99.9361946555346
                    ]
                },
                "beneficiary_address": {
                    "value": "168 MID ZHIYUAN AVENUE BINHAI NEW AREA SHAOXING",
                    "coordinate": [
                        [
                            431,
                            634,
                            1309,
                            683
                        ]
                    ],
                    "model_confidence": [
                        73.25622130638124
                    ]
                },
                "consignee_name": {
                    "value": "CADCHEM LABORATORIES LTD.",
                    "coordinate": [
                        [
                            319,
                            971,
                            984,
                            1013
                        ]
                    ],
                    "model_confidence": [
                        94.08297658891607
                    ]
                },
                "invoice_no": {
                    "value": "NUMBERCP202130061",
                    "coordinate": [
                        [
                            1721,
                            953,
                            2140,
                            988
                        ]
                    ],
                    "model_confidence": [
                        97.82
                    ]
                },
                "consignee_address": {
                    "value": "ADDVILLAGE JAUIA KHURD TEHSIL DERA BASSI PUNJABINDIA",
                    "coordinate": [
                        [
                            230,
                            1034,
                            1274,
                            1150
                        ]
                    ],
                    "model_confidence": [
                        99.89486513486511
                    ]
                },
                "date_of_invoice": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1577,
                            1073,
                            1897,
                            1111
                        ]
                    ],
                    "model_confidence": [
                        71.35
                    ]
                },
                "payment_terms_terms_of_delivery_&_payment": {
                    "value": "PAYMENTLC 90 DAYS AFTER B/L DATE",
                    "coordinate": [
                        [
                            233,
                            1297,
                            994,
                            1346
                        ]
                    ],
                    "model_confidence": [
                        84.36412726838586
                    ]
                },
                "description_of_goods": {
                    "value": "RIFAMYCIN O",
                    "coordinate": [
                        [
                            629,
                            1578,
                            850,
                            1620
                        ]
                    ],
                    "model_confidence": [
                        73.44775684322786
                    ]
                },
                "total_quantity_of_goods": {
                    "value": "20 2",
                    "coordinate": [
                        [
                            1535,
                            1557,
                            2103,
                            1599
                        ]
                    ],
                    "model_confidence": [
                        75.8
                    ]
                },
                "lc_ref_no": {
                    "value": "NO0041FLC210044",
                    "coordinate": [
                        [
                            483,
                            1693,
                            858,
                            1732
                        ]
                    ],
                    "model_confidence": [
                        99.19
                    ]
                },
                "lc_date": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1006,
                            1686,
                            1232,
                            1725
                        ]
                    ],
                    "model_confidence": [
                        98.65
                    ]
                },
                "net_weight": {
                    "value": "",
                    "coordinate": [
                        [
                            431,
                            1767,
                            659,
                            1806
                        ]
                    ],
                    "model_confidence": [
                        99.82
                    ]
                },
                "gross_weight": {
                    "value": "",
                    "coordinate": [
                        [
                            434,
                            1844,
                            662,
                            1886
                        ]
                    ],
                    "model_confidence": [
                        98.42
                    ]
                },
                "country_of_origin_origin_of_goods": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            773,
                            2135,
                            877,
                            2167
                        ]
                    ],
                    "model_confidence": [
                        99.8
                    ]
                },
                "declaration": {
                    "value": "ZHEJIANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            1505,
                            2731,
                            2150,
                            2795
                        ]
                    ],
                    "model_confidence": [
                        99.6404008233665
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1546,
                            2283,
                            1916,
                            2520
                        ]
                    ],
                    "model_confidence": [
                        0.605141282081604
                    ]
                },
                "is_stamp": {},
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
            }
        },
        "page10": {
            "docClass": "CI",
            "keys_extraction": {
                "beneficiary_drawer_exporter_seller_supplier_name": {
                    "value": "ZHEJIANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            768,
                            547,
                            1631,
                            596
                        ]
                    ],
                    "model_confidence": [
                        98.69770288248337
                    ]
                },
                "beneficiary_address": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            421,
                            631,
                            2003,
                            683
                        ]
                    ],
                    "model_confidence": [
                        99.33386761621668
                    ]
                },
                "cosignee_name": {
                    "value": "TOCADCHEM LABORATORIES LTD. MEDICINE COO.,",
                    "coordinate": [
                        [
                            218,
                            974,
                            974,
                            1010
                        ],
                        [
                            659,
                            2356,
                            962,
                            2391
                        ]
                    ],
                    "model_confidence": [
                        90.87890967894793,
                        35.47
                    ]
                },
                "invoice_no": {
                    "value": "NUMBERCP202130061",
                    "coordinate": [
                        [
                            1708,
                            960,
                            2127,
                            995
                        ]
                    ],
                    "model_confidence": [
                        85.08
                    ]
                },
                "consignee_address": {
                    "value": "ADDVILLAGE JAUIA KHURD TEHSIL DERA BASSI PUNJABINDIA",
                    "coordinate": [
                        [
                            218,
                            1038,
                            1259,
                            1136
                        ]
                    ],
                    "model_confidence": [
                        99.81028960817717
                    ]
                },
                "date_of_invoice": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1564,
                            1143,
                            1884,
                            1181
                        ]
                    ],
                    "model_confidence": [
                        70.69
                    ]
                },
                "usance_tenor": {
                    "value": "90",
                    "coordinate": [
                        [
                            458,
                            1364,
                            498,
                            1395
                        ]
                    ],
                    "model_confidence": [
                        98.81
                    ]
                },
                "tenor_indicator": {
                    "value": "DAYS",
                    "coordinate": [
                        [
                            510,
                            1364,
                            624,
                            1395
                        ]
                    ],
                    "model_confidence": [
                        99.44
                    ]
                },
                "indicator_type": {
                    "value": "AFTER",
                    "coordinate": [
                        [
                            639,
                            1364,
                            776,
                            1392
                        ]
                    ],
                    "model_confidence": [
                        95.07
                    ]
                },
                "indicator_date": {
                    "value": "BL DATE",
                    "coordinate": [
                        [
                            788,
                            1360,
                            979,
                            1392
                        ]
                    ],
                    "model_confidence": [
                        98.96
                    ]
                },
                "goods_description": {
                    "value": "500.00KGS RIFAMYCIN FCA O WA O",
                    "coordinate": [
                        [
                            275,
                            1588,
                            1187,
                            1683
                        ]
                    ],
                    "model_confidence": [
                        79.2625
                    ]
                },
                "rate_per_unit": {
                    "value": "USD84.50KG",
                    "coordinate": [
                        [
                            1096,
                            1553,
                            1331,
                            1595
                        ]
                    ],
                    "model_confidence": [
                        81.66
                    ]
                },
                "total_quantity_of_goods": {
                    "value": "20 2",
                    "coordinate": [
                        [
                            1802,
                            1602,
                            2080,
                            1690
                        ]
                    ],
                    "model_confidence": [
                        69.46
                    ]
                },
                "invoice_amount": {
                    "value": "42,250.00",
                    "coordinate": [
                        [
                            1440,
                            1606,
                            1698,
                            1644
                        ]
                    ],
                    "model_confidence": [
                        44.26
                    ]
                },
                "lc_ref_no": {
                    "value": "NO0041FLC210044",
                    "coordinate": [
                        [
                            500,
                            1753,
                            875,
                            1788
                        ]
                    ],
                    "model_confidence": [
                        99.5
                    ]
                },
                "lc_date": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1024,
                            1749,
                            1247,
                            1781
                        ]
                    ],
                    "model_confidence": [
                        97.23
                    ]
                },
                "country_of_origin_of_goods": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            756,
                            2198,
                            858,
                            2233
                        ]
                    ],
                    "model_confidence": [
                        89.76
                    ]
                },
                "declaration_by_issuer": {
                    "value": "LTD. HT ZHEJLANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            974,
                            2356,
                            1068,
                            2388
                        ],
                        [
                            1480,
                            2886,
                            2127,
                            3030
                        ]
                    ],
                    "model_confidence": [
                        64.16,
                        58.03784096212526
                    ]
                },
                "signature_of_the_issuer": {
                    "value": "A RS",
                    "coordinate": [
                        [
                            1755,
                            2868,
                            2055,
                            2949
                        ]
                    ],
                    "model_confidence": [
                        97.76349397590363
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1553,
                            2620,
                            2054,
                            2829
                        ]
                    ],
                    "model_confidence": [
                        0.7659828066825867
                    ]
                },
                "is_stamp": {},
                "invoice_currency": {
                    "value": "USD",
                    "coordinate": [
                        [
                            1440,
                            1606,
                            1698,
                            1644
                        ]
                    ],
                    "model_confidence": [
                        44.26
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
                "port_of_loading": {},
                "bill_of_lading_no": {},
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
                "invoice_amount_in_words": {},
                "beneficiary_country": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            421,
                            631,
                            2003,
                            683
                        ]
                    ],
                    "model_confidence": [
                        99.33386761621668
                    ]
                },
                "remitter_drawee_applicant_importer_buyer_name": {}
            }
        },
        "page19": {
            "docClass": "COO",
            "keys_extraction": {
                "consignor_name": {
                    "value": "MEDICINE CO., LTD. 1.",
                    "coordinate": [
                        [
                            262,
                            168,
                            788,
                            217
                        ]
                    ],
                    "model_confidence": [
                        97.95874543737291
                    ]
                },
                "consignor_address": {
                    "value": "168 ZHIYUANZHONG AVENUE BINHAT NEW AREA SHAOXING ZHEJIANG 312366 P R ",
                    "coordinate": [
                        [
                            302,
                            220,
                            1046,
                            294
                        ]
                    ],
                    "model_confidence": [
                        99.6586813786083
                    ]
                },
                "consignee_name": {
                    "value": "CADOBEWE LABORATORIES LTD",
                    "coordinate": [
                        [
                            307,
                            476,
                            744,
                            522
                        ]
                    ],
                    "model_confidence": [
                        99.64406522561855
                    ]
                },
                "consignee_address": {
                    "value": "VILLAGE JAUIA KHURD TEHSIL DERA BASSI PUNJAB140501 ",
                    "coordinate": [
                        [
                            302,
                            519,
                            979,
                            592
                        ]
                    ],
                    "model_confidence": [
                        99.25
                    ]
                },
                "means_of_transport": {
                    "value": "AIR",
                    "coordinate": [
                        [
                            1036,
                            775,
                            1091,
                            803
                        ]
                    ],
                    "model_confidence": [
                        98.65
                    ]
                },
                "marks_and_no_of_packages": {
                    "value": "NM",
                    "coordinate": [
                        [
                            297,
                            1388,
                            354,
                            1437
                        ]
                    ],
                    "model_confidence": [
                        99.42
                    ]
                },
                "description_of_goods": {
                    "value": "TWENTY (20) DRUMS OF RIFANYCIN O FER EEE EEE EEE DOE",
                    "coordinate": [
                        [
                            701,
                            1392,
                            1125,
                            1504
                        ]
                    ],
                    "model_confidence": [
                        87.50007844046618
                    ]
                },
                "original_or_copy": {
                    "value": "ORIGINAL",
                    "coordinate": [
                        [
                            1170,
                            80,
                            1435,
                            119
                        ]
                    ],
                    "model_confidence": [
                        98.48
                    ]
                },
                "coo_issuer_address": {
                    "value": "THE REPUBLIC OF ",
                    "coordinate": [
                        [
                            1378,
                            497,
                            2303,
                            536
                        ]
                    ],
                    "model_confidence": [
                        99.22488071570575
                    ]
                },
                "invoice_no": {
                    "value": "B00KCS",
                    "coordinate": [
                        [
                            1892,
                            1399,
                            1998,
                            1430
                        ]
                    ],
                    "model_confidence": [
                        64.94
                    ]
                },
                "signature": {
                    "value": "LE ARH",
                    "coordinate": [
                        [
                            471,
                            2882,
                            915,
                            2959
                        ]
                    ],
                    "model_confidence": [
                        83.91
                    ]
                },
                "declaration_by_exporter": {
                    "value": "ZHEJIANG MEDICINE CO., LTD,",
                    "coordinate": [
                        [
                            471,
                            2984,
                            1111,
                            3058
                        ]
                    ],
                    "model_confidence": [
                        99.36017390426595
                    ]
                },
                "issue_date": {
                    "value": "DEC. 30,2021",
                    "coordinate": [
                        [
                            788,
                            3187,
                            1004,
                            3236
                        ]
                    ],
                    "model_confidence": [
                        98.15196113074205
                    ]
                },
                "is_signed": {},
                "is_stamp": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1611,
                            2742,
                            2137,
                            3227
                        ]
                    ],
                    "model_confidence": [
                        0.8968883752822876
                    ]
                },
                "consignor_address_country": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            302,
                            220,
                            1046,
                            294
                        ]
                    ],
                    "model_confidence": [
                        99.6586813786083
                    ]
                },
                "consignee_address_country": {
                    "value": "INDIA",
                    "coordinate": [
                        [
                            302,
                            519,
                            979,
                            592
                        ]
                    ],
                    "model_confidence": [
                        99.25
                    ]
                },
                "coo_issuer_address_country": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            1378,
                            497,
                            2303,
                            536
                        ]
                    ],
                    "model_confidence": [
                        99.22488071570575
                    ]
                },
                "certificate_no": {},
                "vessel_details": {},
                "country_of_origin_of_goods": {},
                "original_number": {},
                "invoice_date": {},
                "lc_date": {},
                "declaration_by_certification": {},
                "ref_no": {},
                "coo_issuer_name": {},
                "lc_ref_no": {},
                "from_place": {},
                "certificate_stamped": {},
                "page_no": {},
                "gross_weight": {},
                "net_weight": {},
                "final_destination": {},
                "to_place": {}
            }
        },
        "page23": {
            "docClass": "AWB",
            "keys_extraction": {
                "house_awb_bill_no": {
                    "value": "13139055402 SHAE21122181",
                    "coordinate": [
                        [
                            283,
                            151,
                            2223,
                            207
                        ]
                    ],
                    "model_confidence": [
                        30.57
                    ]
                },
                "consignee_name": {
                    "value": "HEJIANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            252,
                            339,
                            818,
                            372
                        ]
                    ],
                    "model_confidence": [
                        95.31369496301515
                    ]
                },
                "consignee_address": {
                    "value": "8 MID ZHIYUAN AVENUE BINHAI NEW AREA SHAOXING ITY ZHEJIANG PROVINCE 312366 PR CHINA 252 382 1341 471 9724846134116223 790 930 910 930 910 460 950 840 960 960 950 930 910 960 910 900~8 MID ZHIYUAN AVENUE BINHAI NEW AREA SHAOXING ITY ZHEJIANG PROVINCE 312366 PR CHINA 252 382 1341 471 9724846134116223 790 930 910 930 910 460 950 840 960 960 950 930 910 960 910 900 252 382 1341 471 9724846134116223 790 930 910 930 910 460 950 840 960 960 950 930 910 960 910 900~",
                    "coordinate": [
                        [
                            252,
                            382,
                            1341,
                            471
                        ]
                    ],
                    "model_confidence": [
                        79.33935828078994
                    ]
                },
                "agent_name": {
                    "value": "XIS BANK LTD",
                    "coordinate": [
                        [
                            255,
                            607,
                            520,
                            643
                        ]
                    ],
                    "model_confidence": [
                        75.63592055003821
                    ]
                },
                "agent_address": {
                    "value": "CHANDIGARH160022,",
                    "coordinate": [
                        [
                            777,
                            663,
                            1211,
                            699
                        ]
                    ],
                    "model_confidence": [
                        25.1
                    ]
                },
                "notify_party_name": {
                    "value": "ADCHEM LABORATORIES LIMITED",
                    "coordinate": [
                        [
                            252,
                            891,
                            895,
                            943
                        ]
                    ],
                    "model_confidence": [
                        76.3446085161755
                    ]
                },
                "notify_party_address": {
                    "value": "ILLAGE JAULA KHURD TEHSIL DERABASSI DISTRIK 4S NAGAR PUNJAB140501 ",
                    "coordinate": [
                        [
                            252,
                            947,
                            1203,
                            1029
                        ]
                    ],
                    "model_confidence": [
                        52.879085148288766
                    ]
                },
                "freight_collect_or_prepaid": {
                    "value": "FREIGHT COLLECT",
                    "coordinate": [
                        [
                            1606,
                            966,
                            1960,
                            993
                        ]
                    ],
                    "model_confidence": [
                        96.49
                    ]
                },
                "gross_weight": {
                    "value": "6",
                    "coordinate": [
                        [
                            308,
                            1768,
                            413,
                            1798
                        ]
                    ],
                    "model_confidence": [
                        94.15
                    ]
                },
                "carriage_condition": {
                    "value": "AS ANY PART OF THE NAME AND ISIN PROPER CONTIN OTA ECHO FOR CARRIAGE BY AIR ACCORDING TQ ; OSG IC AYE? |; 9 BY AIR FOR CONDITION BY AIR FOR",
                    "coordinate": [
                        [
                            1014,
                            2715,
                            2312,
                            2808
                        ]
                    ],
                    "model_confidence": [
                        86.02107603409931
                    ]
                },
                "awb_bill_issue_date": {
                    "value": "23,DEC 2021",
                    "coordinate": [
                        [
                            1017,
                            3029,
                            1252,
                            3062
                        ]
                    ],
                    "model_confidence": [
                        95.88550757923748
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1917,
                            2791,
                            2137,
                            3152
                        ]
                    ],
                    "model_confidence": [
                        0.5714031457901001
                    ]
                },
                "is_stamp": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1380,
                            2652,
                            1942,
                            3031
                        ]
                    ],
                    "model_confidence": [
                        0.8947916030883789
                    ]
                },
                "notify_party_address_country": {
                    "value": "INDIA",
                    "coordinate": [
                        [
                            252,
                            947,
                            1203,
                            1029
                        ]
                    ],
                    "model_confidence": [
                        52.879085148288766
                    ]
                },
                "declared_value_of_carriage": {},
                "flight_details": {},
                "flight_date": {},
                "airport_of_departure": {},
                "stamp": {},
                "dimension": {},
                "lc_no": {},
                "carrier_name": {},
                "master_awb_bill_no": {},
                "airport_of_destination": {},
                "signature": {},
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
                "goods_description": {}
            }
        },
        "page21": {
            "docClass": "COO",
            "keys_extraction": {
                "consignor_name": {
                    "value": "MEDICINE CO., 1. BWBGABNG LTD.",
                    "coordinate": [
                        [
                            323,
                            141,
                            841,
                            204
                        ]
                    ],
                    "model_confidence": [
                        98.57067048040635
                    ]
                },
                "consignor_address": {
                    "value": "168 ZHI SHAOXING AVENUE BINHAI NEW AREA R ZHEJIANG 312366 P ",
                    "coordinate": [
                        [
                            341,
                            188,
                            1099,
                            280
                        ]
                    ],
                    "model_confidence": [
                        99.80047342534891
                    ]
                },
                "consignee_name": {
                    "value": "LTD",
                    "coordinate": [
                        [
                            744,
                            462,
                            800,
                            491
                        ]
                    ],
                    "model_confidence": [
                        76.34
                    ]
                },
                "consignee_address": {
                    "value": "VILLAGE JAUIA KHURD TEHSIL DERA BASSI PUNJAB140501 ",
                    "coordinate": [
                        [
                            357,
                            501,
                            1032,
                            574
                        ]
                    ],
                    "model_confidence": [
                        99.74
                    ]
                },
                "means_of_transport": {
                    "value": "AIR",
                    "coordinate": [
                        [
                            1091,
                            759,
                            1144,
                            788
                        ]
                    ],
                    "model_confidence": [
                        99.01
                    ]
                },
                "marks_and_no_of_packages": {
                    "value": "20 NM",
                    "coordinate": [
                        [
                            354,
                            1379,
                            948,
                            1415
                        ]
                    ],
                    "model_confidence": [
                        85.775
                    ]
                },
                "description_of_goods": {
                    "value": "TWENTY DRUMS OF RIFAMYCIN 0 EK ER EK OER",
                    "coordinate": [
                        [
                            754,
                            1382,
                            1122,
                            1501
                        ]
                    ],
                    "model_confidence": [
                        75.55
                    ]
                },
                "declaration_by_exporter": {
                    "value": "CO., LTD. THEYIANG",
                    "coordinate": [
                        [
                            499,
                            2983,
                            1132,
                            3088

            ]
                    ],
                    "model_confidence": [
                        92.57
                    ]
                },
                "certificate_stamped": {
                    "value": "NEDICINE",
                    "coordinate": [
                        [
                            721,
                            3003,
                            918,
                            3069
                        ]
                    ],
                    "model_confidence": [
                        30.09
                    ]
                },
                "signature": {
                    "value": "MI",
                    "coordinate": [
                        [
                            1139,
                            3042,
                            1297,
                            3220
                        ]
                    ],
                    "model_confidence": [
                        88.97
                    ]
                },
                "issue_date": {
                    "value": "DEC. 30, 2021",
                    "coordinate": [
                        [
                            844,
                            3191,
                            1058,
                            3237
                        ]
                    ],
                    "model_confidence": [
                        97.99968085106383
                    ]
                },
                "original_or_copy": {
                    "value": "COPY",
                    "coordinate": [
                        [
                            1287,
                            69,
                            1440,
                            108
                        ]
                    ],
                    "model_confidence": [
                        97.16
                    ]
                },
                "coo_issuer_address": {
                    "value": "THE REPUBLIC OF ",
                    "coordinate": [
                        [
                            1435,
                            491,
                            2356,
                            531
                        ]
                    ],
                    "model_confidence": [
                        99.74754016064257
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1132,
                            3037,
                            1353,
                            3181
                        ]
                    ],
                    "model_confidence": [
                        0.5235992074012756
                    ]
                },
                "is_stamp": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1710,
                            2791,
                            2212,
                            3272
                        ]
                    ],
                    "model_confidence": [
                        0.9021368026733398
                    ]
                },
                "consignor_address_country": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            341,
                            188,
                            1099,
                            280
                        ]
                    ],
                    "model_confidence": [
                        99.80047342534891
                    ]
                },
                "consignee_address_country": {
                    "value": "INDIA",
                    "coordinate": [
                        [
                            357,
                            501,
                            1032,
                            574
                        ]
                    ],
                    "model_confidence": [
                        99.74
                    ]
                },
                "coo_issuer_address_country": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            1435,
                            491,
                            2356,
                            531
                        ]
                    ],
                    "model_confidence": [
                        99.74754016064257
                    ]
                },
                "certificate_no": {},
                "vessel_details": {},
                "country_of_origin_of_goods": {},
                "original_number": {},
                "invoice_date": {},
                "invoice_no": {},
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
            }
        },
        "page6": {
            "docClass": "BOE",
            "keys_extraction": {
                "bill_exchange_date": {
                    "value": "JANUARY 10,2022",
                    "coordinate": [
                        [
                            2458,
                            1210,
                            2756,
                            1254
                        ]
                    ],
                    "model_confidence": [
                        71.22
                    ]
                },
                "tenor_indicator": {
                    "value": "DAYS",
                    "coordinate": [
                        [
                            1276,
                            1371,
                            1364,
                            1480
                        ]
                    ],
                    "model_confidence": [
                        47.38
                    ]
                },
                "indicator_type": {
                    "value": "FROM",
                    "coordinate": [
                        [
                            1392,
                            1413,
                            1472,
                            1480
                        ]
                    ],
                    "model_confidence": [
                        48.03
                    ]
                },
                "indicator_date": {
                    "value": "DATE AWS",
                    "coordinate": [
                        [
                            1493,
                            1391,
                            1662,
                            1450
                        ]
                    ],
                    "model_confidence": [
                        73.38
                    ]
                },
                "invoice_due_date": {
                    "value": "20211223",
                    "coordinate": [
                        [
                            1676,
                            1391,
                            1830,
                            1488
                        ]
                    ],
                    "model_confidence": [
                        8.84
                    ]
                },
                "signature": {
                    "value": "ZHEJIANG WEDICINE CO., LBD",
                    "coordinate": [
                        [
                            2016,
                            2117,
                            2546,
                            2162
                        ]
                    ],
                    "model_confidence": [
                        68.19700960473855
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1625,
                            1485,
                            1973,
                            2073
                        ]
                    ],
                    "model_confidence": [
                        0.5434515476226807
                    ]
                },
                "is_stamp": {},
                "lc_ref_no": {},
                "drawer_address": {},
                "boe_currency": {},
                "original_or_copy": {},
                "drawer_bank_name": {},
                "issue_place": {},
                "drawer_name": {},
                "invoice_no": {},
                "stamp": {},
                "boe_amount": {},
                "diclaration_by": {},
                "amount_in_words": {},
                "invoice_amount": {},
                "invoice_date": {},
                "country_of_origin": {},
                "drawee_name": {},
                "drawee_address": {},
                "bill_exchange_no": {},
                "usance_tenor": {},
                "drawee_bank_address": {},
                "lc_date": {},
                "drawee_bank_name": {},
                "invoice_currency": {},
                "drawer_bank_address": {},
                "tenor_type": {}
            }
        },
        "page25": {
            "docClass": "AWB",
            "keys_extraction": {
                "house_awb_bill_no": {
                    "value": "1122181",
                    "coordinate": [
                        [
                            2093,
                            168,
                            2226,
                            198
                        ]
                    ],
                    "model_confidence": [
                        67.81
                    ]
                },
                "shipper_name": {
                    "value": "ZHENANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            224,
                            333,
                            816,
                            372
                        ]
                    ],
                    "model_confidence": [
                        96.05260930273148
                    ]
                },
                "shipper_address": {
                    "value": "168 MID ZHIYUAN AVENUE BINHAI NEW AREA SH CITY ZHEJIANG PROVINCE 312366",
                    "coordinate": [
                        [
                            224,
                            386,
                            1203,
                            468
                        ]
                    ],
                    "model_confidence": [
                        98.16632046750343
                    ]
                },
                "consignee_address": {
                    "value": "PR CHINA 930 435 1139 465 905 820 960 750 790 850 920 900 950 960~PR CHINA 930 435 1139 465 905 820 960 750 790 850 920 900 950 960 930 435 1139 465 905 820 960 750 790 850 920 900 950 960~",
                    "coordinate": [
                        [
                            930,
                            435,
                            1139,
                            465
                        ]
                    ],
                    "model_confidence": [
                        92.98457207713531
                    ]
                },
                "consignee_name": {
                    "value": "AXIS BANK LTD",
                    "coordinate": [
                        [
                            221,
                            610,
                            520,
                            643
                        ]
                    ],
                    "model_confidence": [
                        98.21572559366754
                    ]
                },
                "notify_party_name": {
                    "value": "CADCHEM LABORATORIES LIMITED",
                    "coordinate": [
                        [
                            216,
                            897,
                            892,
                            930
                        ]
                    ],
                    "model_confidence": [
                        85.47930210248255
                    ]
                },
                "notify_party_address": {
                    "value": "VILLAGE JAULA KHURD TEHSIL DERABASSI DISTRI SAS NAGAR PUNJAB 140501 ",
                    "coordinate": [
                        [
                            216,
                            943,
                            1193,
                            1026
                        ]
                    ],
                    "model_confidence": [
                        94.92786950217496
                    ]
                },
                "airport_of_departure": {
                    "value": "PUDONG",
                    "coordinate": [
                        [
                            214,
                            1188,
                            374,
                            1221
                        ]
                    ],
                    "model_confidence": [
                        85.02
                    ]
                },
                "signature": {
                    "value": "POT IK =F AN IME ME NE ",
                    "coordinate": [
                        [
                            145,
                            1217,
                            479,
                            1369
                        ],
                        [
                            351,
                            2356,
                            879,
                            2570
                        ],
                        [
                            145,
                            2673,
                            283,
                            2890
                        ],
                        [
                            736,
                            2676,
                            867,
                            2775
                        ]
                    ],
                    "model_confidence": [
                        31.98,
                        49.592709149163404,
                        51.96,
                        51.14
                    ]
                },
                "gross_weight": {
                    "value": "6",
                    "coordinate": [
                        [
                            306,
                            1758,
                            413,
                            1811
                        ]
                    ],
                    "model_confidence": [
                        85.84
                    ]
                },
                "is_signed": {},
                "is_stamp": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1393,
                            2649,
                            1969,
                            3030
                        ]
                    ],
                    "model_confidence": [
                        0.8090240359306335
                    ]
                },
                "consignee_address_country": {
                    "value": "CHINA CHINA",
                    "coordinate": [
                        [
                            930,
                            435,
                            1139,
                            465
                        ]
                    ],
                    "model_confidence": [
                        92.98457207713531
                    ]
                },
                "notify_party_address_country": {
                    "value": "INDIA",
                    "coordinate": [
                        [
                            216,
                            943,
                            1193,
                            1026
                        ]
                    ],
                    "model_confidence": [
                        94.92786950217496
                    ]
                },
                "declared_value_of_carriage": {},
                "flight_details": {},
                "flight_date": {},
                "freight_collect_or_prepaid": {},
                "stamp": {},
                "dimension": {},
                "carriage_condition": {},
                "lc_no": {},
                "carrier_name": {},
                "agent_name": {},
                "master_awb_bill_no": {},
                "airport_of_destination": {},
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
                "declared_value_of_custom": {},
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
                "goods_description": {},
                "awb_bill_issue_date": {}
            }
        },
        "page4": {
            "docClass": "CS",
            "keys_extraction": {
                "drawee_bank_name": {
                    "value": "AXIS BANK LTD,",
                    "coordinate": [
                        [
                            205,
                            564,
                            528,
                            599
                        ]
                    ],
                    "model_confidence": [
                        98.84855172413793
                    ]
                },
                "drawee_bank_address": {
                    "value": "SCO 343344SECTOR 35B ",
                    "coordinate": [
                        [
                            205,
                            613,
                            761,
                            690
                        ]
                    ],
                    "model_confidence": [
                        99.4803345814132
                    ]
                },
                "csh_ref_no": {
                    "value": "BP33221C10637901 0041FLC210044 CP202130061",
                    "coordinate": [
                        [
                            1212,
                            813,
                            1559,
                            1181
                        ]
                    ],
                    "model_confidence": [
                        52.29
                    ]
                },
                "csh_bill_currency": {
                    "value": "USD",
                    "coordinate": [
                        [
                            1212,
                            911,
                            1292,
                            943
                        ]
                    ],
                    "model_confidence": [
                        99.14
                    ]
                },
                "csh_bill_amount": {
                    "value": "42,250.00",
                    "coordinate": [
                        [
                            1304,
                            911,
                            1470,
                            946
                        ]
                    ],
                    "model_confidence": [
                        96.62
                    ]
                },
                "usance_tenor": {
                    "value": "90",
                    "coordinate": [
                        [
                            1212,
                            1010,
                            1252,
                            1038
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
                            1264,
                            1006,
                            1373,
                            1038
                        ]
                    ],
                    "model_confidence": [
                        98.02
                    ]
                },
                "tenor_indicator_type": {
                    "value": "FROM",
                    "coordinate": [
                        [
                            1388,
                            1006,
                            1505,
                            1038
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
                            1517,
                            1006,
                            1736,
                            1038
                        ]
                    ],
                    "model_confidence": [
                        99.62
                    ]
                },
                "csh_due_date": {
                    "value": "20211223 20220323",
                    "coordinate": [
                        [
                            1745,
                            1006,
                            1909,
                            1038
                        ],
                        [
                            1488,
                            1764,
                            1698,
                            1795
                        ]
                    ],
                    "model_confidence": [
                        99.4,
                        92.54
                    ]
                },
                "drawer_bank_name": {
                    "value": "INDUSTRIAL AND COMMERCIAL BANK OF CHINA HANGZHOU BRANCH",
                    "coordinate": [
                        [
                            1515,
                            164,
                            2184,
                            227
                        ]
                    ],
                    "model_confidence": [
                        89.96394366197183
                    ]
                },
                "drawer_bank_address": {
                    "value": "3FNO4 HUANCHENGBE ROAD ZHEJIANG TEL8657 HANGZHOU ",
                    "coordinate": [
                        [
                            1515,
                            241,
                            2189,
                            308
                        ]
                    ],
                    "model_confidence": [
                        97.6
                    ]
                },
                "drawer_bank_bic": {
                    "value": "SWIFTICBKCNBJZJP",
                    "coordinate": [
                        [
                            1517,
                            322,
                            1835,
                            347
                        ]
                    ],
                    "model_confidence": [
                        90.16
                    ]
                },
                "csh_presentation_date": {
                    "value": "02-02-2020",
                    "coordinate": [
                        [
                            1517,
                            515,
                            1835,
                            543
                        ]
                    ],
                    "model_confidence": [
                        74.85
                    ]
                },
                "document_enclosed": {
                    "value": "IST 2ND 2/2 1SET 14+2C~DOCUMENT DRAFT AIRWAY BILLS CERTIFICATE OF ORIGIN~\\ST 6 4 2ND~DOCUMENT COMMERCIAL INVOICE PACKING LIST~",
                    "coordinate": [
                        [
                            215,
                            1444,
                            448,
                            1686
                        ]
                    ],
                    "model_confidence": [
                        99.9790142847782
                    ]
                },
                "page_no": {
                    "value": "11",
                    "coordinate": [
                        [
                            2269,
                            3398,
                            2321,
                            3436
                        ]
                    ],
                    "model_confidence": [
                        99.81
                    ]
                },
                "drawee_bank_address_country": {
                    "value": "INDIA",
                    "coordinate": [
                        [
                            205,
                            613,
                            761,
                            690
                        ]
                    ],
                    "model_confidence": [
                        99.4803345814132
                    ]
                },
                "drawer_bank_address_country": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            1515,
                            241,
                            2189,
                            308
                        ]
                    ],
                    "model_confidence": [
                        97.6
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
                "currency_amount": {},
                "drawee_bank_bic": {},
                "drawer_bank_bottom_address": {},
                "drawer_bank_bottom_name": {},
                "drawer_ref_no": {},
                "nostro_bank_address": {},
                "drawer_name": {}
            }
        },
        "page27": {
            "docClass": "AWB",
            "keys_extraction": {
                "shipper_name": {
                    "value": "ZHEILEANG MEDICINE HTE INDIA",
                    "coordinate": [
                        [
                            224,
                            336,
                            816,
                            366
                        ],
                        [
                            224,
                            679,
                            328,
                            735
                        ]
                    ],
                    "model_confidence": [
                        75.80333333333333,
                        55.19
                    ]
                },
                "shipper_address": {
                    "value": "ITY ZNENANG PROVINGE",
                    "coordinate": [
                        [
                            237,
                            432,
                            752,
                            462
                        ]
                    ],
                    "model_confidence": [
                        51.49567404426559
                    ]
                },
                "notify_party_name": {
                    "value": "LARCIRATORIES",
                    "coordinate": [
                        [
                            443,
                            897,
                            736,
                            927
                        ]
                    ],
                    "model_confidence": [
                        39.92
                    ]
                },
                "consignee_address": {
                    "value": "62 4D 2ZAIVYUAN ",
                    "coordinate": [
                        [
                            252,
                            386,
                            892,
                            415
                        ]
                    ],
                    "model_confidence": [
                        67.03325425412993
                    ]
                },
                "airport_of_destination": {
                    "value": "AL NEW ARES",
                    "coordinate": [
                        [
                            861,
                            382,
                            1101,
                            429
                        ]
                    ],
                    "model_confidence": [
                        24.78650538231051
                    ]
                },
                "airport_of_departure": {
                    "value": "CHANDIGARH",
                    "coordinate": [
                        [
                            777,
                            663,
                            1035,
                            693
                        ]
                    ],
                    "model_confidence": [
                        38.17
                    ]
                },
                "good_marks": {
                    "value": "6",
                    "coordinate": [
                        [
                            892,
                            432,
                            910,
                            462
                        ]
                    ],
                    "model_confidence": [
                        14.18
                    ]
                },
                "notify_party_address": {
                    "value": "PLA",
                    "coordinate": [
                        [
                            928,
                            435,
                            984,
                            462
                        ]
                    ],
                    "model_confidence": [
                        9.33
                    ]
                },
                "final_destination": {
                    "value": "CHINA",
                    "coordinate": [
                        [
                            1042,
                            435,
                            1134,
                            462
                        ]
                    ],
                    "model_confidence": [
                        18.09
                    ]
                },
                "freight_collect_or_prepaid": {
                    "value": "FREIGHT COLLECT",
                    "coordinate": [
                        [
                            1606,
                            963,
                            1950,
                            990
                        ]
                    ],
                    "model_confidence": [
                        96.54
                    ]
                },
                "carriage_condition": {
                    "value": "SOFAR AS ANY PART OF THE NAME AND IS INEROPERCONDITION",
                    "coordinate": [
                        [
                            1912,
                            2719,
                            2198,
                            2772
                        ]
                    ],
                    "model_confidence": [
                        98.39
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1929,
                            2800,
                            2108,
                            3133
                        ]
                    ],
                    "model_confidence": [
                        0.5154562592506409
                    ]
                },
                "is_stamp": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1386,
                            2647,
                            1952,
                            3044
                        ]
                    ],
                    "model_confidence": [
                        0.8870110511779785
                    ]
                },
                "consignee_address_country": {
                    "value": "GIN",
                    "coordinate": [
                        [
                            252,
                            386,
                            892,
                            415
                        ]
                    ],
                    "model_confidence": [
                        67.03325425412993
                    ]
                },
                "declared_value_of_carriage": {},
                "flight_details": {},
                "flight_date": {},
                "stamp": {},
                "dimension": {},
                "lc_no": {},
                "carrier_name": {},
                "gross_weight": {},
                "agent_name": {},
                "master_awb_bill_no": {},
                "signature": {},
                "agent_address": {},
                "invoice_date": {},
                "at_place": {},
                "place_of_receipt": {},
                "signed_by_carrier": {},
                "transaction_date": {},
                "net_weight": {},
                "awb_original_or_copy": {},
                "gross_quantity": {},
                "declared_value_of_custom": {},
                "invoice_number": {},
                "lc_date": {},
                "carrier_address": {},
                "amount_insurance": {},
                "signed_by_agent": {},
                "house_awb_bill_no": {},
                "flight_no": {},
                "freight_collected_at": {},
                "awb_original_number": {},
                "awb_bill_no": {},
                "goods_description": {},
                "awb_bill_issue_date": {},
                "consignee_name": {}
            }
        },
        "page18": {
            "docClass": "PL",
            "keys_extraction": {
                "beneficiary_drawer_exporter_seller_supplier_name": {
                    "value": "ZHEJIANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            776,
                            547,
                            1641,
                            599
                        ]
                    ],
                    "model_confidence": [
                        99.95166610210502
                    ]
                },
                "beneficiary_address": {
                    "value": "MID ZHIYUAN AVENUE BINHAI NEW AREA",
                    "coordinate": [
                        [
                            493,
                            641,
                            1143,
                            680
                        ]
                    ],
                    "model_confidence": [
                        68.25304387817361
                    ]
                },
                "consignee_name": {
                    "value": "TOCADCHEM LABORATORIES LTD.",
                    "coordinate": [
                        [
                            220,
                            971,
                            979,
                            1006
                        ]
                    ],
                    "model_confidence": [
                        69.46779246399684
                    ]
                },
                "invoice_no": {
                    "value": "NUMBERCP202130061",
                    "coordinate": [
                        [
                            1713,
                            964,
                            2132,
                            995
                        ]
                    ],
                    "model_confidence": [
                        99.16
                    ]
                },
                "consignee_address": {
                    "value": "ADDVILLAGE JAUIA KHURD TEHSIL DERA BASSI PUNJABINDIA",
                    "coordinate": [
                        [
                            220,
                            1034,
                            1264,
                            1132
                        ]
                    ],
                    "model_confidence": [
                        99.9
                    ]
                },
                "date_of_invoice": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1569,
                            1083,
                            1889,
                            1118
                        ]
                    ],
                    "model_confidence": [
                        71.36
                    ]
                },
                "payment_terms_terms_of_delivery_&_payment": {
                    "value": "PAYMENTLC 90 DAYS AFTER B/L DATE",
                    "coordinate": [
                        [
                            223,
                            1294,
                            984,
                            1339
                        ]
                    ],
                    "model_confidence": [
                        85.40541749093853
                    ]
                },
                "description_of_goods": {
                    "value": "RIFAMYCIN O",
                    "coordinate": [
                        [
                            617,
                            1578,
                            840,
                            1620
                        ]
                    ],
                    "model_confidence": [
                        99.9534599156118
                    ]
                },
                "total_quantity_of_goods": {
                    "value": "20 2",
                    "coordinate": [
                        [
                            1522,
                            1567,
                            2090,
                            1606
                        ]
                    ],
                    "model_confidence": [
                        55.6
                    ]
                },
                "lc_ref_no": {
                    "value": "NO0041FLC210044",
                    "coordinate": [
                        [
                            471,
                            1693,
                            845,
                            1728
                        ]
                    ],
                    "model_confidence": [
                        99.16
                    ]
                },
                "lc_date": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            994,
                            1693,
                            1220,
                            1728
                        ]
                    ],
                    "model_confidence": [
                        97.32
                    ]
                },
                "net_weight": {
                    "value": "",
                    "coordinate": [
                        [
                            416,
                            1767,
                            644,
                            1806
                        ]
                    ],
                    "model_confidence": [
                        99.83
                    ]
                },
                "gross_weight": {
                    "value": "",
                    "coordinate": [
                        [
                            419,
                            1844,
                            647,
                            1886
                        ]
                    ],
                    "model_confidence": [
                        98.45
                    ]
                },
                "declaration": {
                    "value": "ZHEJLANG MEDICINE CO.,LTD,",
                    "coordinate": [
                        [
                            1297,
                            2707,
                            1941,
                            2770
                        ]
                    ],
                    "model_confidence": [
                        96.13
                    ]
                },
                "country_of_origin_origin_of_goods": {
                    "value": "ORIGINCHINA",
                    "coordinate": [
                        [
                            620,
                            2135,
                            741,
                            2177
                        ]
                    ],
                    "model_confidence": [
                        33.27
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1338,
                            2275,
                            1707,
                            2514
                        ]
                    ],
                    "model_confidence": [
                        0.6833178400993347
                    ]
                },
                "is_stamp": {},
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
            }
        },
        "page16": {
            "docClass": "PL",
            "keys_extraction": {
                "beneficiary_drawer_exporter_seller_supplier_name": {
                    "value": "ZHEJIANG MEDICINE CO., LTD.",
                    "coordinate": [
                        [
                            773,
                            543,
                            1639,
                            596
                        ]
                    ],
                    "model_confidence": [
                        99.95232916870246
                    ]
                },
                "beneficiary_address": {
                    "value": "168 MID ZHIYUAN AVENUE BINHAI NEW AREA",
                    "coordinate": [
                        [
                            426,
                            641,
                            1143,
                            683
                        ]
                    ],
                    "model_confidence": [
                        86.11455390001088
                    ]
                },
                "consignee_name": {
                    "value": "TOCADCHEM LABORATORIES LTD.",
                    "coordinate": [
                        [
                            223,
                            974,
                            979,
                            1010
                        ]
                    ],
                    "model_confidence": [
                        69.15433378196501
                    ]
                },
                "invoice_no": {
                    "value": "NUMBERCP202130061",
                    "coordinate": [
                        [
                            1713,
                            957,
                            2132,
                            995
                        ]
                    ],
                    "model_confidence": [
                        99.09
                    ]
                },
                "consignee_address": {
                    "value": "VILLAGE JAUIA KHURD TEHSIL DERA BASSI PUNJABINDIA",
                    "coordinate": [
                        [
                            225,
                            1034,
                            1267,
                            1139
                        ]
                    ],
                    "model_confidence": [
                        99.89
                    ]
                },
                "date_of_invoice": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            1569,
                            1080,
                            1889,
                            1118
                        ]
                    ],
                    "model_confidence": [
                        71.36
                    ]
                },
                "payment_terms_terms_of_delivery_&_payment": {
                    "value": "PAYMENTLC 90 DAYS AFTER B/L DATE",
                    "coordinate": [
                        [
                            225,
                            1297,
                            987,
                            1343
                        ]
                    ],
                    "model_confidence": [
                        85.2218617527539
                    ]
                },
                "description_of_goods": {
                    "value": "RIFAMYCIN O",
                    "coordinate": [
                        [
                            620,
                            1578,
                            843,
                            1620
                        ]
                    ],
                    "model_confidence": [
                        97.15178512396695
                    ]
                },
                "total_quantity_of_goods": {
                    "value": "20 2",
                    "coordinate": [
                        [
                            1525,
                            1564,
                            2093,
                            1602
                        ]
                    ],
                    "model_confidence": [
                        77.68
                    ]
                },
                "lc_ref_no": {
                    "value": "NO0041FLC210044",
                    "coordinate": [
                        [
                            476,
                            1693,
                            850,
                            1732
                        ]
                    ],
                    "model_confidence": [
                        98.89
                    ]
                },
                "lc_date": {
                    "value": "13-12-2021",
                    "coordinate": [
                        [
                            999,
                            1690,
                            1222,
                            1728
                        ]
                    ],
                    "model_confidence": [
                        97.38
                    ]
                },
                "net_weight": {
                    "value": "",
                    "coordinate": [
                        [
                            421,
                            1771,
                            649,
                            1809
                        ]
                    ],
                    "model_confidence": [
                        99.46
                    ]
                },
                "gross_weight": {
                    "value": "",
                    "coordinate": [
                        [
                            426,
                            1848,
                            652,
                            1886
                        ]
                    ],
                    "model_confidence": [
                        97.1
                    ]
                },
                "declaration": {
                    "value": "MEDICINE CO., LTD. ZHEJLANG",
                    "coordinate": [
                        [
                            1401,
                            2581,
                            2043,
                            2672
                        ]
                    ],
                    "model_confidence": [
                        60.82569821317352
                    ]
                },
                "country_of_origin_origin_of_goods": {
                    "value": "ORIGINCHINA",
                    "coordinate": [
                        [
                            627,
                            2139,
                            746,
                            2181
                        ]
                    ],
                    "model_confidence": [
                        33.27
                    ]
                },
                "is_signed": {
                    "value": "TRUE",
                    "coordinate": [
                        [
                            1411,
                            2202,
                            1936,
                            2421
                        ]
                    ],
                    "model_confidence": [
                        0.6954280138015747
                    ]
                },
                "is_stamp": {},
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
            }
        }
    }
}


extraction_result_pdf_1 =  {"results": {
            "1609flc230614_14.png": {
                "docClass": "CI",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "GAGA AND CHLORIDES",
                        "coordinate": [
                            [
                                188,
                                95,
                                516,
                                179
                            ]
                        ],
                        "model_confidence": [
                            40.995000000000005
                        ]
                    },
                    "beneficiary_address": {
                        "value": "VINYLS 3RD FLOOR NEW DL TOWERS NATED NDIA",
                        "coordinate": [
                            [
                                157,
                                151,
                                292,
                                203
                            ]
                        ],
                        "model_confidence": [
                            72.78
                        ]
                    },
                    "consignee_address": {
                        "value": "DANGANO FORT MUNDRA PORT ",
                        "coordinate": [
                            [
                                127,
                                223,
                                218,
                                263
                            ]
                        ],
                        "model_confidence": [
                            52.83
                        ]
                    },
                    "invoice_amount_in_words": {
                        "value": "TWO HUNDRED PFTHEN THOUSAND AND SEX HUNDRED",
                        "coordinate": [
                            [
                                230,
                                532,
                                443,
                                560
                            ]
                        ],
                        "model_confidence": [
                            99.56
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
                        "value": "CHINA",
                        "coordinate": [
                            [
                                127,
                                223,
                                218,
                                263
                            ]
                        ],
                        "model_confidence": [
                            52.83
                        ]
                    },
                    "invoice_no": {},
                    "incoterm": {},
                    "vessel_flight_no": {},
                    "consignor_name": {},
                    "beneficiary_bank_country": {},
                    "transaction_currency": {},
                    "transaction_amonunt_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_tin": {},
                    "cosignee_name": {},
                    "bill_of_lading_date": {},
                    "invoice_tax_ccy": {},
                    "consignee_country": {},
                    "country_of_origin_of_goods": {},
                    "tenor_indicator": {},
                    "net_weight": {},
                    "total_quantity_of_goods": {},
                    "goods_description": {},
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
                    "port_of_discharge": {},
                    "port_of_loading": {},
                    "bill_of_lading_no": {},
                    "date_of_invoice": {},
                    "lc_ref_no": {},
                    "signature_of_the_issuer": {},
                    "lc_date": {},
                    "invoice_tax_amount": {},
                    "invoice_currency": {},
                    "notify_party_name": {},
                    "original_or_copy": {},
                    "invoice_amount": {},
                    "rate_per_unit": {},
                    "notify_party_address": {},
                    "beneficiary_bank_identifier": {},
                    "awb_number": {},
                    "page_no": {},
                    "remitter_address": {},
                    "shipper_name": {},
                    "beneficiary_bank_name": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_25.png": {},
            "1609flc230614_32.png": {},
            "1609flc230614_34.png": {
                "docClass": "COO",
                "keys_extraction": {
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
                    "certificate_no": {},
                    "vessel_details": {},
                    "country_of_origin_of_goods": {},
                    "declaration_by_exporter": {},
                    "consignor_address": {},
                    "original_number": {},
                    "invoice_date": {},
                    "consignee_name": {},
                    "invoice_no": {},
                    "lc_date": {},
                    "declaration_by_certification": {},
                    "consignor_name": {},
                    "marks_and_no_of_packages": {},
                    "ref_no": {},
                    "consignee_address": {},
                    "description_of_goods": {},
                    "coo_issuer_address": {},
                    "coo_issuer_name": {},
                    "means_of_transport": {},
                    "lc_ref_no": {},
                    "from_place": {},
                    "signature": {},
                    "certificate_stamped": {},
                    "issue_date": {},
                    "page_no": {},
                    "gross_weight": {},
                    "net_weight": {},
                    "original_or_copy": {},
                    "final_destination": {},
                    "to_place": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_20.png": {},
            "1609flc230614_19.png": {
                "docClass": "IC",
                "keys_extraction": {
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
                    "from_place": {},
                    "address_of_assured": {},
                    "insurance_issuer_address": {},
                    "policy_no": {},
                    "subject_matter_insured": {},
                    "declaration_by": {},
                    "claim_payable_in": {},
                    "country_of_origin_origin_of_goods": {},
                    "original_copy": {},
                    "name_of_assured": {},
                    "sum_insured_amount": {},
                    "conditions_of_coverage": {},
                    "expiry_date": {},
                    "premium": {},
                    "claim_payable_by_address": {},
                    "lc_date": {},
                    "vessel_or_flight_name": {},
                    "page_no": {},
                    "insurance_issuer_name": {},
                    "certificate_no": {},
                    "insurance_issuer_address_bottom": {},
                    "lc_ref_no": {},
                    "signature": {},
                    "original_Number": {},
                    "claim payable_by_name": {},
                    "insurance_issuer_name_bottom": {},
                    "issue_date": {},
                    "to_place": {},
                    "mode_of_transport": {},
                    "sum_insured_currency": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_15.png": {
                "docClass": "BOL",
                "keys_extraction": {
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
                    "country_of_origin": {},
                    "net_weight": {},
                    "shipper_name": {},
                    "vessel_name": {},
                    "freight_collect_or_prepaid": {},
                    "bill_of_lading_issue_date": {},
                    "port_of_discharge": {},
                    "bol_original_or_copy": {},
                    "page_no": {},
                    "lc_date": {},
                    "signed_By_agent": {},
                    "goods_marks_and_nos": {},
                    "transaction_date": {},
                    "signed_by_carrier": {},
                    "stamp": {},
                    "goods_quantity": {},
                    "consignee_name": {},
                    "shipper_address": {},
                    "container_number": {},
                    "gross_weight": {},
                    "signature": {},
                    "final_destination": {},
                    "measurement_or_dimension": {},
                    "lc_ref_number": {},
                    "notify_party_name": {},
                    "place_of_receipt": {},
                    "bill_of_lading_number": {},
                    "carrier_country": {},
                    "bol_original_number": {},
                    "place_of_issue": {},
                    "agent_country": {},
                    "carrier_name": {},
                    "notify_party_address": {},
                    "voyage_number": {},
                    "pre_carriage_by": {},
                    "goods_description": {},
                    "port_of_loading": {},
                    "freight_collect_at": {},
                    "agent_name": {},
                    "consignee_address": {},
                    "shipped_onboard_date": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_5.png": {
                "docClass": "CI",
                "keys_extraction": {
                    "original_or_copy": {
                        "value": "ORIGINAL,",
                        "coordinate": [
                            [
                                441,
                                99,
                                520,
                                125
                            ]
                        ],
                        "model_confidence": [
                            48.68
                        ]
                    },
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "VINYLS AND",
                        "coordinate": [
                            [
                                155,
                                159,
                                202,
                                187
                            ]
                        ],
                        "model_confidence": [
                            71.94
                        ]
                    },
                    "beneficiary_address": {
                        "value": "FLOOR CHLORDDES DLP TOWERS DELI10015 NDIA",
                        "coordinate": [
                            [
                                181,
                                170,
                                292,
                                212
                            ]
                        ],
                        "model_confidence": [
                            54.11
                        ]
                    },
                    "cosignee_name": {
                        "value": "LIMITED",
                        "coordinate": [
                            [
                                255,
                                159,
                                291,
                                187
                            ]
                        ],
                        "model_confidence": [
                            65.76
                        ]
                    },
                    "consignee_address": {
                        "value": "SIVAN MAR NEW AINGANG PORT FORT INA CHINA 121 184 222 274 7773015706806282 560 410 930 270 680 910 760 410 350~SIVAN MAR NEW AINGANG PORT FORT INA CHINA 121 184 222 274 7773015706806282 560 410 930 270 680 910 760 410 350 121 184 222 274 7773015706806282 560 410 930 270 680 910 760 410 350~",
                        "coordinate": [
                            [
                                121,
                                184,
                                222,
                                274
                            ]
                        ],
                        "model_confidence": [
                            50.35507853403141
                        ]
                    },
                    "declaration_by_issuer": {
                        "value": "BOHUA CHEMICAL CO, LTD.",
                        "coordinate": [
                            [
                                167,
                                429,
                                341,
                                457
                            ]
                        ],
                        "model_confidence": [
                            92.55224299065421
                        ]
                    },
                    "signature_of_the_issuer": {
                        "value": "SAW",
                        "coordinate": [
                            [
                                190,
                                480,
                                219,
                                508
                            ]
                        ],
                        "model_confidence": [
                            56.24
                        ]
                    },
                    "invoice_currency": {
                        "value": "",
                        "coordinate": [
                            [
                                455,
                                518,
                                473,
                                525
                            ]
                        ],
                        "model_confidence": [
                            85.01
                        ]
                    },
                    "invoice_amount": {
                        "value": "215,6000",
                        "coordinate": [
                            [
                                480,
                                518,
                                519,
                                525
                            ]
                        ],
                        "model_confidence": [
                            87.21
                        ]
                    },
                    "invoice_amount_in_words": {
                        "value": "TWO HUNDRED FIFTEEN THOUSAND AND SO HUNDRED",
                        "coordinate": [
                            [
                                240,
                                544,
                                456,
                                572
                            ]
                        ],
                        "model_confidence": [
                            99.69
                        ]
                    },
                    "invoice_no": {
                        "value": "165FLCZ614",
                        "coordinate": [
                            [
                                208,
                                594,
                                263,
                                601
                            ]
                        ],
                        "model_confidence": [
                            29.11
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
                        "value": "MAR CHINA MAR CHINA",
                        "coordinate": [
                            [
                                121,
                                184,
                                222,
                                274
                            ]
                        ],
                        "model_confidence": [
                            50.35507853403141
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
                    "country_of_origin_of_goods": {},
                    "tenor_indicator": {},
                    "net_weight": {},
                    "total_quantity_of_goods": {},
                    "goods_description": {},
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
                    "port_of_discharge": {},
                    "port_of_loading": {},
                    "bill_of_lading_no": {},
                    "date_of_invoice": {},
                    "lc_ref_no": {},
                    "lc_date": {},
                    "invoice_tax_amount": {},
                    "notify_party_name": {},
                    "rate_per_unit": {},
                    "notify_party_address": {},
                    "beneficiary_bank_identifier": {},
                    "awb_number": {},
                    "page_no": {},
                    "remitter_address": {},
                    "shipper_name": {},
                    "beneficiary_bank_name": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_6.png": {
                "docClass": "PL",
                "keys_extraction": {
                    "vessel_flight_no": {
                        "value": "ALSGLIVIA 2270",
                        "coordinate": [
                            [
                                144,
                                494,
                                225,
                                501
                            ]
                        ],
                        "model_confidence": [
                            99.20062499999999
                        ]
                    },
                    "net_weight": {
                        "value": "20010 22200  ",
                        "coordinate": [
                            [
                                157,
                                546,
                                209,
                                587
                            ]
                        ],
                        "model_confidence": [
                            80.72
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
                    "shipper_address": {},
                    "lc_date": {},
                    "notify_party_address": {},
                    "awb_number": {},
                    "date_of_invoice": {},
                    "track_reference": {},
                    "country_of_origin_origin_of_goods": {},
                    "declaration": {},
                    "notify_party_name": {},
                    "bill_of_lading_date": {},
                    "dimension": {},
                    "transaction_currency": {},
                    "port_of_loading": {},
                    "gross_weight": {},
                    "transaction_date": {},
                    "lc_ref_no": {},
                    "total_quantity_of_goods": {},
                    "country_of_final_destination": {},
                    "consignee_name": {},
                    "invoice_amount": {},
                    "shipper_name": {},
                    "beneficiary_address": {},
                    "transaction_amount_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_name": {},
                    "consignor_address": {},
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
                    "invoice_no": {},
                    "port_of_discharge": {},
                    "original_copy": {},
                    "description_of_goods": {},
                    "awb_date": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_13.png": {
                "docClass": "PL",
                "keys_extraction": {
                    "original_copy": {
                        "value": "ORIGINAL,",
                        "coordinate": [
                            [
                                413,
                                97,
                                489,
                                122
                            ]
                        ],
                        "model_confidence": [
                            49.86
                        ]
                    },
                    "declaration": {
                        "value": "TANI BOMUA CO, LTD.",
                        "coordinate": [
                            [
                                142,
                                431,
                                355,
                                459
                            ]
                        ],
                        "model_confidence": [
                            94.61
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
                    "shipper_address": {},
                    "lc_date": {},
                    "notify_party_address": {},
                    "awb_number": {},
                    "vessel_flight_no": {},
                    "date_of_invoice": {},
                    "track_reference": {},
                    "country_of_origin_origin_of_goods": {},
                    "notify_party_name": {},
                    "bill_of_lading_date": {},
                    "dimension": {},
                    "transaction_currency": {},
                    "port_of_loading": {},
                    "gross_weight": {},
                    "net_weight": {},
                    "transaction_date": {},
                    "lc_ref_no": {},
                    "total_quantity_of_goods": {},
                    "country_of_final_destination": {},
                    "consignee_name": {},
                    "invoice_amount": {},
                    "shipper_name": {},
                    "beneficiary_address": {},
                    "transaction_amount_value": {},
                    "beneficiary_drawer_exporter_seller_supplier_name": {},
                    "consignor_address": {},
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
                    "invoice_no": {},
                    "port_of_discharge": {},
                    "description_of_goods": {},
                    "awb_date": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_4.png": {},
            "1609flc230614_2.png": {},
            "1609flc230614_26.png": {
                "docClass": "COO",
                "keys_extraction": {
                    "original_or_copy": {
                        "value": "ORIGINAL",
                        "coordinate": [
                            [
                                265,
                                33,
                                317,
                                42
                            ]
                        ],
                        "model_confidence": [
                            98.56
                        ]
                    },
                    "signature": {
                        "value": "JETOWARION",
                        "coordinate": [
                            [
                                295,
                                205,
                                346,
                                234
                            ]
                        ],
                        "model_confidence": [
                            20.08
                        ]
                    },
                    "certificate_stamped": {
                        "value": "JNTERNATIONAL",
                        "coordinate": [
                            [
                                297,
                                228,
                                370,
                                256
                            ]
                        ],
                        "model_confidence": [
                            8.94
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
                    "certificate_no": {},
                    "vessel_details": {},
                    "country_of_origin_of_goods": {},
                    "declaration_by_exporter": {},
                    "consignor_address": {},
                    "original_number": {},
                    "invoice_date": {},
                    "consignee_name": {},
                    "invoice_no": {},
                    "lc_date": {},
                    "declaration_by_certification": {},
                    "consignor_name": {},
                    "marks_and_no_of_packages": {},
                    "ref_no": {},
                    "consignee_address": {},
                    "description_of_goods": {},
                    "coo_issuer_address": {},
                    "coo_issuer_name": {},
                    "means_of_transport": {},
                    "lc_ref_no": {},
                    "from_place": {},
                    "issue_date": {},
                    "page_no": {},
                    "gross_weight": {},
                    "net_weight": {},
                    "final_destination": {},
                    "to_place": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_0.png": {},
            "1609flc230614_28.png": {
                "docClass": "IC",
                "keys_extraction": {
                    "insurance_issuer_address": {
                        "value": "TREN,",
                        "coordinate": [
                            [
                                254,
                                116,
                                289,
                                147
                            ]
                        ],
                        "model_confidence": [
                            17.31
                        ]
                    },
                    "sum_insured_currency": {
                        "value": "EER",
                        "coordinate": [
                            [
                                65,
                                226,
                                95,
                                242
                            ]
                        ],
                        "model_confidence": [
                            34.29
                        ]
                    },
                    "insurance_issuer_name_bottom": {
                        "value": "DIETICIAN",
                        "coordinate": [
                            [
                                253,
                                718,
                                319,
                                746
                            ]
                        ],
                        "model_confidence": [
                            45.19
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
                    "from_place": {},
                    "address_of_assured": {},
                    "policy_no": {},
                    "subject_matter_insured": {},
                    "declaration_by": {},
                    "claim_payable_in": {},
                    "country_of_origin_origin_of_goods": {},
                    "original_copy": {},
                    "name_of_assured": {},
                    "sum_insured_amount": {},
                    "conditions_of_coverage": {},
                    "expiry_date": {},
                    "premium": {},
                    "claim_payable_by_address": {},
                    "lc_date": {},
                    "vessel_or_flight_name": {},
                    "page_no": {},
                    "insurance_issuer_name": {},
                    "certificate_no": {},
                    "insurance_issuer_address_bottom": {},
                    "lc_ref_no": {},
                    "signature": {},
                    "original_Number": {},
                    "claim payable_by_name": {},
                    "issue_date": {},
                    "to_place": {},
                    "mode_of_transport": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_29.png": {
                "docClass": "PL",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "INTERNATIONAL PVT LIMITED",
                        "coordinate": [
                            [
                                215,
                                99,
                                447,
                                114
                            ]
                        ],
                        "model_confidence": [
                            99.81438596491228
                        ]
                    },
                    "beneficiary_address": {
                        "value": "9 EY",
                        "coordinate": [
                            [
                                206,
                                118,
                                295,
                                127
                            ]
                        ],
                        "model_confidence": [
                            71.49212298682284
                        ]
                    },
                    "port_of_discharge": {
                        "value": "MUNDRA",
                        "coordinate": [
                            [
                                139,
                                267,
                                223,
                                276
                            ]
                        ],
                        "model_confidence": [
                            40.6
                        ]
                    },
                    "net_weight": {
                        "value": "210000 0",
                        "coordinate": [
                            [
                                151,
                                556,
                                203,
                                584
                            ]
                        ],
                        "model_confidence": [
                            98.48
                        ]
                    },
                    "gross_weight": {
                        "value": "2",
                        "coordinate": [
                            [
                                155,
                                579,
                                199,
                                588
                            ]
                        ],
                        "model_confidence": [
                            96.45
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
                    "shipper_address": {},
                    "lc_date": {},
                    "notify_party_address": {},
                    "awb_number": {},
                    "vessel_flight_no": {},
                    "date_of_invoice": {},
                    "track_reference": {},
                    "country_of_origin_origin_of_goods": {},
                    "declaration": {},
                    "notify_party_name": {},
                    "bill_of_lading_date": {},
                    "dimension": {},
                    "transaction_currency": {},
                    "port_of_loading": {},
                    "transaction_date": {},
                    "lc_ref_no": {},
                    "total_quantity_of_goods": {},
                    "country_of_final_destination": {},
                    "consignee_name": {},
                    "invoice_amount": {},
                    "shipper_name": {},
                    "transaction_amount_value": {},
                    "consignor_address": {},
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
                    "invoice_no": {},
                    "original_copy": {},
                    "description_of_goods": {},
                    "awb_date": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_22.png": {
                "docClass": "PL",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "INTERNATIONAL RELY HU PVT LIMITED KEL OAD",
                        "coordinate": [
                            [
                                217,
                                69,
                                457,
                                111
                            ]
                        ],
                        "model_confidence": [
                            85.66
                        ]
                    },
                    "declaration": {
                        "value": "TWOHNORED BAS OY.",
                        "coordinate": [
                            [
                                278,
                                516,
                                385,
                                551
                            ]
                        ],
                        "model_confidence": [
                            76.37
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
                    "shipper_address": {},
                    "lc_date": {},
                    "notify_party_address": {},
                    "awb_number": {},
                    "vessel_flight_no": {},
                    "date_of_invoice": {},
                    "track_reference": {},
                    "country_of_origin_origin_of_goods": {},
                    "notify_party_name": {},
                    "bill_of_lading_date": {},
                    "dimension": {},
                    "transaction_currency": {},
                    "port_of_loading": {},
                    "gross_weight": {},
                    "net_weight": {},
                    "transaction_date": {},
                    "lc_ref_no": {},
                    "total_quantity_of_goods": {},
                    "country_of_final_destination": {},
                    "consignee_name": {},
                    "invoice_amount": {},
                    "shipper_name": {},
                    "beneficiary_address": {},
                    "transaction_amount_value": {},
                    "consignor_address": {},
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
                    "invoice_no": {},
                    "port_of_discharge": {},
                    "original_copy": {},
                    "description_of_goods": {},
                    "awb_date": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_9.png": {},
            "1609flc230614_27.png": {},
            "1609flc230614_33.png": {},
            "1609flc230614_24.png": {},
            "1609flc230614_7.png": {
                "docClass": "BOL",
                "keys_extraction": {
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
                    "country_of_origin": {},
                    "net_weight": {},
                    "shipper_name": {},
                    "vessel_name": {},
                    "freight_collect_or_prepaid": {},
                    "bill_of_lading_issue_date": {},
                    "port_of_discharge": {},
                    "bol_original_or_copy": {},
                    "page_no": {},
                    "lc_date": {},
                    "signed_By_agent": {},
                    "goods_marks_and_nos": {},
                    "transaction_date": {},
                    "signed_by_carrier": {},
                    "stamp": {},
                    "goods_quantity": {},
                    "consignee_name": {},
                    "shipper_address": {},
                    "container_number": {},
                    "gross_weight": {},
                    "signature": {},
                    "final_destination": {},
                    "measurement_or_dimension": {},
                    "lc_ref_number": {},
                    "notify_party_name": {},
                    "place_of_receipt": {},
                    "bill_of_lading_number": {},
                    "carrier_country": {},
                    "bol_original_number": {},
                    "place_of_issue": {},
                    "agent_country": {},
                    "carrier_name": {},
                    "notify_party_address": {},
                    "voyage_number": {},
                    "pre_carriage_by": {},
                    "goods_description": {},
                    "port_of_loading": {},
                    "freight_collect_at": {},
                    "agent_name": {},
                    "consignee_address": {},
                    "shipped_onboard_date": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_12.png": {},
            "1609flc230614_11.png": {
                "docClass": "IC",
                "keys_extraction": {
                    "original_Number": {
                        "value": "2",
                        "coordinate": [
                            [
                                465,
                                601,
                                470,
                                610
                            ]
                        ],
                        "model_confidence": [
                            97.91
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
                    "from_place": {},
                    "address_of_assured": {},
                    "insurance_issuer_address": {},
                    "policy_no": {},
                    "subject_matter_insured": {},
                    "declaration_by": {},
                    "claim_payable_in": {},
                    "country_of_origin_origin_of_goods": {},
                    "original_copy": {},
                    "name_of_assured": {},
                    "sum_insured_amount": {},
                    "conditions_of_coverage": {},
                    "expiry_date": {},
                    "premium": {},
                    "claim_payable_by_address": {},
                    "lc_date": {},
                    "vessel_or_flight_name": {},
                    "page_no": {},
                    "insurance_issuer_name": {},
                    "certificate_no": {},
                    "insurance_issuer_address_bottom": {},
                    "lc_ref_no": {},
                    "signature": {},
                    "claim payable_by_name": {},
                    "insurance_issuer_name_bottom": {},
                    "issue_date": {},
                    "to_place": {},
                    "mode_of_transport": {},
                    "sum_insured_currency": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_16.png": {},
            "1609flc230614_3.png": {},
            "1609flc230614_31.png": {
                "docClass": "BOL",
                "keys_extraction": {
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
                    "country_of_origin": {},
                    "net_weight": {},
                    "shipper_name": {},
                    "vessel_name": {},
                    "freight_collect_or_prepaid": {},
                    "bill_of_lading_issue_date": {},
                    "port_of_discharge": {},
                    "bol_original_or_copy": {},
                    "page_no": {},
                    "lc_date": {},
                    "signed_By_agent": {},
                    "goods_marks_and_nos": {},
                    "transaction_date": {},
                    "signed_by_carrier": {},
                    "stamp": {},
                    "goods_quantity": {},
                    "consignee_name": {},
                    "shipper_address": {},
                    "container_number": {},
                    "gross_weight": {},
                    "signature": {},
                    "final_destination": {},
                    "measurement_or_dimension": {},
                    "lc_ref_number": {},
                    "notify_party_name": {},
                    "place_of_receipt": {},
                    "bill_of_lading_number": {},
                    "carrier_country": {},
                    "bol_original_number": {},
                    "place_of_issue": {},
                    "agent_country": {},
                    "carrier_name": {},
                    "notify_party_address": {},
                    "voyage_number": {},
                    "pre_carriage_by": {},
                    "goods_description": {},
                    "port_of_loading": {},
                    "freight_collect_at": {},
                    "agent_name": {},
                    "consignee_address": {},
                    "shipped_onboard_date": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_1.png": {},
            "1609flc230614_21.png": {},
            "1609flc230614_8.png": {},
            "1609flc230614_10.png": {
                "docClass": "COO",
                "keys_extraction": {
                    "original_or_copy": {
                        "value": "ORIGINAL",
                        "coordinate": [
                            [
                                253,
                                35,
                                305,
                                44
                            ]
                        ],
                        "model_confidence": [
                            98.34
                        ]
                    },
                    "certificate_stamped": {
                        "value": "HINA TRADEIS",
                        "coordinate": [
                            [
                                293,
                                207,
                                343,
                                238
                            ]
                        ],
                        "model_confidence": [
                            45.64
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
                    "certificate_no": {},
                    "vessel_details": {},
                    "country_of_origin_of_goods": {},
                    "declaration_by_exporter": {},
                    "consignor_address": {},
                    "original_number": {},
                    "invoice_date": {},
                    "consignee_name": {},
                    "invoice_no": {},
                    "lc_date": {},
                    "declaration_by_certification": {},
                    "consignor_name": {},
                    "marks_and_no_of_packages": {},
                    "ref_no": {},
                    "consignee_address": {},
                    "description_of_goods": {},
                    "coo_issuer_address": {},
                    "coo_issuer_name": {},
                    "means_of_transport": {},
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
                "statusCode": "200"
            },
            "1609flc230614_23.png": {
                "docClass": "BOL",
                "keys_extraction": {
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
                    "country_of_origin": {},
                    "net_weight": {},
                    "shipper_name": {},
                    "vessel_name": {},
                    "freight_collect_or_prepaid": {},
                    "bill_of_lading_issue_date": {},
                    "port_of_discharge": {},
                    "bol_original_or_copy": {},
                    "page_no": {},
                    "lc_date": {},
                    "signed_By_agent": {},
                    "goods_marks_and_nos": {},
                    "transaction_date": {},
                    "signed_by_carrier": {},
                    "stamp": {},
                    "goods_quantity": {},
                    "consignee_name": {},
                    "shipper_address": {},
                    "container_number": {},
                    "gross_weight": {},
                    "signature": {},
                    "final_destination": {},
                    "measurement_or_dimension": {},
                    "lc_ref_number": {},
                    "notify_party_name": {},
                    "place_of_receipt": {},
                    "bill_of_lading_number": {},
                    "carrier_country": {},
                    "bol_original_number": {},
                    "place_of_issue": {},
                    "agent_country": {},
                    "carrier_name": {},
                    "notify_party_address": {},
                    "voyage_number": {},
                    "pre_carriage_by": {},
                    "goods_description": {},
                    "port_of_loading": {},
                    "freight_collect_at": {},
                    "agent_name": {},
                    "consignee_address": {},
                    "shipped_onboard_date": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_30.png": {
                "docClass": "CI",
                "keys_extraction": {
                    "beneficiary_drawer_exporter_seller_supplier_name": {
                        "value": "INTERNATIONAL PVT LIMITED VINYLS AND CHLORIDES",
                        "coordinate": [
                            [
                                162,
                                69,
                                474,
                                188
                            ]
                        ],
                        "model_confidence": [
                            84.70494807687635
                        ]
                    },
                    "original_or_copy": {
                        "value": "ORIGINAL",
                        "coordinate": [
                            [
                                438,
                                98,
                                511,
                                123
                            ]
                        ],
                        "model_confidence": [
                            37.6
                        ]
                    },
                    "signature_of_the_issuer": {
                        "value": "COMMERCIAL LUNTTED",
                        "coordinate": [
                            [
                                206,
                                143,
                                314,
                                156
                            ],
                            [
                                128,
                                544,
                                161,
                                572
                            ]
                        ],
                        "model_confidence": [
                            42.82,
                            27.2
                        ]
                    },
                    "cosignee_name": {
                        "value": "LIMITED",
                        "coordinate": [
                            [
                                260,
                                160,
                                295,
                                188
                            ]
                        ],
                        "model_confidence": [
                            57.37
                        ]
                    },
                    "beneficiary_address": {
                        "value": "MARA 3RD FLOOR NEW DLP TOWHRS NDIA",
                        "coordinate": [
                            [
                                166,
                                173,
                                298,
                                213
                            ]
                        ],
                        "model_confidence": [
                            90.57
                        ]
                    },
                    "consignee_address": {
                        "value": "FORT PORT DOU",
                        "coordinate": [
                            [
                                171,
                                234,
                                221,
                                274
                            ]
                        ],
                        "model_confidence": [
                            69.89
                        ]
                    },
                    "invoice_amount": {
                        "value": "21540000",
                        "coordinate": [
                            [
                                477,
                                516,
                                515,
                                528
                            ]
                        ],
                        "model_confidence": [
                            65.3
                        ]
                    },
                    "invoice_amount_in_words": {
                        "value": "TWO HUNDRED PFTHEN THOUSAND AND",
                        "coordinate": [
                            [
                                237,
                                544,
                                394,
                                572
                            ]
                        ],
                        "model_confidence": [
                            90.19
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
                    "invoice_no": {},
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
                    "country_of_origin_of_goods": {},
                    "tenor_indicator": {},
                    "net_weight": {},
                    "total_quantity_of_goods": {},
                    "goods_description": {},
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
                    "port_of_discharge": {},
                    "port_of_loading": {},
                    "bill_of_lading_no": {},
                    "date_of_invoice": {},
                    "lc_ref_no": {},
                    "lc_date": {},
                    "invoice_tax_amount": {},
                    "invoice_currency": {},
                    "notify_party_name": {},
                    "rate_per_unit": {},
                    "notify_party_address": {},
                    "beneficiary_bank_identifier": {},
                    "awb_number": {},
                    "page_no": {},
                    "remitter_address": {},
                    "shipper_name": {},
                    "beneficiary_bank_name": {},
                    "remitter_drawee_applicant_importer_buyer_name": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_17.png": {
                "docClass": "BOL",
                "keys_extraction": {
                    "signed_by_carrier": {
                        "value": "EAEREN",
                        "coordinate": [
                            [
                                359,
                                594,
                                361,
                                610
                            ]
                        ],
                        "model_confidence": [
                            30.08
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
                    "country_of_origin": {},
                    "net_weight": {},
                    "shipper_name": {},
                    "vessel_name": {},
                    "freight_collect_or_prepaid": {},
                    "bill_of_lading_issue_date": {},
                    "port_of_discharge": {},
                    "bol_original_or_copy": {},
                    "page_no": {},
                    "lc_date": {},
                    "signed_By_agent": {},
                    "goods_marks_and_nos": {},
                    "transaction_date": {},
                    "stamp": {},
                    "goods_quantity": {},
                    "consignee_name": {},
                    "shipper_address": {},
                    "container_number": {},
                    "gross_weight": {},
                    "signature": {},
                    "final_destination": {},
                    "measurement_or_dimension": {},
                    "lc_ref_number": {},
                    "notify_party_name": {},
                    "place_of_receipt": {},
                    "bill_of_lading_number": {},
                    "carrier_country": {},
                    "bol_original_number": {},
                    "place_of_issue": {},
                    "agent_country": {},
                    "carrier_name": {},
                    "notify_party_address": {},
                    "voyage_number": {},
                    "pre_carriage_by": {},
                    "goods_description": {},
                    "port_of_loading": {},
                    "freight_collect_at": {},
                    "agent_name": {},
                    "consignee_address": {},
                    "shipped_onboard_date": {}
                },
                "statusCode": "200"
            },
            "1609flc230614_18.png": {
                "docClass": "COO",
                "keys_extraction": {
                    "original_or_copy": {
                        "value": "ORIGINAL",
                        "coordinate": [
                            [
                                258,
                                39,
                                311,
                                48
                            ]
                        ],
                        "model_confidence": [
                            98.29
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
                    "certificate_no": {},
                    "vessel_details": {},
                    "country_of_origin_of_goods": {},
                    "declaration_by_exporter": {},
                    "consignor_address": {},
                    "original_number": {},
                    "invoice_date": {},
                    "consignee_name": {},
                    "invoice_no": {},
                    "lc_date": {},
                    "declaration_by_certification": {},
                    "consignor_name": {},
                    "marks_and_no_of_packages": {},
                    "ref_no": {},
                    "consignee_address": {},
                    "description_of_goods": {},
                    "coo_issuer_address": {},
                    "coo_issuer_name": {},
                    "means_of_transport": {},
                    "lc_ref_no": {},
                    "from_place": {},
                    "signature": {},
                    "certificate_stamped": {},
                    "issue_date": {},
                    "page_no": {},
                    "gross_weight": {},
                    "net_weight": {},
                    "final_destination": {},
                    "to_place": {}
                },
                "statusCode": "200"
            }
        }
}
def remove_non_alnum(page_x):
    if not page_x:
        return page_x
    page_x = "".join([x for x in page_x if x == " " or x.isalnum()])
    return page_x.lower().strip()


def fuzz_ratios(page_x, page_y):
    s1 = remove_non_alnum(page_x)
    s2 = remove_non_alnum(page_y)
    return (fuzz.ratio(s1, s2), fuzz.partial_ratio(s1, s2), fuzz.token_set_ratio(s1, s2), fuzz.token_sort_ratio(s1, s1))


def match_tuple_words(page_x, page_y, page_wise_unit):
    """
    match_tuple = (ratio,partial_ratio,tokenset,tokensort ratio
    """
    match_tuple_index = 2
    page_x_value = [x['value'] if 'value' in x else x for x in page_wise_unit[page_x]]
    page_y_value = [x['value'] if 'value' in x else x for x in page_wise_unit[page_y]]
    match_value = 0
    unit_len = len(page_x_value)
    for unit_index in range(len(page_x_value)):
        match_tuple = fuzz_ratios(page_x_value[unit_index], page_y_value[unit_index])
        match_value += match_tuple[match_tuple_index]
        page_x_value[unit_index] = (page_x_value[unit_index],match_tuple)
        page_y_value[unit_index] = (page_y_value[unit_index],match_tuple)
    match_value = match_value / (unit_len * 100)
    return (match_value,page_x_value,page_y_value)


def create_page_wise_unit(doc_pagewise_data:dict, pages_list:list,doc_wise_map_key):
    page_wise_unit:dict = {}
    for page_name, page_data in doc_pagewise_data.items():
        print(page_name)
        print(page_data.keys())
        exit('+++++++')
        page_wise_unit[page_name] = [page_data[k].get("value","") if k in page_data else "" for k in doc_wise_map_key ]
        keys_count = [len(value_x.get('value',""))>0 for key_x,value_x in page_data.items()].count(True)
        pages_list.append((page_name,keys_count))
    return page_wise_unit,pages_list


def get_document_set_wise(document_name, doc_pagewise_data, doc_wise_map_key):
    pages_list:list = []
    page_wise_match:dict = {}
    set_wise_pages:dict = {}
    set_wise_pages_debug:dict = {}

    page_wise_unit,pages_list = create_page_wise_unit(doc_pagewise_data,pages_list,doc_wise_map_key)
    print(page_wise_unit)
    print(pages_list)
    exit('++')
    with open(f"LOGS/{timestamp}/page_wise_units.json",'w') as file:
        json.dump(page_wise_unit,file,indent=2)
    for page_x in pages_list:
        page_x_unit_values = [(page_y, match_tuple_words(page_x, page_y, page_wise_unit)) for page_y in pages_list if
                              page_x != page_y]
        sorted_page_units = sorted(page_x_unit_values, key=lambda item: int(item[1][0]), reverse=True)
        matched_pages = [x for x in sorted_page_units if x[1][0] !=0 and x[1][0] == sorted_page_units[0][1][0]]
        page_wise_match[page_x] = matched_pages

    with open(f"LOGS/{timestamp}/page_wise_match.json", 'w') as file:
        json.dump(page_wise_match, file, indent=2)
    page_check:dict = {}
    _ = [page_check.update({_:False}) for _ in pages_list]
    for page,page_wise_data in page_wise_match.items():
        page_check[page] = True
        set_name = document_name+"_"+page
        if not page_wise_data:
            set_wise_pages.setdefault(set_name, set()).add(page)
            set_wise_pages_debug.setdefault(set_name, set()).add(page)

            continue

        for __page in page_wise_data:
            if not page_check[__page[0]]:
                page_check[__page[0]] = True
                set_wise_pages.setdefault(set_name, set()).add(page)
                set_wise_pages.setdefault(set_name,set()).add(__page[0])
                set_wise_pages_debug.setdefault(set_name, set()).add(page)
                print(__page)
                print(set_wise_pages_debug)
                set_wise_pages_debug.setdefault(set_name, set()).add(__page)
    with open(f"LOGS/{timestamp}/set_wise_page_match.txt","w") as file:
        file.write(f"{set_wise_pages_debug}")

    return set_wise_pages


def multipages_samekey_data_merge(key_data: list):
    max_key_len, key_value = 0, key_data[0]
    for i in range(len(key_data)):
        if len(key_data[i]) > max_key_len:
            max_key_len, key_value = len(key_data), key_data[i]
    return key_value


def get_merge_pages_data_util(pages_set:set, doc_pagewise_data:dict):
    merged_pages_data = {}
    for page_x in pages_set:
        for page_x_key, page_x_data in doc_pagewise_data[page_x].items():
            merged_pages_data.setdefault(page_x_key, []).append(page_x_data)
    return merged_pages_data


def get_merged_pages_data(pages_set: set, doc_pagewise_data: dict):
    merged_pages_data: dict = get_merge_pages_data_util(pages_set=pages_set,
                                                        doc_pagewise_data=doc_pagewise_data)

    for key_x, key_data in merged_pages_data.items():
        merged_pages_data[key_x] = multipages_samekey_data_merge(key_data)

    return merged_pages_data


def get_document_sets_master(document_name: dict, doc_pagewise_data: dict,
                             doc_wise_map_keys) -> dict:
    """doc:{page0:{value,coordinate},}"""

    document_set_wise: dict = get_document_set_wise(document_name, doc_pagewise_data,
                                                    doc_wise_map_keys)
    ## docuemnt_set_wise = {set1:{page1,page2,pag4},set3:{page4,page5}

    ###merge set pages
    for set_x, pages_set in document_set_wise.items():
        document_set_wise[set_x] = get_merged_pages_data(pages_set, doc_pagewise_data)

    return document_set_wise


def get_document_wise_data(data: dict):
    document_wise_data = {}
    for page_name, page_data in data.items():
        document_wise_data.setdefault(page_data['docClass'], {}).update({page_name: page_data['keys_extraction']})
    return document_wise_data


def get_multiple_documents_extraction(data: dict, mapping_doc_keys):
    """
  1. { doc: {page:{},page2:{} } pages wise documents
  2. { BOL: ["bol_no", "drawer_name"] } mapping data keys
  3. { BOL: {page0:["abc","df"], pag1:["12"."134"]} } set_value
  4. unique sets of pages
  5. each set has keys and return single value for key
  """
    ##documentwise documents
    document_wise_data = get_document_wise_data(data)
    document_wise_data = {"BOL": document_wise_data["BOL"]}
    document_wise_final_data: dict = {}

    for document, doc_pagewise_data in document_wise_data.items():
        document_sets: dict = get_document_sets_master(document, doc_pagewise_data, mapping_doc_keys[document])
        document_wise_final_data.update({document: document_sets})

    return document_wise_final_data


if __name__ == "__main__":
    map_doc_keys = {"BOL": ["bol_no"], "AWB": ["house_awb_bill_no"], "CI": ["invoice_no","beneficiary_drawer_exporter_seller_supplier_name"], "BOE": [], "PL": [], "COO": [],
                    "CS": []}
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    os.makedirs(f"LOGS/{timestamp}")
    #######Convert empty dicts to proper format
    for page,page_data in extraction_result_pdf_1['results'].items():
        if not page_data:
            extraction_result_pdf_1['results'][page] = {'docClass':"OTHERS","keys_extraction":{}}


    result = get_multiple_documents_extraction(extraction_result_pdf_1["results"], mapping_doc_keys=map_doc_keys)
    # print(result["CI"]["CI_page9"].keys())
