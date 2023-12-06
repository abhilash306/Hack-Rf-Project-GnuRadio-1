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
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
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
import try1_const_rx_epy_block_0_0 as epy_block_0_0  # embedded python block
import try1_const_rx_epy_block_1_0 as epy_block_1_0  # embedded python block
import try1_const_rx_epy_block_1_0_0 as epy_block_1_0_0  # embedded python block
import try1_const_rx_epy_block_1_0_1 as epy_block_1_0_1  # embedded python block
import try1_const_rx_epy_block_1_0_2 as epy_block_1_0_2  # embedded python block
import try1_const_rx_epy_block_1_0_2_0 as epy_block_1_0_2_0  # embedded python block
import try1_const_rx_epy_block_1_0_2_0_0 as epy_block_1_0_2_0_0  # embedded python block



from gnuradio import qtgui

class try1_const_rx(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "try1_const_rx")

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
        self.variable_constellation_rect_0 = variable_constellation_rect_0 = digital.constellation_rect([-1-1j, -1+1j, 1+1j, 1-1j], [0, 1, 3, 2],
        4, 2, 2, 1, 1).base()
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0 = digital.adaptive_algorithm_cma( variable_constellation_rect_0, .0001, 4).base()
        self.timing_loop_bw = timing_loop_bw = 6.28/100.0
        self.taps = taps = [1.0, 0.25-0.25j, 0.50 + 0.10j, -0.3 + 0.2j]
        self.samp_rate = samp_rate = 2000000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.phase_bw = phase_bw = 6.28/100.0
        self.noise_0 = noise_0 = 0
        self.noise = noise = 0
        self.excess_bw = excess_bw = 0.35
        self.arity = arity = 4

        ##################################################
        # Blocks
        ##################################################
        self._timing_loop_bw_range = Range(0.0, 0.2, 0.01, 6.28/100.0, 200)
        self._timing_loop_bw_win = GrRangeWidget(self._timing_loop_bw_range, self.set_timing_loop_bw, "Time: BW", "slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._timing_loop_bw_win)
        self._phase_bw_range = Range(0.0, 1.0, 0.01, 6.28/100.0, 200)
        self._phase_bw_win = GrRangeWidget(self._phase_bw_range, self.set_phase_bw, "Phase: Bandwidth", "slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._phase_bw_win)
        self.qtgui_number_sink_0_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0_0_0.set_title('snr CH2 50KHZ')

        labels = ['snr selected', '', '', '', '',
            '', '', '', '', '']
        units = ['db', '', '', '', '',
            '', '', '', '', '']
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0_0_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0_0_0_0.set_max(i, 30)
            self.qtgui_number_sink_0_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_0_0_0_win)
        self.qtgui_number_sink_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0_0.set_title('snr CH1 100KHZ')

        labels = ['snr selected', '', '', '', '',
            '', '', '', '', '']
        units = ['db', '', '', '', '',
            '', '', '', '', '']
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0_0_0.set_max(i, 30)
            self.qtgui_number_sink_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_0_0_win)
        self.qtgui_number_sink_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0.set_title('selected snr')

        labels = ['snr selected', '', '', '', '',
            '', '', '', '', '']
        units = ['db', '', '', '', '',
            '', '', '', '', '']
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0_0.set_max(i, 30)
            self.qtgui_number_sink_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_0_win)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title('reciver snr')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_win)
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
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_source_0.set_time_now(osmosdr.time_spec_t(time.time()), osmosdr.ALL_MBOARDS)
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(600e6, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(50, 0)
        self.osmosdr_source_0.set_if_gain(60, 0)
        self.osmosdr_source_0.set_bb_gain(60, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(5e6, 0)
        self._noise_0_range = Range(0, 5, 0.0001, 0, 200)
        self._noise_0_win = GrRangeWidget(self._noise_0_range, self.set_noise_0, "noise of channel 2 50khz", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._noise_0_win)
        self._noise_range = Range(0, 5, 0.01, 0, 200)
        self._noise_win = GrRangeWidget(self._noise_range, self.set_noise, "noise of channel1 100khz", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._noise_win)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                10e3,
                5e3,
                window.WIN_RECTANGULAR,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                10e3,
                5e3,
                window.WIN_RECTANGULAR,
                6.76))
        self.epy_block_1_0_2_0_0 = epy_block_1_0_2_0_0.blk()
        self.epy_block_1_0_2_0 = epy_block_1_0_2_0.blk()
        self.epy_block_1_0_2 = epy_block_1_0_2.blk()
        self.epy_block_1_0_1 = epy_block_1_0_1.blk()
        self.epy_block_1_0_0 = epy_block_1_0_0.blk()
        self.epy_block_1_0 = epy_block_1_0.blk()
        self.epy_block_0_0 = epy_block_0_0.blk()
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_cc(
            digital.TED_MUELLER_AND_MULLER,
            sps,
            0.0628,
            1.0,
            1.0,
            1.5,
            1,
            digital.constellation_bpsk().base(),
            digital.IR_MMSE_8TAP,
            128,
            [])
        self.digital_probe_mpsk_snr_est_c_0_1_0 = digital.probe_mpsk_snr_est_c(0, 10000, 0.001)
        self.digital_probe_mpsk_snr_est_c_0_1 = digital.probe_mpsk_snr_est_c(0, 10000, 0.001)
        self.digital_probe_mpsk_snr_est_c_0_0 = digital.probe_mpsk_snr_est_c(0, 10000, 0.001)
        self.digital_probe_mpsk_snr_est_c_0 = digital.probe_mpsk_snr_est_c(0, 10000, 0.001)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, timing_loop_bw, rrc_taps, nfilts, (nfilts/2), 1.5, 2)
        self.digital_linear_equalizer_0 = digital.linear_equalizer(15, 2, variable_adaptive_algorithm_0, True, [ ], 'corr_est')
        self.digital_costas_loop_cc_0_0_0 = digital.costas_loop_cc(phase_bw, arity, False)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_1_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 50e3, 10, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 100e3, 10, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.digital_probe_mpsk_snr_est_c_0, 'snr'), (self.epy_block_1_0_0, 'snr'))
        self.msg_connect((self.digital_probe_mpsk_snr_est_c_0, 'snr'), (self.epy_block_1_0_2_0, 'snr'))
        self.msg_connect((self.digital_probe_mpsk_snr_est_c_0_0, 'snr'), (self.epy_block_1_0_1, 'snr'))
        self.msg_connect((self.digital_probe_mpsk_snr_est_c_0_0, 'snr'), (self.epy_block_1_0_2_0_0, 'snr'))
        self.msg_connect((self.digital_probe_mpsk_snr_est_c_0_1, 'snr'), (self.epy_block_1_0, 'snr'))
        self.msg_connect((self.digital_probe_mpsk_snr_est_c_0_1_0, 'snr'), (self.epy_block_1_0_2, 'snr'))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.digital_linear_equalizer_0, 0), (self.digital_costas_loop_cc_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_linear_equalizer_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.digital_probe_mpsk_snr_est_c_0_1, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.epy_block_0_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.epy_block_0_0, 0), (self.digital_probe_mpsk_snr_est_c_0_1_0, 0))
        self.connect((self.epy_block_1_0, 0), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.epy_block_1_0_0, 0), (self.epy_block_0_0, 2))
        self.connect((self.epy_block_1_0_1, 0), (self.epy_block_0_0, 3))
        self.connect((self.epy_block_1_0_2, 0), (self.qtgui_number_sink_0_0_0, 0))
        self.connect((self.epy_block_1_0_2_0, 0), (self.qtgui_number_sink_0_0_0_0, 0))
        self.connect((self.epy_block_1_0_2_0_0, 0), (self.qtgui_number_sink_0_0_0_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.digital_probe_mpsk_snr_est_c_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.epy_block_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.digital_probe_mpsk_snr_est_c_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.epy_block_0_0, 1))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "try1_const_rx")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_constellation_rect_0(self):
        return self.variable_constellation_rect_0

    def set_variable_constellation_rect_0(self, variable_constellation_rect_0):
        self.variable_constellation_rect_0 = variable_constellation_rect_0

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_variable_adaptive_algorithm_0(self):
        return self.variable_adaptive_algorithm_0

    def set_variable_adaptive_algorithm_0(self, variable_adaptive_algorithm_0):
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0

    def get_timing_loop_bw(self):
        return self.timing_loop_bw

    def set_timing_loop_bw(self, timing_loop_bw):
        self.timing_loop_bw = timing_loop_bw
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.timing_loop_bw)

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 10e3, 5e3, window.WIN_RECTANGULAR, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 10e3, 5e3, window.WIN_RECTANGULAR, 6.76))
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps(self.rrc_taps)

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self.digital_costas_loop_cc_0_0_0.set_loop_bandwidth(self.phase_bw)

    def get_noise_0(self):
        return self.noise_0

    def set_noise_0(self, noise_0):
        self.noise_0 = noise_0

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity




def main(top_block_cls=try1_const_rx, options=None):

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
