def _my_rule_impl(ctx):
    output = ctx.actions.declare_file(ctx.attr.name + ".txt")

    ctx.actions.run_shell(
        command = "echo 'This message will appear during the execution phase' && echo 'Hello, World!' > " + output.path,
        outputs = [output],
    )

my_rule = rule(
    implementation = _my_rule_impl,
)
