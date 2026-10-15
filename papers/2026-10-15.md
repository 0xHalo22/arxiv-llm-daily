# arxiv LLM daily — 2026-10-15

the 30 most recent papers from cs.CL and cs.AI.

### [Modeling and Understanding Neural Weights of Humanoid Policies with Diffusion](http://arxiv.org/abs/2610.20606v1)
_Huixuan Cheng, Bike Zhang, Shankar Sastry, Koushil Sreenath_ • 2026-10-14

Recent advances in robot learning have driven rapid progress in humanoid control, enabling increasingly agile behaviors in the real world. However, humanoid control networks are typically obtained through conventional training procedures, while comparatively little attention has been given to directly modeling the d...

### [Hierarchical Residual Policy Learning for Real-World Mobile Manipulation with Sparse Human Guidance](http://arxiv.org/abs/2610.20607v1)
_Zhefei Gong, Hefeifei Jiang, Zehao Wang, Jiachen Li_ • 2026-10-14

Mobile Manipulation (MoMa) is a cornerstone of autonomous robotic systems, yet real-world fine-tuning remains a formidable challenge because of high-dimensional action spaces and intricate coupling between heterogeneous modules. In this paper, we propose HiRe-MoMa (Hierarchical Residual Mobile Manipulation), a syste...

### [Co-Evolving Acting and Forecasting for Language Agents](http://arxiv.org/abs/2610.20597v1)
_Haofei Yu, Yixing Chen, Yining Zhao, Xuyan Ye, Yuxiang Liu, +4 more_ • 2026-10-14

Training language agents is bottlenecked by the high cost of long-horizon rollouts, yet standard agentic reinforcement learning (RL) learns only from a terminal scalar reward, leaving the supervision in intermediate steps largely unused. Prior work exploits this supervision through value targets that estimate per-st...

### [Your Transformer Is Secretly Elastic](http://arxiv.org/abs/2610.20588v1)
_Walter Simoncini, Dheeraj Varghese, Gertjan J. Burghouts, Cees G. M. Snoek_ • 2026-10-14

Scaling up transformers has produced models with broad capabilities, deployed across heterogeneous hardware and fluctuating workloads. Yet, model families offer only a few fixed sizes (e.g., S, B, L), forcing users to commit to a model based on hardware and latency constraints. This rigidity is often suboptimal unde...

### [Price of Anarchy of First-Price Auctions in Agentic Markets](http://arxiv.org/abs/2610.20587v1)
_Shubhendu Trivedi, Jacob Eisenstein, Alekh Agarwal, Ian Gemp, Michael Kaisers, +1 more_ • 2026-10-14

An agentic market is a decentralized serving-time market where AI agents bid to claim each user prompt. An agent's bid is based on its expected value for the prompt, which is the expectation of the reward for its response minus its inference costs. First-price auctions (FPAs), in which the highest bidder pays its bi...

### [Continuum Attention](http://arxiv.org/abs/2610.20586v1)
_Afshin Khadangi_ • 2026-10-14

We introduce Continuum Attention (CA), a causal Transformer attention operator that replaces discrete key and value lookup with integration over a continuous, piecewise linear memory curve. Each query induces an exponential relevance density along the curve. Integrating the density and interpolated values yields exa...

### [Player-1: Learning to Play from Synthetic Experience](http://arxiv.org/abs/2610.20584v1)
_Mingyu Ouyang, Yiran Wang, Siyuan Hu, Xingyilang Yin, Huiqiang Sun, +7 more_ • 2026-10-14

Computer-use agents have demonstrated strong capabilities in interpreting screens and executing keyboard and mouse actions. However, games, with their visually rich worlds and diverse mechanics, remain challenging and offer a demanding next step toward general digital control. Current game-agent learning pipelines o...

### [Latent Compaction with Test-Time Training](http://arxiv.org/abs/2610.20582v1)
_Yingfa Chen, Xingyu Shen, Chaojun Xiao, Xu Han_ • 2026-10-14

