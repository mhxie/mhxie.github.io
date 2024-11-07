---
layout: default
---


*My name is Minghao Xie, and I am a final\-year Computer Engineering Ph.D. candidate at the Baskin School of Engineering, UC Santa Cruz. I hold a B.E. degree (with honor) in Computer Science from Sichuan University, China.*

*I am advised by Prof.* [*Chen Qian*](https://users.soe.ucsc.edu/~qian/) *and Prof.* [*Heiner Litz*](https://people.ucsc.edu/~hlitz/)*. My research interests encompass computer networks and systems, with a current focus on flash storage disaggregation within data centers. Recently, I have expanded my focus to include AI infrastructure, particularly in areas such as scalable compute platforms and distributed computing frameworks. My PhD research was supported by the IAB members of the Center for Research in Systems and Storage (*[*CRSS*](https://www.crss.ucsc.edu/index.html)*) at UCSC, and the National Science Foundation (NSF).* 

*I am passionate about developing scalable, high\-performance, and reliable systems. I enjoy exploring new technologies and researching design trade\-offs among them. In my free time, I spend time with my two adorable cats,* [Toby](https://reflect.site/g/mhx/bc2a9325a02c4288b0ce4be9294f6862) *and* [Haruka](https://reflect.site/g/mhx/45fbba594816419dbe8120dfb3252d04)*, who often appear in my recent Instagram posts.*

*I also watch NBA games, and my favorite players are Kevin Durant of the Phoenix Suns. Despite being one of the most talented players in NBA history, KD remains humble and dedicated to continuous improvement. His relentless work ethic and passion for basketball inspire me to uphold similar values of dedication and humility in my own pursuits.*

## Research Experience

**Thesis: Predictable Cloud Storage System**, 2019 \- 2024  
*Advisors: Heiner Litz, Chen Qian \| Funding: CRSS and NSF*

- Analyzed the performance unpredictability in ephemeral storage (for **serverless** computing) and engineered a profile\-based system, enhancing goodput predictability by up to **3x**.
- Created a high\-performance, μs\-level **async** serverless client library using **Cython**, and developed cloud\-native applications (e.g. ML and microservices) with it on **AWS**.
- Designed and implemented a novel flow\-based scheduler using **Ray**, resulting in **37%** TCO savings without compromising SLO guarantee on IOPS nor **tail latency**.
- Finished two papers for top\-tier conferences: **En4S** \[[PDF](https://github.com/mhxie/mhxie.github.io/blob/main/assets/paper/En4S.pdf)] \[[Code](https://github.com/mhxie/En4S)] (SoCC ’24\), **LESS** \[PDF] \[Code] (in sub).

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

**Evaluating 100Gbps Flash Disaggregation on ARM SoC** \[[Code](https://github.com/mhxie/reflex4arm)], 2018 \- 2019  
*Advisor: Heiner Litz and Chen Qian, Funding: CRSS, Broadcom and NSF*

- Built a performant open\-sourced storage system with **SPDK** and **DPDK** in **C**.
- Optimized the **ARM** system at the **assembly** level, reducing TCO by **2\.57x**.

## Teaching

- CSE150 (TA): Introduction to Computer Networks, 24Spring
- CSE120 (TA): Computer Architecture, **24Fall**, 24Win, 23Fall, 22Spring, 21Fall, 21Win, 20Win
- CMPE110 (TA): Computer Architecture, 19Win

## Publications

1. Liu, Y., **Xie, M.**, Shi, S., Xu, Y., Litz, H., \& Qian, C. (2025\). Outback: Fast and communication\-efficient index for key\-value store on disaggregated memory. In conference of the VLDB Endowment (VLDB ’25\). \[PDF]

2. **Xie, M**., Qian, C., Litz, H. (2024\). En4S: Enabling SLOs in serverless storage systems. Proceedings of the ACM Symposium on Cloud Computing (SoCC ’24\). \[[PDF](https://github.com/mhxie/mhxie.github.io/blob/main/assets/paper/En4S.pdf)]

3. Liu, Y., Shi, S., **Xie, M**., Litz H., Qian, C. Smash: Flexible, Fast, and Resource\-efficient Placement and Lookup of Distributed Storage. In conference of the ACM special interest group for the computer systems performance evaluation community (SIGMETRICS '23\). \[[PDF](https://github.com/mhxie/mhxie.github.io/blob/main/assets/paper/Smash.pdf)]

4. Shi, S., Yu, Y., **Xie, M.**, Li X., Li, X., Zhang, Y., Qian, C. Concury: A Fast and Light\-weight Software Cloud Load Balancer. In conference of the ACM Symposium on Cloud Computing 2020 (SoCC '20\). \[[PDF](https://github.com/mhxie/mhxie.github.io/blob/main/assets/paper/Concury.pdf)]

5. **Xie, M.**, Qian, C., Litz, H. ReFlex4ARM: Supporting 100GbE Flash Storage Disaggregation on ARM SoC. OCP Future Technologies Symposium 2020\. Poster session in San Jose, CA (OCP '20\). \[[PDF](https://github.com/mhxie/mhxie.github.io/blob/main/assets/paper/ReFlex4ARM.pdf)]

6. **Xie, M.**, Qian, C., Litz, H. (2019, August 4\-6\). Evaluating 100Gbps Flash Disaggregation on ARM SoC. Flash Memory Summit 2019 (FMS '19\). Poster session in Santa Clara, CA.



Last update on 2024-11-07