---
layout: default
---


*My name is Minghao Xie, and I am a final-year Ph.D. candidate in Computer Engineering at the Baskin School of Engineering, UC Santa Cruz. I hold a B.E. degree (with honors) in Computer Science from Sichuan University, China. Advised by Prof.* [*Chen Qian*](https://users.soe.ucsc.edu/~qian/) *and Prof.* [*Heiner Litz*](https://people.ucsc.edu/~hlitz/)*, my research focuses on computer networks and systems, particularly flash storage disaggregation within data centers. Recently, I have expanded my work to AI infrastructure, exploring scalable compute platforms and distributed computing frameworks. My Ph.D. research has been supported by the IAB members of the Center for Research in Systems and Storage (*[*CRSS*](https://www.crss.ucsc.edu/index.html)*) at UCSC and National Science Foundation (NSF).*

*I am passionate about building scalable, high-performance, and predictable systems. Outside of work, I love exploring new places, as traveling opens my mind to fresh perspectives and diverse ways of life. Strategy-based and board games are a favorite pastime, challenging me to solve problems creatively and adapt to evolving scenarios. And as an NBA fan, I admire the dedication and humility of players like Kevin Durant, inspiring me to bring the same relentless commitment to my own goals.*

*I am also a software engineer at* [*Anyscale*](https://www.anyscale.com/)*, where we’re building cutting-edge solutions for scalable AI infrastructure.* ***We’re hiring!*** *If you’re interested in joining us, feel free to* ***email me your resume****, and I’d be happy to refer you if there’s a match.*

## Work Experience

**Transport Optimization for Storage Disaggregation**, June - Sep 2022   
*Meta Platform, Research Engineering Intern at CEA*

- Collaborated with the storage team to identify transport alternatives to **Thrift** for internal storage workloads, focusing on enhancing performance and scalability.
- Achieved a **2.6x** increase in throughput and a **63%** reduction in latency by optimizing data transport mechanisms and implementing efficient algorithms in **C++**.
- Removed bottlenecks through advanced **profiling** and **tuning** techniques, leading to **linear** throughput scalability and proportional cost efficiency improvements.

**Disaggregated Optane SSD for Embedding Table**, July - Sep 2021   
*Facebook, Research Engineering Intern at CEA*

- Worked closely with the ML team to analyze and address scaling bottlenecks and disaggregation needs of internal **PyTorch**-based **SparseNN** workloads.
- Developed a fast userspace NBD **driver** in **C++**, achieving a speedup of **1.7x** to **6.7x**, demonstrating proficiency in low-level systems programming and perf. optimization.
- Enhanced support for large-scale **ML workloads** by contributing to an internal library, and published a comprehensive project note to document its impact.

## Research Experience

**Thesis: Towards Efficient, Predictable, and Scalable Ephemeral Storage Systems**, 2019 - 2024   
*UC Santa Cruz, Research Assistant, Funded by CRSS and NSF*

- Analyzed the performance unpredictability in ephemeral storage (for **serverless** computing) and engineered a profile-based system, enhancing goodput predictability by up to **3x**.
- Created a high-performance, μs-level **async** serverless client library using **Cython**, and developed cloud-native applications (e.g. ML and microservices) with it on **AWS**.
- Designed and implemented a novel flow-based scheduler using [[Ray](https://www.ray.io/)], resulting in **37%** TCO savings without compromising SLO guarantee on IOPS nor **tail latency**.
- The Data Plane Paper: **En4S** [[PDF](https://github.com/mhxie/mhxie.github.io/blob/main/assets/paper/En4S.pdf)] [[Code](https://github.com/mhxie/En4S)] (SoCC ’24), **Best Paper Award**
- The Control Plane Paper: **TBD** [PDF] [Code] (in sub)
- The Application Paper: **LESS** [PDF] (NSDI ‘25 Poster)

**Evaluating 100Gbps Flash Disaggregation on ARM SoC** [[Code](https://github.com/mhxie/reflex4arm)], 2018 - 2019   
*UC Santa Cruz, Research Assistant, Funded by CRSS and Broadcom Inc.*

- Built a performant open-sourced storage system with **SPDK** and **DPDK** in **C**.
- Optimized the **ARM** system at the **assembly** level, reducing TCO by **2.57x**.

**Stateful SDN-based Caching Strategy for NDN Networks**, 2017 - 2018   
*Sichuan University, Research Assistant, Funded by* [*The Pilot Project 1.0*](https://zh.wikipedia.org/wiki/%E5%9F%BA%E7%A1%80%E5%AD%A6%E7%A7%91%E6%8B%94%E5%B0%96%E5%AD%A6%E7%94%9F%E5%9F%B9%E5%85%BB%E8%AF%95%E9%AA%8C%E8%AE%A1%E5%88%92)

- Developed the Edge-Recency Interior-Frequency (ERIF)caching strategy with stateful **SDN** for **NDN** networks, achieving **2.3x** higher cache hit rates and reducing response time by **38%** through a hybrid of **Hungarian** and **greedy algorithms** to manage cache allocation effectively.
- Implemented extensible finite state machines (**XFSMs**) on the data plane to support real-time caching decisions, enhancing system adaptability and lowering latency by **30%** in simulations compared to traditional on-path caching methods

## Teaching

- CSE150 (TA): Introduction to Computer Networks, 24Spring
- CSE120 (TA): Computer Architecture, 24Fall, 24Win, 23Fall, 22Spring, 21Fall, 21Win, 20Win, 19Win

## Publications

1. [VLDB '25] Liu, Y., **Xie, M.**, Shi, S., Xu, Y., Litz, H., Qian, C. (2025, September). Outback: Fast and communication-efficient index for key-value store on disaggregated memory. In conference of the VLDB Endowment. [[PDF](https://dl.acm.org/doi/10.14778/3705829.3705849)]

2. [SoCC '24] **Xie, M.**, Qian, C., Litz, H. (2024, November). En4S: Enabling SLOs in Serverless Storage Systems. In *Proceedings of the 2024 ACM Symposium on Cloud Computing* (pp. 160-177). [[PDF](https://dl.acm.org/doi/10.1145/3698038.3698529)]

3. [SIGMETRICS '23] Liu, Y., Shi, S., **Xie, M.**, Litz, H., Qian, C. (2023, June). Smash: Flexible, fast, and resource-efficient placement and lookup of distributed storage. *Proceedings of the ACM on Measurement and Analysis of Computing Systems*, *7*(2), 1-22. [[PDF](https://dl.acm.org/doi/10.1145/3606376.3593569)]

4. [SoCC '20] Shi, S., Yu, Y., **Xie, M.**, Li, X., Li, X., Zhang, Y., Qian, C. (2020, October). Concury: A fast and light-weight software cloud load balancer. In *Proceedings of the 11th ACM Symposium on Cloud Computing* (pp. 179-192). [[PDF](https://dl.acm.org/doi/10.1145/3419111.3421279)]

5. [OCP '20] **Xie, M.**, Qian, C. (2020, January). ReFlex4arm: Supporting 100GbE flash storage disaggregation on ARM SoC. In *OCP Future Technology Symposium*. [[PDF](https://github.com/mhxie/mhxie.github.io/blob/main/assets/paper/ReFlex4ARM.pdf)]

6. [FMS '19] **Xie, M.**, Qian, C., Litz, H. (2019, August). Evaluating 100Gbps flash disaggregation on ARM SoC. In *Flash Memory Summit*.

Last update on 2025-04-06