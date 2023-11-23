from python import Call
import semmle.python.ApiGraphs

class ModelSelectionSourceConfig extends TaintTracking::Configuration {
  ModelSelectionSourceConfig() { this = "ModelSelectionSourceConfig" }

  override predicate isSource(DataFlow::Node source) {
    exists(DataFlow::AttrRead read |
      read.getObject().getALocalSource().(DataFlow::CallCfgNode).getFunction().getAPredecessor*() = semmle.python.ApiGraphs::API::moduleImport("imblearn", "over_sampling").getMember("*") and
      source = read
    )
  }

  override predicate isSink(DataFlow::Node sink) {
    exists(semmle.python.ApiGraphs::API::Node callNode |
      callNode.getAUse() = sink.asExpr() and
      (
        callNode = semmle.python.ApiGraphs::API::moduleImport("sklearn", "model_selection").getMember("GroupKFold") or
        callNode = semmle.python.ApiGraphs::API::moduleImport("sklearn", "model_selection").getMember("GroupShuffleSplit") or
        callNode = semmle.python.ApiGraphs::API::moduleImport("sklearn", "model_selection").getMember("KFold") or
        callNode = semmle.python.ApiGraphs::API::moduleImport("sklearn", "model_selection").getMember("LeaveOneGroupOut") or
        //... include the remaining functions here in the same way ...
        callNode = semmle.python.ApiGraphs::API::moduleImport("sklearn", "model_selection").getMember("cross_val_score")
      )
    )
  }
}
