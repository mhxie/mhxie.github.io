---
layout: default
---


**I am currently seeking job opportunities in the fields of computer networks, systems, and storage technologies.**

*My name is Minghao Xie, and I am a Computer Engineering Ph.D. candidate at the Baskin School of Engineering, UC Santa Cruz. I hold a B.E. degree in Computer Science from Sichuan University, China.*

*I am advised by Prof.* [*Chen Qian*](https://users.soe.ucsc.edu/~qian/) *and Prof.* [*Heiner Litz*](https://people.ucsc.edu/~hlitz/)*. My research interests lie in computer networks and systems, with a current focus on flash storage disaggregation within data centers. This work is part of the Center for Research in Systems and Storage (*[*CRSS*](https://www.crss.ucsc.edu/index.html)*) and the Hardware Systems Collective (*[*HSC*](https://hsc.ucsc.edu/)*) at UCSC. I am dedicated to building scalable, high\-performance, and reliable systems.*

*I am passionate about research and coding. I am an active language learner, fluent in both Chinese and English, and currently learning Japanese. In my free time, I enjoy spending time with my two cats,* [Toby](https://reflect.site/g/mhx/bc2a9325a02c4288b0ce4be9294f6862) *and* [Haruka](https://reflect.site/g/mhx/45fbba594816419dbe8120dfb3252d04)*, who often appear in my recent Instagram posts.*

## Teaching

- CSE150 (TA): Introduction to Computer Networks, 24Spring
- CSE120 (TA): Computer Architecture, **24Fall**, 24Win, 23Fall, 22Spring, 21Fall, 21Win, 20Win
- CMPE110 (TA): Computer Architecture, 19Win

## Projects

**Thesis: Predictable Cloud Storage System** \[GitHub] \[Paper], 2019 \- 2023  
*Advisors: Heiner Litz, Chen Qian \| Funding: CRSS, NSF*

- Analyzed the performance unpredictability in ephemeral storage (for **serverless** computing) and engineered a profile\-based system, enhancing goodput predictability by up to **3x**.
- Created a high\-performance, μs\-level **async** serverless client library using **Cython**, and developed cloud\-native applications (e.g. ML and microservices) with it on **AWS**.
- Designed and implemented a novel flow\-based scheduler using **Ray**, resulting in **37%** TCO savings without compromising SLO guarantee on IOPS nor **tail latency**.
- Finished two papers for top\-tier conferences: \[En4S] \[[Code](https://github.com/mhxie/En4S)] (SoCC ’24\), \[LESS] \[Code] (in sub).

**Trading Density for Performance in DNA\-based Archival Storage Systems**, 23Spring  
*Advisor:* [*Ethan Miller*](https://ethanmiller.org/)*, CSE 290S: Advanced Topics in Computer Systems*

- Conducted research on the trade\-offs between storage density and performance in DNA\-based archival storage systems
- Designed and evaluated novel approaches to optimize performance without significantly compromising storage density

**AIRD: Your Personal AI RSS Daily** \[[GitHub](https://github.com/mhxie/AIRD)], 2024  
*Personal Project*

- Developed an AI\-powered RSS assistant in **Python** for filtering and summarizing articles, featuring advanced deduplication and data privacy.
- Configured customizable, multilingual support with plans for enhanced link reading and automated tagging.

**Transport Optimization for Storage Disaggregation**, June \-\- Sep 2022  
*Company: Meta Platform, Mentor:* [*Minkyu Jeong*](https://www.linkedin.com/in/mjeong?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAIT7fQBX6a1l-fYTtJhoWnOUIwTX7fz1Og&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_people%3BeWoiB6C1RqaKfsxOwmswmw%3D%3D)*,* *Position: Research Engineering Intern at CEA*

- Collaborated with the storage team to identify transport alternatives to **Thrift** for internal storage workloads, focusing on enhancing performance and scalability.
- Achieved a **2\.6x** increase in throughput and a **63%** reduction in latency by optimizing data transport mechanisms and implementing efficient algorithms in **C\+\+**.
- Removed bottlenecks through advanced **profiling** and **tuning** techniques, leading to **linear** throughput scalability and proportional cost efficiency improvements.

**Disaggregated Optane SSD for Embedding Table**, July \-\- Sep 2021  
*Company: Facebook, Mentor:* [*Niket Agarwal*](https://www.linkedin.com/in/niket-agarwal-9522b27?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAFKFc4B5KbmtZ193V1qc9l8Z-_1dAoXSaU)*, Position: Research Engineering Intern at CEA*

- Worked closely with the ML team to analyze and address scaling bottlenecks and disaggregation needs of internal **PyTorch**\-based **SparseNN** workloads.
- Developed a fast userspace NBD **driver** in **C\+\+**, achieving a speedup of **1\.7x** to **6\.7x**, demonstrating proficiency in low\-level systems programming and perf. optimization.
- Enhanced support for large\-scale **ML workloads** by contributing to an internal library, and published a comprehensive project note to document its impact.

**Exploring the New SPDK Threading Model and its Scheduling Possibility**, 20Winter  
*Advisor:* [*Ethan Miller*](https://ethanmiller.org/)*, CSE 231: Advanced Operating Systems*

- Conducted code analysis and performance evaluations on the new SPDK threading library
- Designed and partially implemented a cooperative IO\-thread scheduler with new SPDK APIs

**Supporting Scalable Fault\-Tolerant Distributed** **Message Queue with Persistent Storage** \[[Github](https://github.com/mhxie/disque_protocol)]**,** 19Fall  
*Advisor:* [*Faisal Nawab*](https://www.nawab.me/)*, CSE 214: Principles of Database Systems*

- Designed a distributed message queue framework with fault tolerance
- Implemented log\-based mechanism to resolve the inter\-broker failures

**A Ultra\-low Latency QUIC\-stack Acceleration Engine**, 19Winter  
*Advisor:* [*Scott Beamer*](https://scottbeamer.net/)*, CMPE 293: Programmable Hardware Accelerators*

- Conducted characterization of **QUIC** protocol and workload analysis
- Designed a **NetFPGA**\-based acceleration engine

**Towards Single Round\-Trip: An Efficient Metadata Offloading Mechanism for Tree\-based Oblivious RAM**, 19Winter  
*Advisor: Chen Qian, CMPE 253: Network Security*

- Designed a way of efficient metadata management based on ring **ORAM** and Information\-theoretical Private\-information\-retrieval (ITPIR)
- Optimized the algorithm with multi\-step bit\-based accelerations

**Evaluating 100Gbps Flash Disaggregation on ARM SoC** \[[GitHub](https://github.com/mhxie/reflex4arm)] \[[Paper](https://www.ssrc.ucsc.edu/media/pubs/89a276a7823f1ca45cb66c163f20dccc81bfa959.pdf)], 2018 \- 2019  
*Advisor: Heiner Litz and Chen Qian, Funding: CRSS, Broadcom \& NSF*

- Built a performant open\-sourced storage system with **SPDK** and **DPDK** in **C**.
- Optimized the **ARM** system at the **assembly** level, reducing TCO by **2\.57x**.

## Publications

1. Liu, Y., Shi, S., **Xie, M**., Litz H., \& Qian, C. SMASH: Flexible, Fast, and Resource\-efficient Placement and Lookup of Distributed Storage. In conference of the ACM special interest group for the computer systems performance evaluation community (SIGMETRICS '23\).

2. Shi, S., Yu, Y., **Xie, M.**, Li X., Li, X., Zhang, Y. \& Qian, C. Concury: A Fast and Light\-weight Software Cloud Load Balancer. In conference of the ACM Symposium on Cloud Computing 2020 (SOCC '20\).

3. **Xie, M.**, Qian, C., Litz, H. ReFlex4ARM: Supporting 100GbE Flash Storage Disaggregation on ARM SoC. OCP Future Technologies Symposium 2020\. Poster session in San Jose, CA (OCP '20\).

4. **Xie, M.**, Qian, C., Litz, H. (2019, August 4\-6\). Evaluating 100Gbps Flash Disaggregation on ARM SoC. Flash Memory Summit 2019\. Poster session in Santa Clara, CA.



Last update on 2024-10-17