Long contexts enlarge key--value (KV) caches, increasing memory use and attention costs during generation. Compressing these caches must preserve information for unseen questions. We introduce **Latent Compaction**, which learns a compact document-specific cache through test-time training. We initialize cache entrie...

### [One Task, Many Interfaces: Simple Cross-Interface Consistency Training Improves LLM Agent Robustness](http://arxiv.org/abs/2610.20576v1)
_Artin Tajdini, Manpreet Kaur, Peng Qi_ • 2026-10-14

Post-training binds the competence of an LLM agent to the interface it was trained on. Semantics-preserving perturbations of that interface, such as renaming an action or changing the notation, leave the underlying task unchanged yet make the agent worse at it. Scoring each sample independently means interface rando...

### [Beyond LLM Judge: Mechanical Verification for Agentic Autoformalization](http://arxiv.org/abs/2610.20573v1)
_Anna Mei, Michael R. Douglas_ • 2026-10-14

We introduce a novel method for verifying Lean formalizations that goes beyond LLM-judged faithfulness. Unlike most verification methods, which rely on LLMs or trained models, our method combines LLM-based semantic review with mechanical numerical and vacuity checks, providing checkable feedback and detecting errors...

### [Recovering Reliable Supervision via Critique-Guided On-Policy Distillation](http://arxiv.org/abs/2610.20572v1)
_Kaixiang Zhao, Tianrun Yu, Shangzhe Li, Yuxiao Yang, Amanda Hughes, +2 more_ • 2026-10-14

On-policy distillation (OPD) trains a student model on its own rollouts with token-level supervision from a teacher, assuming that the teacher can reach a correct answer from any prefix the student writes. We call this property the recoverability of the teacher and show it fails on incorrect rollouts: the teacher fo...

### [Manacá-1B-Instruct-2: Reproducible Safety Alignment for a Native Brazilian-Portuguese LLM. Negative DPO Results, a Controlled Composition Scan, and a Silent Failure Mode of the LLM Judge](http://arxiv.org/abs/2610.20570v1)
_Bruno Leonardo Santos Menezes, Carlos Leonardo Souza Cardoso, Fabio André Machado Porto_ • 2026-10-14

