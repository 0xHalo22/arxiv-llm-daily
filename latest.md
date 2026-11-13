# arxiv LLM daily — 2026-11-13

the 30 most recent papers from cs.CL and cs.AI.

### [ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research](http://arxiv.org/abs/2611.17332v1)
_Jie Wang, Tong Zhu, JiaHao Kuang, Zhe Xu, Yunkai Chai, +6 more_ • 2026-11-12

Model architecture shapes the scaling behavior, training efficiency, and inference cost of LLMs, making it a central focus of both industry and academia. In industry, teams such as those behind DeepSeek, Qwen, and Kimi routinely introduce architectural innovations, yet public reports rarely document which ideas succ...

### [AgentSSL: Can MLE Agents Leverage Unlabeled Data?](http://arxiv.org/abs/2611.17323v1)
_Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun_ • 2026-11-12

Applying machine learning systems to new domains introduces bottlenecks in both labeled data acquisition and manual pipeline engineering. While recent MLE agents show promise in automating pipeline design, they have been studied almost exclusively in fully supervised settings, leaving them untested in realistic regi...

### [Learning When Diffusion Language Models Should Regenerate](http://arxiv.org/abs/2611.17320v1)
_Minhae Oh, Jeonghye Kim, Jinwoo Koo, Yeongoon Kim, Jimin Seo, +2 more_ • 2026-11-12

Remasking allows diffusion language models to revisit generated text, but effective correction requires knowing when and what to revise. Our diagnosis on Sudoku reveals two gaps. Hidden states contain error information that token confidence does not reliably expose, and remasking an isolated error usually reproduces...

### [CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation](http://arxiv.org/abs/2611.17316v1)
_Peiwen Li, Harshit Verma, Sophia Zhou, Haiwen Wang, Ngoc Bui, +4 more_ • 2026-11-12

Coding agents tackle successive tasks on an evolving repository, carrying forward edits and writing memory before the next task is known. Selecting memory for unknown next tasks requires balancing future usefulness against the costs of writing and reading it. The actor must also decide when acting on available memor...

### [Linking Rapid Learning to Compositional Structure in Neural Networks: Evidence from Additive Analogies in Meta-Learned Parameter Spaces](http://arxiv.org/abs/2611.17314v1)
_Abigail L. Tenenbaum, R. Thomas McCoy_ • 2026-11-12

Humans can learn rapidly from limited experience, while neural networks typically require extensive training. In this work, we investigate what properties of a neural network can enable it to learn rapidly. We study neural networks that have been optimized via meta-learning, a technique that exposes a network to man...

### [Sketching Language Models for Context Attribution](http://arxiv.org/abs/2611.17313v1)
_Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, Felix Zhou_ • 2026-11-12

Context attribution asks how removing parts of a prompt changes a language model's output. We study leave-one-out (LOO) attribution for a prompt of $n$ tokens and a fixed measurement function. Computing all LOO values directly requires $n$ model evaluations. Under a stability assumption, our algorithm estimates all...

### [Classical Energies Learn to Reason 1,000x Faster than Looped Models](http://arxiv.org/abs/2611.17309v1)
_Benjamin Hoover, Hugh Blayney, James C. R. Whittington_ • 2026-11-12

Looped models have emerged as a prominent paradigm for reasoning, with successes on simple reasoning puzzles such as Sudoku-Extreme and Maze-Unique. However, these models can be unstable, slow to train, and use many parameters and FLOPs to solve simple puzzles. Descent on an energy not only mitigates these issues bu...

### [Consistent Video-to-Video Translation via Explicit Correspondences](http://arxiv.org/abs/2611.17298v1)
_Gaurav Parmar, Zhengqi Li, Richard Zhang, Jun-Yan Zhu, Srinivasa Narasimhan, +2 more_ • 2026-11-12

Interactive video-to-video applications require real-time generation while maintaining long-range temporal consistency. However, recent methods achieve speed by restricting attention to a fixed-length causal window. This limits long-range consistency whenever relevant history falls outside the context window. To add...

### [Goal Encoding in LLMs](http://arxiv.org/abs/2611.17297v1)
_Arnab Sen Sharma, Eric Todd, Sheridan Feucht, Andy Arditi, Rohit Gandikota, +5 more_ • 2026-11-12

We investigate whether and how LLMs encode goals: internal neural representations that precede and guide action, and that are flexible enough to be realized through many different execution paths. We construct a coding setting with multiple sub-tasks that allows us to evaluate goal-seeking behavior and the selection...

### [Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon](http://arxiv.org/abs/2611.17294v1)
_Haozhe Wang, Lina Chen, Fanqi Wan, Qi Han, Yinmin Zhang, +3 more_ • 2026-11-12

On-device inference requires kernels that make effective use of local accelerators. Efficient training and evaluation of models that generate Apple Metal kernels benefit from native macOS tools and concurrent agent sessions. These sessions alternate between model requests, development commands, and GPU execution, le...

### [Negative-Only Policy Optimization for One-Sided Verifiable Rewards](http://arxiv.org/abs/2611.17287v1)
_Jiacheng Xu, Shuo He, Fuxiang Zhang, Chaojie Wang, Bo An_ • 2026-11-12

