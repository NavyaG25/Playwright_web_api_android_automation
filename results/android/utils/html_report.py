from pathlib import Path
import json
from datetime import datetime

def generate_html_report(json_path: str, html_path: str = None):
    with open(json_path, 'r', encoding='utf-8') as f:
        result = json.load(f)

    if not html_path:
        html_path = str(Path(json_path).with_suffix('.html'))

    steps_html = ""
    for idx, step in enumerate(result.get('steps', []), 1):
        status_color = '#27ae60' if step['status'] == 'passed' else '#e74c3c'
        steps_html += f"<tr><td>{idx}</td><td>{step['step'].replace('_',' ').title()}</td><td style='color:{status_color};font-weight:bold'>{step['status'].title()}</td><td>{step['details']}</td></tr>"

    # Only show the main screenshot (homepage or login success)
    screenshot_path = result.get('screenshot')
    screenshot_html = ""
    if screenshot_path:
        screenshot_html = f"<div class='screenshot-block'><h3>Screenshot</h3><img src='../{screenshot_path}' alt='Screenshot' class='main-screenshot'></div>"

    html = f"""
    <html>
    <head>
        <title>Test Report - {result.get('test','')}</title>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #f8f9fa; margin: 0; padding: 0; }}
            .container {{ max-width: 900px; margin: 40px auto; background: #fff; border-radius: 12px; box-shadow: 0 2px 12px #0001; padding: 32px; }}
            h1 {{ color: #2c3e50; }}
            h2 {{ margin-top: 0; }}
            table {{ border-collapse: collapse; width: 100%; margin-top: 24px; }}
            th, td {{ border: 1px solid #e1e4e8; padding: 10px 12px; text-align: left; }}
            th {{ background: #f2f2f2; color: #34495e; }}
            tr:nth-child(even) {{ background: #f9f9f9; }}
            .main-screenshot {{ max-width: 500px; border-radius: 8px; border: 2px solid #e1e4e8; margin-top: 16px; }}
            .screenshot-block {{ margin: 32px 0; text-align: center; }}
            .status-badge {{ display: inline-block; padding: 6px 18px; border-radius: 20px; font-size: 1.1em; font-weight: bold; color: #fff; background: {'#27ae60' if result.get('status')=='passed' else '#e74c3c'}; }}
            .footer {{ margin-top: 40px; color: #888; font-size: 0.95em; text-align: right; }}
        </style>
    </head>
    <body>
        <div class='container'>
            <h1>Test Report: {result.get('test','')}</h1>
            <h2>Status: <span class='status-badge'>{result.get('status','').title()}</span></h2>
            <h3>Test Steps</h3>
            <table>
                <tr><th>#</th><th>Step</th><th>Status</th><th>Details</th></tr>
                {steps_html}
            </table>
            {screenshot_html}
            <div class='footer'>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
        </div>
    </body>
    </html>
    """
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    return html_path

# Usage example:
# generate_html_report('reports/login_test_result_20250825_153000.json')
