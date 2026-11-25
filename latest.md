# arxiv LLM daily — 2026-11-25

the 30 most recent papers from cs.CL and cs.AI.

### [OmniAct: One Policy, One Million Embodiments](http://arxiv.org/abs/2611.33158v1)
_Xiang Fan, Yuheng Wang, Jiayuan Yan, Bohan Fang, Wisdom Oluchi Ikezogwo, +5 more_ • 2026-11-24

A single policy that controls diverse robots must not only transfer task knowledge across embodiments, but also adapt its behavior to each robot's capabilities. Existing approaches facilitate transfer through shared action representations, but these representations do not necessarily capture how differences in robot...

### [DiaCap: Jointly Learning Who Speaks When for Audiovisual Dialogue Captioning](http://arxiv.org/abs/2611.33153v1)
_Binfei Ji, Zhiwen Cao, Anqi Yang, Prem Seetharaman, Shuo Yang, +3 more_ • 2026-11-24

We present DiaCap, an audiovisual LLM for comprehensive dialogue captioning, which produces the transcript, timestamps, and a visual description of the speaker for every utterance in a video. Considering that utterance timing and audiovisual diarization are tightly coupled, DiaCap unifies the tasks in a single model...

### [CoT-Proxy: Cross-Format Transfer for Distilling Long-Horizon Policies](http://arxiv.org/abs/2611.33148v1)
_Dawid J. Kopiczko, Tijmen Blankevoort, Yuki M. Asano_ • 2026-11-24

Reasoning models become long-horizon agents through reinforcement learning or, more cheaply, through fine-tuning on a stronger teacher's trajectories, which contain the teacher's chain-of-thought as well as its actions. The standard fine-tuning approach imitates both, yet the strongest teachers are closed models who...

### [BriConstrain: Geometrically Constrained Decoding for Autoregressive Brick Assembly Generation](http://arxiv.org/abs/2611.33135v1)
_Nadav Magar, Amir Hertz, Ariel Shamir, Or Patashnik_ • 2026-11-24

Language models can generate LEGO$^\circledR$ assemblies from text, but their builds often contain parts that collide or attach to nothing. The usual approach of rejecting and resampling invalid placements discards decoded tokens without guaranteeing a valid build. We present BriConstrain, a constrained decoding met...

### [A Bias in Disguise: Tiny Gradient Edits Stop a Small Language Model's Thinking Loops and Complement a Frontier Model's Weight Edit](http://arxiv.org/abs/2611.33133v1)
_Hussamuddin Syed_ • 2026-11-24

Qwen3.5-0.8B rarely finishes reasoning in thinking mode: at a 4,096-token budget only 1 or 2 of 500 MATH-500 answers close their think block (two seeds), and accuracy is 15.4%. A recent demonstration had GPT-6 Astra edit 131,072 of the model's weights without gradients and reported MATH-500 rising from 7.9% to 48.1%...

### [SAG-Mem-1.0 Technical Report](http://arxiv.org/abs/2611.33124v1)
_Yuchao Wu, XingCheng Liang, Xuanze Wang, Yini Huang, Yue Wu_ • 2026-11-24

Long-term conversational memory requires retrieving complementary facts scattered across dialogue sessions, including intermediate evidence with limited similarity to the original question. Existing approaches often rely on derived memory representations or persistent relational structures, introducing construction...

### [MetaFORGE: A Meta-Learning Framework for Harness Optimization in Automated Code Generation for Parallel Computing](http://arxiv.org/abs/2611.33119v1)
_Scott Piersall, Yang Gao, Shenyang Liu, Liqiang Wang_ • 2026-11-24

Large language models (LLMs) can generate parallel programs, but their correctness and performance depend strongly on the instructions that guide generation. We present \textsc{MetaFORGE}, an execution-grounded meta-learning framework that iteratively optimizes persistent natural-language skill specifications for MP...

### [Draft Calibration for Speculative Decoding: Accelerating LLM Serving by Matching Draft and Target Distributions](http://arxiv.org/abs/2611.33111v1)
_Yuxing Liu, Wei Zuo, Walid Krichene, Tong Zhang, Li Zhang_ • 2026-11-24

Speculative decoding accelerates large language model (LLM) inference by employing a lightweight draft model to propose draft tokens and allowing the target model to verify the new tokens in parallel to improve inference-time compute utilization. The speedup relies on the acceptance probability of draft tokens in ta...

### [Temporal Conditioning for Human Behavioral Cloning in Chess](http://arxiv.org/abs/2611.33106v1)
_Victor Dziwniel, Tianxiang Lu_ • 2026-11-24

Behavioral cloning models in chess typically predict human moves from board states while ignoring temporal inputs such as the remaining clock. However, time pressure is a major determinant of human decision-making quality, and temporal state is a missing dimension of human behavioral modeling. This paper introduces...

### [Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance](http://arxiv.org/abs/2611.33098v1)
_Lingwei Gu, Jimmy Lin_ • 2026-11-24