Reinforcement learning with verifiable rewards (RLVR) typically relies on a verifier that can reliably judge whether sampled solutions are correct. However, in many realistic settings, complete verification is generally unavailable, while cheap checks can only falsify failures. We formalize this regime as one-sided...

### [Synthesis Smuggling: Maliciously Hiding Inferred Personal Attributes in LLM Outputs](http://arxiv.org/abs/2611.17280v1)
_Gautam Galada, Supreeth Shastri, Sagnik Ray Choudhury_ • 2026-11-12

We propose Synthesis Smuggling, a novel threat model in which an adversarial LLM infers sensitive information about a user from routine assistance-seeking interactions and steganographically encodes that into innocuous-looking model-generated content. The user may then unknowingly transmit that information by sharin...

### [LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds](http://arxiv.org/abs/2611.17267v1)
_Pengcheng Zhou, Xuanyu Liu, Yanchen Yin, Tianjie Ju, Bobo Li, +4 more_ • 2026-11-12

We introduce GeoWorld, a controllable and continuously evolving geographic environment platform for LLM agents, and LiveGeo, a benchmark for evaluating reliable decision-making in real-world geographic environments using GeoWorld. Unlike existing evaluations that largely reason and plan over fixed geographic states,...

### [Ballad: Bandit-Based LLM Routing for Automated Heuristic Discovery](http://arxiv.org/abs/2611.17241v1)
_Samidha Verma, Ankit Anand, Sayan Ranu_ • 2026-11-12

Modern automated heuristic discovery (AHD) systems increasingly rival hand-crafted heuristics by leveraging Large Language Models (LLMs) to iteratively mutate and refine solutions. A natural assumption is that more powerful and more expensive models consistently yield better heuristics. We challenge this empirically...

### [When Both Sides Adapt: The Challenges of Evaluating Interactive LLM Systems](http://arxiv.org/abs/2611.17239v1)
_Hannah Li_ • 2026-11-12

In interactive systems where users engage with LLMs, users are adaptive and, after observing LLM responses, can change their prompting strategy, as well as the type and difficulty of subsequent tasks. Thus model responses can influence the set of prompts on which the model is subsequently evaluated. We study the imp...

### [Al-Ghasali: A Computational Framework for Simulating Islamic Jurisprudential Rulings via Finite State Automata and Large Language Models](http://arxiv.org/abs/2611.17235v1)
_Elnaserledinellah Mahmoud Abdelwahab_ • 2026-11-12

This paper presents Al Ghasali, a computational framework designed to formalize and simulate Islamic jurisprudential (Fiqh) rulings. Building upon recent set theoretic formalizations of al sabr wa al Taqsim that extract minimal operational rules as simple Horn clause logical programs, this work proves that the seman...

### [Scalable Conversational Assessment: Chat-Based Exams with a Two-Agent LLM Pipeline](http://arxiv.org/abs/2611.17220v1)
_Geoffrey Challen, Craig Zilles_ • 2026-11-12

Oral exams are compelling because (1) students can be asked to provide their reasoning for an answer and (2) their interactive nature permits follow-up questions to resolve ambiguous answers. But oral exams scale poorly. In this paper, we present scalable conversational assessment, an LLM-based system that conducts...

### [Introducing Feedback Delays to Non-Delayed Adversarial MDPs: Optimal $\sqrt S$ and $\sqrt K$ Dependencies in Tabular and Linear AMDPs](http://arxiv.org/abs/2611.17214v1)
_Aarush Kulkarni, Khang Nguyen, William Chang, Yan Dai_ • 2026-11-12

We study regret minimization in episodic Adversarial Markov Decision Processes (AMDPs) with unknown transitions and bandit feedback. In tabular AMDPs with $S$ states, $A$ actions, and horizon $H$, the best known $K$-episode regret is $\tilde O(HS\sqrt{AK})$, whose $\sqrt S$ gap to the $Ω(H\sqrt{SAK})$ lower bound ha...

### [MALNISI-Infused Graph Construction and Weighted Contrastive Loss based GAT for Unsupervised Representation Learning in HSI](http://arxiv.org/abs/2611.17199v1)
_Soumi Sarkar, Subhadip Boral, Sarbani Palit, Ashish Ghosh_ • 2026-11-12

Hyperspectral images (HSI) possess discriminating spectral characteristics with respect to land utilization due to high-dimensional information. Recently, unsupervised representation learning using graph neural networks has unveiled these utilization-specific complex spectral relations. This article has three main c...

### [Maximizing Capacity Utilization of LoRA Adapters for Mitigating the Learning-Forgetting Trade-off](http://arxiv.org/abs/2611.17191v1)
_Tomohiro Sawada, Kartik Goyal_ • 2026-11-12

Low-Rank Adaptation (LoRA) often underperforms full fine-tuning, especially in heterogeneous and continual-learning settings in which substantial forgetting occurs. In general, it suffers from an undesirable learning-forgetting trade-off across diverse fine-tuning settings. We identify a potential contributor: LoRA...

