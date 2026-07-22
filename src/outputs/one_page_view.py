"""
One-Page Executive View Generator.
Renders standalone HTML executive report from synthetic data.
Supports Jinja2 if available, or stdlib fallback formatting.
"""
import os
from typing import List, Dict, Any
from src.models.initiative import Initiative
from src.metrics.engine import MetricsEngine

class OnePageViewGenerator:
    def __init__(self, template_path: str = "templates/one_page_view.html"):
        self.template_path = template_path

    def generate_html(self, initiatives: List[Initiative], summary_text: str, output_path: str) -> str:
        engine = MetricsEngine()
        metrics = engine.calculate_portfolio_summary(initiatives)
        metrics["executive_summary"] = summary_text

        with open(self.template_path, "r", encoding="utf-8") as f:
            template_str = f.read()

        try:
            from jinja2 import Template
            template = Template(template_str)
            html_content = template.render(**metrics)
        except ImportError:
            # Fallback stdlib string replacement
            html_content = template_str
            html_content = html_content.replace("{{ total_initiatives }}", str(metrics["total_initiatives"]))
            html_content = html_content.replace("{{ overall_rag }}", str(metrics["overall_rag"]))
            html_content = html_content.replace("{{ \"%.2f\"|format(total_budget / 1000000.0) }}", f"{metrics['total_budget']/1e6:.2f}")
            html_content = html_content.replace("{{ health_score }}", str(metrics["health_score"]))
            html_content = html_content.replace("{{ executive_summary }}", summary_text)

            rows_html = ""
            for cat, data in metrics["by_category"].items():
                rows_html += f"""<tr>
        <td><strong>{cat}</strong></td>
        <td>{data['count']}</td>
        <td>£{data['budget']/1e6:.2f}M</td>
        <td>£{data['actual_cost']/1e6:.2f}M</td>
        <td><span class="rag-badge rag-RED">{data['red_count']}</span></td>
        <td><span class="rag-badge rag-AMBER">{data['amber_count']}</span></td>
        <td><span class="rag-badge rag-GREEN">{data['green_count']}</span></td>
      </tr>\n"""
            
            # Simple replace loop section
            start_tag = "{% for cat, data in by_category.items() %}"
            end_tag = "{% endfor %}"
            if start_tag in html_content and end_tag in html_content:
                prefix = html_content.split(start_tag)[0]
                suffix = html_content.split(end_tag)[1]
                html_content = prefix + rows_html + suffix

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        return output_path
