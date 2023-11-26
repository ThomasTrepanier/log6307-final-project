def _message_consumer_impl(ctx):
    messages = []
    for dep in ctx.attr.deps:
        for file in dep[DefaultInfo].files.to_list():
            # read the file contents into 'messages'
            pass
    # do something with 'messages'

message_consumer = rule(
    implementation = _message_consumer_impl,
    attrs = {"deps": attr.label_list()},
)