### [Cortex-FL: Agent-Mediated Collaboration for Federated Learning](http://arxiv.org/abs/2611.17186v1)
_Rui Sun, Jinfeng Peng, Zehua Cheng, Jiahao Sun, Zhipeng Wang_ • 2026-11-12

Federated learning (FL) enables independent data owners to train models collaboratively without centralizing raw data. However, identifying collaborators, preparing training tasks, and coordinating execution and incentives hinder its practical adoption by organizations without specialized expertise. We present Corte...

### [Parsed, Plausible, Wrong: Output Format Controls Silent Errors in Small-Model Semantic Parsing](http://arxiv.org/abs/2611.17169v1)
_Umar Ahmed, Maxim Dunaev, Mohammad Nour Al Awad, Sergey Ivanov, Ivan Khodnenko_ • 2026-11-12

A small fine-tuned parser that emits a well-formed but wrong tree fails silently: nothing downstream can tell. We ask whether the output format, a free design choice, controls how often this happens. On the PIZZA ordering benchmark we fine-tune two sub-billion models (Qwen3.5-0.8B and LFM2.5-350M) with LoRA on six l...

### [Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents](http://arxiv.org/abs/2611.17167v1)
_Haochen Liu, Qianhao Zhu, Zixuan Wang, Dingming Li, Tongbo Chen, +5 more_ • 2026-11-12

Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score every action to teach a policy with reinforcement learning. Prior work has studied them mainly as actors, judging the...

### [Cited but Unused: Parametric Provenance in Retrieval-Augmented Generation](http://arxiv.org/abs/2611.17161v1)
_Tanzeel Abbas, Tehseen Zia, David Windridge_ • 2026-11-12

Retrieval-augmented generation systems attach citations to attribute claims to their sources. These citations frequently misstate provenance, and standard verification cannot detect this. We measure provenance by counterfactual value substitution: a fact in the retrieved passages is replaced with a false variant and...

### [Parameter-Efficient Conciseness Adaptation: Differentiable Length Control for Concise Clinical Reasoning in Smaller Language Models](http://arxiv.org/abs/2611.17128v1)
_Tanzeel Abbas, Ahmad Kamran Malik, Nafees Qamar, Sana Liaqat_ • 2026-11-12

Smaller language models (SLMs) make it feasible to deploy clinical natural language processing where large proprietary models are too costly, and parameter-efficient fine-tuning allows them to be specialised on commodity hardware. One obstacle persists after training: on medical tasks these models answer at far grea...

### [CapLite: Prompt-Injection Defense for Small Language Model Agents without Model-Written Security Artifacts](http://arxiv.org/abs/2611.17115v1)
_Zimo Xu, Wenzhuo Liu, Hideki Nakayama_ • 2026-11-12

Enforcement defenses against prompt injection, such as CaMeL, Progent, IPIGuard and DRIFT, ask the agent's own model to write a security artifact (a program, a privilege policy, a dependency graph or a constraint list) that code then enforces. We ask whether small language model (SLM) agents can be trusted to write...

### [Designing Institutions for Autonomous AI](http://arxiv.org/abs/2611.17114v1)
_Petter Törnberg_ • 2026-11-12

As autonomous AI agents increasingly interact in persistent populations, their collective capabilities and alignment depend not only on individual models, but also on the institutions governing their interactions. Yet AI research has largely focused on individual agents. In this Perspective, we argue that institutio...

### [SALA: Semantically Aligned Latent Actions Enable Dual-Axis Scaling of Embodied Foundation Models](http://arxiv.org/abs/2611.17110v1)
_Jiachun Jin, Zetong Zhou, Haonan Wang, Xiao Yang, Jun Zhu, +1 more_ • 2026-11-12

Embodied foundation models hinge on diverse robot interaction data, which are costly to collect. Egocentric human videos offer a complementary source of experience, and latent action models (LAMs) provide a popular means of leveraging these videos for policy supervision. Compared with world-action models (WAMs), LAM...

### [LazyWeights: Decode-on-Demand Edge LLMs](http://arxiv.org/abs/2611.17108v1)
_Arnab Sanyal, Gourav Datta, Sandeep P. Chinchali_ • 2026-11-12

Memory decides which LLMs an edge device runs, and how fast: capacity on a $4$ GB Jetson Nano, bandwidth on an $8$ GB Jetson Orin Nano Super. Deployed formats (GPTQ, AWQ, $\texttt{llama.cpp}$'s K- and I-quants) spend equal bits on every integer code of a matrix, although the codes are far from uniform. $\texttt{Lazy...

### [Disentangling Spurious Correlations: How IRM Handles Diverse Shortcuts in Text Classification](http://arxiv.org/abs/2611.17107v1)
_Paul Grunenwald, Benoît Crabbé, Guillaume Wisniewski, Pirmin Lemberger_ • 2026-11-12

In NLP, models trained via Empirical Risk Minimization (ERM) often exploit spurious correlations, such as dialectal markers, at the expense of robust linguistic features, thereby degrading their out-of-distribution (OOD) generalization. Invariant Risk Minimization (IRM) aims to suppress such shortcuts by identifying...

_snapshot taken at 2026-11-13T20:38:36+00:00_