Agents built on frontier language models are expensive. At every step, the frontier model re-reads its entire context and executes every subtask regardless of its difficulty. This paper explores the simple thesis that much of this cost can be removed by delegating easy subtasks to a small language model, or SLM, tha...

### [EventDiffusion: Learning Native Event Stream Distribution from Videos](http://arxiv.org/abs/2611.33096v1)
_Karthik Sundar Senthilkumar, Christopher Thirgood, Simon Hadfield_ • 2026-11-24

Event cameras capture asynchronous brightness changes at high temporal resolution, but scarce recordings constrain data-driven research. Sparse RGB observations cannot uniquely determine intervening events since identical frames may correspond to streams with different activity, polarities, and timing. Existing simu...

### [AIChipBench: Benchmarking LLM Agents for Automated AI Accelerator Design](http://arxiv.org/abs/2611.33093v1)
_Guangyuan Wang, Chengran Li, Minchen Luo, Jichen Feng, Mengdi Wang, +1 more_ • 2026-11-24

A language-model decoder carries state between decoding steps, and in hardware a wrong state update can leave the current token correct and corrupt the output several tokens later, so a design can pass output tests and still be wrong. AIChipBench asks what LLM coding agents need to build such hardware correctly. Age...

### [Uncertainty-Aware Candidate Generation for Entity Linking in Cyber Threat Intelligence](http://arxiv.org/abs/2611.33086v1)
_Nasser Alkhulaifi, Direnc Pekaslan, Christian Wagner_ • 2026-11-24

