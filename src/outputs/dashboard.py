"""
Local HTML Dashboard Generator.
Generates local dashboard HTML site into outputs/dashboard/.
Supports Jinja2 if available, or stdlib fallback formatting.
"""
import os
import shutil
from typing import List
from src.models.initiative import Initiative
from src.metrics.engine import MetricsEngine

class DashboardGenerator:
    def generate_dashboard(self, initiatives: List[Initiative], output_dir: str) -> str:
        engine = MetricsEngine()
        metrics = engine.calculate_portfolio_summary(initiatives)

        template_path = "templates/dashboard/index.html"
        with open(template_path, "r", encoding="utf-8") as f:
            template_str = f.read()

        try:
            from jinja2 import Template
            template = Template(template_str)
            html_content = template.render(**metrics)
        except ImportError:
            # Fallback stdlib replacement
            html_content = template_str
            html_content = html_content.replace("{{ total_initiatives }}", str(metrics["total_initiatives"]))
            html_content = html_content.replace("{{ overall_rag }}", str(metrics["overall_rag"]))
            html_content = html_content.replace("{{ \"%.2f\"|format(total_budget / 1000000.0) }}", f"{metrics['total_budget']/1e6:.2f}")
            html_content = html_content.replace("{{ health_score }}", str(metrics["health_score"]))

            rows_html = ""
            for cat, data in metrics["by_category"].items():
                rows_html += f"""<tr>
        <td><strong>{cat}</strong></td>
        <td>{data['count']}</td>
        <td>£{data['budget']/1e6:.2f}M</td>
        <td>£{data['actual_cost']/1e6:.2f}M</td>
        <td><span class="badge-RED">{data['red_count']}</span></td>
        <td><span class="badge-AMBER">{data['amber_count']}</span></td>
        <td><span class="badge-GREEN">{data['green_count']}</span></td>
      </tr>\n"""
            start_tag = "{% for cat, d in by_category.items() %}"
            end_tag = "{% endfor %}"
            if start_tag in html_content and end_tag in html_content:
                prefix = html_content.split(start_tag)[0]
                suffix = html_content.split(end_tag)[1]
                html_content = prefix + rows_html + suffix

        os.makedirs(output_dir, exist_ok=True)
        out_html = os.path.join(output_dir, "index.html")
        with open(out_html, "w", encoding="utf-8") as f:
            f.write(html_content)

        # Copy CSS
        css_src = "templates/dashboard/styles.css"
        if os.path.exists(css_src):
            shutil.copy(css_src, os.path.join(output_dir, "styles.css"))

        return out_html
