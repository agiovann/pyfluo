Core Data Structures
=======================

The advantage of pyfluo is that its core data structures are subclasses of numpy's ndarray. This means that by and large, native numpy operations work on pyfluo Movies, Traces, ROIs, etc. However, these objects also store other data, including frame rates, time vectors, associated points, information, etc. where applicable. The biggest challenge in development has been to properly handle the advanced slicing, and as such, some features may break when slicing pyfluo objects. If this occurs, you can always retrieve raw forms of your data using:

.. code-block:: python
    
    raw_data = my_obj.view(np.ndarray)
    
where my_obj can be a Movie, Trace, ROI, etc. This page is a summary (albeit incomplete) of the important data structures.

.. autosummary::
	
	traces.Trace
	movies.Movie
    roi.ROI

Traces
---------------

.. currentmodule:: traces

.. autoclass:: Trace
   :members: plot, normalize

Movie
------------

.. currentmodule:: movies

.. autoclass:: Movie
   :members: project, play, extract_by_roi, correct_motion, select_roi


ROI
------------

.. currentmodule:: roi

.. autoclass:: ROI
    :members: show, add