Entity Resolution (ER) pipelines often collapse ambiguity into early hard decisions: upstream Named Entity Recognition (NER) selects a single span and type, and downstream Entity Linking (EL) treats that choice as ground truth. This discards valuable information about the ambiguity of the underlying data (e.g., span...

### [FOL-Proof: Verifying LLM Text-to-Logic Translations via Deterministic Semantics](http://arxiv.org/abs/2611.33078v1)
_Yisrael Clark, Guy Katz_ • 2026-11-24

Large Language Models (LLMs) are increasingly used to translate natural-language statements into first-order logic (FOL) to improve reasoning. However, LLMs are prone to errors, and so a semantically unfaithful FOL formula could corrupt downstream reasoning. We present FOL-Proof, a semantic firewall pipeline that va...

### [On the Creation of Object-Centric Event Logs from Patient Journeys](http://arxiv.org/abs/2611.33074v1)
_Saimir Bala, Neven Borak, Maximilian König, Anjo Seidel, Zeinab Soleimani, +4 more_ • 2026-11-24

Interactions between patients and health systems as well as conditions that individuals experience during a disease are represented in patient journeys. Therefore, patient journeys are important assets to investigate how care is being provided, and how health systems can be designed to better suit the needs of patie...

### [Auditing the Judge: Human-Derived Bias Discovery, Quantification, and Mitigation in LLM Judges](http://arxiv.org/abs/2611.33065v1)
_Hamin Koo, Chanjoo Jung, Fangzhao Wu, Jaehyung Kim_ • 2026-11-24

While Large Language Models (LLMs) are increasingly deployed as automated evaluators in evaluation and training pipelines, their judgements are often affected by systematic biases that conflict with human preferences. Although prior work has identified various biases and proposed methods for detecting and mitigating...

### [ClusterVAD: Threshold-Free Unsupervised Voice Activity Detection with Pre-Trained Neural Representations](http://arxiv.org/abs/2611.33059v1)
_Karl El Hajal, Mathew Magimai. -Doss_ • 2026-11-24

Voice activity detection (VAD) is one of the first steps in speech processing pipelines, from transcription and diarization to speech language models. Supervised detectors need labelled data and inherit the domain and annotation conventions of their training corpora. Existing unsupervised detectors rely on hand-craf...

### [Worth the Wait? How Response Time and Streaming Shape Judgments of Generative AI Answers and Chatbot Engagement](http://arxiv.org/abs/2611.33050v1)
_Zihan Chen, Di Zhu, Lei Nico Zheng_ • 2026-11-24

Answers from generative AI chatbots built on large language models (LLMs) now arrive at very different speeds: reasoning models deliberate before replying, while response caches can return a stored answer at once. Blind preference votes, which rank these models, are read as judgments of their text, and if delivery m...

### [Latent Merger: Latent-Space Composition of Hypernetwork-Generated LoRAs](http://arxiv.org/abs/2611.33048v1)
_Yanlai Yang, Minki Kang, Divyam Madaan, Sung Ju Hwang, Mengye Ren_ • 2026-11-24

Recent work proposes hypernetworks that convert a document into a low-rank parameter update (LoRA) in a single forward pass, enabling fast injection of new knowledge into a frozen LLM. However, storing separate LoRA adapters for each document can be unsustainable in streaming settings. In this paper, we study the pr...

### [Towards Realistic Evaluation of Uncertainty Quantification for LLM-Based Recommender Systems](http://arxiv.org/abs/2611.33036v1)
_Hao Wu, Sipeng Chen, Weikai Li, Tianyi Chen, Qiancheng Yang, +4 more_ • 2026-11-24

Large language models (LLMs) provide a flexible interface for recommendation systems. However, their issued rankings require reliable instance-level uncertainty monitoring. In this scenario, comparing uncertainty quantification (UQ) methods becomes challenging because LLM rankers lack a standard item-classification...

### [Hybrid AI for AI-Native RAN Control: A Functional Perspective](http://arxiv.org/abs/2611.33035v1)
_Sabrine Aroua, Osama Arouk, Pegah Alizadeh_ • 2026-11-24

AI-native radio access network (RAN) control involves interdependent decisions across network entities, protocol layers, and timescales. Understanding how AI and conventional methods can jointly support these decisions requires a common basis for comparing their functional roles. This survey introduces a technique-a...

### [Can a Frontier LLM Repair a Quantized Network by Tool-Free Weight-Space Programming?](http://arxiv.org/abs/2611.33031v1)
_Steffen Urban_ • 2026-11-24

We give four large language models (LLMs) of the Claude family the complete weights of a 20k-parameter CIFAR-10 CNN as text and ask them to produce a 4-bit network without tools, data or the ability to run inference. Standard round-to-nearest (RTN) quantization to 4 bit lowers the test accuracy from 81.4% to 60.4%....

### [SALSA: Sampling Adversarial Suffixes from Learned Distributions for LLM Safety Assessment](http://arxiv.org/abs/2611.33030v1)
_Shivank Rajput, Himanshu Singh, A. V. Subramanyam_ • 2026-11-24

Large language models (LLMs) remain vulnerable to jailbreak attacks, where adversaries append optimized suffixes to otherwise benign looking prompts to bypass safety alignment. Existing optimization-based GCG-style attacks can be effective, but they are expensive at inference time, and suffer from poor transfer. We...

### [RecordRoute: Auditing Agent Failures with Localization-Guided Diagnosis](http://arxiv.org/abs/2611.33022v1)
_Yifan Duan, Lihuan Li, Chao Xue, Siyuan Zheng, Du Yin, +1 more_ • 2026-11-24

Auditing failed agent executions requires identifying the responsible actor, the earliest decisive step, and the error mode. Representative supervised methods either focus on step localization or predict multiple attribution targets from shared trajectory representations. These methods do not use the localization re...

### [Can LLM Judges Catch Unsafe Clinical Actions? A Fault-Injection Study](http://arxiv.org/abs/2611.33012v1)
_Neda Ghafouri_ • 2026-11-24

As clinical AI agents begin to interact with electronic health records (EHRs), large language models (LLMs) are increasingly used to evaluate their actions. But how reliably can these judges recognize clinically dangerous mistakes, especially when an agent appears to have completed its task successfully? We investig...

### [Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies](http://arxiv.org/abs/2611.33010v1)
_Xuanchen Liu, Hejun Zhang, Boxuan Dong, Ying Wu, Heshuai Li, +3 more_ • 2026-11-24

Can a simple mirror expose the limitations of today's robotic manipulation policies? Inspired by the mirror self-recognition test in animal cognition, we investigate whether robot policies can reliably manipulate physical objects in scenes containing their reflections. We introduce RoboDojo-Mirror, a benchmark built...

### [Leto: Utility-Centric Agent Memory](http://arxiv.org/abs/2611.33005v1)
_Shuguang Chen, Salman Paracha_ • 2026-11-24

Large language model (LLM) agents rely on external memory to retain and reuse information across interactions. Existing memory systems treat memory as a record of the past and evaluate it by fidelity to the conversation. However, the value of memory lies in whether it improves the agent's response. A memory system d...

### [LEGOSpec: A Composable and Efficient Framework for Speculative Draft Design and Training](http://arxiv.org/abs/2611.33004v1)
_Hanzhen Wang, Jiaming Xu, Guohao Dai_ • 2026-11-24

Speculative decoding accelerates large language model (LLM) generation using a lightweight draft. Existing methods evaluate complete recipes under different training configurations, leaving component effects, interactions, and composition benefits unclear. Therefore, we present LEGOSpec, a composable framework for s...

### [One, No One and One Hundred Thousand CTs: Testing Anatomical Control in Text-to-CT Generation](http://arxiv.org/abs/2611.33003v1)
_Francesca Pia Panaccione, Eugenio Lomurno, Matteo Matteucci_ • 2026-11-24

Recent advances in deep learning and the public availability of computed tomography (CT) datasets with paired reports have enabled many Text-to-CT generators. However, their evaluations almost always differ in preprocessing and metrics, which hinders comparison. Moreover, their protocols almost never test how editin...

### [Modelling Billingual Learning Through LLM Training: A Critical-Period Exploration](http://arxiv.org/abs/2611.32997v1)
_Uriel Benymon, Tristan Whipps, Armita Ghobadi_ • 2026-11-24

Critical-period accounts of second-language (L2) acquisition suggest that the ability to learn a new language may depend on how easily previously acquired first-language (L1) knowledge can be modified. This exploratory computational study extends a neural language-model approach to critical period effects by examini...

_snapshot taken at 2026-11-25T22:44:03+00:00_
