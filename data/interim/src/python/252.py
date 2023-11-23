def _my_rule_impl(ctx):
    toolchain = ctx.toolchains["@bazel_tools//tools/cpp:toolchain_type"]
    # Now you can access information about the toolchain and use it in your rule.
