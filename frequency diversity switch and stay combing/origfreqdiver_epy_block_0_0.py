"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt
import time
from gnuradio import grc
import inspect

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self,threshold=5):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='SelectionCombining',   # will show up in GRC
            in_sig=[np.complex64,np.complex64,np.float32,np.float32],
            out_sig=[np.complex64]
        )
        #self.flag=0
        self.th = threshold
        #print("1")
      
    
    def work(self, input_items, output_items):
        """example: multiply with constant"""
        
        if input_items[2][0]>input_items[3][0]:
            output_items[0][:] = input_items[0]
        else:
            output_items[0][:] = input_items[1]
        return len(output_items[0])