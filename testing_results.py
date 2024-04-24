# if __name__ == "__main__":
#     path = "/home/ntlpt59/Downloads/MainSheetTesting.xlsx"
#     import pandas as pd
#     df = pd.read_excel(path, sheet_name='TestResult')
#     df = df[df['RuleId'].apply(lambda x: x[0:3] == 'ucp')]
#
#     print(df.columns)
#     print("#### UCP Results #####")
#     print(df['Result'].value_counts())
#
#
#     api_remarks_counts = df['API REMARKS'].value_counts()
#     print(api_remarks_counts)
#
#     # Print Rule IDs next to the count of API REMARKS
#     print("\n#### API Remarks with Rule IDs #####")
#     for api_remark, count in api_remarks_counts.items():
#         rule_ids_for_remark = df[df['API REMARKS'] == api_remark]['RuleId'].tolist()
#         print(f"{api_remark}: {count} - {rule_ids_for_remark}")
#
#
#     # Extract Rule IDs for entries with "Accepted" results
#     accepted_rule_ids = df[df['Result'] == 'Accepted']['RuleId'].tolist()
#     not_accepted_rule_ids = df[df['Result'] == 'Not Accepted']['RuleId'].tolist()
#
#     print("\n#### Accepted Rule IDs #####")
#     print(accepted_rule_ids)
#
#     print("\n#### Not Accepted Rule IDs #####")
#     print(not_accepted_rule_ids)
#
#     # Save the results to a CSV file
#     output_path = "/home/ntlpt59/Downloads/ResultsOutput.csv"
#
#     # Save the UCP Results
#     ucp_results_path = output_path.replace(".csv", "_UCP_Results.csv")
#     df['Result'].value_counts().to_frame().to_csv(ucp_results_path, header=['Count'])
#
#     # Save the API Remarks Counts
#     api_remarks_counts_path = output_path.replace(".csv", "_API_Remarks_Counts.csv")
#     api_remarks_counts.to_frame().to_csv(api_remarks_counts_path, header=['Count'])
#
#     # Save the API Remarks with Rule IDs
#     api_remarks_with_rule_ids_path = output_path.replace(".csv", "_API_Remarks_with_Rule_IDs.csv")
#     api_remarks_with_rule_ids_df = pd.DataFrame(columns=['API Remark', 'Count', 'Rule IDs'])
#     for api_remark, count in api_remarks_counts.items():
#         rule_ids_for_remark = df[df['API REMARKS'] == api_remark]['RuleId'].tolist()
#         api_remarks_with_rule_ids_df = api_remarks_with_rule_ids_df.append(
#             {'API Remark': api_remark, 'Count': count, 'Rule IDs': rule_ids_for_remark}, ignore_index=True)
#     api_remarks_with_rule_ids_df.to_csv(api_remarks_with_rule_ids_path, index=False)
#
#     # Save the Accepted and Not Accepted Rule IDs
#     accepted_rule_ids_path = output_path.replace(".csv", "_Accepted_Rule_IDs.csv")
#     not_accepted_rule_ids_path = output_path.replace(".csv", "_Not_Accepted_Rule_IDs.csv")
#     pd.DataFrame(accepted_rule_ids, columns=['Accepted Rule IDs']).to_csv(accepted_rule_ids_path, index=False)
#     pd.DataFrame(not_accepted_rule_ids, columns=['Not Accepted Rule IDs']).to_csv(not_accepted_rule_ids_path, index=False)
#
#
#
#
# #
# # if __name__ == "__main__":
# #     path = "/home/ntlpt59/Downloads/MainSheetTesting.xlsx"
# #     import pandas as pd
# #     df = pd.read_excel(path,sheet_name='TestResult')
# #     df = df[df['RuleId'].apply(lambda x : x[0:3]=='ucp')]
#     print(df.columns)
#     print("#### UCP Results #####")
#     print(df['Result'].value_counts())
#
#
#     api_remarks_counts = df['API REMARKS'].value_counts()
#     print(api_remarks_counts)
#
#     # Print Rule IDs next to the count of API REMARKS
#     print("\n#### API Remarks with Rule IDs #####")
#     for api_remark, count in api_remarks_counts.items():
#         rule_ids_for_remark = df[df['API REMARKS'] == api_remark]['RuleId'].tolist()
#         print(f"{api_remark}: {count} - {rule_ids_for_remark}")
#
#
#     # Extract Rule IDs for entries with "Accepted" results
#     accepted_rule_ids = df[df['Result'] == 'Accepted']['RuleId'].tolist()
#     not_accepted_rule_ids = df[df['Result'] == 'Not Accepted']['RuleId'].tolist()
#
#     print("\n#### Accepted Rule IDs #####")
#     print(accepted_rule_ids)
#
#     print("\n#### Not Accepted Rule IDs #####")
#     print(not_accepted_rule_ids)
#
#
# import re
#
# ###########################
# ocr_data = "Franchise a 2 5 adf, excess 10a l;akdj;alsjdfasjdf"
# franchise_match = re.findall(r'franchise.', ocr_data, re.IGNORECASE)
# print(franchise_match)
# exit('+')
# franchise_match = re.search(r'franchise', ocr_data, re.IGNORECASE)
# excess_match = re.search(r'excess\s*?(\d+)', ocr_data, re.IGNORECASE)
# franchise_value = franchise_match.group(1) if franchise_match else None
# excess_value = excess_match.group(1) if excess_match else None
# # franchise_match = re.findall(r"Franchise(.*.)", text)
# # excess_match = re.findall(r"excess(\d+)", text)
# print(franchise_value)
# print(excess_value)
#
# exit('+++')
# if __name__ == "__main__":
#     path = "/home/ntlpt59/Downloads/MainSheetTesting.xlsx"
#     import pandas as pd
#
#     # Read data and filter based on 'RuleId'
#     df = pd.read_excel(path, sheet_name='TestResult')
#     df = df[df['RuleId'].apply(lambda x: x[0:3] == 'ucp')]
#
#     # Print UCP Results
#     print(df.columns)
#     print("#### UCP Results #####")
#     print(df['Result'].value_counts())
#
#     # Count API Remarks
#     api_remarks_counts = df['API REMARKS'].value_counts()
#     print(api_remarks_counts)
#
#     # Print Rule IDs next to the count of API REMARKS
#     print("\n#### API Remarks with Rule IDs #####")
#     api_remarks_with_rule_ids_data = []
#
#     for api_remark, count in api_remarks_counts.items():
#         rule_ids_for_remark = df[df['API REMARKS'] == api_remark]['RuleId'].tolist()
#         api_remarks_with_rule_ids_data.append(
#             {'API Remark': api_remark, 'Count': count, 'Rule IDs': rule_ids_for_remark})
#
#     for item in api_remarks_with_rule_ids_data:
#         print(f"{item['API Remark']}: {item['Count']} - {item['Rule IDs']}")
#
#     # Extract Rule IDs for entries with "Accepted" and "Not Accepted" results
#     accepted_rule_ids = df[df['Result'] == 'Accepted']['RuleId'].tolist()
#     not_accepted_rule_ids = df[df['Result'] == 'Not Accepted']['RuleId'].tolist()
#
#     # Print Accepted and Not Accepted Rule IDs
#     print("\n#### Accepted Rule IDs #####")
#     print(accepted_rule_ids)
#
#     print("\n#### Not Accepted Rule IDs #####")
#     print(not_accepted_rule_ids)
#
#     # Save the results to a CSV file
#     output_path = "/home/ntlpt59/Downloads/ResultsOutput.csv"
#
#     # Save the UCP Results
#     ucp_results_path = output_path.replace(".csv", "_UCP_Results.csv")
#     df['Result'].value_counts().to_frame().to_csv(ucp_results_path, header=['Count'])
#
#     # Save the API Remarks Counts
#     api_remarks_counts_path = output_path.replace(".csv", "_API_Remarks_Counts.csv")
#     api_remarks_counts.to_frame().to_csv(api_remarks_counts_path, header=['Count'])
#
#     # Save the API Remarks with Rule IDs
#     api_remarks_with_rule_ids_path = output_path.replace(".csv", "_API_Remarks_with_Rule_IDs.csv")
#     pd.DataFrame(api_remarks_with_rule_ids_data).to_csv(api_remarks_with_rule_ids_path, index=False)
#
#     # Save the Accepted and Not Accepted Rule IDs
#     accepted_rule_ids_path = output_path.replace(".csv", "_Accepted_Rule_IDs.csv")
#     not_accepted_rule_ids_path = output_path.replace(".csv", "_Not_Accepted_Rule_IDs.csv")
#
#     # Create new columns and populate them with lists of values
#     df['Unexpected'] = ['Passed', 'Passed enhancement', 'Fail', 'Disregard', 'Failed enhancement']
#     df.to_csv(accepted_rule_ids_path, index=False)
#
#     pd.DataFrame(not_accepted_rule_ids, columns=['Not Accepted Rule IDs']).to_csv(not_accepted_rule_ids_path,
#
#                                                               index=False)
#
#
# exit('++++++=')
if __name__ == "__main__":
    path = "/home/ntlpt59/Desktop/results/MainSheetTesting.xlsx"
    import pandas as pd

    # Read data and filter based on 'RuleId'
    df = pd.read_excel(path, sheet_name='TestResult')
    df = df[df['RuleId'].apply(lambda x: x[0:3] == 'ucp')]

    # Print UCP Results
    print(df.columns)
    print("#### UCP Results #####")
    print(df['Result'].value_counts())

    # Count API Remarks
    api_remarks_counts = df['API REMARKS'].value_counts()
    print(api_remarks_counts)

    # Print Rule IDs next to the count of API REMARKS
    print("\n#### API Remarks with Rule IDs #####")
    api_remarks_with_rule_ids_data = []

    for api_remark, count in api_remarks_counts.items():
        rule_ids_for_remark = df[df['API REMARKS'] == api_remark]['RuleId'].tolist()
        api_remarks_with_rule_ids_data.append(
            {'API Remark': api_remark, 'Count': count, 'Rule IDs': rule_ids_for_remark})

    for item in api_remarks_with_rule_ids_data:
        print(f"{item['API Remark']}: {item['Count']} - {item['Rule IDs']}")

    # Extract Rule IDs for entries with "Accepted" and "Not Accepted" results
    accepted_rule_ids = df[df['Result'] == 'Accepted']['RuleId'].tolist()
    not_accepted_rule_ids = df[df['Result'] == 'Not Accepted']['RuleId'].tolist()

    # Print Accepted and Not Accepted Rule IDs
    print("\n#### Accepted Rule IDs #####")
    print(accepted_rule_ids)

    print("\n#### Not Accepted Rule IDs #####")
    print(not_accepted_rule_ids)

    # Save the results to a CSV file
    output_path = "/home/ntlpt59/Desktop/results/ResultsOutput.csv"

    # Save the UCP Results
    ucp_results_path = output_path.replace(".csv", "_UCP_Results.csv")
    df['Result'].value_counts().to_frame().to_csv(ucp_results_path, header=['Count'])

    # Save the API Remarks Counts
    api_remarks_counts_path = output_path.replace(".csv", "_API_Remarks_Counts.csv")
    api_remarks_counts.to_frame().to_csv(api_remarks_counts_path, header=['Count'])

    # Save the API Remarks with Rule IDs
    api_remarks_with_rule_ids_path = output_path.replace(".csv", "_API_Remarks_with_Rule_IDs.csv")
    pd.DataFrame(api_remarks_with_rule_ids_data).to_csv(api_remarks_with_rule_ids_path, index=False)

    # Save the Accepted and Not Accepted Rule IDs
    accepted_rule_ids_path = output_path.replace(".csv", "_Accepted_Rule_IDs.csv")
    not_accepted_rule_ids_path = output_path.replace(".csv", "_Not_Accepted_Rule_IDs.csv")
    pd.DataFrame(accepted_rule_ids, columns=['Accepted Rule IDs']).to_csv(accepted_rule_ids_path, index=False)
    pd.DataFrame(not_accepted_rule_ids, columns=['Not Accepted Rule IDs']).to_csv(not_accepted_rule_ids_path,
                                                                                  index=False)
