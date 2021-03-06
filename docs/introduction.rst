About this library
--------------------
The **pyfluo** library enables easy and efficient manipulation of imaging data using a set of custom-built data structures and functions.

This project is `hosted on github <https://github.com/bensondaled/pyfluo/>`_.

Note that **pyfluo** is a work in progress; neither the code nor the documentation is complete. That said, it is already functional for a wide variety of tasks.

Because the library is constantly under progress, the documentation for functions and classes on this site may be out of date. The most reliable way to determine the available functions and their signatures is to interactively check them after importing the package (for example in ipython).

Requirements
--------------
The library has the following dependencies:

* numpy
* scipy
* scikit-learn
* matplotlib
* opencv
* pims (for tiffs)

Note that currently, only numpy, scipy, and matplotlib are enforced on installation of the package.

Installation
-------------
#. Download the project `here <https://github.com/bensondaled/pyfluo/>`_.
#. Extract and navigate to the root directory.
#. Run ``python setup.py install``

A quick example
-----------------
Here is a quick-start example to get you moving with pyfluo.

.. code-block:: python
    :linenos:

    from pyfluo import ROI, Tiff, Movie, Trace, correct_motion, compute_dff, pca_ica, comp_to_mask, save

    # create a movie from a tiff file
    mov = Movie('/Users/ben/PhD/data/mov.tif', Ts=0.03)

    # motion correct the movie
    mov = correct_motion(mov, n_iters=1) #or use the convenience method mov.correct_motion

    # convert the movie to delta f over f
    mov = compute_dff(mov, window_size=1.0, step_size=0.100)

    # play the movie
    mov.play(fps=30, scale=5, contrast=3)

    # manually select some ROIs
    roi = mov.select_roi(3)

    # or alternatively: use PCA/ICA to determine ROIs
    #comp = pca_ica(mov, components=12)
    #roi = ROI(mask=comp_to_mask(comp))

    # display the movie with its ROIs
    mov.project(show=True, roi=roi)

    # extract traces
    tr = mov.extract_by_roi(roi)

    # display traces
    tr.plot()

    # save the traces
    save('my_data', traces=tr)

Shown below are examples of the projected movie (left), and extracted traces (right).

.. image:: imgs/movie.png
    :width: 40% 
.. image:: imgs/traces.png
    :width: 40%

Troubleshooting
------------------
A list of known fixes for common problems will be kept here.

* For windows installations, VisualStudio often causes problems in installing tiff-related modules. An example fix to such a problem is explained `here <http://stackoverflow.com/questions/2817869/error-unable-to-find-vcvarsall-bat>`_.
