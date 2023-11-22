class MetricsComputer:

    def compute_comment_to_code_ratio(self, code: str) -> float:
        lines = code.split('\n')[:-1]
        if len(lines) == 0:
            return 0

        comment_lines = list(
            filter(lambda line: line.strip().startswith('//'), lines))

        return len(comment_lines) / len(lines)
