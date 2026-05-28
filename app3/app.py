from extract import extract_data
import pandas as pd
import matplotlib.pyplot as plt
from reporting import create_compliance_report, ReportData

def main():
    file_path = "./data/cap_app_inventory.csv"
    try:
        inventory_df = extract_data(file_path)
        print(inventory_df.head())  # Print the first few rows of the extracted data
    except Exception as e:
        print(f"An error occurred: {e}")
    
    file_path = "./data/cap_compliance_status.csv"
    try:
        compliance_df = extract_data(file_path)
        print(compliance_df.head())  # Print the first few rows of the extracted data
    except Exception as e:
        print(f"An error occurred: {e}")

    # Inner join the two DataFrames on a common column App_ID
    try:
        merged_df = inventory_df.merge(compliance_df, on="App_ID", how="inner")
        print(merged_df.head())  # Print the first few rows of the merged data
    except Exception as e:
        print(f"An error occurred during merging: {e}")
    
    ## bolierPlate Load all other files and perform the same operations as above


    ## End Here
    # Write the merged DataFrame to a new CSV file
    try:
        merged_df.to_csv("./output/merged_data.csv", index=False)
        print("Merged data has been written to merged_data.csv")
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")

    # Generate  insights from the merged data (e.g., count of compliant vs non-compliant applications)
    try:
        compliance_counts = merged_df['Status'].value_counts()
        print("Compliance Status Counts:")
        print(compliance_counts)
    except Exception as e:
        print(f"An error occurred while generating insights: {e}")


    # merged_df.info()
    # Convert 'Compliance_Score' to numeric, handling non-numeric values, remove % symbol if present
    try:
        merged_df['Compliance_Score'] = merged_df['Compliance_Score'].str.rstrip('%')
        merged_df['Compliance_Score'] = pd.to_numeric(merged_df['Compliance_Score'], errors='coerce')
    except Exception as e:
        print(f"An error occurred while converting Compliance_Score to numeric: {e}")

    merged_df.info()  # Check the data types after conversion
    # Barchart of Comliance Score by Department
    try:
        plt.figure(figsize=(10, 6))
        merged_df.groupby('Department')['Compliance_Score'].mean().plot(kind='bar')
        plt.title('Average Compliance Score by Department')
        plt.xlabel('Department')
        plt.ylabel('Average Compliance Score')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('./output/compliance_score_by_department.png')
    except Exception as e:
        print(f"An error occurred while generating the bar chart: {e}")

    # Generate a report summarizing the insights (e.g., save to a text file)
    try:
        report_data = ReportData(
            company_title="Company Title",
            status_counts=compliance_counts.to_dict(),
            department_scores=merged_df.groupby('Department')['Compliance_Score'].mean().to_dict(),
            generation_time=pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
            reporter_name="Reporter"
        )
        create_compliance_report(report_data)
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")

if __name__ == "__main__":
    main()