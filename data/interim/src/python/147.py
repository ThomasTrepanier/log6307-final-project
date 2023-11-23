import python
import semmle.python.dataflow.new.TaintTracking
import semmle.python.ApiGraphs

class StartFromOverSampling extends TaintTracking::Configuration {
    StartFromOverSampling() { this = "StartFromOverSampling" }

  override predicate isSource(DataFlow::Node source) {
    exists(DataFlow::CallCfgNode call |
      (call.getFunction().(DataFlow::AttrRead).getAttributeName().matches("%fit_sample%") or
       call = API::moduleImport("imblearn").getMember("over_sampling").getMember("SMOTE").getACall()) and
      source = call
    )
  }

  override predicate isSink(DataFlow::Node sink) {
    any()
  }

  override predicate isAdditionalTaintStep(DataFlow::Node node1, DataFlow::Node node2) {
    exists(DataFlow::CallCfgNode call | 
        node2 = call and 
        node1 = call.getArg(_)
    )
  }
}

from DataFlow::Node src, DataFlow::Node dst, StartFromOverSampling config
where config.hasFlow(src, dst)
select src.getLocation(), dst.getLocation(), src, dst, "This call"
