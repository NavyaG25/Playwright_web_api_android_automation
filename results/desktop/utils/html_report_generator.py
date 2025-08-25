"""
Beautiful HTML Report Generator for Desktop Web Automation
"""
import json
import os
from datetime import datetime


from utils.test_utils import STATIC_JSON_FILE, STATIC_HTML_FILE

class HTMLReportGenerator:
    def __init__(self, test_results_file: str = STATIC_JSON_FILE):
        self.test_results_file = test_results_file
        
    def generate_beautiful_report(self):
        """Generate a beautiful HTML report"""
        # Read test results
        if not os.path.exists(self.test_results_file):
            return "No test results found"
            
        with open(self.test_results_file, 'r') as f:
            data = json.load(f)
            
        html_content = self._create_html_template(data)
        
        # Save HTML report
        report_path = STATIC_HTML_FILE
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        return report_path
        
    def _create_html_template(self, data):
        """Create HTML template with test results"""
        passed_tests = data.get('passed', 0)
        failed_tests = data.get('failed', 0)
        total_tests = data.get('total_tests', 0)
        pass_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desktop Web Automation Test Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .summary {{
            padding: 30px;
            background: #f8f9fa;
        }}
        
        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .summary-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            border-left: 4px solid;
        }}
        
        .summary-card.total {{ border-left-color: #3498db; }}
        .summary-card.passed {{ border-left-color: #27ae60; }}
        .summary-card.failed {{ border-left-color: #e74c3c; }}
        .summary-card.rate {{ border-left-color: #f39c12; }}
        
        .summary-card h3 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            color: #2c3e50;
        }}
        
        .summary-card p {{
            color: #7f8c8d;
            font-weight: 600;
        }}
        
        .progress-bar {{
            width: 100%;
            height: 10px;
            background: #ecf0f1;
            border-radius: 5px;
            overflow: hidden;
            margin: 20px 0;
        }}
        
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #27ae60, #2ecc71);
            width: {pass_rate}%;
            transition: width 0.5s ease;
        }}
        
        .test-results {{
            padding: 30px;
        }}
        
        .test-results h2 {{
            color: #2c3e50;
            margin-bottom: 25px;
            font-size: 1.8em;
        }}
        
        .test-item {{
            background: white;
            margin-bottom: 20px;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            border-left: 4px solid;
        }}
        
        .test-item.passed {{ border-left-color: #27ae60; }}
        .test-item.failed {{ border-left-color: #e74c3c; }}
        
        .test-header {{
            padding: 20px;
            background: #f8f9fa;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .test-name {{
            font-weight: 600;
            color: #2c3e50;
        }}
        
        .test-status {{
            padding: 5px 15px;
            border-radius: 20px;
            color: white;
            font-weight: 600;
            font-size: 0.9em;
        }}
        
        .test-status.passed {{ background: #27ae60; }}
        .test-status.failed {{ background: #e74c3c; }}
        
        .test-details {{
            padding: 20px;
            display: none;
        }}
        
        .test-details.show {{
            display: block;
        }}
        
        .test-meta {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 15px;
        }}
        
        .meta-item {{
            background: #f8f9fa;
            padding: 10px;
            border-radius: 5px;
        }}
        
        .meta-label {{
            font-weight: 600;
            color: #7f8c8d;
            font-size: 0.9em;
        }}
        
        .meta-value {{
            color: #2c3e50;
            margin-top: 5px;
        }}
        
        .screenshots {{
            margin-top: 20px;
        }}
        
        .screenshot-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 10px;
            margin-top: 10px;
        }}
        
        .screenshot-item {{
            background: #f8f9fa;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            font-size: 0.9em;
            color: #7f8c8d;
        }}
        
        .footer {{
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 20px;
        }}
        
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .test-item {{
            animation: fadeIn 0.5s ease forwards;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 Desktop Web Automation Report</h1>
            <p>Automation Exercise - Test Execution Results</p>
            <p>Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        </div>
        
        <div class="summary">
            <div class="summary-grid">
                <div class="summary-card total">
                    <h3>{total_tests}</h3>
                    <p>Total Tests</p>
                </div>
                <div class="summary-card passed">
                    <h3>{passed_tests}</h3>
                    <p>Passed</p>
                </div>
                <div class="summary-card failed">
                    <h3>{failed_tests}</h3>
                    <p>Failed</p>
                </div>
                <div class="summary-card rate">
                    <h3>{pass_rate:.1f}%</h3>
                    <p>Pass Rate</p>
                </div>
            </div>
            
            <div class="progress-bar">
                <div class="progress-fill"></div>
            </div>
        </div>
        
        <div class="test-results">
            <h2>📋 Test Execution Details</h2>
"""
        
        # Add test results
        for i, test in enumerate(data.get('test_results', [])):
            status_class = test['status'].lower()
            html += f"""
            <div class="test-item {status_class}" style="animation-delay: {i * 0.1}s;">
                <div class="test-header" onclick="toggleDetails({i})">
                    <div class="test-name">{test['test_name']}</div>
                    <div class="test-status {status_class}">{test['status']}</div>
                </div>
                <div class="test-details" id="details-{i}">
                    <div class="test-meta">
                        <div class="meta-item">
                            <div class="meta-label">Duration</div>
                            <div class="meta-value">{test['duration']:.2f} seconds</div>
                        </div>
                        <div class="meta-item">
                            <div class="meta-label">Timestamp</div>
                            <div class="meta-value">{test['timestamp']}</div>
                        </div>
                        <div class="meta-item">
                            <div class="meta-label">Screenshots</div>
                            <div class="meta-value">{len(test.get('screenshots', []))} captured</div>
                        </div>
                    </div>
                    
                    {f'<div class="meta-item"><div class="meta-label">Details</div><div class="meta-value">{test["details"]}</div></div>' if test.get('details') else ''}
                    
                    {self._generate_screenshots_section(test.get('screenshots', []))}
                </div>
            </div>
"""
        
        html += """
        </div>
        
        <div class="footer">
            <p>🤖 Generated by Desktop Web Automation Framework</p>
            <p>Powered by Playwright & Python</p>
        </div>
    </div>
    
    <script>
        function toggleDetails(index) {
            const details = document.getElementById(`details-${index}`);
            details.classList.toggle('show');
        }
    </script>
</body>
</html>
"""
        return html
        
    def _generate_screenshots_section(self, screenshots):
        """Generate screenshots section"""
        if not screenshots:
            return ""
            
        html = """
        <div class="screenshots">
            <div class="meta-label">Screenshots</div>
            <div class="screenshot-grid">
"""
        for screenshot in screenshots:
            filename = os.path.basename(screenshot) if screenshot else "No screenshot"
            html += f"""
                <div class="screenshot-item">
                    📷 {filename}
                </div>
"""
        html += """
            </div>
        </div>
"""
        return html


if __name__ == "__main__":
    generator = HTMLReportGenerator()
    report_path = generator.generate_beautiful_report()
    print(f"Beautiful HTML report generated: {report_path}")
