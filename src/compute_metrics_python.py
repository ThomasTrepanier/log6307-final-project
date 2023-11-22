from radon.complexity import cc_visit
from radon.metrics import h_visit, h_visit_ast, mi_visit, HalsteadReport
from radon.raw import analyze
import json


class MetricsComputer:

    def compute_maintainability_index(self, code: str) -> float:
        try:
            result = mi_visit(code, multi=False)
        except:
            return -1

        return result

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
        result = analyze(code)
        if result is None or result.loc == 0:
            return 0

        return result.comments / result.loc
