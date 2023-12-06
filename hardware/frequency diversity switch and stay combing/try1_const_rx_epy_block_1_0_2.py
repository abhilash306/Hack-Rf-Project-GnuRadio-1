"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt
from gnuradio import grc

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='datatypeconversion',   # will show up in GRC
            in_sig=None,
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.selectPortName = 'snr'
        self.message_port_register_in(pmt.intern(self.selectPortName))
        self.set_msg_handler(pmt.intern(self.selectPortName), self.handle_msg)
        self.snr=0
        #print(222)
    def handle_msg(self,msg):
        self.snr=pmt.to_float(msg)
        #print(22)
        
    def work(self, input_items, output_items):
        """example: multiply with constant"""
        #print(2)
        output_items[0][:] = self.snr 
        return len(output_items[0])
