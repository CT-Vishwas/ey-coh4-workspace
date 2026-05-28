import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from dataclasses import dataclass

@dataclass
class ReportData:
    company_title: str
    status_counts: dict
    department_scores: dict
    generation_time: str
    reporter_name: str
    chart_path: str = "compliance_score_by_department.png"  # Default path for the chart image

def create_compliance_report(report_data: ReportData) -> None:
    # 2. Set up the Jinja2 template environment
    # Assumes 'compliance_template.html' is in the same directory
    current_dir = os.path.dirname(os.path.abspath(__file__)) if __file__ else '.'
    env = Environment(loader=FileSystemLoader(current_dir))
    template = env.get_template('./templates/compliant_report.html')

    # 3. Render template with our data context
    print("Rendering the compliance report template...")
    print(f"Report Data: {type(report_data)}, {report_data}")
    html_out = template.render(report_data.__dict__)

    # render HTML to a HTML File
    with open("./output/compliance_report.html", "w") as f:
        f.write(html_out)


if __name__ == "__main__":
    create_compliance_report()