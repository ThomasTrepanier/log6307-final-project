override predicate isSource(DataFlow::Node source) {
    exists(DataFlow::CallCfgNode call, API::Node class |
        class = API::moduleImport("imblearn").getMember("over_sampling").getAMember().getReturn().getAUse() and
        call.getFunction().(DataFlow::AttrRead).getObject().getALocalSource() = class and
        source = call
    )
}