Brazilian Portuguese remains underserved by open-source language models, and the few that are safety-aligned rarely document what did not work or validate comparisons with statistical significance. We present Manacá-1B-Instruct-2, the second-generation post-training alignment of Manacá-1B (1.72B parameters, trained...

### [Scaling Discovery Requires Forgetting](http://arxiv.org/abs/2610.20563v1)
_Shangyin Tan, Ben Zhou, Lakshya A Agrawal, Jialin Zhang, Yilin Chen, +6 more_ • 2026-10-14

Automated research with LLM agents has shown promising results in various domains. Through iterative refinement and scored verifiers, LLM agents are capable of discovering new ideas. There are different ways to scale automated research: let one agent iterate for longer, run several agents in parallel, or further let...

### [PhySGA: A Physics-Space Grounded Agentic Framework for Generalizable and Interactive 3D Composition](http://arxiv.org/abs/2610.20560v1)
_Weichen Lyu, Chong Xia, Mingyu Dong, Long Xu, Shengjun Zhang, +1 more_ • 2026-10-14

3D object composition is pivotal to digital content creation and robot simulation, while also serving as a critical testbed for physical intelligence in foundation models. Previous methods either leverage large language models to directly predict object coordinates, or utilize generative diffusion priors to synthesi...

### [PerSo: Investigating Facets of LLMs' Social Intelligence in Real-World Persuasion Scenarios](http://arxiv.org/abs/2610.20548v1)
_Ali Zamani, Soroush Esfahanian, Erfan Shahabi, Mohammad Taher Pilehvar, Azadeh Shakery, +1 more_ • 2026-10-14

Understanding the social intelligence of large language models (LLMs) is increasingly important for applications involving human-AI interaction and multi-agent environments. Social intelligence comprises two aspects: cognitive intelligence, the ability to infer others' mental states, and behavioral intelligence, the...

### [Detection of Potato Plant Leaf Diseases using Convolutional Neural Networks](http://arxiv.org/abs/2610.20544v1)
_Haimanot Bitew Alemayehu, Simachew Melaku Ayalew, Chilotie Desalew Mengesha, Ayisheshim Almaw Bogale, Anteneh Birhan Yenew, +1 more_ • 2026-10-14

Potato is an important food-security crop in Ethiopia, but its production is affected by foliar diseases, particularly early blight and late blight. This study develops a lightweight convolutional neural network (CNN) to classify potato leaves into three categories: healthy, early blight, and late blight. The propos...

### [PrismaCoder: Pushing the Boundaries of Open Multimodal Code Intelligence through Decomposed Rubric Synthesis](http://arxiv.org/abs/2610.20538v1)
_Qiushi Sun, Jingyang Gong, Yang Liu, Qiaosheng Chen, Zhangyue Yin, +12 more_ • 2026-10-14

Multimodal code intelligence connects the symbolic world of programs with the visual world their execution creates. Interest in this capability is burgeoning, as models are increasingly asked to produce charts, webpages, animations, and semi-structured documents. Recently, proprietary models have pushed far ahead, p...

### [ActiveEvidence: Decision-Focused Evidence Graphs with Verifiable Acquisition Gaps](http://arxiv.org/abs/2610.20532v1)
_Miaobo Hu, Shuhao Hu, Xiaobo Guo, Xin Wang, Bokun Wang, +3 more_ • 2026-10-14

A multimodal agent must decide whether visual evidence is worth acquiring, which candidate or resolution to query, and when further interaction can no longer change its decision. We study this problem under a strict free-metadata/paid-observation boundary, stochastic vector costs, and a frozen execution trace, and t...

### [The Wealth of Agents: Scaling Agentic AI Across Developers](http://arxiv.org/abs/2610.20518v1)
_Austin W. Hanjie, Carlos E. Jimenez, Zirui Wang, Karthik Narasimhan_ • 2026-10-14

Today's agentic systems are typically designed, built, and deployed by single developers with full control over all participating agents. While this simplifies development, it limits the potential scale of agentic systems. We study multi-developer agentic systems (MDAs) which enable developers to collaboratively bui...

### [VASPO: Self-Distillation with Privileged Value Estimation](http://arxiv.org/abs/2610.20516v1)
_Fei Wu, Zhenrong Zhang, Jianshu Zhang, Jun Du_ • 2026-10-14

On-policy self-distillation provides dense supervision for reasoning models via a privileged self-teacher. However, this supervision reflects local token preferences rather than the expected return of an unguided student continuation. Recent methods combine this signal with GRPO. They use GRPO for update directions...

### [VascuSR: Iterative Anatomy-Aware Diffusion for CT Super-Resolution](http://arxiv.org/abs/2610.20509v1)
_Hairong Ni, Jiahe Huang, Minghao Guo, Wojciech Matusik, Rose Yu_ • 2026-10-14

Generative super-resolution (SR) can recover sharp detail in computed tomography (CT) images from severely downsampled observations, but the missing high-frequency content is not uniquely determined by the low-resolution input. Consequently, visually plausible reconstructions may contain anatomically unsupported vas...

### [ReaDy: Recurrent States as Dynamic Context for Speculative Drafting in Hybrid Linear Attention Large Language Models](http://arxiv.org/abs/2610.20503v1)
_Bohan Sun, Zunhai Su, Xialie Zhuang, Jianjin Li, Ngai Wong, +1 more_ • 2026-10-14

Speculative decoding accelerates autoregressive generation by drafting multiple tokens per step, yet feature-based drafters rely on target hidden features whose contextual emphasis may not align with the needs of subsequent draft positions. Hybrid linear attention (HLA) models maintain compact recurrent states that...

### [Hindsight-Privileged RLVR: Single-Rollout Token Credit Without Group Sampling](http://arxiv.org/abs/2610.20497v1)
_Wei Chen, Yubing Wu, Zhou Xu, Haoyue Zhang, Delu Zeng, +7 more_ • 2026-10-14

Reinforcement learning with verifiable rewards (RLVR) trains language models from checked task outcomes, but assigning a terminal reward to individual reasoning tokens or actions remains difficult. Group-relative methods such as Group Relative Policy Optimization (GRPO) sample several attempts per prompt, but lose t...

### [Quantifying privacy risks in foundation model representations of brain MRI](http://arxiv.org/abs/2610.20494v1)
_Imen Bajar, Héber Hwang Arcolezi, Antoine Boutet, Carole Frindel, Mohamed Maouche_ • 2026-10-14

Pretrained representations are increasingly used to share and reuse information from medical images without exposing the original scans, but it is unclear how much patient-specific information these representations retain. We investigate this question for brain magnetic resonance imaging (MRI) by evaluating five fro...

### [Lost in Translation: Why Lower Bias Scores Don't Mean Fairer Models](http://arxiv.org/abs/2610.20479v1)
_Harsh Kumar_ • 2026-10-14

Bias audits of multilingual language models usually compare a model's average stereotype score in English with its average in another language and read the difference as a difference in fairness. We ask how much of that difference is noise. Auditing ten open models in eight languages, we measure how far scores move...

### [AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](http://arxiv.org/abs/2610.20474v1)
_Peidong Wang, Ying Chang, Zhiming Ma, Xiaocui Yang, Shi Feng, +6 more_ • 2026-10-14

Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks. Recursive self-improvement (RSI) offers a remedy, but embodied RSI methods either refine the harness around a frozen executor and so cannot add a missing motion, or train the executor on persistent failures without a...

### [SafeAdapt-Poker: Counterfactual Risk Calibration for Budgeted Adaptation under Opponent Shift](http://arxiv.org/abs/2610.20473v1)
_Miaobo Hu, Shuhao Hu, Xiaobo Guo, Xin Wang, Bokun Wang, +3 more_ • 2026-10-14

Opponent histories can mislead after behavioral shifts. SafeAdapt-Poker formulates budgeted adaptation under opponent shift as a dual-counterfactual sequential-control problem using only information available before each decision. At each decision the controller asks two distinct questions: what local downside a dev...

### [ChronoCulture: Evaluating Cultural Awareness Across Time in Large Language Models](http://arxiv.org/abs/2610.20472v1)
_Rusali Saha, Nitya Khurana, Ruihong Huang, Kuan-Hao Huang_ • 2026-10-14

Cultural attitudes and social norms evolve over time, yet most cultural benchmarks for large language models (LLMs) treat culture as a static attribute of a country or region. We introduce ChronoCulture, a benchmark of 10,360 temporal pairs built from longitudinal survey data across 72 countries. Each pair contains...

### [Selective Growing Q-Networks (SGQN): An Analysis of Adaptive Action Grids in Decoupled Q-Learning](http://arxiv.org/abs/2610.20463v1)
_Parham Nooranbakht, Seyed Mahdi Basiri Azad, Joschka Bödecker_ • 2026-10-14

Value-based Q-learning for continuous control can discretise the action space, but the resolution of the discretisation trades early exploration against final precision. Growing Q-Networks (GQN) grow the resolution uniformly from coarse to fine. We introduce Selective Growing Q-Networks (SGQN), which keeps decoupled...

### [Equal CER, Unequal Damage: Severity-Weighted Character Error Rate for OCR](http://arxiv.org/abs/2610.20461v1)
_Nguyen Nguyen, Yongyi Zang_ • 2026-10-14

Character Error Rate (CER), the standard metric for OCR and vision-language models (VLMs), charges a typo as much as a wrong name. We introduce semCER, which keeps CER's alignment and denominator and charges each grapheme edit a severity from an LLM judge, with no word segmentation. Normalized CER keeps the score of...

_snapshot taken at 2026-10-15T17:52:11+00:00_
