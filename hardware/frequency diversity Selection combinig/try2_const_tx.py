#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: abhilash
# GNU Radio version: 3.10.4.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, GrRangeWidget
from PyQt5 import QtCore
import osmosdr
import time



from gnuradio import qtgui

class try2_const_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "try2_const_tx")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_range_1 = variable_qtgui_range_1 = 1
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 1
        self.variable_constellation_0 = variable_constellation_0 = digital.constellation_qpsk().base()
        self.sps = sps = 2
        self.signal_power_0 = signal_power_0 = 10
        self.signal_power = signal_power = 10
        self.samp_rate = samp_rate = 2000000
        self.freq1 = freq1 = 100000

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_1_range = Range(-1000, 1000000, 1, 1, 200)
        self._variable_qtgui_range_1_win = GrRangeWidget(self._variable_qtgui_range_1_range, self.set_variable_qtgui_range_1, "CHANNEL 1 100KHZ", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._variable_qtgui_range_1_win)
        self._variable_qtgui_range_0_range = Range(-1000, 1000000, 1, 1, 200)
        self._variable_qtgui_range_0_win = GrRangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, "CHANNEL 2 50KHZ", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._variable_qtgui_range_0_win)
        self._signal_power_0_range = Range(-1000, 1000000, 1, 10, 200)
        self._signal_power_0_win = GrRangeWidget(self._signal_power_0_range, self.set_signal_power_0, "increase signal carrier power 50Khz", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._signal_power_0_win)
        self._signal_power_range = Range(-1000, 1000000, 1, 10, 200)
        self._signal_power_win = GrRangeWidget(self._signal_power_range, self.set_signal_power, "increase signal power 100khz", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._signal_power_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_sink_0.set_time_now(osmosdr.time_spec_t(time.time()), osmosdr.ALL_MBOARDS)
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(600e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(50, 0)
        self.osmosdr_sink_0.set_if_gain(60, 0)
        self.osmosdr_sink_0.set_bb_gain(60, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(500e4, 0)
        self.digital_constellation_modulator_0 = digital.generic_mod(
            constellation=variable_constellation_0,
            differential=True,
            samples_per_symbol=2,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False,
            truncate=False)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_xx_1 = blocks.multiply_const_cc(variable_qtgui_range_0, 1)
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_cc(variable_qtgui_range_1, 1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_1_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 50e3, signal_power_0, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 100e3, signal_power, 0, 0)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 2, 1000))), True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_xx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_const_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_const_xx_1, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.qtgui_const_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "try2_const_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_qtgui_range_1(self):
        return self.variable_qtgui_range_1

    def set_variable_qtgui_range_1(self, variable_qtgui_range_1):
        self.variable_qtgui_range_1 = variable_qtgui_range_1
        self.blocks_multiply_const_xx_0.set_k(self.variable_qtgui_range_1)

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0
        self.blocks_multiply_const_xx_1.set_k(self.variable_qtgui_range_0)

    def get_variable_constellation_0(self):
        return self.variable_constellation_0

    def set_variable_constellation_0(self, variable_constellation_0):
        self.variable_constellation_0 = variable_constellation_0

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_signal_power_0(self):
        return self.signal_power_0

    def set_signal_power_0(self, signal_power_0):
        self.signal_power_0 = signal_power_0
        self.analog_sig_source_x_1_0.set_amplitude(self.signal_power_0)

    def get_signal_power(self):
        return self.signal_power

    def set_signal_power(self, signal_power):
        self.signal_power = signal_power
        self.analog_sig_source_x_0.set_amplitude(self.signal_power)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_freq1(self):
        return self.freq1

    def set_freq1(self, freq1):
        self.freq1 = freq1




def main(top_block_cls=try2_const_tx, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
