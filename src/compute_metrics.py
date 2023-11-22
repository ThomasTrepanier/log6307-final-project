from radon.complexity import cc_visit
from radon.metrics import h_visit, h_visit_ast, mi_visit, HalsteadReport
import json


class CyclomaticComplexity:

    def compute_complexity(self, code) -> int:
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
