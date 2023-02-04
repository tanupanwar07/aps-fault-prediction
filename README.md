AIR PRESSURE SYSTEM FAULT DETECTION

🟢 Introduction
Heavy vehicles play a huge role in industrial sectors as the primary medium of road transportation. They are the most flexible and economic mode of transportation and they run on a daily basis in every industry.

A well done maintenance is the key to avoid any undesired breakdowns, thus saving money and time. In this context, it is of fundamental importance that all the vehicle components are regularly maintained.

One such vital component is the Air Pressure System (APS). The APS generates pressurized air that is used for diﬀerent tasks such as braking, gear changing etc. , making it a very important subject of maintenance.

🟢 Content
The dataset consists of data collected from heavy Scania trucks in everyday usage. The system in focus is the Air Pressure system (APS) which generates pressurized air that is utilized in various functions in a truck, such as braking and gear changes. The datasets' positive class consists of component failures for a specific component of the APS system. The negative class consists of trucks with failures for components not related to the APS. The data consists of a subset of all available data, selected by experts.

🟢 Constraints
The main constraint for this problem is to minimize the total cost of making false predictions which is explained as follows.

Total Cost = Cost 1 * False Positives + Cost 2 * False Negatives

Cost 1 : An unnecessary check done by a mechanic ($10)

Cost 2 : Missing a faulty truck, which may cause a future breakdown ($500)

The goal is to minimize the total cost and one can notice that cost 2 far exceeds cost 1. This means that our ML model should be able to reduce false negatives as many as possible
