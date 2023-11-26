def _my_rule_impl(ctx):
    # Declare the output file
    output_file = ctx.actions.declare_file(ctx.attr.name + ".txt")

    # Command to create the output file
    command = "echo 'Hello, World!' > " + output_file.path

    # Create an action that runs the command
    ctx.actions.run_shell(
        outputs=[output_file],
        command=command,
    )

    # Return the output file as a DefaultInfo provider
    return [DefaultInfo(files=depset([output_file]))]

# Rule definition
my_rule = rule(
    implementation=_my_rule_impl,
    attrs={},
)
