.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_auto_examples_plotting_plot_celltype_quantification.py>`     to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _sphx_glr_auto_examples_plotting_plot_celltype_quantification.py:


visualize cell fractions
========================

This example demonstrates how to generate celltype quantification plots. These types of plots 
can be used to visually represent the number of cells that belong to a certain subset or condition.



.. code-block:: default


    import besca as bc 

    #import dataset to workwith
    adata = bc.datasets.Peng2019_processed()








quantify specific celllabels as a stacked barplot


.. code-block:: default


    bc.pl.celllabel_quant_stackedbar(adata, count_variable = 'Cell_type', subset_variable = 'Patient')





.. image:: /auto_examples/plotting/images/sphx_glr_plot_celltype_quantification_001.png
    :alt: plot celltype quantification
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    /pstore/home/julienla/miniconda3/envs/besca_2.2/lib/python3.6/site-packages/anndata/_core/anndata.py:1094: FutureWarning:

    is_categorical is deprecated and will be removed in a future version.  Use is_categorical_dtype instead

    /pstore/home/julienla/Code/Besca/besca_dev/besca/pl/_celltype_quantification.py:143: UserWarning:

    Tight layout not applied. The bottom and top margins cannot be made large enough to accommodate all axes decorations. 


    <AxesSubplot:ylabel='percentage'>



quantify number of cells belong to each condition in a specific subset

here each dot represents one Patient, the boxplots are grouped according to tissue type (Normal or Tumoral)


.. code-block:: default

    bc.pl.celllabel_quant_boxplot(adata, count_variable = 'Cell_type', subset_variable = 'Patient', condition_identifier = 'Type',  plot_percentage = True)




.. image:: /auto_examples/plotting/images/sphx_glr_plot_celltype_quantification_002.png
    :alt: plot celltype quantification
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    <Figure size 800x400 with 1 Axes>



here you can also choose to plot total counts instead of percentages


.. code-block:: default

    bc.pl.celllabel_quant_boxplot(adata, count_variable = 'Cell_type', subset_variable = 'Patient', condition_identifier = 'Type',  plot_percentage = False)


.. image:: /auto_examples/plotting/images/sphx_glr_plot_celltype_quantification_003.png
    :alt: plot celltype quantification
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    /pstore/home/julienla/miniconda3/envs/besca_2.2/lib/python3.6/site-packages/anndata/_core/anndata.py:1094: FutureWarning:

    is_categorical is deprecated and will be removed in a future version.  Use is_categorical_dtype instead


    <Figure size 800x400 with 1 Axes>




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  19.096 seconds)


.. _sphx_glr_download_auto_examples_plotting_plot_celltype_quantification.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: plot_celltype_quantification.py <plot_celltype_quantification.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: plot_celltype_quantification.ipynb <plot_celltype_quantification.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_