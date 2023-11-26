# Declare the aspect.
MainClassAspect = aspect(
    implementation = _main_class_aspect_impl,
    attr_aspects = ["deps"],
)

# Implementation of the aspect.
def _main_class_aspect_impl(target, ctx):
    main_class = ""

    # If the target has a `main_class` attribute, get its value.
    if hasattr(target, "main_class"):
        main_class = target.main_class

    # Collect main classes from dependencies.
    deps_main_classes = []
    for dep in ctx.rule.attr.deps:
        if MainClassAspect in dep:
            deps_main_classes.append(dep[MainClassAspect].main_class)

    # Return a struct with the main classes of the target and its dependencies.
    return struct(
        main_class = main_class,
        deps_main_classes = deps_main_classes,
    )

# Rule that applies the aspect to its dependencies.
my_java_binary = rule(
    implementation = _my_java_binary_impl,
    attrs = {
        "deps": attr.label_list(aspects = [MainClassAspect]),
        # Other attributes...
    },
)

def _my_java_binary_impl(ctx):
    # Implementation of the rule...
    pass
