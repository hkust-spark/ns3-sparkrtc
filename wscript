## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):
    module = bld.create_ns3_module('ns3-sparkrtc', ['internet', 'network'])
    module.source = [
        'model/game-client.cc',
        'model/game-server.cc',
        'model/network-packet-header.cc',
        'model/network-packet.cc',
        'model/packet-group.cc',
        'model/packet-receiver.cc',
        'model/packet-sender.cc',
        'model/video-decoder.cc',
        'model/video-encoder.cc',
        'model/fec/fec-policy.cc',
        'model/fec/hairpin-policy.cc',
        'model/fec/webrtc-policy.cc',
        'model/fec/other-policy.cc',
        'model/fec/webrtc-fec-array.cc',
        'model/fec/webrtc-adjust-array.cc',
        'model/congestion-control/rtc_base/checks.cc',
        'model/congestion-control/sender-based-controller.cc',
        'model/congestion-control/nada-controller.cc',
        'model/congestion-control/gcc-controller.cc'
        ]

    headers = bld(features='ns3header')
    headers.module = 'ns3-sparkrtc'
    headers.source = [
        'model/common-header.h',
        'model/game-client.h',
        'model/game-server.h',
        'model/network-packet-header.h',
        'model/network-packet.h',
        'model/packet-group.h',
        'model/packet-receiver.h',
        'model/packet-sender.h',
        'model/video-decoder.h',
        'model/video-encoder.h',
        'model/fec/fec-policy.h',
        'model/fec/hairpin-policy.h',
        'model/fec/webrtc-policy.h',
        'model/fec/other-policy.h',
        'model/fec/webrtc-fec-array.h',
        'model/fec/webrtc-adjust-array.h',
        'model/congestion-control/rtc_base/checks.h',
        'model/congestion-control/rtc_base/type_traits.h',
        'model/congestion-control/rtc_base/numeric/safe_compare.h',
        'model/congestion-control/rtc_base/numeric/safe_minmax.h',
        'model/congestion-control/rtc_base/system/inline.h',
        'model/congestion-control/sender-based-controller.h',
        'model/congestion-control/nada-controller.h',
        'model/congestion-control/gcc-controller.h',
        ]

    
    if (bld.env['ENABLE_EXAMPLES']):
        bld.recurse('examples')
