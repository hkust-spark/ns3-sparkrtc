# SparkRTC ns-3 Simulator

This is an ns-3 simulator specifically designed to simulate the real-time communication (RTC) applications. It has integrated the congestion control algorithms (GCC and NADA), forward error correction algorithms (WebRTC, Hairpin, and others), and the backpressure bit-rate adaptation algorithm. It also has the capability to simulate the network conditions in the real world.

The simulator has been used in the following papers. Please cite us if you want to use the simulator in your research.
```
@inproceedings{sigcomm2022zhuge,
  title = {{Achieving Consistent Low Latency for Wireless Real Time Communications with the Shortest Control Loop}},
  author = {Meng, Zili and Guo, Yaning and Sun, Chen and Wang, Bo and Sherry, Justine and Liu, Hongqiang Harry and Xu, Mingwei},
  year = {2022},
  booktitle = {Proc. ACM SIGCOMM}
}

@inproceedings{nsdi2024hairpin,
  title={Hairpin: Rethinking Packet Loss Recovery in Edge-based Interactive Video Streaming},
  author={Meng, Zili and Kong, Xiao and Chen, Jing and Wang, Bo and Xu, Mingwei and Han, Rui and Liu, Honghao and Arun, Venkat and Hu, Hongxin and Wei, Xue},
  booktitle={Proc. USENIX NSDI},
  year={2024}
}
```

## Usage
DO NOT CLONE THE REPO BEFOREHAND! Please follow the instructions below to install the simulator.

We provide two versions of the simulator based on ns-3 version 3.33 and 3.40 (this is because ns-3 upgrades its compilation toolchain from `waf` to `cmake`). The default branch is 3.40. If you want to use the 3.33 version, please switch to the `ns-3.33` branch.

### 1. Install ns-3
```
wget https://www.nsnam.org/releases/ns-allinone-3.40.tar.bz2
tar xjf ns-allinone-3.40.tar.bz2
cd ns-allinone-3.40/ns-3.40/
```

### 2. Install the simulator
Make sure that you're now in the `ns-3.40` directory.
```
git clone https://github.com/hkust-spark/ns3-sparkrtc src/sparkrtc
```

### 3. Build the simulator
Make sure that you're now in the `ns-3.40` directory.

Configure the ns-3 with examples enabled.
```
./ns3 configure --enable-examples
```
Compile the ns-3.
```
./ns3
```

### 4. Run the example in the simulator
Make sure that you're now in the `ns-3.40` directory.
```
./ns3 run "rtc-test --vary=1 --fecPolicy=hairpin"
```
The above command will run the simulator with the Hairpin FEC policy, under the sample network trace `sample.tr` in `examples/`.

### 5. Check the results and logs
The results are stored in the `logs/` directory under `ns-3.40/`. 

## Analysis
We explain the format of three output logs (`ns-3.40/logs`) and the input network traces (`examples/sample.tr`).

### 1. `app.log` 
It records the encoding and playing time of each frame, in the unit of millisecond. For example, the following line:
```
Frame 10 encoded 166 played at 176 missddl? 0
```
indicates that the 10th frame was encoded at t=166ms (at the server) and delivered to the client and was played at t=176ms (at the client). The last column indicates whether the frame was missed its deadline (1) or not (0).

### 2. `fec.log`
It records the FEC encoding information of each FEC block. For example, the following line:
```
33 frameId 2 groupId 2 txCnt 0 batchId 2 batchDataNum 45 batchFecNum 0 encodeTime 33 measuredRtt 23 measuredLoss 0 measuredRttStd 0 fecRate 0
```
indicates that at time t=33ms, the 2nd frame, also the 2nd group (for some frames, one frame can have multiple groups), is the first time of transmission (`txCnt 0`).
The size of the FEC block is 45 packets (`batchDataNum 45`), and the number of FEC packet is 0 (`batchFecNum 0`). The encoding time is 33ms (`encodeTime 33`), and the measured RTT is 23ms (`measuredRtt 23`). The measured loss rate is 0 (`measuredLoss 0`), and the measured RTT standard deviation is 0 (`measuredRttStd 0`). The FEC rate is 0 (`fecRate 0`).

### 3. `debug.log`
This is used to store the logs output from the `m_debugStream`, which can be customized by the user.

### 4. `sample.tr`
This is the network trace used in the example. It is a text file, and each line represents a measurement sample. The 1st, 2nd and 3rd columns are the bandwidth, RTT, and loss rate.
The interval between two samples are defined as the `variation_interval` CLI argument in `examples/rtc-test.cc`. The default value is 16ms (for 60fps video streaming).