"""
Stub for connecting a real AI provider.

Set AI_MODE=real and implement run_real_review() to call an LLM provider
(Anthropic, OpenAI, etc). Not used by default — mock_ai_service.py is the
default review engine.
"""


def run_real_review(files, policy_name):
    raise NotImplementedError(
        "Real AI mode is not configured. Implement run_real_review() "
        "and set AI_MODE=real to enable it."
    )