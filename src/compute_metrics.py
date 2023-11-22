from radon.complexity import cc_visit
from radon.metrics import h_visit, h_visit_ast, mi_visit, HalsteadReport
import json


class MetricsComputer:

    def compute_cyclomatic_complexity(self, code) -> int:
        # Use cc_visit to get a list of complexity results
        try:
            results = cc_visit(code)
        except:
            return -1

        # Initialize total cognitive complexity
        total_cognitive_complexity = 0

        # Iterate over the results and accumulate cognitive complexity
        for result in results:
            total_cognitive_complexity += result.complexity

        return total_cognitive_complexity

    def compute_comment_to_code_ratio(self, code: str) -> float:
        lines = code.split('\n')[:-1]
        if len(lines) == 0:
            return 0

        comment_lines = list(
            filter(lambda line: line.strip().startswith('#'), lines))

        return len(comment_lines) / len(lines)
