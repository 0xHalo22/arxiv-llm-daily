# arxiv LLM daily — 2026-10-19

the 30 most recent papers from cs.CL and cs.AI.

### [Rethinking the design space of Vanilla Pixel Diffusion Transformers](http://arxiv.org/abs/2610.23854v1)
_Soumik Mukhopadhyay, Long Mai, Abhinav Shrivastava, Aniruddha Mahapatra_ • 2026-10-16

Pixel-space diffusion models have recently re-emerged as a compelling alternative to latent diffusion, avoiding the lossy latent bottleneck and separately trained autoencoder. JiT shows that a vanilla diffusion transformer can generate directly in pixel space by replacing the commonly used velocity prediction ($\bol...

### [Behavioral Couplings: From Formation to Behavioral Emergence in Language Models](http://arxiv.org/abs/2610.23847v1)
_Dongyoon Hahm, Woogyeol Jin, Dennis Wei, Yi Zhou, Nathalie Baracaldo, +1 more_ • 2026-10-16

Fine-tuning large language models (LLMs) can induce behaviors beyond those explicitly targeted. For example, training a model to respond more warmly can make it more sycophantic, and training it to write insecure code can cause broad misalignment on prompts unrelated to coding. We refer to a relationship between beh...

### [AI-Driven Reproducibility and Analytical Robustness in Scientific Discovery](http://arxiv.org/abs/2610.23845v1)
_Shicheng Liu, Krista Opsahl-Ong, Andrew Drozdov, Julian Killingback, Arnav Singhvi, +4 more_ • 2026-10-16

Reproducible and analytically robust research findings are essential to scientific progress, but evaluating these properties typically requires costly manual effort. We investigate whether LLM agents can help automate reproduction and robustness analysis, using a medical case study grounded in the Surveillance, Epid...

### [DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses](http://arxiv.org/abs/2610.23839v1)
_Jianyuan Zhong, Chenwei Wu, Zhaochen Yu, Xixian Jiang, Xuewei Li, +19 more_ • 2026-10-16

Scientific discovery requires developing worthwhile hypotheses into practical investigations, yet learning from this evolving research process remains challenging. We introduce an operational definition of valuable and testable research hypotheses: evidence-grounded claims about consequential uncertainties, coupled...

### [Beyond the Answer: Student-Conditioned Trace Construction for Reasoning Distillation](http://arxiv.org/abs/2610.23831v1)
_Shaoang Li, Yanhang Shi, Yufei Li, Mingfu Liang, Frank Shyu, +4 more_ • 2026-10-16

A reasoning trace can accompany a correct answer without providing effective supervision for a particular student. We study how to construct traces that improve learning beyond answer-only supervision by considering both their intermediate content and their accessibility to the target learner. We introduce ReDiST, a...

### [Self-Building Labs](http://arxiv.org/abs/2610.23826v1)
_Jiaru Bai, Yuchi Zhao, Han Hao, Miroslav Bogdanovic, Yang Cao, +2 more_ • 2026-10-16

Self-driving laboratories (SDLs) accelerate scientific discovery by automating experimental execution and optimization. AI agents can increasingly propose new experiments, but existing SDLs can only run the procedures they were built for. Adapting them to a new experiment still takes extensive manual engineering, wh...

### [Acceptance Is Not Speed: Length Inflation in Training-Free Lossy Speculative Decoding](http://arxiv.org/abs/2610.23818v1)
_Chiatzen Wang, Bill Xu, Haochen Gu, Hongyang Zhang_ • 2026-10-16

Speculative decoding typically characterizes speedup by draft tokens accepted per verification round. Lossless verification preserves the target model's output distribution and thus expected completion length, making this metric a meaningful efficiency proxy. Relaxed (lossy) verification accepts tokens that lossless...

### [Steering beyond Language: Improving Multilingual Training-Free Text Embeddings via Paired-Residual Subspace Removal](http://arxiv.org/abs/2610.23807v1)
_Ailiang Lin, Zhuoyun Li, Yusong Wang, Keyu Mao, Kotaro Funakoshi, +1 more_ • 2026-10-16

While deriving text embeddings directly from frozen LLMs has emerged as a promising direction, existing methods focus almost exclusively on English, leaving multilingual settings largely unexplored. In this work, we present the first systematic study of multilingual training-free text embeddings in LLMs. Our analysi...

### [Beyond SAEs: Consistent Concept Discovery with Sparse Coding](http://arxiv.org/abs/2610.23801v1)
_Jinho Choi, Hyesu Lim, Jaegul Choo, Steffen Schneider_ • 2026-10-16

Sparse autoencoders (SAEs) explain foundation model representations by decomposing activations into sparse combinations of learned dictionary atoms. However, the learned dictionaries can vary across training runs, limiting the reliability and reproducibility of SAE-based analyses. We propose Consistent Sparse Dictio...

### [FuTransformer: FP8 prefill and INT4 decode for Llama-style inference on Hopper](http://arxiv.org/abs/2610.23796v1)
_Wei Wang_ • 2026-10-16

Transformer prefill reuses weights across tokens and is dominated by matrix multiplication and activation data movement; single-token decode has limited reuse and is dominated by weight and KV-cache reads. We present FUTRANSFORMER, a CUDA implementation of a Llama-style Transformer block for NVIDIA Hopper GPUs. It a...

### [DrugHarness: An Evolvable Agent Harness for Computational Drug Discovery](http://arxiv.org/abs/2610.23791v1)
_Yuxing Chen, Zhisheng Zhang, Cheng Tang, Wei Li, Minghui Zhang, +18 more_ • 2026-10-16

Computational drug discovery requires agents to compose scientific operations and adapt to changing evidence and constraints. Here we introduce DrugHarness, an evolvable agent harness coupling composable scientific execution with conditional skill induction. Its environment integrates over 80 scientific operations,...

### [DLite: History-free Speculative Decoding for Agentic AI](http://arxiv.org/abs/2610.23787v1)
_Jiaming Xu, Hanzhen Wang, Tianlang Zhao, Jiewen Xiao, Chengze Yuan, +5 more_ • 2026-10-16

Speculative decoding has become a mainstream technique for accelerating large language model (LLM) inference by using a lightweight draft model to generate candidate tokens that are subsequently verified by the target model. However, agentic workloads introduce long and continuously evolving contexts and frequent mu...

### [VocalGrad: Evaluating Acoustic Perception in Audio Language Models](http://arxiv.org/abs/2610.23745v1)
_Koki Ryu, Hitomi Yanaka_ • 2026-10-16

Recent large audio language models (LALMs) have extended their capabilities beyond lexical speech understanding to tasks requiring paralinguistic and non-linguistic audio understanding, such as emotion recognition. However, these models still struggle to reliably utilize acoustic information, particularly when it co...

### [The Italian lawmaking process: a unified and structured dataset](http://arxiv.org/abs/2610.23741v1)
_Matilde Contestabile, Chiara Ferrara, Giovanni Parrillo, Lorenzo Emer, Andrea Vandin_ • 2026-10-16

The Italian legislative process is documented in detailed parliamentary records hosted in institutional websites. However, much of this information is available only as unstructured text, limiting its systematic reuse. We applied a controlled, systematic LLM-based extraction procedure, validated against manually ann...

### [Bridging the Language Gap in Scholarly Data II: Enhancing Gender Inference for Chinese Names](http://arxiv.org/abs/2610.23734v1)
_Lisette Espín-Noboa, Mingrong She, Ana Maria Jaramillo, Liuhuaying Yang_ • 2026-10-16

Perceived gender inference from names is important for inclusive scientometrics research, yet existing methods perform poorly on non-Western scholars. We address this gap for Chinese names, which appear in two forms, Hanzi and Pinyin, its Romanized form (e.g., Zhang Wei, Li Na). In international bibliographic record...

### [Beyond Large Language Models: A Mental World Model Framework for Mental Modeling, Simulation, Evolution, and Interpretability](http://arxiv.org/abs/2610.23722v1)
_Qingshi Wang_ • 2026-10-16

Understanding and simulating how subjective cognition and mental states emerge, evolve, and shape behavior is essential for advancing artificial intelligence toward deeper social cognition and general intelligence. Existing large language models (LLMs) and Theory of Mind (ToM) methods primarily infer mental states f...

### [Recognizing Study Lineage Is Not Enough: Over-Crediting Same-Trial Evidence in LLM-Based Medical Verification](http://arxiv.org/abs/2610.23721v1)
_Mukand Krishna, Anoushka Harit, Chenghao Xiao, Zhongtian Sun_ • 2026-10-16

Publication count is not study count. A model can identify shared trial lineage correctly in a direct task yet over-credit a second publication from the same trial when aggregating evidence. We evaluate this behavior in medical LLM verification using 14 source-audited clinical families and five model conditions. The...

### [Neural Expansion: A Unified Mechanism for How Deep Neural Networks Generalize](http://arxiv.org/abs/2610.23716v1)
_Chashi Mahiul Islam, Samuel Jacob Chacko, Mao Nishino, Canlin Zhang, Xiuwen Liu_ • 2026-10-16

Deep neural networks demonstrate remarkable generalization despite being highly over-parameterized, challenging traditional statistical learning theories. While several theoretical paradigms such as margin-based bounds, PAC-Bayesian analyses, and neural tangent kernels provide global explanations, they often lack me...

### [The Cognitive Cost of LLM Writing: A Reading-Time Comparison with Human Text](http://arxiv.org/abs/2610.23715v1)
_Kamer Cekini, Elisabetta Biondi, Chiara Boldrini, Andrea Passarella, Marco Conti_ • 2026-10-16

Although linguistic differences between human-written and Large Language Model (LLM)-generated texts have been extensively studied, their implications for the cognitive effort involved in reading remain less explored. In psycholinguistics, reading time is commonly used as an indirect measure of cognitive processing...

### [GLOBE: Evolving Structured Agentic Memory for E-commerce Product Optimization in Generative Search](http://arxiv.org/abs/2610.23709v1)
_Hyunseo Kim, Suil Choe, Sukkyoung So, Daeyeon Yi_ • 2026-10-16

Optimizing product listings for generative search requires language agents not only to rewrite effectively but also to continually self-improve by retaining successful strategies across diverse categories. However, existing approaches often treat structured listings as free-form text, leaving effective strategies im...

### [VISTA: Steering LLMs with Latent User Values Inferred from a Few Survey Answers](http://arxiv.org/abs/2610.23702v1)
_Yinuo Xu, Jadie Adams, Brian Hu, Shivani Kumar, David Jurgens, +1 more_ • 2026-10-16

Personalizing a language model requires knowing what a person values, which stays largely consistent across tasks. Yet most methods either learn task-specific preferences or place the user's profile in the prompt, where models struggle to act on it. We introduce VISTA (Value-Informed Steering and Targeted Acquisitio...

### [Beyond the Benchmark: Conditioning, Domains and Failure Modes of Qwen3-TTS](http://arxiv.org/abs/2610.23678v1)
_Séverin Baroudi, Yanis Labrak, Petr Motlicek, Hervé Bredin, Ricard Marxer_ • 2026-10-16

Qwen3-TTS reports state-of-the-art zero-shot voice cloning, but its technical report leaves open how the model should be conditioned, how it behaves outside read speech, and how it fails. We characterise its two cloning interfaces, in-context learning (ICL) and X-Vector, against Chatterbox, XTTS-v2 and F5-TTS on rea...

### [On the possibilities and limitations of LLM-based multi-agent systems for multi-criteria decision-making in healthcare operations management](http://arxiv.org/abs/2610.23673v1)
_Marco Boresta, Tommaso Giovannelli, Sepehr Namirad, Giulia Riccardi_ • 2026-10-16

Multi-criteria models for healthcare operations need weights that express how stakeholders trade off patient waiting time, provider workload, and operating cost, but these weights are difficult to quantify. Teams of large language model (LLM) agents, each prompted to represent a stakeholder, have been used to supply...

### [OwlSight: A Panoramic Monitor for Chain-of-Thought Reasoning](http://arxiv.org/abs/2610.23670v1)
_Lewen Yan, Yanxu Zhu, Jie Zhang, Jing Shao_ • 2026-10-16

Chain-of-Thought (CoT) monitoring offers actionable evidence for oversight AI systems, with the potential to enable early detection and intervention. However, existing approaches are focused on specific tasks, whereas the regulation of AI, particularly reasoning models, requires monitoring a broader range of tasks....

### [TUPLE-Bench: Evaluating and Mitigating Privacy-Utility Trade-offs in Typed Decision Models](http://arxiv.org/abs/2610.23668v1)
_Yiqu Yang, Qiaoyuan Zheng, Yang Tian, Yu Fan, Elliott Ash_ • 2026-10-16

Typed decision models often return more than a selected category. They also expose probabilities for each candidate and, sometimes, a separate confidence score. These fields support downstream decisions but may reveal information beyond a recipient's authorization. We introduce TUPLE-Bench (Typed decision models' Ut...

### [In Human Memories. Technology, Creativity and Self-Determination: An Ethical Proposal](http://arxiv.org/abs/2610.23651v1)
_Francesco Vitucci, Giuseppe Silvi, Francesco Abbrescia, Anthony Di Furia, Francesco Scagliola_ • 2026-10-16

This research investigates the role of artificial intelligence (AI) in modern compositional practices, with a particular focus on two case studies: Convergence (2020/21) by Alexander Schubert, for String Ensemble and AI System, and In Human Memories (2024) by Francesco Vitucci, for four cellos and one electroacousti...

### [PresenceBench: An Exploratory Evaluation of Large Language Model Adaptation to User State](http://arxiv.org/abs/2610.23625v1)
_Peña Arroyo Gallego, Mauro Ruiz Moreno, Alejandro Acien, Sergio Romero-Tapiador, Teresa Arroyo-Gallego_ • 2026-10-16

Presence-aware intelligence is the capacity of an AI system's intelligence layer to adapt appropriately to the functional state of the person it serves (here readiness, flow, and stability) while preserving task quality and safety. We introduce PresenceBench, an instrument for measuring it. PresenceBench evaluates h...

### [GEMS: Molecular Structure Elucidation as Learned Search over Isomer Graphs](http://arxiv.org/abs/2610.23617v1)
_Utku Umur Acikalin, Yingheng Wang, Goncalo J. Gouveia, Tyler J. Schwertfeger, Frank C. Schroeder, +1 more_ • 2026-10-16

Identifying small-molecule structures from molecular formulas and tandem mass spectra remains a bottleneck in untargeted metabolomics and natural-product discovery. Even when database retrieval or de novo prediction misses the exact structure, the resulting candidates can provide starting points for exploring nearby...

### [Beyond Action Prediction: Learning Search-Free Planning in Latent Space](http://arxiv.org/abs/2610.23615v1)
_Guanchen Du, Jinhao Du, Yanpeng Sun, Shan Zhang, Na Zhao, +1 more_ • 2026-10-16

Latent world models learn action-conditioned state transitions in a compact representation space, providing a predictive model for visual planning and control. However, planning with these models typically requires costly test-time optimization over action sequences. We propose to replace this online search with a g...

### [Trajectory-Triggered Sparse Collaborative Decoding](http://arxiv.org/abs/2610.23613v1)
_Amit Ranjan Trivedi, Sruthikesh Surineni, Kyong Ho Lee, Mohit Mittal, Steven Li, +1 more_ • 2026-10-16

Dense assistance methods such as speculative decoding repeatedly verify draft tokens with a target model, keeping target computation coupled to generation. We study sparse collaborative decoding, where a draft model generates most tokens and a target model is invoked only for short corrective segments. The key probl...

_snapshot taken at 2026-10-19T19:27:48+00:00_
