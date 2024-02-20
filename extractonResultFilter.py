from copy import deepcopy

data = {
    "doc_wise": {
        "IC": [
            "1609flc230614_12.png",
            "1609flc230614_29.png",
            "1609flc230614_20.png"
        ],
        "BOL": [
            "1609flc230614_24.png",
            "1609flc230614_8.png",
            "1609flc230614_32.png",
            "1609flc230614_16.png"
        ],
        "COO": [
            "1609flc230614_27.png",
            "1609flc230614_11.png",
            "1609flc230614_19.png",
            "1609flc230614_35.png"
        ],
        "ELB": [
            "1609flc230614_5.png"
        ],
        "PL": [
            "1609flc230614_7.png",
            "1609flc230614_14.png",
            "1609flc230614_23.png",
            "1609flc230614_30.png"
        ]
    },
    "set_wise": {
        "IC": {
            "IC_1": {
                "SET_1_CPY": {
                    "1609flc230614_29.png": {
                        "page_no": 1,
                        "original": 0,
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
                        }
                    }
                }
            },
            "IC_2": {
                "SET_1_CPY": {
                    "1609flc230614_20.png": {
                        "page_no": 1,
                        "original": 0,
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
                        }
                    }
                }
            },
            "OTHERS_SET_1": {
                "1609FLC230614_pdf_1_jan_31_12.png": {
                    "page_no": 1,
                    "original": 0,
                    "keys_extraction": {}
                }
            }
        },
        "BOL": {
            "BOL_1": {
                "SET_1_CPY": {
                    "1609flc230614_24.png": {
                        "page_no": 1,
                        "original": 0,
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
                        }
                    }
                }
            },
            "BOL_2": {
                "SET_1_CPY": {
                    "1609flc230614_8.png": {
                        "page_no": 1,
                        "original": 0,
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
                        }
                    }
                }
            },
            "BOL_3": {
                "SET_1_ORG": {
                    "1609flc230614_32.png": {
                        "page_no": 1,
                        "original": 1,
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
                        }
                    }
                }
            },
            "BOL_4": {
                "SET_1_CPY": {
                    "1609flc230614_16.png": {
                        "page_no": 1,
                        "original": 0,
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
                        }
                    }
                }
            }
        },
        "COO": {
            "COO_1": {
                "SET_1_ORG": {
                    "1609flc230614_27.png": {
                        "page_no": 1,
                        "original": 1,
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
                        }
                    },
                    "1609flc230614_11.png": {
                        "page_no": 2,
                        "original": 1,
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
                        }
                    }
                },
                "SET_2_ORG": {
                    "1609flc230614_19.png": {
                        "page_no": 1,
                        "original": 1,
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
                        }
                    },
                    "1609flc230614_35.png": {
                        "page_no": 2,
                        "original": 1,
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
                        }
                    }
                }
            }
        },
        "ELB": {
            "OTHERS_SET_1": {
                "page_no": 1,
                "original": 0,
                "keys_extraction": {}
            }
        },
        "PL": {
            "OTHERS_SET_1": {
                "page_no": 1,
                "original": 1,
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
                }
            },
            "OTHERS_SET_2": {
                "page_no": 2,
                "original": 1,
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
                }
            },
            "OTHERS_SET_3": {
                "page_no": 3,
                "original": 1,
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
                }
            },
            "OTHERS_SET_4": {
                "page_no": 4,
                "original": 1,
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
                }
            }
        }
    }
}


def merge_data(set_info: dict, key_type="image") -> dict:
    set_info_copy: dict = deepcopy(set_info)
    keys_data: dict = {}
    for img_name, set_info in set_info_copy.items():
        if key_type == "image":
            keys_extraction = set_info['keys_extraction']
            _ = [keys_data.setdefault(k, []).append(v.get("value", "")) for k, v in keys_extraction.items()]
        elif key_type == "set":
            _ = [keys_data.setdefault(k, []).append(v) for k, v in set_info.items()]

    for __key, __data in keys_data.items():
        max_len, max_data = 0, ""
        for value in __data:
            if len(value) > max_len:
                max_data, max_data = len(value), value
        keys_data[__key] = max_data

    return keys_data


def extraction_results_update(data: dict) -> dict:
  data = data.get("set_wise", data)
  final_data: dict = {}
  merged_images_data: dict = {}

  for doc, doc_set in data.items():
    for doc_int_set, set_info in doc_set.items():
      if doc_int_set.lower().strip()[:6] == "others":
        first_key:str = list(set_info.keys())[0]
        merged_images_data.setdefault(doc, {}).update({doc_int_set: set_info.get(first_key,{}).get("keys_extraction",set_info)})
        continue
      for org_cpy_set, org_cpy_info in set_info.items():
        merge_sets_data: dict = merge_data(org_cpy_info, key_type="image")
        merged_images_data.setdefault(doc, {}).setdefault(doc_int_set, {}).update(
            {org_cpy_set: merge_sets_data})

  for doc, doc_set in merged_images_data.items():
    for doc_int_set, set_info in doc_set.items():
      if doc_int_set.lower().strip()[:6] == "others":
          first_key:str = next(iter(set_info))
          final_data.setdefault(doc, {}).update({doc_int_set: set_info.get(first_key,{}).get("keys_extraction",set_info)})
      else:
          merge_set_data: dict = merge_data(set_info, key_type="set")
          final_data.setdefault(doc, {}).update({doc_int_set: merge_set_data})

  return final_data


if __name__ == "__main__":
    res = extraction_results_update(data=data)
    print(res)
