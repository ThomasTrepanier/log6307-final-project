import pandas as pd
from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

file = """
1: frack 0.733, shale 0.700, 
10: space 0.645, station 0.327, nasa 0.258, 
4: celebr 0.262, bahar 0.345 
"""

grammar = Grammar(
    r"""
    expr    = (garbage / line)+

    line    = id colon pair*
    pair    = term ws weight sep? ws?
    garbage = ws+

    id      = ~"\d+"
    colon   = ws? ":" ws?
    sep     = ws? "," ws?

    term    = ~"[a-zA-Z]+"
    weight  = ~"\d+(?:\.\d+)?"

    ws      = ~"\s+"
    """
)

tree = grammar.parse(file)

class PandasVisitor(NodeVisitor):
    def generic_visit(self, node, visited_children):
        return visited_children or node

    def visit_pair(self, node, visited_children):
        term, _, weight, *_ = visited_children
        return (term.text, weight.text)

    def visit_line(self, node, visited_children):
        id, _, pairs = visited_children
        return [(id.text, *pair) for pair in pairs]

    def visit_garbage(self, node, visited_children):
        return None

    def visit_expr(self, node, visited_children):
        return [item
                for lst in visited_children
                for sublst in lst if sublst
                for item in sublst]

pv = PandasVisitor()
out = pv.visit(tree)

df = pd.DataFrame(out, columns=["Id", "Term", "weight"])
print(df)
