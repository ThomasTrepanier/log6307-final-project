def pr_auc_score(y, y_pred, **kwargs):
  classes = list(range(y_pred.shape[1]))
  if len(classes) == 2:
      precision, recall, _ = precision_recall_curve(y, y_pred[:,1],
                                                    **kwargs)
  else:
    Y = label_binarize(y, classes=classes)
    precision, recall, _ = precision_recall_curve(Y.ravel(), y_pred.ravel(),
                                                  **kwargs)
  return auc(recall, precision)
