import semmle.python.ApiGraphs

override predicate isSink(DataFlow::Node sink) {
    exists(DataFlow::CallCfgNode call, string funcName |
        funcName in ["GroupKFold", "GroupShuffleSplit", "KFold", "LeaveOneGroupOut", 
                     "LeavePGroupsOut", "LeaveOneOut", "LeavePOut", "PredefinedSplit",
                     "RepeatedKFold"] and
        call.getFunction() = API::moduleImport("sklearn.model_selection").getMember(funcName).getAUse() and
        sink = call
    )
}
