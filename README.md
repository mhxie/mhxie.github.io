# Minghao Xie | Home Page

- Office: E2-211 at UCSC main campus
- Preferred Contact: mhxie@ucsc.edu
- [Google Scholar](https://scholar.google.com/citations?user=LXVzkq8AAAAJ&hl=en&oi=ao), [Github](https://github.com/mhxie), [LinkedIn](https://www.linkedin.com/in/minghao-xie/), Minghao's Blog

## ![](https://firebasestorage.googleapis.com/v0/b/reflect-prod.appspot.com/o/users%2FrpjjtPwtlCY7bNVJhb94utcVoXV2%2F95ed05ddfa954e688242b8eba60d7081?alt=media\&token=e17a270d-ee32-44d8-8e34-874d93738b46)

## About Me

**I am currently seeking job opportunities in the fields of computer networks, systems, and storage technologies.**

My name is Minghao Xie, and I am a sixth-year Computer Engineering Ph.D. candidate at the Baskin School of Engineering, UC Santa Cruz. I hold a B.E. degree in Computer Science from Sichuan University, China.

I am fortunate to be advised by [Prof. Chen Qian](https://users.soe.ucsc.edu/~qian/) and [Prof. Heiner Litz](https://people.ucsc.edu/~hlitz/). My research interests lie in computer networks and systems, with a current focus on flash storage disaggregation within data centers. This work is part of the Center for Research in Systems and Storage ([CRSS](https://www.crss.ucsc.edu/index.html)) and the Hardware Systems Collective ([HSC](https://hsc.ucsc.edu/)) at UCSC. I am dedicated to building scalable, high-performance, and reliable systems.

I am passionate about research and coding. I am an active language learner, fluent in both Chinese and English, and currently learning Japanese. In my free time, I enjoy spending time with my two cats, Toby and Haruka, who often appear in my recent Instagram posts.

## Teaching

- CSE 150 (TA): Introduction to Computer Networks, 24Spring
  - Lab Section: Monday 16:00pm - 18:00pm 23
- CSE120 (TA): Computer Architecture, 24Win, 23Fall, 22Spring, 21Fall, 21Win, 20Win
- CMPE110 (TA): Computer Architecture, 19Win

## Projects

**LESS: An SLO-aware Serverless Storage System** [GitHub] (2019 - 2023)
_Advisors: Heiner Litz, Chen Qian | Funding: CRSS, NSF_
- Built a storage system with **SPDK** & **DPDK** in **C**, achieving 1M IOPS/core.
- Designed an SLO scheduler deployed with **Ray**, saving up to 37% TCO.
- Developed microsecond-level **Cython**-based **asynchronous** storage library.
- Implemented applications (e.g., **Microservice**) deployed with **Terraform** on **AWS**.

**Trading Density for Performance in DNA-based Archival Storage Systems** (23Spring)
_Advisor: [Ethan Miller](https://users.soe.ucsc.edu/~elm/), CSE 290S: Advanced Topics in Computer Systems_
- Conducted research on the trade-offs between storage density and performance in DNA-based archival storage systems
- Designed and evaluated novel approaches to optimize performance without significantly compromising storage density

**AIRD: Your Personal AI RSS Daily** [GitHub](https://github.com/mhxie/AIRD) (2024)
_Personal Project_
- Developed an AI-powered RSS assistant in **Python** for filtering and summarizing articles, featuring advanced deduplication and data privacy.
- Configured customizable, multilingual support with plans for enhanced link reading and automated tagging.

**Transport Optimization for Storage Disaggregation** (June -- Sep 2022)
_Company: Meta Platform, Mentor: [Minkyu Jeong](https://www.linkedin.com/in/mjeong?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAIT7fQBX6a1l-fYTtJhoWnOUIwTX7fz1Og&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_people%3BeWoiB6C1RqaKfsxOwmswmw%3D%3D), Position: Research Engineering Intern at CEA_
- Optimized and achieved 2.6x gain on throughput, 63% reduction in latency
- Removed the performance bottleneck and scaled throughput linearly in **C++**

**Disaggregated Storage for Embedding Table** (July -- Sep 2021)
_Company: Facebook, Mentor: [Niket Agarwal](https://www.linkedin.com/in/niket-agarwal-9522b27?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAFKFc4B5KbmtZ193V1qc9l8Z-_1dAoXSaU), Position: Research Engineering Intern at CEA_
- Analyzed the bottleneck of internal **PyTorch**-based SparseNN workloads
- Implemented a userspace NBD **driver** sped up by 1.7x\~6.7x in **C++**

**Exploring the New SPDK Threading Model and its Scheduling Possibility** (20Winter)
_Advisor: Ethan Miller, CSE 231: Advanced Operating Systems_
- Conducted code analysis and performance evaluations on the new SPDK threading library
- Designed and partially implemented a cooperative IO-thread scheduler with new SPDK APIs

**Supporting Scalable Fault-Tolerant Distributed** **Message Queue with Persistent Storage** [GitHub](https://github.com/mhxie/disque_protocol) (19Fall)
_Advisor: [Faisal Nawab](https://www.nawab.me/), CSE 214: Principles of Database Systems_
- Designed a distributed message queue framework with fault tolerance
- Implemented log-based mechanism to resolve the inter-broker failures

**A Ultra-low Latency QUIC-stack Acceleration Engine** (19Winter)
_Advisor: [Scott Beamer](https://scottbeamer.net/), CMPE 293: Programmable Hardware Accelerators_
- Conducted characterization of **QUIC** protocol and workload analysis
- Designed a **NetFPGA**-based acceleration engine

**Towards Single Round-Trip: An Efficient Metadata Offloading Mechanism for Tree-based Oblivious RAM** (19Winter)
_Advisor: Chen Qian, CMPE 253: Network Security_
- Designed a way of efficient metadata management based on ring **ORAM** and Information-theoretical Private-information-retrieval (ITPIR)
- Optimized the algorithm with multi-step bit-based accelerations

**Evaluating 100Gbps Flash Disaggregation on ARM SoC** [GitHub](https://github.com/mhxie/reflex4arm) [Paper](https://www.ssrc.ucsc.edu/media/pubs/89a276a7823f1ca45cb66c163f20dccc81bfa959.pdf) (2018 - 2019)
_Advisor: Heiner Litz and Chen Qian, Funding: CRSS, Broadcom & NSF_
- Developed a cross-platform networked storage stack in **C** using **SPDK** and **DPDK**, built with **Meson**
- Optimized **ARM** platform code at assembly level, achieving 2M IOPS

## Publication

1. Liu, Y., Shi, S., **Xie, M**., Litz H., & Qian, C. SMASH: Flexible, Fast, and Resource-efficient Placement and Lookup of Distributed Storage. In conference of the ACM special interest group for the computer systems performance evaluation community (SIGMETRICS '23).
2. Shi, S., Yu, Y., **Xie, M.**, Li X., Li, X., Zhang, Y. & Qian, C. Concury: A Fast and Light-weight Software Cloud **Load Balancer**. In conference of the ACM Symposium on Cloud Computing 2020 (SOCC '20).
3. **Xie, M.**, Qian, C., Litz, H. ReFlex4ARM: Supporting 100GbE Flash Storage Disaggregation on ARM SoC. OCP Future Technologies Symposium 2020. Poster session in San Jose, CA (OCP '20).
4. **Xie, M.**, Qian, C., Litz, H. (2019, August 4-6). Evaluating 100Gbps Flash Disaggregation on ARM SoC. Flash Memory Summit 2019. Poster session in Santa Clara, CA.