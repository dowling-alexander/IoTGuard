Install requirements:

user$ python -m pip install -r requirements.txt

Below is an outline for a masters project im reviewing for cyber security. The outline is currently broad but the intent will be to over time hone and focus the project further once i understand the subject matter in more detail.

Intended Structure:
/IoTGuard/
├── config/ 
│   ├── iotguard.conf
│   ├── logstash.conf
│   └── elasticsearch.yml
├── data/
│   ├── logs/
│   │   ├── iotguard/
│   └── pcap/
├── scripts/
│   ├── start_iotguard.sh
│   ├── start_elk.sh
│   └── analyze_traffic.py
├── models/
│   ├── anomaly_detection_model.pkl
│   └── intrusion_detection_model.h5
├── docs/
│   ├── project_proposal.md
│   ├── design_document.md
│   └── user_manual.md
└── src/
    ├── main.py
    ├── utils.py
    └── iot_traffic_analyzer.py


Resource Ideas and Further Learning.
Python Libraries:
Scapy for packet manipulation.
Pandas and NumPy for data analysis.
TensorFlow or Scikit-learn for machine learning, intent would be to optimise this over time. (this may be future work after the project)
Flask or FastAPI, this will form a web interface. Need to spend some time on generating this and understanding what is required.
Data Collection and Analysis:
Wireshark for packet analysis.
Elasticsearch, Logstash, Kibana (ELK Stack) for log management and visualization.
Communication Protocols:
MQTT or CoAP for IoT device communication.

Will resume work on this mid November, currently studying for exams and CPTS
