"""
Deterministic Offline AI Fallback Engine.
Generates predictable, high-confidence executive summaries without requiring external API keys.
"""
from datetime import datetime
from typing import Dict, Any
from src.ai.adapter import BaseAIAdapter

class OfflineFallbackAIAdapter(BaseAIAdapter):
    def generate_summary(self, prompt_template_name: str, context: Dict[str, Any]) -> Dict[str, Any]:
        now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

        if prompt_template_name == "portfolio_summary":
            tot = context.get("total_initiatives", 50)
            rag = context.get("overall_rag", "AMBER")
            red = context.get("red_count", 5)
            amb = context.get("amber_count", 8)
            grn = context.get("green_count", 37)
            budget = context.get("total_budget", 45000000.0)
            actual = context.get("total_actual_cost", 22000000.0)
            var_pct = context.get("spend_variance_pct", 8.5)
            health = context.get("health_score", 82.5)

            text = (
                f"Executive Portfolio Summary ({now_str}):\n"
                f"The enterprise portfolio comprises {tot} active and shaping initiatives with an overall {rag} health status "
                f"and composite health score of {health}/100. "
                f"Current RAG distribution indicates {grn} GREEN, {amb} AMBER, and {red} RED initiatives. "
                f"Total approved budget is £{budget:,.2f} against an actual spend to date of £{actual:,.2f} "
                f"(variance: {var_pct}%). Key focus remains on resolving cost overruns and milestone delays across RED status initiatives."
            )
        elif prompt_template_name == "initiative_summary":
            init_id = context.get("initiative_id", "INIT-001")
            title = context.get("title", "Initiative")
            cat = context.get("portfolio_category", "Technology")
            stage = context.get("lifecycle_stage", "Active")
            rag = context.get("rag_status", "GREEN")
            prog = context.get("progress_pct", 50.0)
            text = (
                f"Initiative Summary for {init_id} ({title}):\n"
                f"{init_id} is currently in {stage} stage under the {cat} portfolio with {rag} status. "
                f"Overall delivery progress stands at {prog}%. Governance oversight is active."
            )
        else:
            text = f"Generic executive narrative summary generated for template '{prompt_template_name}'."

        return {
            "text": text,
            "generation_mode": "OFFLINE_FALLBACK",
            "confidence": "HIGH",
            "timestamp": now_str,
            "prompt_template": prompt_template_name,
            "source_data_snapshot": context,
        }
