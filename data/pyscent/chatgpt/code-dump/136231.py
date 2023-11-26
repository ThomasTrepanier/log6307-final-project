# my_rule.bzl
def _my_rule_impl(ctx):
    output = ctx.outputs.out
    ctx.actions.write(output, "Hello, World!", is_executable=False)
my_rule = rule(
    implementation = _my_rule_impl,
    outputs = {"out": "%{name}.txt"},
)
