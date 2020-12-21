<<<<<<< HEAD
from ._auto_annot import read_data, read_raw, read_adata, merge_data, naive_merge, \
        scanorama_merge, remove_genes, intersect_genes, remove_nonshared, fit, linear_svm, \
        rbf_svm, sgd_svm, random_forest, logistic_regression, logistic_regression_ovr, logistic_regression_elastic,\
        adata_predict, predict,  adata_pred_prob, predict_proba, report

__all__ = ['read_data', 'read_raw', 'read_adata', 'merge_data', 'naive_merge', 'scanorama_merge', 'remove_genes', 'intersect_genes', 'remove_nonshared',
           'fit', 'linear_svm', 'rbf_svm', 'sgd_svm', 'random_forest', 'logistic_regression','logistic_regression_ovr',
            'logistic_regression_elastic', 'adata_predict', 'predict',  'adata_pred_prob', 'predict_proba' ,'report']
=======
from ._auto_annot import read_data, read_raw, read_adata, merge_data, naive_merge, scanorama_merge, remove_genes, intersect_genes, remove_nonshared, fit, linear_svm, rbf_svm, sgd_svm, random_forest, logistic_regression, logistic_regression_ovr, logistic_regression_elastic, adata_predict, predict, report,  plot_confusion_matrix, adata_pred_prob, predict_proba

__all__ = ['read_data', 'read_raw', 'read_adata', 'merge_data', 'naive_merge', 'scanorama_merge', 'remove_genes', 'intersect_genes', 'remove_nonshared', 'fit', 'linear_svm', 'rbf_svm', 'sgd_svm', 'random_forest', 'logistic_regression','logistic_regression_ovr', 'logistic_regression_elastic', 'adata_predict', 'predict', 'report', 'plot_confusion_matrix', 'adata_pred_prob', 'predict_proba']
>>>>>>> 9d06da3 (Adding back report functions (from commit f714872e6e53e3f749d69097e097c029c0adf571))
