def _my_rule_impl(ctx):
    print("This message will appear during the analysis phase")

    # This message will NOT appear during the execution phase
    ctx.actions.run_shell(
        command = "echo 'This message will NOT appear during the execution phase'",
        outputs = [ctx.actions.declare_file(ctx.attr.name + ".txt")],
    )

my_rule = rule(
    implementation = _my_rule_impl,
)
