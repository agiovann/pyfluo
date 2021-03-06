from ts_base import TSBase
import numpy as np
import pylab as pl
import warnings

class Trace(TSBase):
    """An object to hold one or more data vectors along with a single time vector

    Parameters
    ----------
    data : np.ndarray
        input data, either 1d or 2d. Details below
    time : [optional] np.ndarray, list 
        time vector with n elements
    Ts : [optional] float
        sampling period
    info : [optional] list, np.ndarray
        info vector with n elements

    The data in Trace objects is stored following the standard pyfluo convention in which the 0th axis corresponds to time. For example, trace[0] corresponds to the data at time 0. 

    This object can be used to store multiple time series of data, for example the traces corresponding to multiple ROIs in a movie. In this case, the above convention still holds, and trace[0] will supply an n-length vector corresponding to n series of data at time 0.

    It should be noted that error checking with regard to the time vector is still under progress. All tested operations are functional, but thorough testing has not yet been performed.
    """
    def __new__(cls, data, **kwargs):
        return super(Trace, cls).__new__(cls, data, _ndim=[1,2], **kwargs)

    def as2d(self):
        """Return 2d version of object

        Useful because the object can in principle be 1d or 2d
        """
        if self.ndim == 1:
            return np.rollaxis(np.atleast_2d(self),-1)
        else:
            return self

    def normalize(self, minmax=(0., 1.), axis=None):
        """Normalize the data
        
        Parameters
        ----------
        minmax : list, tuple 
            ``[post_normalizaton_data_min, max]``
        axis : int 
            axis over which to normalize
            
        Returns
        -------
        A new Trace object, normalized
        """
        newmin,newmax = minmax
        omin,omax = self.min(axis=axis),self.max(axis=axis)
        new_obj = self.copy() 
        new_obj.data = (self-omin)/(omax-omin) * (newmax-newmin) + newmin
        return new_obj

    def plot(self, stacked=True, subtract_minimum=True, cmap=pl.cm.jet, **kwargs):
        """Plot the data
        
        Parameters
        ----------
        stacked : bool 
            for multiple columns of data, stack instead of overlaying
        subtract_minimum : bool
            subtract minimum from each individual trace
        cmap : matplotlib.LinearSegmentedColormap
            color map for display. Options are found in pl.colormaps(), and are accessed as pl.cm.my_favourite_map
        kwargs : dict
            any arguments accepted by matplotlib.plot

        Returns
        -------
        The matplotlib axes object corresponding to the data plot
        """
        d = np.atleast_2d(self).copy()

        ax = pl.gca()

        colors = cmap(np.linspace(0, 1, d.shape[1]))
        ax.set_color_cycle(colors)

        if subtract_minimum:
            d -= d.min(axis=0)
        if stacked:
            d += np.append(0, np.cumsum(d.max(axis=0))[:-1])
        ax.plot(self.time, d)        
       
        # display trace labels along right
        ax2 = ax.twinx()
        ax2.set_ylim(ax.get_ylim())
        ax2.set_yticks(d.mean(axis=0))
        ax2.set_yticklabels([str(i) for i in xrange(d.shape[1])], weight='bold')
        [l.set_color(c) for l,c in zip(ax2.get_yticklabels(), colors)]

        pl.gcf().canvas.draw()

        return ax
