arXiv:1912.00421v1  [q‑bio.NC]  1 Dec 2019
# Biological Blueprints for Next Generation AI Systems

# Thomas Dean¹,²

# Chaofei Fan²

# Francis E. Lewis²

# Megumi Sano²

# Abstract

Diverse subfields of neuroscience have enriched artificial intelligence for many decades. With recent advances in machine learning and artificial neural networks, many neuroscientists are partnering with AI researchers and machine learning experts to analyze data and construct models. This paper attempts to demonstrate the value of such collaborations by providing examples of how insights derived from neuroscience research are helping to develop new machine learning algorithms and artificial neural network architectures. We survey the relevant neuroscience necessary to appreciate these insights and then describe how we can translate our current understanding of the relevant neurobiology into algorithmic techniques and architectural designs. Finally, we characterize some of the major challenges facing current AI technology and suggest avenues for overcoming these challenges that draw upon research in developmental and comparative cognitive neuroscience.

Affiliations: 1Brown University, 2Stanford University


---

# Contents

1. Introduction 1
2. Neuroscience 1
1. Connectivity 2
2. Reciprocity 4
3. Sensorimotor Hierarchy 6
4. Basal Ganglia 8
5. Hippocampal Complex 10
3. Architecture 14
1. Embodied Cognition 15
2. Conscious Attention 17
3. Action Selection 20
4. Executive Control 24
5. Digital Assistants 27
6. End-to-End Systems 30
4. Discussion 31
1. Child Development 31
2. Inductive Bias 32
3. Natural Language 32


---

# 1 Introduction

Artificial neural networks support distributed computations in which concepts are represented as patterns of activity in the units that comprise the network layers, and inference is carried out by propagating activation levels between layers weighted by learned connection weights. Artificial neural networks provide a type of fast, flexible computing well suited to handling ambiguity of the sort we routinely encounter in real-world environments, and, by doing so, they complement traditional symbolic computing technologies.

Engineers frequently borrow ideas from nature and generally find it more practical to translate these ideas into current technology rather than attempt to reproduce nature’s solutions in detail. Indeed, the basic idea of artificial neural networks has been implemented multiple times using different technologies in order to approximate the connectivity patterns and signal transmission characteristics of real neural circuits while largely ignoring the physiology of real neurons in their implementation.

The human brain supports a wide array of learning and memory systems. Some we have begun to understand functionally and behaviorally, others we can only hypothesize must exist, and still others about which we haven’t a clue. Just knowing that the brain supports a particular capability can serve as an important clue in engineering complex AI systems. Knowing how can lead to an innovative design, enhanced performance and extended competence. In particular, knowing something about how specific biological circuits relate to behavior helps in designing novel network architectures.

We are interested in designing neural network architectures that leverage what is known about biological information processing to solve complex real-world problems. To focus our efforts, we have set out to design end-to-end systems that assist human programmers in writing, debugging and modifying software. We benefit considerably from working closely with scientists from diverse subdisciplines of neuroscience to seek solutions to specific problems and identify additional problems we may have overlooked. The following section explains why this commingling of people, ideas and technologies is so valuable to us in pursuit of our objectives.

# 2 Neuroscience

From the brain of an Etruscan shrew weighing in at less than a tenth of a gram to a sperm whale brain weighing more than eight kilograms, it is clear that natural selection has stumbled on a basic brain plan and set of developmental strategies that enables it to construct a diverse set of special-purpose brain architectures for efficiently expressing a wide range of sophisticated behavior [57, 182]. The human brain with its approximately 100 billion neurons and the shrew brain with approximately 1 million neurons share the same basic architecture.

The mouse brain has homologues of most human subcortical nuclei and has contributed significantly to our understanding of the human brain and human neurodegenerative disease in particular. The differences between human and chimpanzee brains are subtle [129] and yet humans display a much wider range of behavior and express a much larger repertoire of genes than any other species [88]. So what makes the difference?

It’s the connections between neurons that matter or, more generally, it’s the different types of communication between neurons that biologists refer to as pathways. There are electrical, chemical and genetic pathways and each of them obey different constraints and are used for different purposes. They include point-to-point and broadcast methods of communication [86]. They transfer information at different speeds and using different coding strategies. Layered architectures are


---

# Primary somatosensory cortex

# Primary motor cortex

# Somatosensory association area

# Motor association area

# Visual association area

# Visual cortex

# Wernicke's area

# Auditory cortex

# Auditory association area

Figure 1: A highly stylized rendering of the major functional areas of the human cortex shown from the side with the head facing to right. Highlighted regions include the occipital lobe shown in shades of green including the primary visual cortex; the parietal lobe shown in shades of blue, including the primary somatosensory cortex; the temporal lobe shown in shades of yellow including the primary auditory cortex; and the frontal lobe shown in shades of pink, including the primary motor and prefrontal cortex. The region outlined by a dashed line on the right is Broca's area and it is historically associated with the production of speech and hence its position relative to the motor cortex. The region outlined by a dashed line on the left is Wernicke's area and it is historically associated with the understanding of speech and hence its position relative to the sensory cortex.

common not just in the cortex but throughout the brain. It’s the wiring that sets humans apart.

# 2.1 Connectivity

Figure 1 shows the major functional areas of the human neocortex including the primary and secondary sensory and motor areas. The proximal locations of the areas provide a very rough idea of how different functions might relate to another. The graphic shown belies the fact that the brain is three dimensional and much of its functional circuitry hidden under the cortical sheet. The human cerebral cortex is complexly folded to fit within the skull with much of it hidden within the folds. This folded sheet of tissue accounts for more than 75% of the human brain by volume [170] and is largely responsible for the rich behavioral repertoire that humans exhibit. It is worth pointing out in this context that the cortical sheet enshrouds a collection of evolutionarily preserved and highly specialized circuits homologues of which are found in all mammals and without which the cortex would be useless.

The graphic shown in Figure 1 is a simplification of the standard medical textbook diagram. In particular, several of the association areas are not shown and those that are shown are labeled somewhat differently than is common practice. The organizing biological principle is that, the further away from the primary sensory areas, associative functions become more general by integrating information from multiple modalities to construct abstract representations tailored to serve ecologically relevant objectives [186]. It is worth contemplating the arrangement of areas to note that they converge on locations in the cortex that will play an important role in decision making and


---

# BASAL GANGLIA

# HIPPOCAMPUS

# THALAMUS

# THALAMUS

# BASAL GANGLIA

# VENTRICLE

# HIPPOCAMPUS

# AMYGDALA

# CEREBELLUM

# VENTRICLE

# CEREBELLUM

Figure 2: Two 3-D renderings of the human brain generated by the Allen Institute Brain Explorer from the Allen Human Brain Reference Atlas [89]. The inset shown in the left upper corner of each panel indicates the orientation of the head. The left panel (A) shows 3-D reconstructions of several subcortical nuclei featured in this paper. A cross-sectional view of the whole brain is projected on the mid-sagittal plane dividing the right and left sides of the brain illustrating how the cortex envelopes the subcortical regions. The right panel (B) shows the same subcortical nuclei as seen from above (horizontal plane) and to the rear of the brain illustrating how the thalamus is located between the cortical sheet and the subcortical nuclei serving in its role as a relay between the two regions.

Figure 2 highlights the 3-D structure of several subcortical nuclei emphasized in this paper showing how they relate anatomically to one another and to the cortex. The reconstructions were generated from data generated by functional magnetic resonance imaging (fMRI) of adult human subjects [89] and offer additional functional insight complementing conventional histological studies [31]. They don’t however provide detailed information concerning either local or long-range connectivity.

Traditionally, tracing connections between individual neurons has been accomplished using a variety of techniques including conventional histological and staining techniques, electrophysiology, neurotropic retroviruses and transgenic organisms expressing fluorescent proteins. However, these methods yield relatively sparse reconstructions and don’t scale well to large tissue samples [10, 34].

Small samples of neural tissue can be fixed, stained and sliced into thin sections. Each of the sections is then scanned with an electron microscope and the resulting digital images analyzed with computer vision software to reconstruct neurons and identify synapses [124]. The process is time consuming but can be fully automated and scaled to handle larger samples [94, 189].

It is also possible to reconstruct the major white matter tracts formed by bundles of myelinated fibers using diffusion-weighted fMRI and averaging over multiple subjects after registering the individual brain scans with a reference atlas [134, 176]. Unlike the previous technologies, this method is not destructive so it can be applied to human subjects and accuracy is improved by averaging over multiple subjects after registering the individual brain scans with a reference atlas.

These major tracts increase the speed of signal transmission between regions allowing for more distant communication in larger brains. The differences between the neocortex in humans and chimpanzees are subtle [129]; however, white matter connections observed in humans but not in chimpanzees particularly link multimodal areas of the temporal, lateral parietal, and inferior frontal.


---

Figure 3: White matter tracts corresponding to bundles of myelinated neurons speed the transmission of information between distant regions of the brain. The left panel (A) shows the connections between the prefrontal cortex and circuits in the parietal and temporal cortex that shape conscious awareness, guide attention and support short-term memory maintenance [39, 49]. The parietal and temporal cortices are known for being home to association areas that integrate information from multiple sensory systems thereby creating rich representations necessary for abstract thinking. In humans, white matter tracts between the frontal cortex and the cerebellum — shown in the right panel (B) — facilitate higher-order cognitive function in addition to their role in supporting motor function in all mammals. For example, these connections are particularly important in the development of reading skills in children and adolescents [172, 106].

The cerebellum in mammals serves to shape motor activities selected in the basal ganglia by ensuring they are precisely timed and well-coordinated. Such activities are initiated by the basal ganglia with executive oversight from the prefrontal cortex. In humans, the cerebellum also supports cognitive functions such as those involved in reading [172]. Figure 3 (B) shows the white matter tracts connecting the cerebellum and prefrontal cortex where such abstract cognitive functions originate.

A white matter bundle called the arcuate fasciculus — Figure 3 (A) — provides reciprocal connections between the frontal cortex and association areas in the parietal and temporal lobes plays a key role in attention and the active maintenance of short-term working memory, including support for language processing in the left hemisphere and visuospatial processing in the right hemisphere [39].

The human brain exhibits structure at many scales, the white matter tracts being but one example. A common pattern involves paths that connect multiple circuits that have their own internal components and connections. At a global scale, processing begins in primary sensory areas, propagates forward through dorsal regions integrating additional sources of information to produce composite representations that are processed in the frontal cortex before returning through ventral regions responsible for motivation and action selection.

# 2.2 Reciprocity

Many of the connections within such paths are reciprocal allowing feedback to adjust behavior and improve prediction. Similar reflective and self-corrective patterns arise within subcortical regions.


---

# Figure 4

| A | Frontal < | 46 |    |    |    |
| - | --------- | -- | -- | -- | -- |
|   | Pa        | 19 | 23 | 8  |    |
|   | Calidate  |    | 22 | 21 |    |
|   | Pittamen  | 20 |    | 13 |    |
|   |           |    |    | 11 | 12 |

The left panel (A) illustrates the reciprocal connections between two subnuclei of the basal ganglia, the putamen and caudate nucleus, and locations in prefrontal cortex responsible for influencing action selection. The distinctions between frontal, parietal and temporal cortical areas provide only a very general indication of how their function relates to that of the basal ganglia.

The right panel (B) highlights reciprocal connections between cortical regions — identified by the Brodmann areas 7, 8, 9, 11, 12, 13, 19, 20, 21, 22, 23 and 46 — and the hippocampal complex via the adjacent perirhinal (blue) and the parahippocampal (red) areas. The indicated Brodmann areas generally provide a more nuanced understanding of their possible function than does simply stipulating the cortical lobe they reside in.

including the hippocampal complex and basal ganglia, e.g., between the dentate gyrus and CA1 in the hippocampus and as layered networks inside individual subcomponents such as the mossy fiber network within the dentate gyrus. Each level solves different problems, offers general insights and provides hints about how one might realize such solutions in artificial systems.

Figure 4 describes how subcortical nuclei such as the hippocampal complex and basal ganglia interact with cortical regions. Such attributions provide insight on how to construct complex artificial neural architectures composed of simpler subnetworks ostensibly responsible for component functions including perception, action selection and episodic memory.

Here we consider two levels of granularity: the first is coarse grained relying on major anatomical divisions illustrated in Figure 1. The second is somewhat finer grained and relies on areal divisions based on cytoarchitectural distinctions involving cell types, neural processes including dendrites and axons, and other histological characteristics.

The former generally employs Korbinian Brodmann’s decomposition of the cortex into 52 areas published in 1909 [32] and revised several times since then to take advantage of more modern staining and imaging technologies as well as improved methods for functional localization. In many cases, identifying the Brodmann area associated with the endpoint of a neural connection can tell us a good deal about the functional relationship between two brain regions.

The left side of Figure 4 (A) highlights the reciprocal connections between two subnuclei of the basal ganglia, the putamen and caudate nucleus, and locations in prefrontal cortex responsible for influencing action selection by adjusting input to the basal ganglia and, by way of the thalamus, locations in the parietal and temporal cortex that provide information about the current state relevant to decision making.

We can often improve functional descriptions if we localize to specific Brodmann areas. For example, the orbitofrontal cortex (OFC) is located in the prefrontal cortex is a region of the frontal


---

# 2.3 Sensorimotor Hierarchy

Much of the cortex is in the business of learning representations of concepts relevant to survival. Perception is the means by which we apprehend and act on the physical realization of the concepts we have learned. It seems obvious that perception serves action. It may not seem so obvious that action serves perception, but the fact is we are almost always moving our head, hands and torso in order to resolve ambiguities in what we see, feeling the shape of unfamiliar objects in order to grasp them firmly and twisting about to see who is behind us calling our name or to get a better idea of where we’ve come from in order to ensure we can retrace our steps. These are complex sensorimotor activities we depend on every day.

In thinking about physically realizable concepts we think first about what they look, feel, sound and smell like. The sensory cortex is responsible for constructing a hierarchy of representations to characterize such concepts, not to capture everything we sense, but rather to account for what we need to know about concepts to survive. Reconstructing scenes with photographic realism is not what our sensory systems were designed for. Circuits of the primary sensory cortex feed into the circuits of the (unimodal) association sensory cortex that feed into (multimodal) sensory cortex.


---

# Figure 5: A simplified block diagram of the cortex.

| Posterior Associative Cortex | Prefrontal Executive Cortex |
| ---------------------------- | --------------------------- |
| Sensory Associative Cortex   | Premotor Cortex             |
| Primary Sensory Cortex       | Primary Motor Cortex        |
| Environment                  |                             |

The column on the left represents the posterior cortex including the occipital, temporal and parietal lobes. The column on the right represents the frontal lobe of the cortex corresponding to the primary motor cortex, premotor cortex (association motor cortex) and prefrontal cortex. Green arrows represent interaction with the environment, black arrows represent sensorimotor abstractions and red arrows indicate cognitive activity relating speech, planning and abstract thinking. See the main text for more detail. Adapted from Figure 8.9 in [68]

of these representations are abstract and yet patterns of regionalization are remarkably preserved within species [36, 146, 103].

Concepts arise in patterns of neural activity that account for what we need to know about them, including how they appear to us so we can recognize them, what affordances they offer for us to make use of them and how we might predict their occurrence in decision making. Many of the concepts that are represented in our brains serve to model the dynamics of physical systems that we interact with every day, such as riding a bike, working with tools, opening doors, negotiating stairs and riding escalators in department stores. Just as important, if not more so, are the social dynamics we deal with at work and school with their constantly shifting personal relationships and status rankings.

If you are a software engineer designing robot control systems, you might give action much the same scrutiny as perception and build a parallel hierarchy of representations that describes the concepts that relate to movement including navigation, articulation and manipulation ranging from servo-motor commands to strategies for moving furniture, but designing or learning these hierarchies independently is generally a bad idea. In mammals, these two hierarchies are tightly coupled to account for how they depend on one another [69].

Indeed, determining what sensory representations to learn depends upon and influences what motor representations to learn and vice versa, where we follow the convention of using the term motor as a catchall term for concepts relating to muscles and movement. As pointed out in the introduction, there is evidence to suggest that circuits occurring early in the ventral visual stream code for object-selective features and exhibit large-scale organization characterized by the high-level properties of animacy and object size [104, 114].

Figure 5 is a simplified block diagram of the cortex organized as two columns. The left column represents the posterior cortex consisting of the occipital, temporal and parietal lobes that are primarily concerned with processing sensory information. The relevant brain areas are summarized in three blocks roughly corresponding to primary sensory cortex, unimodal association cortex and multimodal association cortex stacked so the least abstract concepts are on the bottom and most abstract on the top. The combined area is often referred to as semantic memory and characterized as long-term declarative memory [26].

The right column represents the frontal lobe of the cortex corresponding to the primary motor cortex, premotor cortex (associative motor cortex) and prefrontal cortex.


---

is responsible for creating abstract representations of motor activity throughout the body. The pre-motor cortex is responsible for integrating sensory and motor abstractions to construct sensorimotor representations. The prefrontal cortex orchestrates cognitive behavior including speech, planning and abstract thinking, and is reciprocally connected to the association areas just mentioned as well subcortical structures including the basal ganglia and hippocampus.

The two columns are connected with one another at multiple levels: by physical interaction with the environment (green arrows), by sensorimotor abstraction and alignment (black arrows), and by cognitive effort in directing activity mediated through subcortical structures (red arrows). This arrangement supports the formation of rich representations that serve a wide range of cognitive function. The sensorimotor connections and feedback through the environment provide an inductive bias to guide learning, ground inference and reduce sample complexity by reducing reliance on labeled data and enabling opportunities for unsupervised learning [16].

Simple as this model of cortical function may seem, it may be one of the most important architectural contributions of neuroscience to the development of artificial intelligence patterned after the human brain. Some of the lessons have already been integrated into the discipline of control theory through exposure to early work in biological cybernetics [67, 111, 93, 72, 122, 174], but some of the most important lessons impact the application of machine learning in building autonomous embodied systems including robots and digital assistants as alluded to above.

# 2.4 Basal Ganglia

There is a long history of neuroscientists constructing computational models of human cognition [117, 118, 110, 136, 29]. Different modeling tools make different assumptions and support different levels of detail from rule-based systems to spiking neurons [140, 141, 149, 60, 27, 95]. In this paper, we are primarily concerned with computational models that leverage ideas from neuroscience to develop AI systems for practical problems. In this subsection and the next, we take a closer look at the basal ganglia and hippocampus using models from neuroscience that reveal computational principles we can apply in a wide range of practical problems.

In contrast with the relative simplicity of the neocortical architecture, the basal ganglia consist of specialized subcortical nuclei that are related by their evolved function. In the following, we emphasize and simplify some of those nuclei and ignore others to focus the discussion and simplify the biology. The basal ganglia provide the basis for motor activity controlled by circuits in the brainstem and conserved throughout vertebrate evolution for nearly half a billion years. The cerebral cortex has been around in the form of a six-layer sheet tiled with a repeating columnar structure since the early mammals came on the scene in the Jurassic period about 200 million years ago. Our lineage separated from mice around 100 million and from macaques and other old world monkeys around 25 million years ago. The modern human neocortex owes much to these earlier evolutionary innovations but is different in ways that make possible our facility with language, complex social organization and sophisticated abstract thinking. Compared with the basal ganglia, the neocortex is structurally elegant and functionally general.

The basal ganglia have evolved along with our neocortex to provide us with a powerful thinking machine, while at the same time leaving us to make do with some less-than-ideal adaptations. We can simulate a conventional computer in our heads but are limited to fewer than a dozen memory registers. Most of us can’t perform long division in our heads even though we might know the algorithm and aided with paper and pencil carry out the necessary computations to produce an answer. We rely on the same basic cognitive machinery we use to list a few names in alphabetical order to perform all sorts of more complicated cognitive tasks. Even simpler, however, is the basic operation of choosing one of several actions to perform next. The basal ganglia play a key role in


---

# Figure 6

The left panel (A) provides a highly stylized anatomical drawing of the basal ganglia. Figure 4 (A) provides more anatomical detail while the above drawing abstracts from the structural detail in order to simplify the functional account. The block diagram shown in the right panel (B) depicts the primary components involved in action selection as functional blocks. The blocks shown in blue represent components in the direct path and are described in the text proper. The blocks shown in light green with dashed borders represent additional components that contribute to the indirect path. Good explanations of the indirect path are described in O’Reilly et al [141] or Wang et al [177] and we return to the basal ganglia in the next section when we look at the executive role of the prefrontal cortex in modulating behavior.

Supporting action selection and it is worth looking at in a little more detail in order to get a handle on some of the parts of the brain that figure prominently in human cognition. Recall that the cortex is a sheet of neural tissue more or less homogeneous in terms of its local structure quite unlike almost any other part of the brain except for the cerebellar cortex. The cortex sits on top of a structure called the thalamus which among other things serves as a relay in passing information back and forth between the cortex and various subcortical nuclei.

The basal ganglia consist of a bunch of circuits, of varied size, sometimes but not always consisting primarily of one cell type, sometimes but not necessarily compactly clustered together, sporting projections that seem to wander off aimlessly, but more or less located above the brainstem and below the cortex. As a general principle, if a signal sets off along some path exiting from a circuit, then expect some derivative of that signal to appear later reentering the circuit to serve as feedback. Everything about the brain, and your entire body for that matter, has to be carefully regulated to maintain a dynamic state of equilibrium, and unlike human designs, evolution is generally not able to cleanly separate the parts of the circuit that perform computations in service to behavior from those that deal with respiration, immune response, waste removal, cell repair, death and regeneration, etc.

The basal ganglia are depicted in Figure 6 (A) taking some artistic license to keep things simple. The thalamus along with another structure called the striatum provide the interface between the cortex and basal ganglia. The striatum is a combination of a number of smaller nuclei that are anatomically and functionally related; they include the Globus Pallidus (GP), Putamen and Caudate Nucleus and aside from their function as part of the striatum, only the GP will figure prominently in our discussion and only one part of it — referred to as the internal GP and identified with the ”i” subscript to distinguish it from the external part with ”e” subscript.

The other players include the Substantia Nigra (SN) which is at one end of the striatum nestled close to the amygdala which is part of the limbic system involved with memory, decision-making and modulating emotional responses, and the Subthalamic Nucleus (STN). You can think of the cortex as integrating sensory and motor information and making suggestions for what action to take.


---

next and the amygdala as supplying information pertaining to the possible emotional consequences of taking different actions to be used as input to action selection. Figure 6 (B) reconfigures these component nuclei into a smaller number of functionally motivated blocks that control two pathways — the direct pathway associated primarily with inhibition and consisting of the internal GP and SN and the indirect pathway playing an excitatory role and consisting of the external GP and STN [141, 177].

The lines connecting the functional blocks shown in Figure 6 (B) imply neural connectivity, with arrows indicating the direction of influence and colors indicating the valence of the influence, green for excitatory and red for inhibitory. In the action selection cycle, the cortex forwards activations that you can think of as suggestions for what action to take next. These suggestions are propagated through the striatum and forwarded along the direct pathway where two stages of inhibitory neurons initially suppress all of the suggestions and propagate signals back to the cortex to activate inhibitory neurons that suppress activity at the source. As this cycle continues, an additional process takes place in the indirect path — identified with dashed lines — that weighs the advantages and disadvantages of the proposed actions taking in information from throughout the cortex and adjusting the inhibitory bias accordingly.

Eventually, one proposal wins out and all of the others are suppressed allowing a single preferred action to be executed. This cycle of exploring the options for acting and then selecting a single action to execute is constantly repeated during your waking hours. Additional machinery in the thalamus and brain stem regulate whether or not to forward suggestions for acting during sleep when your cortex receives no sensory input and hence any suggestions for acting uninformed by sensory input are ill-advised if not outright dangerous. The above description doesn’t begin to convey the complexity of what’s going on at the level of individual neurons. Suffice it to say that the usual perfunctory summary consisting of ”the winner takes all” doesn’t begin to do it justice. The subtleties that arise from the way in which the evidence for and against an action proposal is combined, how ties are broken and deciding when enough evaluation is determined sufficient to make a final choice.

# 2.5 Hippocampal Complex

Figure 12 provides a glimpse of how we construct memories of our experience and subsequently retrieve those memories to support a diverse range of cognitive strategies. In this case, the hippocampus will play a central role as did the basal ganglia in the previous example. In the next section, we explore how the basal ganglia work in concert with the hippocampus to support reinforcement learning. For now, our goal is simply to describe the process whereby we consolidate and then encode experience. In doing so we take the opportunity to talk about the process whereby we retrieve memories, reconstruct a version of that past experience to perform counterfactual inference and imagine possibilities that we have never actually experienced.

The name hippocampus like so many biological terms has obscure origins, generally in Latin or Greek and in this case the latter, relating to its shape that looked like a seahorse to some early anatomists. As shown in Figure 12 (A) it is primarily comprised of four subnuclei referred to as CA1, CA2, CA3 and CA4, the first two characters in each abbreviation recalling a previous Latin name, Cornu Ammanonis associated with a ram’s horn, apparently preferred by even earlier anatomists. These nuclei are capped by the dentate gyrus (DG) at one end and the fornix at the other.

The hippocampus consists of two nearly identical structures, one in each hemisphere, connected where the parallel tracts of the fornix come together at the midline of the brain. The hippocampus is tightly coupled with the entorhinal cortex (EHC) that plays an important role in memory, navigation and our perception of time. Information flows from the EHC to the hippocampus by one of two


---

# Figure 7

| A   |     |                   | B                 |        |
| --- | --- | ----------------- | ----------------- | ------ |
|     |     | Cortex            | DG                |        |
|     |     | Thalamus          |                   |        |
|     |     | Fornix            | EHC               |        |
|     |     | Hippocampus       | CA3               | CA1    |
| CA4 | CA3 | CA2               | CA1               |        |
|     |     | Dentate Gyrus     |                   |        |
|     |     | Association Areas | MEMORY ENCODING   | Cortex |
|     |     | Entorhinal Cortex | MEMORY RETRIEVAL  |        |
|     |     |                   | KEY CONSOLIDATION |        |

On the left you see a cartoon drawing of the hippocampus and related cortical and subcortical areas. The primary components include the entorhinal cortex or EHC, the dentate gyrus or DG and two hippocampal (out of four) nuclei referred to as CA3 and CA1. Figure 4 provides additional anatomical detail regarding the connections between cortical regions and the perirhinal and parahippocampal areas adjacent to the hippocampus. The block diagram on the right summarizes the component circuits, along with their projections and reciprocal connections. Pathways: either through the DG to CA3 or via reciprocal connections to and from CA1. The EHC also has reciprocal connections to many cortical areas. Figure 4 (A) provides additional anatomical detail.

In the process of creating a new memory, the hippocampus receives input from multiple cortical areas relevant to current experience, consolidates this information in a condensed format that will enable subsequent retrieval and stores the resulting encoding in memory. In retrieving an existing memory, The EHC starts with cortical activity, typically from motor and sensory association areas, and uses this information to reconstruct a previous memory by activating cortical areas corresponding to the original memory. Before describing how we think such creative consolidation and subsequent reconstruction works, a word about why this process is beneficial might be in order.

Almost every stage of memory is fraught with opportunities to alter stored representations of prior experience. Reconstruction is a creative process in which we are more often than not forced to fill in some details that we might think we observed at the time but actually didn’t. In the formation of new memories, consolidation can only make do with whatever information about the experience we have gleaned from observation and committed to short-term memory. If you don’t rehearse what you’ve stored in short-term memory then it will quickly fade, losing detail and potentially introducing errors of omission and commission.

The basic algorithm carried out by the hippocampus and entorhinal cortex working together is illustrated in Figure 12 (B). There are two basic processes that we consider here: encoding new memories and retrieving old memories. Encoding involves collecting information gleaned from diverse neural activity originating in multiple cortical regions and consolidating this information to construct a compact encoding that serves as a key or index that will enable subsequent stable — meaning reliably consistent even in the presence of distracting information — retrieval and reconstruction.

EHC receives input from all cortical regions in a condensed form and the axons of EHC pyramidal neurons project primarily to the DG but also to CA1. DG then projects to CA3 which plays a particularly important role in encoding and retrieving memories. CA3 is thought to behave as an autoassociative memory shown here as a recursive neural network. The crucial property of an autoassociative memory is that it is able to retrieve an item from memory using only a portion of the information associated with that item.


---

# Figure 8:

The three panels shown here represent the autoassociative network representing the function of CA3 in the hippocampus. Connection weights are shown as diagonal lines, e.g., the dotted blue lines shown in the network on the far left represent the connection weights prior to any training. The middle panel represents the network after encoding the stimulus pattern corresponding to the cortical activation of A and C, and the panel on the far right represents the network, when presented with a partial pattern consisting of just C, employing the recurrent connections of the autoassociator to complete the pattern for the original stimulus and using it to reconstruct the corresponding activation of A and C in the cortex.

The hippocampus serves as an index, storing different patterns of cortical activity and allowing us to retrieve our memories using only a fragment of what we can recall. The recurrent connections of CA3 are thought to enable this sort of creative reconstruction and play a role in both encoding and retrieving memories. CA3 then projects to CA1 and from there back to the EHC completing the loop and thereby providing recurrent activity involving a much larger circuit.

There are a couple of details that are worth pointing out here as they demonstrate both the strengths and weaknesses of human episodic memory. The first concerns the issue of retrieving a complete memory given a partial index and the second concerns how to retrieve a memory when that memory is similar to one or more other memories, at least in the sense that their respective indices are similar to one another. In the model described here, the first issue is handled by the autoassociative network.

The triptych shown in Figure 8 illustrates how the autoassociative network solves this problem. The panel on the far left is meant to indicate the autoassociative network and its initial state. In the middle panel, we assume the input from the dentate gyrus consist of the two sub patterns A and C and illustrates the reciprocal connections that would be strengthened were we to train the network with this composite pattern of activity. CA3 is responsible for encoding these memory specific patterns of activity for all of our memories. The panel on the far right is intended to illustrate how given a partial pattern, in this case just one of the two representative patterns that comprise the composite pattern shown in the middle panel, is able to reconstruct the other representative pattern by using the trained autoassociative network to first identify and then strengthen the connections in the original composite.

The second detail concerns the possibility that the encodings for two memories are alike enough to be mistaken with one another. A full account of any of the theories explaining how the human brain solves this problem is beyond the scope of what we can go into here but one theory — first articulated by David Marr [116, 183] — posits that, since the dentate gyrus has a larger number of cells than the EHC, its forward projection will tend to produce an expansion recoding in the DG leading to an increase in the separation between the patterns in CA3.

To complete our account of memory retrieval, we look at how the path that started in the EHC loops back to complete a feedback loop that stabilizes the encoding of memories. So far we’ve seen how an experience represented by a pattern of activity in the cortex is compressed and represented.


---

in the entorhinal cortex which projects this pattern onto the cells in the dentate gyrus thereby increasing the separation between competing patterns the results of which are bound together to generate an index. This index is fed to CA3 where it is incorporated in an autoassociative recursive network so that subsequently when a feature of the original stimulus is present in our conscious experience it activates a subset of the original neurons activated in CA3 and the recurrent connections in the autoassociative network reactivate the remaining neurons completing the pattern that was incorporated when the experience was initially encoded in memory.

The remaining step involves explaining how the representation in CA3 reactivates the original stimulus. As shown in Figure 12 (B), the entorhinal cortex projects to CA1 in addition to the dentate gyrus. When neurons are projected forward to DG and activated in CA3 they are also activated in CA. Since they are activated at the same time, the connections between the neurons in CA3 and CA1 are strengthened by long-term potentiation. The result is a stable, sparse, invertible mapping that allows the hippocampus to recreate the original cortical activity patterns during retrieval [137, 119]. Reactivating the same combination of cortical areas as the original stimulus and causing us to reexperience the event as a memory. An additional process called reconsolidation is thought to allow previously-consolidated memories become labile again as a consequence of reactivation. See Box A for detail on storing and retrieving memories in the hippocampus.

# Box A: Pattern Separation, Completion and Integration

As discussed in Section 2.5, pattern separation reduces the similarity between input patterns of activity by orthogonalizing inputs to minimize interference between patterns and increase hippocampal storage capacity [99]. Pattern separation involves primarily DG and CA3 — see Section 2.5 for an explanation of the acronyms. The DG maps input from EHC to a much larger and sparsely active GC population. In rats, the number of neurons in the DG exceeds that in EHC by about 5:1 [58]. This expansion coding with strong inhibitory interneurons and a competitive learning rule can greatly reduce the overlap between inputs. The DG connects to CA3 mainly through mossy fibers that reliably activate CA3 pyramidal neurons and sustain activation for tens of seconds [175]. Each CA3 neuron receives a small number of these connections from DG so the degree of sparsity is maintained [99].

Pattern completion reconstructs the complete stored pattern given a partial input. Each pyramidal neuron in CA3 receives a large number of synapses from other pyramidal cells forming a recurrent network that serves as an autoassociative memory for pattern completion [99]. During learning, recurrent connections between active CA3 neurons are strengthened and later when neurons encoding part of an episode are reactivated, they recurrently activate other connected cells to reconstruct the original episode. Basket cells in CA3 form inhibitory synapses to pyramidal cells to dampen excitatory responses thereby emphasizing key features [133].

Pattern completion provides access to relevant experience to support decision making in novel situations, and while pattern separation helps downstream discrimination, perfectly orthogonal representations are not ideal in the case we want events that occurred close together to have similar representations. In this case, pattern integration represents related experiences as overlapping populations. There are a number of neural mechanisms suggested to support pattern integration in the hippocampus. We consider two here, the first of which involves neurogenesis.

There is evidence that hundreds of new GCs are added to an adult human hippocampus.


---

everyday [168], and stronger evidence suggests that thousands of new GCs are added to rodents hippocampus, though not all survive [101]. Unlike mature GCs that fire sparsely, immature GCs are more active and have lower threshold for induction of long-term potentiation [1, 70, 163]. Aimone et al [1] posit that a population of hyperactive young GCs could collectively encode events close in time to decrease pattern separation in DG. Others hypothesize that neurogenesis may increase storage capacity by protecting old GCs from new information [19, 185] or that young active GCs could improve the resolution of memory content [2]. Alternatively, pattern integration might be enabled by recurrent connections involving the hippocampus and neocortex. Recurrent connections in the hippocampus, mainly in CA3 region, can replay an entire episode given a part of it. The replayed episode is backprojected to the neocortex through EHC, that can then recirculate the replayed episode as input to hippocampus to trigger replay of another episode that has overlapping elements with previous one. Kumaran et al [108] propose that this kind replay between hippocampus and neocortical regions can combine representations of elements that seldom occur together but appear in similar contexts. In addition to integrating experiences with shared elements, backprojection to the medial prefrontal cortex (mPFC) may bias hippocampus to reactivate experiences that are more behaviorally relevant [162] — see Box B for more on behavioral relevance. The concurrent presentation of these memories in mPFC may further improve the learning of abstraction relations across episodes.

# 3 Architecture

The architecture of the human brain, at any scale you choose to consider, bears little or no resemblance to conventional computer architectures. There is no separate program memory, no centralized processing unit, no highly stable, random-access, non-volatile memory and nothing like the digital level of abstraction that enables software engineers to ignore instabilities in the analog circuits that implement logic gates. Since representations (data) are collocated with the transformations (computations) that operate on them and different parts of the brain perform different computations requiring different types of memory, the human brain has to support multiple memory systems.

Human memory is characterized along several dimensions depending on what sort of information is stored, how it is accessed and how long it remains accessible [43]. Short-term, long-term and working memory are differentiated on the basis of access, persistence, volatility and the effort required to maintain. Short term is measured in seconds, long term in days, months or years and working memory is essentially short-term memory that can be maintained (with cognitive effort) indefinitely and manipulated (very roughly) analogous to a register in the ALU of a von Neumann machine [12].

Declarative memory is defined by the ability to explicitly (consciously) recollect facts, whereas non-declarative memory is accessed unconsciously or implicitly through performance rather than recollection. Episodic memory is generally considered long-term and declarative, and is further differentiated on the basis of the kinds of relationships it can encode, including spatial, temporal and social [169, 156, 109, 41]. Procedural knowledge, including motor, visuospatial and cognitive skills, is encoded in the cerebellum, the putamen and caudate nucleus of the basal ganglia, the motor cortex, and frontal cortex.

To ground the discussion, we introduce the programmer’s apprentice as an example of the sort of digital assistants we envision as an application of the technologies presented in this paper.


---

# 3.1 Embodied Cognition

Embodied cognition is the theory that an organism’s body shapes its understanding of the environment it inhabits and grounds its perception of and interaction with that environment. Importantly, the environment completes a loop that links perception and action enabling the organism to formulate and test predictive models that guide behavior. Such models serve as the foundation for commonsense reasoning and provide a starting point for understanding a much wider range of concrete and abstract systems, giving rise to a tendency in humans to attribute self-styled agency to both animate and inanimate objects.

To ground our discussion, we consider a personal assistant that works with a software engineer in the role of an apprentice learning on the job, as was common in the guilds and trade associations of medieval cities. The programmer’s apprentice we imagine here is a novice programmer but has the intuitive skills of an idiot savant, given that the apprentice has a suite of powerful programming tools as an integral part of its brain. These tools constitute the assistant’s body, its peripheral nervous system if you will.

The original programmer’s apprentice was the name of project initiated at MIT by Chuck Rich and Dick Waters and Howie Shrobe to build an intelligent assistant that would help a programmer to write, debug and evolve software. Our version of the programmer’s apprentice is implemented as an instance of a hierarchical neural network architecture. It has a variety of conventional inputs including speech, text and vision, as well as output modalities including the ability to run code and display program output and execution traces.

The programmer’s apprentice relies on multiple sources of input, including dialogue in the form of text utterances, visual information from an editor buffer shared by the programmer and apprentice and information from a fully instrumented integrated development environment (FIDE) designed for analyzing, writing and debugging code adapted to interface seamlessly with the apprentice as we might move our limbs or direct our gaze. As in case of the legs you were born with, the apprentice has to learn how to use its prosthetic extensions.

This input is processed by a collection of neural networks modeled after the primary sensory areas in the primate brain. The outputs of these networks feed into a hierarchy of additional networks corresponding to uni-modal secondary and multi-modal association areas that produce increasingly abstract representations as one ascends the hierarchy as illustrated in Figure 9.

Architecturally, the apprentice’s FIDE is an instance of a differentiable neural computer (DNC) introduced by Alex Graves and his colleagues at DeepMind. The assistant combined with its FIDE corresponds to a neural network that can read from and write to an external memory matrix, combining the characteristics of a random-access memory and set of memory-mapped device drivers and programmable interrupt controllers. The interface supports a fixed number of commands and channels that provide feedback.


---

# Figure 9

The architecture of the apprentice sensory cortex including the layers corresponding to abstract, multi-modal representations handled by the association areas can be realized as a multi-layer hierarchical neural network model consisting of standard neural network components. This graphic depicts these components as encapsulated in thought bubbles of the sort often employed in cartoons to indicate what some cartoon character is thinking. Analogously, the technical term “thought vector” is used to refer to the activation state of the output layer of such a component.

All of the bubbles appear to contain networks with exactly the same architecture, where one might expect sensory modality to dictate local architecture. The hierarchical architecture depicted here is modeled after the mammalian neocortex that appears to be tiled with columnar component networks called cortical columns that self-assemble into larger networks and adapt locally to accommodate their input. In practice, it may be necessary to engineer modality-specific networks for the lowest levels of the hierarchy — analogous to the primary sensory and motor areas of the neocortex, but more general-purpose networks for the higher levels in the hierarchy — analogous to the sensory and motor association areas.


---

The integrated development environment and its associated software engineering tools constitute an extension of the apprentice's capabilities in much the same way that a piano or violin extends a musician. The extension becomes an integral part of the person possessing it and over time their brain creates a topographic map that facilitates interacting with the extension. We expect the same to occur in the case of the assistant.

# 3.2 Conscious Attention

Stanislas Dehaene and his colleagues have developed a computational model of consciousness that provides a practical framework for thinking about consciousness that is sufficiently detailed for much of what an engineer might care about in designing digital assistants [49]. Dehaene’s work extends the Global Workspace Theory of Bernard Baars [11]. Dehaene’s version of the theory combined with Yoshua Bengio’s concept of a consciousness prior and deep reinforcement learning [126, 131] suggest a model for constructing and maintaining the cognitive states that arise and persist during complex problem solving [23].

Global Workspace Theory accounts for both conscious and unconscious thought with the primary distinction for our purpose being that the former has been selected for attention and the latter has not been so selected. Sensory data arrives at the periphery of the organism. The data is initially processed in the primary sensory areas located in posterior cortex, propagates forward and is further processed in increasingly-abstract multimodal association areas. Even as information flows forward toward the front of the brain, the results of abstract computations performed in the association areas are fed back toward the primary sensory cortex. This basic pattern of activity is common in all mammals.

Humans have a large frontal cortex that includes machinery responsible for conscious awareness and that depends on an extensive network of specialized neurons called spindle cells that span a large portion of the posterior cortex allowing circuits in the frontal cortex to sense relevant activity throughout this area and then manage this activity by creating and maintaining the persistent state vectors that are necessary when generating extended narratives or working on complex problems that require juggling many component concepts at once. Figure 10 suggests a neural architecture combining the idea of a global workspace with that of an attentional system for identifying relevant input.

These attentional networks are connected to regions throughout the cortex and are trained via reinforcement learning to recognize events worth attending to according to the learned value function. Using extensive networks of connections — both incoming and outgoing, attentional networks are able to create a composite representation of the current situation that can serve a wide range of executive cognitive functions, including decision making and imagining possible futures. The basic idea of a neural network trained to attend to relevant parts of the input is key to a number of the systems that we’ll be looking at.

In their paper [79] in Nature, the authors note that "there are interesting parallels between the memory mechanisms of a DNC and the functional capabilities of the mammalian hippocampus. DNC memory modification is fast and can be one-shot, resembling the associative long-term potentiation of hippocampal CA3 and CA1 synapses. The hippocampal dentate gyrus, a region known to support neurogenesis, has been proposed to increase representational sparsity, thereby enhancing memory capacity: usage-based memory allocation and sparse weightings may provide similar facilities." See the discussion of neurogenesis as an algorithmic technique in Box A.

The global workspace summarizes recent experience in terms of sensory input, its integration, abstraction and inferred relevance to the context in which the underlying information was acquired. To exploit the knowledge encapsulated in such experience, the apprentice must identify and make


---

# CONSCIOUSNESS PRIOR

# PREFRONTAL CORTEX

# ATTENTION REINFORCEMENT

# ASSOCIATION AREAS

# POSTERIOR CORTEX

# PRIMARY SENSORY AREAS

# FIDE API  DIALOG API  VISION API

Figure 10: The basic capabilities required to support conscious awareness can be realized in a relatively simple computational architecture that represents the apprentice’s global workspace and incorporates a model of attention that surveys activity throughout somatosensory and motor cortex, identifies the activity relevant to the current focus of attention and then maintains this state of activity so that it can readily be utilized in problem solving. In the case of the apprentice, new information is ingested into the model at the system interface, including dialog in the form of text, visual information in the form of editor screen images, and a collection of programming-related signals originating from a suite of software development tools. Single-modality sensory information feeds into multimodal association areas to create rich abstract representations. Attentional networks in the prefrontal cortex take as input activations occurring throughout the posterior cortex. These networks are trained by reinforcement learning to identify areas of activity worth attending to and the learned policy selects a set of these areas to attend to and sustain. This attentional process is guided by a prior that prefers low-dimensional thought vectors corresponding to statements about the world that are either true, highly probable or very useful for making decisions. Humans can sustain only a few such activations at a time. The apprentice need not be so constrained.


---

GLOBAL WORKSPACE

# DIFFERENTIABLE NEURAL COMPUTER

# CONTROLLER A

# ATTENTION

# ACTIVE MEMORIES

# CONTROLLER B

# EPISODIC MEMORY

Figure 11: You can think of the episodic memory encoded in the hippocampus and entorhinal cortex as RAM and the actively maintained memories in the prefrontal cortex as the contents of registers in a conventional von Neumann architecture. Since the activated memories have different temporal characteristics and functional relationships with the contents of the global workspace, we implement them as two separate NTM memory systems each with its own special-purpose controller. Actively maintained information highlighted in the global workspace is used to generate keys for retrieving relevant memories that augment the highlighted activations. While the associative keys required to access locations only partially match locations, they can still be used to guide attention allowing the NTM to recognize and even partially merge related locations. In general, locations in memory correspond to thought vectors that can be composed with other thought vectors to shape the global context for interpretation.

19



---

available relevant experience. The apprentice’s experience is encoded as tuples in an NTM that supports associative recall. We’ll ignore the details of the encoding process to focus on how episodic memory is organized, searched and applied to solving problems.

# 3.3 Action Selection

In both neuroscience and artificial intelligence, reinforcement learning problems are typically modeled as Markov decision problems (MDPs). While MDPs can be solved in polynomial time, the size of the state space is often prohibitively large, making practical solution intractable [113]. Hierarchical reinforcement learning offers a means of reducing the computational burden by decomposing the state space resulting in a relatively small number of tractable MDPs each of which can be solved independently [97, 54, 91]. However, the problem of finding an optimal decomposition is itself intractable and hence it is necessary to resort heuristic methods and approximate solutions.

There exist a number of approaches that develop solutions to the problem of hierarchical reinforcement learning (HRL) employing various decomposition strategies, several of which we draw inspiration from [132, 5, 157, 107, 15, 127, 144] including a few that relate to biological or biologically plausible models [149, 55, 64, 150]. It’s important to keep in mind that we are dealing a partially-observable, high-dimensional, continuous state space, and an action space that includes abstract cognitive activities in addition to concrete physical activities that engage the motor system in interacting with the environment.

In the treatment here, we emphasize the problem of life-long learning as it relates to the non-stationarity of underlying process as a consequence of changes in the external environment and changes in the goals of the agent and the neural substrate available for computation during development and extending on into adulthood. In the case of a growing infant, the changes involve the appearance and maturation of critical circuits and the limitations of finite memory. In both human and machine, internal representations progress from concrete to abstract, building on a foundation grounded in the environment. This maturation in cognitive capability is accelerated by a curriculum that takes advantage of dependencies between concepts.

The network model shown in Figure 12 illustrates a system that takes as input a pattern of neural activity originating in the medial temporal and inferior parietal cortex and selects an action to perform. This particular example is meant to illustrate how episodic memory might play an expanded role in action selection. For illustration, patterns of activity serve as proxies for the state of the external environment and are represented in the figure as a sequence st, st−1, st−2, .... The subnetworks labeled A and B are relatively straightforward multilayer neural networks that compute features and generate representations as their output. Network A takes as input a representation of the current state, and generates a representation of the context for action selection.

We’ll explain the function of the box labeled M in a moment; assume for now that it generates a representation of the options available for acting in the current context. Network B then takes these suggestions as input and produces as output a representation of the selected action. The boxes labeled C, D, E and F are controllers for two differentiable neural computer (DNC) units that provide storage and access for short-term and long-term memory respectively. The controllers on the left are part of the online system for selecting actions. The controllers on the right are responsible for off-line training during which the recorded actions, along with their associated states and rewards are consolidated in long-term memory using experience replay.

The blue boxes represent stored information in the form of key-value pairs. Each key is associated with a subset or subspace of the set of all states that represents a restricted domain of expertise for selecting actions. The value for this key is a function implemented as a network trained as an expert for the associated subspace. K is an embedding network that takes as input a sequence of states.


---

# NEW PATTERN (OUTPUT)

# ERROR SIGNAL

# INHIBITORY CONNECTIONS

St S t-1 ' t-2

# NEW PATTERN (INPUT)

# RANDOM INPUT

Figure 12: The network shown here takes as input a pattern of activation originating in the temporal and parietal lobes and selects an action to perform.

The subnetworks labeled A and B are relatively straightforward multilayer neural networks that compute features and generate representations as their output. Network A takes as input a representation of the current state, and generates a representation of the context for action selection. Network K is an embedding network that takes as input a sequence of states corresponding to recent activity and generates as output a unique key associated with a subspace of the full MDP state space that includes the current state.

The box labeled M corresponds to a location in working memory. The networks C, D, E and F are controllers for two differentiable neural computer (DNC) peripherals that provide storage and access for short-term and long-term memory respectively. The long-term memory is used to store the weights for networks that encode architecturally identical networks — only the weights are different — providing specialized expertise in restricted domains corresponding to subspaces of the full MDP state space.

The model operates in two modes. In each cycle during the online mode, the C controller loads the selected expert network into location M where it is fed the output of A and produces the input to B. In this mode, the short-term memory is used to record activity traces that are subsequently used in the offline mode to update the networks stored in long-term memory. The network in the lower-right inset implements a version of pseudo rehearsal as a means of mitigating catastrophic forgetting [65].


---

corresponding to recent activity and generates as output a unique key associated with a subspace of the current state. A given state can belong to more than one subspace and the particular key selected at any given point in time depends on the current state and the immediately previous states in a fixed window. The order of the states matters.

In the online phase, the embedding network retrieves this key which it forwards to the controller labeled C that uses it to retrieve the expert for the relevant subspace. The box labeled M corresponds to a location in working memory and in each online cycle the C controller loads the expert subsystem in location M of working memory where it can be utilized to compute a set of options appropriate for the current state. During off-line periods the system uses the recorded sequences of activity to run some variant of experience replay to update the relevant expert subsystems stored in long term memory [6, 161, 112].

The training that occurs offline involves adjusting the weights of networks using relatively small samples and so runs the risk of catastrophic interference in transfer learning [120]. One way in which we hope to ameliorate the adverse consequences of catastrophic interference is by defining separate networks for separate subspaces. The embedding space method mentioned in describing K is designed to isolate expertise by identifying states that tend to occur together. The hope is that the actions exercised in such states will tend to be interrelated and hence they should be represented using the same network to facilitate their coordination.

Of course temporal proximity in their occurrence doesn’t guarantee they serve the same task since we are always getting distracted or interrupted requiring us to interleave tasks that have very little to do with one another. It may be possible to segment activity streams into coherent tasks in a similar way to how we segment conversations involving multiple speakers [165, 166]. Alternatively, there has been some success with the method of pseudo rehearsal which consists of retraining existing networks by interleaving new examples with synthetic-examples produced by randomly activating the existing network [37, 100, 8, 65, 66, 151].

In this model the STM roughly corresponds to the hippocampus as the storage system for episodic memory. The LTM resembles the cerebellum in the way that it essentially compiles prior activity to construct a set of programs each of which spans some portion of the overall state space. As described above, the STM is only used for temporary storage awaiting off-line replay to consolidate recent memories. An alternative is to maintain a much larger collection of episodic memories that can be used in a manner similar to that suggested in Gershman and Daw who posit that we routinely draw upon our stored memories in the hippocampus to figure out what to do in novel situations not covered by our other sources of procedural knowledge [71]. See Box B for more detail concerning episodic memory and experience replay.

# Box B: Replaying Experience, Consolidating Memory

When we encounter a new experience in the environment, we do not act independently of the past, but rather, our past experiences substantially inform our present decisions. Here, we introduce the basic principles of hippocampal replay and a few key ways in which it has motivated reinforcement learning algorithms.

Replay is the process by which hippocampal representations of previous experiences are sequentially reactivated [35]. Studies show that cells in the rodent hippocampus replay past experiences to stabilize behaviorally relevant memories [135, 96]. Though initially observed in spatial tasks, recent work suggests that non-spatial task states are also replayed, and that this


---

phenomenon is common in humans [164]. In the reinforcement learning literature, the experience replay algorithm was introduced as an analogical framework in online learning agents [112]. Transitions containing state, action, and reward information are sequentially stored in memory and sampled randomly for learning. Randomly replaying old memories not only allows decorrelation of consecutive experiences encountered during data collection, but also enables reuse of training data, increasing sample efficiency, and encourages resampling of rare experiences, potentially alleviating forgetting.

A relatively well-studied question is what to replay. Some studies suggest the correlation of replay frequency with novelty approximated by temporal difference (TD) error [63], and others with high reward [135]. In particular, dopaminergic release, which encodes both novelty and reward [123], enhances sharp wave-ripple activation — the basic unit of replay. Yet other studies show that experiences more vulnerable to forgetting are more likely to be replayed [160]. While the exact selection algorithm is unknown, the observed association with novelty inspired the prioritized experience replay algorithm which samples experiences with probabilities weighted by their TD errors and is now consistently preferred to the originally proposed uniform sampling variant [161].

The significantly less studied question is what happens during replay. Besides re-learning of experiences, many neuroscientists support the idea that replay also serves as a substrate for memory consolidation — the gradual integration of new experiences processed into existing knowledge representations in the neocortex [184, 120, 98, 21, 108], as to stabilize memories against interference. The idea is that replaying information stored in memory will encourage synaptic consolidation processes.

While we lack a precise understanding of the underlying mechanisms of consolidation in the brain, in our architecture we frame consolidation as the process by which experiences are used to update expert subsystems stored in long-term memory. We propose an adaptive replay algorithm whereby experiences with contexts similar to the current context are replayed and thus preferentially consolidated into long-term storage. Since action selection directly depends on the relevant expert network drawn from long-term memory, we can ensure to maximally update the currently relevant expert network with existing memories related to its corresponding context. This algorithm is partly inspired by the result by [96] whereby they observed that when a rat pauses at a branching point in a maze, it replays representations of trajectories in the past with similar context to drive its present decision-making.

There exist many other cognitively inspired variants of experience replay. One example is hindsight experience replay [6], where the agent pretends that whatever state it reaches had been the goal state from the start and learns from the experience regardless of whether it actually succeeded, just as humans can learn from undesirable outcomes. In this case, the LTM stores what can be thought of as subroutines or libraries for solving routine problems. Used in the manner described in Gershman and Daw [71], the DNC labeled STM more closely captures the functionality of the hippocampus in combining short-term and long-term episodic memories with specific procedural knowledge based on past experience that may or may not be common enough to warrant compiling as a standalone library. The dentate gyrus is best known for its ability to separate patterns to avoid mistaking one pattern for another. Less well understood is a possible complementary role that involves integrating similar patterns.

The ability to draw upon episodic memory to select what to do in situations similar to those encountered in the past provides a simple form of one-shot learning. It could enable us to make


---

predictions, perform hypothetical reasoning and put ourselves in someone else’s shoes assuming that our ability to retrieve memories allows us match situations that we find ourselves that we haven’t experienced, but know from someone else’s experience. It might avoid some of the problems with interference if the process of integrating new procedural knowledge with old could be spread out over longer periods if, say, each time you encounter a similar situation you make only minor adjustments to the weights of the associated subspace expert network.

# 3.4 Executive Control

There is a growing consensus and a fair bit of evidence to support the hypothesis that the human frontal cortex is in charge of executive control, goal-directed planning and abstract thinking. There are differences in opinion about how these cognitive processes are implemented and how they co-ordinate their activities with that of the rest of the brain. One thing that seems clear is that the frontal cortex and in particular the prefrontal cortex employs many of the same strategies as do networks elsewhere in the brain, both cortical and subcortical.

In particular, circuits in the prefrontal cortex recapitulate the coarse-to-fine, concrete-to-abstract feature hierarchies that we see in the sensory, motor and somatosensory cortex. They exhibit the profuse reciprocal recurrent connections between levels of abstraction that enable us to generalize on the basis of relatively small amounts of information, learn to make accurate predictions in an unsupervised manner depending on observations and interactions with the environment to ground our conclusions, and that provide the foundation for constructing a rich repertoire of representations that serve decision-making.

The neural correlates of abstract thinking, including the circuits that enable us to solve practical problems as well as pursue pure mathematics, are generally agreed to be located in the prefrontal cortex with reciprocal connections throughout the rest of the cerebral cortex, the cerebellar cortex and subcortical regions including the basal ganglia, hippocampal formation and parts of the limbic system involved with emotion, motivation and episodic memory. See Box C for more detail regarding abstraction, hierarchy and executive oversight in the prefrontal cortex.

# Box C: Hierarchy, Abstraction and Executive Control

The prefrontal cortex (PFC) is generally considered to be responsible for executive cognitive control and enabling the synthesis of novel behavior. Here, we briefly review prefrontal anatomy, development and physiology, focusing on three key executive cognitive functions: attentional set, working memory and action selection. For each function, we suggest how our current understanding might lead to new architectures and algorithms for AI systems.

The PFC sits atop a group of hierarchically organized sensory and motor areas in the cortex enforced through reciprocal anatomical connections [69]. This arrangement, referred to as Fusters hierarchy, motivates computational models of the PFC that posit the development of highly abstract representations of the sensorimotor context that can be used understand what we perceive and direct how we act [29]. In addition to connections between layers, Fusters hierarchy stipulates reciprocal connections between sensory and motor areas of cortex at the same level of abstraction within each layer of the hierarchy. This intralayer connectivity between perception and motor suggests that action representations feed back into and enhance perception, a principle codified in the notion of corollary discharge [121].


---

suggests that each layer of the hierarchy along with the layers below but excluding those above, forms a self-contained perception-action loop. Evidently the neocortex undergoes a series of developmental stages with the PFC among the last areas to mature [82]. This implies training of a complex agent may need to unfold in a manner akin to greedy layer-wise deep network training [24, 20], with developmentally-staged, abstraction-comparable, layer-wise learning of the coupled sensorimotor features.

Attentional set (ASET) refers to the preparation of downstream perception and motor cortices for expected stimuli or action. ASET is exhibited in cued-attention tasks where, in anticipating a visual stimuli, PFC and V4 will be active before the stimuli is given [171]. ASET suggests existing inhibitory attention masks may be augmented with additive excitatory attention, allowing a neural network to reduce bottom-up input needed for neuron stimulation or cause neuron firing in the absence of sensory input altogether. Allowing the controller to generate new patterns via network activation even suggests a new model of imagination, with improvements in both sensory synthesis [80] and planning [143].

Working memory is the maintenance of recent stimuli for subsequent action planning. Working memory consists of groups of coupled neural circuits in the PFC called stripes that are connected to potential target stimuli in sensory cortex and access controlled by circuits in the basal ganglia. Computational models of working memory [90] include implementations similar to the recurrent memory circuit of an LSTM cell [92], more exotic architectures involving stacked LSTMs [77] and multiple memory stripes manipulated by a central controller.

In action selection, the PFC generates many actions that are approved or denied by the basal ganglia; both basal ganglia and orbitomedial PFC receive dopaminergic afferents originating in midbrain structures, providing a reward signal that reinforces learning [69]. Computational models of dopaminergic systems [139] point to an architecture similar to existing actor-critic models [125]; a key improvement is the modeling of reward inhibition, whereby learning ceases for repetitive stimuli. Suppression of reward to prevent response overfitting could aid in tackling other problems such as reward hacking [4], catastrophic forgetting, and lifelong learning [37], all challenges in effectively managing the learning process.

With respect to hierarchical goal-based planning, there is growing evidence pointing to a set of adjoining regions in the prefrontal cortex that are responsible for how abstract plans are initially selected, subsequently refined and finally realized as concrete actions. These same regions also appear to be involved in relational reasoning from simple binary relations to higher-order relationships. These theoretical observations combined with behavioral studies and fMRI recordings have led to a number of computational models of hierarchical planning that exhibit similar patterns of cognitive activity. In particular, cognitive neuroscientists have developed models of how such abstract hierarchical reasoning in the prefrontal cortex is related to what we know about how the basal ganglia and areas of the limbic system involved in motivation contribute to action selection [136].

The network shown on the right in Figure 13 consists of three subnetworks that roughly align with the lateral frontal polar cortex (bottom), dorsolateral prefrontal cortex (middle) and anterior premotor cortex (top) as shown in the figure. Each of the subnetworks is composed of three elements: a recurrent multilayer perceptron constructed of interleaved convolutional and max-pooling layers shown in orange, a multilayer attention network shown in green and a masking layer in blue that selectively suppresses a subset of the outputs of the convolutional stack in accordance with the output of the attention network.

Input to each of the three subnetworks includes areas of associative activity throughout the


---

APMC DPFC LFPC

# Figure 13

The panel on the left highlights three areas of the prefrontal cortex shown in the figure from left to right (rostro-caudal) and referred to in the text as the lateral frontal polar cortex (LFPC), dorsolateral prefrontal cortex (DPFC), and anterior premotor cortex (APMC). According to the theory first articulated by Joaquín Fuster and subsequently refined by David Badre [13], Mark D’Esposito [52], and Etienne Koechlin et al [102] and their colleagues, as actions are specified from abstract plans to concrete responses, progressively posterior regions of the lateral frontal cortex are responsible for integrating more concrete information over more proximate time intervals. This process of progressive articulation does not correspond to different stages of execution so much as to how actions are selected, maintained, and inhibited at multiple levels of abstraction [14].

The panel on the right shows a simple neural-network model of the brain regions aligned with the rostro-caudal axis of the frontal cortex and hypothesized to account for how action representations are selected, maintained, and inhibited at multiple levels of abstraction. The neural-network model is described in more detail in the main text, but a few points are in order here:

- A — different abstraction layers may include input from other sources, e.g., natural language embeddings, that are only required at particular levels of abstraction;
- B — each recurrent level of the abstraction hierarchy includes state variables encoding information that would typically appear on the call stack in a conventional computer architecture;
- C — attentional layers mask (suppress) input that is not determined to be relevant to decision making at a given time and level of abstraction resulting in a sparse context vector.


26

---

sensory and motor cortex as well as areas corresponding to higher-level abstractions located in the frontal cortex responsible for abstract thought and subcortical regions responsible for motivation. While not emphasized here, the active maintenance in working memory of information originating from these sources is critical for the cognitive activities that these networks support [42, 75]. The outputs are fed to a network (not shown) that serves as the interface for the peripheral motor system (the fully instrumented integrated development environment (FIDE) in the case of the programmer’s apprentice) which could play the role of the basal ganglia and cerebellum, but could also be considerably simpler depending on the application.

Figure 13 is just a sketch employing familiar neural network components to make the point that building these architectures out of standard components is not the most significant challenge. The real challenge is in training them as part of larger system with lots of moving parts. The expectation here, as in the model sketched in Figure 12, is that end-to-end training with stochastic gradient descent isn’t going to work, and that training will likely require some form of layer-by-layer developmentally-staged curriculum learning [147, 83, 22, 25] and a strategy for holding some weights fixed while adjusting other weights to account for new information and avoid problems like catastrophic forgetting.

# 3.5 Digital Assistants

We focus on automated programming for several reasons: deep neural networks have recently demonstrated progress on automated code synthesis and program repair by leveraging existing technologies; computers and, in particular, modern integrated development environments present a rich alternative to the dominant simulation environments; programming is challenging for humans and machines alike and we foresee opportunities to increase the productivity of software engineers. That said, in this section we emphasize basic tools that enable the assistant to encode, represent and manipulate fully differentiable programs.

The integrated development environment and its associated software engineering tools constitute an extension of the apprentices capabilities in much the same way that a piano or violin extends a musician or a prosthetic limb extends someone who has lost an arm or leg. The extension becomes an integral part of the person possessing it and over time their brain creates a topographic map that facilitates interacting with the extension.

As engineers designing the apprentice, part of our job is to create tools that enable the apprentice to learn its trade and eventually become an expert. Conventional IDE tools simplify the job of software engineers in designing software. The fully instrumented IDE (FIDE) that we engineer for the apprentice will be integrated into the apprentices cognitive architecture so that tasks like stepping a debugger or setting breakpoints are as easy for the apprentice as balancing parentheses and checking for spelling errors in a text editor is for us.

As a first step in simplifying the use of FIDE for coding, the apprentice is designed to manipulate programs as abstract syntax trees (AST) and easily move back and forth between the AST representation and the original source code in collaborating with the programmer. Both the apprentice and the programmer can modify or make references to text appearing in the FIDE window by pointing to items or highlighting regions of the source code. The text and AST versions of the programs represented in the FIDE are automatically synchronized so that the program under development is forced to adhere to certain syntactic invariants.

To support this hypothesis, we are developing distributed representations for programs that enable the apprentice to efficiently search for solutions to programming problems by allowing the apprentice to easily move back and forth between the two paradigms, exploiting both conventional approaches to program synthesis and recent work on machine learning and inference in artificial neu-


---

# Figure 14

We use pointers to represent programs as abstract syntax trees and partition the NTM memory, as in a conventional computer, into program memory and a LIFO execution (call) stack to support recursion and reentrant procedure invocations, including call frames for return addresses, local variable values and related parameters. The NTM controller manages the program counter and LIFO call stack to simulate the execution of programs stored in program memory. Program statements are represented as embedding vectors and the system learns to evaluate these representations in order to generate intermediate results that are also embeddings. It is a simple matter to execute the corresponding code in the FIDE and incorporate any of the results as features in embeddings.


---

# Figure 15

This slide illustrates how we make use of input / output pairs as program invariants to narrow search for the next statement in the evolving target program. At any given moment the call stack contains the trace of a single conditioned path through the developing program. A single path is unlikely to provide sufficient information to account for the constraints implicit in all of the sample input / output pairs and so we intend to use a limited lookahead planning system to sample multiple execution traces in order to inform the prediction of the next program statement. These so-called imagination-augmented agents implement a novel architecture for reinforcement learning that balances exploration and exploitation using imperfect models to generate trajectories from some initial state using actions sampled from a rollout policy [143, 180, 85, 81]. These trajectories are then combined and fed to an output policy along with the action proposed by a model-free policy to make better decisions. There are related reinforcement learning architectures that perform Monte Carlo Markov chain search to apply and collect the constraints from multiple input / output pairs.

Neural Turing Machines coupled with reinforcement learning are capable of learning simple programs [78]. We are interested in representing structured programs expressed in modern programming languages. Our approach is to alter the NTM controller and impose additional structure on the NTM memory designed to support procedural abstraction.

# What could we do with such a representation?

It is important to understand why we don't work with some intermediate representation like bytecodes. By working in the target programming language, we can take advantage of both the abstractions afforded by the language and the expert knowledge of the programmer about how to exploit those abstractions. The apprentice is bootstrapped with several statistical language models: one trained on a natural language corpus and the other on a large code repository. Using these resources and the means of representing and manipulating program embeddings, we intend to train the apprentice to predict the next expression in a partially constructed program by using a variant of imagination-based planning [143]. As another example, we will attempt to leverage NLP methods to generate proposals for substituting one program fragment for another as the basis for code completion.

The Differentiable Neural Program (DNP) representation and associated NTM controller for managing the call stack and single-stepping through such programs allow us to exploit the advantages of distributed vector representations to predict the next statement in a program under construction. This model makes it easy to take advantage of supplied natural language descriptions and example input / output pairs plus incorporate semantic information in the form of execution traces generated by utilizing the FIDE to evaluate each statement and encoding information about.


---

Figure 16: The above graphic illustrates how we might adapt the imagination-based planning (IBP) for reinforcement learning framework [143] for use as the core of the apprentice code synthesis module. Actions in this case correspond to transformations of the program under development. States incorporate the history of the evolving partial program. Imagination consists of exploring sequences of program transformations.

local variables on the stack.

The imagination-based planning (IBP) for reinforcement learning framework [143] serves as an example for how the code synthesis module might be implemented. The IBP architecture combines three separate adaptive components: (a) the controller + memory system which maps a state s ∈ S and history h ∈ H to an action a ∈ A; (b) the manager maps a history h ∈ H to a route u ∈ U that determines whether the system performs an action in the compute environment, e.g., single-step the program in the FIDE, or performs an imagination step, e.g., generates a proposal for modifying the existing code under construction; the imagination model is a form of dynamical systems model that maps a pair consisting of a state s ∈ S and an action a ∈ A to an imagined next state s′ ∈ S and scalar-valued reward r ∈ R.

The imagination model can be implemented as an interaction network [17] or using the graph-networks framework [18, 158]. The three components are trained by three distinct, concurrent, on-policy training loops. The IBP framework shown in Figure 16 allows code synthesis to alternate between exploiting by modifying and running code, and exploring by using the model to investigate and analyze what would happen if you actually did act. The manager chooses whether to execute a command or predict (imagine) its result and can generate any number of trajectories to produce a tree ht of imagined results. The controller takes this tree plus the compiled history and chooses an action (command) to carry out in the FIDE.

# 3.6 End-to-End Systems

The subsections that comprise this section of the paper very roughly account for the functional systems of the human brain. Admittedly perception is given short shrift and the systems that deal with emotion and motivation are hardly mentioned at all, the former to save space and the latter because it isn’t particularly relevant.


---

In addition, there was no effort made to map the artificial neural networks described in this section onto the biological subsystems discussed in Section 2. The goal was to demonstrate how one might build systems that exhibit some desirable cognitive characteristics of human intelligence by leveraging ideas from neuroscience.

The PBWM (prefrontal cortex, basal ganglia, working memory) model described in [138, 90] covers territory that we only sample from, but the PBWM was developed to explain the function of biological brains, not selectively borrow ideas to extend the capabilities of artificial neural networks.

In a complete end-to-end architecture implementing the programmer’s apprentice, the three subsystems described in this subsection would have to be integrated into different parts of the action selection and executive control systems:

- The system in Figure 14 illustrates a differentiable procedural abstraction rich enough to support structured programming in a connectionist setting using standard embedding techniques and memory networks [181, 44, 78, 79].
- The system in Figure 15 provides a sketch of how one might train a language model to predict the next statement in a program under construction using input / output pairs or other program invariants to constrain search [38, 178, 167, 53].
- The system in Figure 16 shows how a variation of imagination-based planning might be used to train a network to predict the next program state using the embodied integrated development environment as a source of ground truth [180, 143, 85].

Exactly how and where these components might be integrated into the overall architecture is beyond the scope of this paper, but research on the neural correlates of mathematical reasoning may provide some useful clues where to start [48, 50, 3].

# 4 Discussion

Training the models described in this paper is a daunting challenge, especially when you consider that current deep neural network technologies rely heavily on large amounts of labeled data and applications like the programmer’s apprentice are particularly vulnerable to catastrophic forgetting. We believe training will require radically new approaches and that cognitive and developmental neuroscience have much to offer in terms of insights drawn from the study of how humans learn.

# 4.1 Child Development

The human brain is organized as a 3-D structure in which specific cell types are positioned in a radial, laminar and areal arrangement that depends on the production, specialization and directed migration of cells from their origin in the embryo to their final destination [148]. It is only on arriving at their final location that they establish connections to other cells. Postnatally laminar and areal differentiation exhibit substantial differences between early (2-3 months) and late (7-12 months) infancy [128, 105]. Functional organization begins early (2-3 months) even as construction continues and the shaping of cortical circuits reflects the consequences of increasingly complex behavior.

All of this carefully orchestrated activity is critical to development. Early brain structures appear as a consequence of the simple reflexive behaviors the infant engages in, laying the foundation for more coordinated behavior depending on increasingly complex internal representations. The infant’s ability to engage its environment broadens, exposing it to more complicated stimuli and

31


---

The opportunity to experiment with new behaviors. The physical and social environment seem to conspire to ensure that the growing infant and then adolescent has the necessary physical and intellectual prerequisites in place when exposed to circumstances that require them. It may be that we will find it useful to recapitulate some version of these developmental strategies for training architectures patterned after the human brain.

# 4.2 Inductive Bias

Most AI systems are trained assuming what is essentially a blank slate in the form of random weights and objective functions that do little to influence the specific content of what is actually learned. In contrast, babies are born with an innate understanding of how objects move around and interact with one another [51]. Before they can even crawl about on their own, they appear to have an intuitive understanding of how space, time and number are interrelated [45, 87]. The bodies, neural architectures, physical and social environments of mammals provide a strong inductive bias in shaping their brains. Prolonged development plays a particularly important role in humans. Most mammals can stand and move about within hours of being born. Many human babies don’t walk until just under one year. However, human infants learn a great deal during this early preperambulatory developmental period, much of it in preparation for subsequent stages of development [115, 152].

It would be difficult if not impossible to genetically encode what a child learns during its lengthy development. And so it seems plausible that evolution would select for a compact general inductive bias enabling us to quickly acquire the basic skills we need to survive while retaining sufficient neural plasticity so that we can adapt to changes during our lifetimes. The schedule of developmental milestones necessary to learn these skills is highly conserved within our species and punctuated by profound changes in the architecture of the brain.

At birth, the architectural foundations are in place to construct the adult brain. For each subsequent developmental milestone, our genes turn on the specific cellular machinery necessary to construct scaffolding, guide neurons of the right cell types to their terminal locations, extend axonal and dendritic processes, eliminate unnecessary neurons and establish new or prune existing synaptic connections. The innate inductive bias and training curriculum implicit in development influence two critical factors that determine human intelligence: First, they serve to initialize the mapping from body to latent state representations throughout the cortex thereby grounding experience in the physical environment. Second, they utilize this grounding as the basis for all subsequent understanding, concrete and abstract.

This basis provides a template or prototype for representing new concepts, whether they be predictive models that allow us to interact with complex dynamical systems or composite categorical representations that enable us to recognize, contrast and compare instances of a particular class of entities [153, 154, 173]. In designing architectures to accommodate learning such representations, recent work on learning relational models that characterize different classes of entities, the relationships they participate in and the rules employed in composing them to form new relationships seems particularly promising [158, 84, 159, 17]. This core competency should also serve as the starting point for reasoning about all sorts of abstract entities including computer programs and mathematical objects.

# 4.3 Natural Language

The use of language and, more generally, symbolic reasoning is an important if not defining characteristic of human intelligence. Some cognitive scientists, including such outspoken proponents as


---

Jerry Fodor and Zenon Pylyshyn, view symbolic representations that exhibit combinatorial syntactic and semantic structure as candidates for a language of thought, and view connectionist proposals as lacking these properties and serving primarily as an account of the neural structures in which symbolic representations are implemented [62, 61]. O’Reilly et al [142] have attempted to reconcile the symbolic and connectionist views, arguing that the two are complementary and that parts of the brain exhibit properties of both symbolic and connectionist information processing.

The evolutionary biologist, Terrence Deacon, argues that our use of language is not a direct consequence of natural selection but rather the result of a collective effort involving millions of human beings working over thousands of years to produce an encyclopedic record of human endeavor to pass down to future generations [46]. It is hard to imagine an effective programmer’s apprentice, much less an accomplished software engineer, lacking the ability to communicate in natural language or denied access to the written word. Recent progress in grounding language learning in an agent’s experience interacting with a suitably complex environment bodes well for applications like the programmer’s apprentice. For these reasons and more, we see the rich complexity of collaborative pair programming as a compelling framework for exploring human-level AI.

# References

1. J. B. Aimone, J. Wiles, and F. H. Gage. Computational influence of adult neurogenesis on memory encoding. Neuron, 61(2):187–202, 2009.
2. James B. Aimone, Wei Deng, and Fred H. Gage. Resolving new memories: A critical look at the dentate gyrus, adult neurogenesis, and pattern separation. Neuron, 70(4):589–596, 2011.
3. Marie Amalric and Stanislas Dehaene. Origins of the brain networks for advanced mathematics in expert mathematicians. Proceedings of the National Academy of Sciences, 113(18):4909–4917, 2016.
4. Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Mané. Concrete problems in ai safety. arXiv preprint arXiv:1606.06565, 2016.
5. Jacob Andreas, Dan Klein, and Sergey Levine. Modular multitask reinforcement learning with policy sketches. CoRR, arXiv:1611.01796, 2016.
6. Marcin Andrychowicz, Filip Wolski, Alex Ray, Jonas Schneider, Rachel Fong, Peter Welinder, Bob McGrew, Josh Tobin, Pieter Abbeel, and Wojciech Zaremba. Hindsight experience replay. CoRR, arXiv:1707.01495, 2017.
7. Natalie Angier. Insights From the Youngest Minds. Feature article on Elizabeth Spelke in the New York Times, April 30, 2012, 2012.
8. Bernard Ans, Stéphane Rousset, Robert French, and Serban Musca. Preventing catastrophic interference in multiple-sequence learning using coupled reverberating elman networks. Proceedings of the 24th Annual Meeting of the Cognitive Science Society, 2002.
9. Dirk Jan Ardesch, Lianne H. Scholtens, Longchuan Li, Todd M. Preuss, James K. Rilling, and Martijn P. van den Heuvel. Evolutionary expansion of connectivity between multimodal association areas in the human brain compared with chimpanzees. Proceedings of the National Academy of Sciences, 116(14):7101–7106, 2019.


---

# References

1. B.R. Arenkiel. Neural Tracing Methods: Tracing Neurons and Their Connections. Springer New York, 2014.
2. B. J. Baars. A cognitive theory of consciousness. Cambridge University Press, New York, NY, 1988.
3. Alan Baddeley. Modularity, mass-action and memory. The Quarterly Journal of Experimental Psychology Section A, 38(4):527–533, 1986.
4. D. Badre and A. D. Wagner. Selection, integration, and conflict monitoring; assessing the nature and generality of prefrontal cognitive control mechanisms. Neuron, 41(3):473–487, 2004.
5. David Badre. Cognitive control, hierarchy, and the rostrocaudal organization of the frontal lobes. Trends in Cognitive Sciences, 12(5):193–200, 2008.
6. Bram Bakker and Jürgen Schmidhuber. Hierarchical reinforcement learning based on subgoal discovery and subpolicy specialization. In Proceedings of the 8th Conference on Intelligent Autonomous Systems, pages 438–445, 2004.
7. Horace B. Barlow. Unsupervised learning. Neural Computation, 1:295–311, 1989.
8. Peter Battaglia, Razvan Pascanu, Matthew Lai, Danilo Jimenez Rezende, and Koray Kavukcuoglu. Interaction networks for learning about objects, relations and physics. In Proceedings of the 30th International Conference on Neural Information Processing Systems, pages 4509–4517. Curran Associates Inc., 2016.
9. Peter W. Battaglia, Jessica B. Hamrick, Victor Bapst, Alvaro Sanchez-Gonzalez, Vinicius Zambaldi, Mateusz Malinowski, Andrea Tacchetti, David Raposo, Adam Santoro, Ryan Faulkner, Caglar Gulcehre, Francis Song, Andrew Ballard, Justin Gilmer, George Dahl, Ashish Vaswani, Kelsey Allen, Charles Nash, Victoria Langston, Chris Dyer, Nicolas Heess, Daan Wierstra, Pushmeet Kohli, Matt Botvinick, Oriol Vinyals, Yujia Li, and Razvan Pascanu. Relational inductive biases, deep learning, and graph networks. CoRR, arXiv:1806.01261, 2018.
10. S. Becker. A computational principle for hippocampal learning and neurogenesis. Hippocampus, 15(6):722–738, 2005.
11. Eugene Belilovsky, Michael Eickenberg, and Edouard Oyallon. Greedy layerwise learning can scale to imagenet. arXiv preprint arXiv:1812.11446, 2018.
12. Daniel Bendor and Matthew A Wilson. Biasing the content of hippocampal replay during sleep. Nature neuroscience, 15(10):1439, 2012.
13. Samy Bengio, Oriol Vinyals, Navdeep Jaitly, and Noam Shazeer. Scheduled sampling for sequence prediction with recurrent neural networks. CoRR, arXiv:1506.03099, 2015.
14. Yoshua Bengio. The consciousness prior. CoRR, arXiv:1709.08568, 2017.
15. Yoshua Bengio, Pascal Lamblin, Dan Popovici, and Hugo Larochelle. Greedy layer-wise training of deep networks. In Advances in Neural Information Processing Systems 19, pages 153–160. MIT Press, Cambridge, MA, 2007.


---

[25] Yoshua Bengio, J´erˆome Louradour, Ronan Collobert, and Jason Weston. Curriculum learning. In Proceedings of the 26th Annual International Conference on Machine Learning, pages 41–48, New York, NY, USA, 2009. ACM.

[26] J. R. Binder and R. H. Desai. The neurobiology of semantic memory. Trends in Cognitive Science, 15(11):527–536, 2011.

[27] Peter Blouw and Chris Eliasmith. A neurally plausible encoding of word order information into a semantic vector space. In 35th Annual Conference of the Cognitive Science Society, pages 1905–1910, 2013.

[28] Matthew Botvinick and James An. Goal-directed decision making in prefrontal cortex: A computational framework. Advances in Neural Information Processing Systems, 21:169–176, 2009.

[29] Matthew M. Botvinick. Multilevel structure in behaviour and in the brain: a model of fuster’s hierarchy. Philosophical transactions of the Royal Society of London. Series B, Biological sciences, 362:1615–1626, 2007.

[30] Edward Boyden. A history of optogenetics: the development of tools for controlling brain circuits with light. F1000 Biology Reports, 3, 2011.

[31] Holly Bridge and Stuart Clare. High-resolution MRI: in vivo histology? Philosophical transactions of the Royal Society of London. Series B, Biological sciences, 361:137–146, 2006.

[32] Korbinian Brodmann. Vergleichende Lokalisationslehre der Grosshirnrinde in ihren Prinzipien dargestellt auf Grund des Zellenbaues. Johann Ambrosius Barth Verlag, Leipzig, 1909.

[33] R.B. Buxton, K. Uludag, D.J. Dubowitz, and T.T. Liu. Modeling the hemodynamic response to brain activation. Neuroimaging, 23:220–233, 2004.

[34] Edward M. Callaway. Transneuronal circuit tracing with neurotropic viruses. Current opinion in neurobiology, 18:617–623, 2008.

[35] Margaret F Carr, Shantanu P Jadhav, and Loren M Frank. Hippocampal replay in the awake state: a potential substrate for memory consolidation and retrieval. Nature neuroscience, 14(2):147, 2011.

[36] X. Chen, Y. Mu, Y. Hu, A. T. Kuan, M. Nikitchenko, O. Randlett, A. B. Chen, J. P. Gavornik, H. Sompolinsky, F. Engert, and M. B. Ahrens. Brain-wide Organization of Neuronal Activity and Convergent Sensorimotor Transformations in Larval Zebrafish. Neuron, 100(4):876–890, 2018.

[37] Zhiyuan Chen and Bing Liu. Continual learning and catastrophic forgetting. In Lifelong Machine Learning, Second Edition, volume 12 of Synthesis Lectures on Artificial Intelligence and Machine Learning, pages 1–207. Morgan &#x26; Claypool Publishers, 2018.

[38] Alex Polozov, Marc Brockschmidt, Rishabh Singh, Chenglong Wang, Po-Sen Huang. Execution-guided neural program decoding. CoRR, arXiv:1807.03100, 2018.

[39] Ana B. Chica, Michel Thiebaut de Schotten, Paolo Bartolomeo, and Pedro M. Paz-Alonso. White matter microstructure of attentional networks predicts attention and consciousness functional interactions. Brain Structure and Function, 223(2):653–668, 2018.


---

# References

1. Eve V. Clark. How language acquisition builds on cognitive development. Trends in Cognitive Sciences, 8(10):472–478, 2004.
2. Neal J. Cohen and Howard Eichenbaum. Memory, amnesia, and the hippocampal system. The MIT Press, Cambridge, MA, US, 1993.
3. S. M. Courtney. Attention and cognitive control as emergent properties of information representation in working memory. Cognitive, Affective and Behavioral Neuroscience, 4(4):501–516, 2004.
4. Nelson Cowan. What are the differences between long-term, short-term, and working memory? Progress in Brain Research, 169:323–338, 2008.
5. Ivo Danihelka, Greg Wayne, Benigno Uria, Nal Kalchbrenner, and Alex Graves. Associative long short-term memory. CoRR, arXiv:1602.03032, 2016.
6. Maria Dolores de Hevia, Véronique Izard, Aurélie Coubart, Elizabeth S. Spelke, and Arlette Streri. Representations of space, time, and number in neonates. Proceedings of the National Academy of Sciences, 111(13):4809–4813, 2014.
7. Terrence W. Deacon. The Symbolic Species: The Co-evolution of Language and the Brain. W. W. Norton, 1998.
8. M. O. Deák. Interrelations of language and cognitive development. In P. Brooks &#x26; V. Kampe, editor, The International Encyclopedia of the Social &#x26; Behavioral Sciences, pages 284–291. SAGE, 2014.
9. S. Dehaene, M. Piazza, P. Pinel, and L. Cohen. Three parietal circuits for number processing. Cognitive Neuropsychology, 20(3):487–506, 2003.
10. Stanislas Dehaene. Consciousness and the Brain: Deciphering How the Brain Codes Our Thoughts. Viking Press, 2014.
11. Stanislas Dehaene and Elizabeth Brannon. Space, Time and Number in the Brain: Searching for the Foundations of Mathematical Thought. Elsevier Science, 2011.
12. G. Dehaene-Lambertz and E.S. Spelke. The infancy of the human brain. Neuron, 88(1):93–109, 2015.
13. M. D’Esposito, J. A. Detre, D. C. Alsop, R. K. Shin, S. Atlas, and M. Grossman. The neural basis of the central executive system of working memory. Nature, 378(6554):279–281, 1995.
14. Jacob Devlin, Jonathan Uesato, Surya Bhupatiraju, Rishabh Singh, Abdel-rahman Mohamed, and Pushmeet Kohli. Robustfill: Neural program learning under noisy i/o. In Proceedings of the 34th International Conference on Machine Learning - Volume 70, pages 990–998. JMLR.org, 2017.
15. Thomas G. Dietterich. Hierarchical reinforcement learning with the MAXQ value function decomposition. Journal of Artificial Intelligence Research, 13:227–303, 2000.
16. C. Diuk, A. Schapiro, N. Córdova, J. Ribas-Fernandes, Y. Niv, and M. Botvinick. Divide and conquer: hierarchical reinforcement learning and task decomposition in humans. In Computational and robotic models of the hierarchical organization of behavior, pages 271–291, Berlin, Heidelberg, 2013. Springer.


---

# References

1. Daniel Dombeck and David Tank. Imaging in neuroscience. In Helmchen and Konnerth, editors, Two-Photon Imaging of Neural Activity in Awake Mobile Mice, pages 355–369. Cold Spring Harbor Press, 2011.
2. Rodney J. Douglas and Kevan A.C. Martin. Behavioral architecture of the cortical sheet. Current Biology, 22(24):R1033–R1038, 2012.
3. L. J. Drew, S. Fusi, and R. Hen. Adult neurogenesis in the mammalian hippocampus: Why the dentate gyrus? Learning and Memory, 20(12):710–729, 2013.
4. Mark Eisenberg, Tali Kobilo, Diego E. Berman, and Yadin Dudai. Stability of retrieved memory: Inverse correlation with trace dominance. Science, 301(5636):1102–1104, 2003.
5. Chris Eliasmith. How to Build a Brain: A Neural Architecture for Biological Cognition. Oxford Series on Cognitive Modeling. Oxford University Press USA, 2013.
6. Jerry Fodor. Modularity of Mind. MIT Press, Cambridge, Massachusetts, 1984.
7. Jerry A. Fodor and Zenon W. Pylyshyn. Connectionism and cognitive architecture. Cognition, 28(1-2):3–71, 1988.
8. David J Foster and Matthew A Wilson. Reverse replay of behavioural sequences in hippocampal place cells during the awake state. Nature, 440(7084):680, 2006.
9. M. J. Frank and D. Badre. Mechanisms of hierarchical reinforcement learning in corticostriatal circuits I: computational analysis. Cerebral Cortex, 22(3):509–526, 2012.
10. Robert French. Catastrophic forgetting in connectionist networks. Trends in Cognitive Sciences, 3:128–135, 1999.
11. Robert M. French. Pseudo-recurrent connectionist networks: An approach to the ’sensitivity-stability’ dilemma. Connection Science, 9(4):353–380, 1997.
12. K. Fukushima. Neocognitron: A self organizing neural network model for a mechanism of pattern recognition unaffected by shift in position. Biological Cybernetics, 36:93–202, 1980.
13. Joaquín M. Fuster. Chapter 8: An Overview of Prefrontal Functions, pages 375–425. Elsevier, London, 2015.
14. Joaquín M. Fuster. Prefrontal Cortex, 5th Edition. Elsevier, London, 2015.
15. S. Ge, E. L. Goh, K. A. Sailor, Y. Kitabatake, G. L. Ming, and H. Song. GABA regulates synaptic integration of newly generated neurons in the adult brain. Nature, 439(7076):589–593, 2006.
16. Samuel J. Gershman and Nathaniel D. Daw. Reinforcement learning and episodic memory in humans and animals: An integrative framework. Annual Reviews of Psychology, 68:101-128, 2017.
17. James J. Gibson. Perception of the Visual World. Houghton Mifflin, Boston, 1950.
18. Jozien Glense, Yvette Bohraus, and Nikos K. Logothetis. fMRI at high spatial resolution: Implications for BOLD-models. Frontiers in computational neuroscience, 10:66–66, 2016.


---

# References

1. Gary H. Glover. Overview of functional magnetic resonance imaging. Neurosurgery clinics of North America, 22:133–144, 2011.
2. Patricia S. Goldman-Rakic. Topography of cognition: Parallel distributed networks in primate association cortex. Annual Review of Neuroscience, 11(1):137–156, 1988.
3. Aida Gómez-Robles, William D. Hopkins, Steven J. Schapiro, and Chet C. Sherwood. Relaxed genetic control of cortical organization in human brains compared with chimpanzees. Proceedings of the National Academy of Sciences, 112(48):14799–14804, 2015.
4. Alex Graves, Abdel-rahman Mohamed, and Geoffrey Hinton. Speech recognition with deep recurrent neural networks. In 2013 IEEE international conference on acoustics, speech and signal processing, pages 6645–6649. IEEE, 2013.
5. Alex Graves, Greg Wayne, and Ivo Danihelka. Neural Turing machines. CoRR, arXiv:1410.5401, 2014.
6. Alex Graves, Greg Wayne, Malcolm Reynolds, Tim Harley, Ivo Danihelka, Agnieszka Grabska-Barwińska, Sergio Gómez Colmenarejo, Edward Grefenstette, Tiago Ramalho, John Agapiou, Adrià Puigdomènech Badia, Karl Moritz Hermann, Yori Zwols, Georg Ostrovski, Adam Cain, Helen King, Christopher Summerfield, Phil Blunsom, Koray Kavukcuoglu, and Demis Hassabis. Hybrid computing using a neural network with dynamic external memory. Nature, 538:471–476, 2016.
7. Karol Gregor, Ivo Danihelka, Alex Graves, and Daan Wierstra. DRAW: A recurrent neural network for image generation. CoRR, arXiv:1502.04623, 2015.
8. Arthur Guez, Théophane Weber, Ioannis Antonoglou, Karen Simonyan, Oriol Vinyals, Daan Wierstra, Rémi Munos, and David Silver. Learning to search with MCTSnets. CoRR, arXiv:1802.04697, 2018.
9. RW Guillery. Is postnatal neocortical maturation hierarchical? Trends in neurosciences, 28(10):512–517, 2005.
10. Caglar Gülcehre, Marcin Moczulski, Francesco Visin, and Yoshua Bengio. Mollifying networks. CoRR, arXiv:1608.04980, 2016.
11. Jessica B. Hamrick, Kelsey R. Allen, Victor Bapst, Tina Zhu, Kevin R. McKee, Joshua B. Tenenbaum, and Peter W. Battaglia. Relational inductive bias for physical construction in humans and machines. CoRR, abs/1806.01203, 2018.
12. Jessica B. Hamrick, Andrew J. Ballard, Razvan Pascanu, Oriol Vinyals, Nicolas Heess, and Peter W. Battaglia. Metacontrol for adaptive imagination-based optimization. CoRR, arXiv:1705.02670, 2017.
13. Yunyun Han, Justus M. Kebschull, Robert A. A. Campbell, Devon Cowan, Fabia Imhof, Anthony M. Zador, and Thomas D. Mrsic-Flogel. The logic of single-cell projections from visual cortex. Nature, 556:51–56, 2018.
14. Marc D. Hauser and Elizabeth Spelke. Evolutionary and developmental foundations of human knowledge: A case study of mathematics. In M. Gazzaniga and N. Logothetis, editors, The Cognitive Neurosciences, III, pages 853–864. MIT Press, Cambridge, MA, 2004.


---

[88] Michael Hawrylycz, Jeremy A. Miller, Vilas Menon, David Feng, Tim Dolbeare, Angela L. Guillozet-Bongaarts, Anil G. Jegga, Bruce J. Aronow, Chang-Kyu Lee, Amy Bernard, Matthew F. Glasser, Donna L. Dierker, Jörg Menche, Aaron Szafer, Forrest Collman, Pascal Grange, Kenneth A. Berman, Stefan Mihalas, Zizhen Yao, Lance Stewart, Albert-László Barabási, Jay Schulkin, John Phillips, Lydia Ng, Chinh Dang, David R. Haynor, Allan Jones, David C. Van Essen, Christof Koch, and Ed Lein. Canonical genetic signatures of the adult human brain. Nature Neuroscience, 18:1832–1844, 2015.

[89] Michael J. Hawrylycz, Ed S. Lein, Angela L. Guillozet-Bongaarts, Elaine H. Shen, Lydia Ng, Jeremy A. Miller, Louie N. van de Lagemaat, Kimberly A. Smith, Amanda Ebbert, Zackery L. Riley, Chris Abajian, Christian F. Beckmann, Amy Bernard, Darren Bertagnolli, Andrew F. Boe, Preston M. Cartagena, M. Mallar Chakravarty, Mike Chapin, Jimmy Chong, Rachel A. Dalley, Barry David Daly, Chinh Dang, Suvro Datta, Nick Dee, Tim A. Dolbeare, Vance Faber, David Feng, David R. Fowler, Jeff Goldy, Benjamin W. Gregor, Zeb Haradon, David R. Haynor, John G. Hohmann, Steve Horvath, Robert E. Howard, Andreas Jeromin, Jayson M. Jochim, Marty Kinnunen, Christopher Lau, Evan T. Lazarz, Changkyu Lee, Tracy A. Lemon, Ling Li, Yang Li, John A. Morris, Caroline C. Overly, Patrick D. Parker, Sheana E. Parry, Melissa Reding, Joshua J. Royall, Jay Schulkin, Pedro Adolfo Sequeira, Clifford R. Slaughterbeck, Simon C. Smith, Andy J. Sodt, Susan M. Sunkin, Beryl E. Swanson, Marquis P. Vawter, Derric Williams, Paul Wohnoutka, H. Ronald Zielke, Daniel H. Geschwind, Patrick R. Hof, Stephen M. Smith, Christof Koch, Seth G. N. Grant, and Allan R. Jones. An anatomically comprehensive atlas of the adult human brain transcriptome. Nature, 489:391–399, 2012.

[90] T. E. Hazy, M. J. Frank, and R. C. O’reilly. Towards an executive without a homunculus: computational models of the prefrontal cortex/basal ganglia system. Philosophical Transactions of the Royal Society London B, Biological Science, 362(1485):1601–1613, 2007.

[91] Bernhard Hengst. Hierarchical reinforcement learning. In Claude Sammut and Geoffrey I. Webb, editors, Encyclopedia of Machine Learning and Data Mining, pages 611–619. Springer US, Boston, MA, 2017.

[92] Sepp Hochreiter and Jürgen Schmidhuber. Long short-term memory. Neural Computing, 9:1735–1780, 1997.

[93] John Hughlings Jackson. Selected Writings of John Hughlings Jackson: Evolution and dissolution of the nervous system. Selected Writings of John Hughlings Jackson. Basic Books, 1958.

[94] Michal Januszewski, Jörgen Kornfeld, Peter H Li, Art Pope, Tim Blakely, Larry Lindsey, Jeremy B Maitin-Shepard, Mike Tyka, Winfried Denk, and Viren Jain. High-precision automated reconstruction of neurons with flood-filling networks. Nature Methods, 15:605–610, 2017.

[95] David Jilk, Christian Lebiere, Randall O’Reilly, and John R. Anderson. SAL: An explicitly pluralistic cognitive architecture. Journal Experimental and Theoretical Artificial Intelligence, 20:197–218, 2008.

[96] Hannah R. Joo and Loren M. Frank. The hippocampal sharp wave-ripple in memory retrieval for immediate use and consolidation. Nature Reviews Neuroscience, 19:744–757, 2018.


---

# References

1. Leslie Pack Kaelbling. Hierarchical reinforcement learning: A preliminary report. In Proceedings Tenth International Conference on Machine Learning, pages 167–173, 1993.
2. Mattias P Karlsson and Loren M Frank. Awake replay of remote experiences in the hippocampus. Nature neuroscience, 12(7):913, 2009.
3. R. P. Kesner and E. T. Rolls. A computational theory of hippocampal function, and tests of the theory: New developments.
4. James Kirkpatrick, Razvan Pascanu, Neil C. Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A. Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, Demis Hassabis, Claudia Clopath, Dharshan Kumaran, and Raia Hadsell. Overcoming catastrophic forgetting in neural networks. CoRR, arXiv:1612.00796, 2016.
5. Y. Kitabatake, K. A. Sailor, G. L. Ming, and H. Song. Adult neurogenesis and hippocampal memory function: new cells, more plasticity, new memories? Neurosurgery Clinics of North America, 18(1):105–113, 2007.
6. Etienne Koechlin, Chrystèle Ody, and Frédérique Kouneiher. The architecture of cognitive control in the human prefrontal cortex. Science, 302:1181–1185, 2003.
7. H. Kolster, J. B. Mandeville, J. T. Arsenault, L. B. Ekstrom, L. L. Wald, and W. Vanduffel. Visual field map clusters in macaque extrastriate visual cortex. Journal Neuroscience, 29(21):7031–7039, 2009.
8. Talia Konkle and Alfonso Caramazza. Tripartite organization of the ventral stream by animacy and object size. Journal of Neuroscience, 33(25):10235–10242, 2013.
9. Ivica Kostović and Miloš Judaš. Early development of neuronal circuitry of the human prefrontal cortex. In Michael S. Gazzaniga, editor, The Cognitive Neurosciences, 4th Edition, pages 29–48. The MIT Press, Cambridge, MA, 2009.
10. Leonard F. Koziol, Deborah Budding, Nancy Andreasen, Stefano D’Arrigo, Sara Bulgheroni, Hiroshi Imamizu, Masao Ito, Mario Manto, Cherie Marvel, Krystal Parker, Giovanni Pezzulo, Narender Ramnani, Daria Riva, Jeremy Schmahmann, Larry Vandervert, and Tadashi Yamazaki. Consensus paper: the cerebellum’s role in movement and cognition. Cerebellum (London, England), 13:151–177, 2014.
11. Tejas D. Kulkarni, Karthik Narasimhan, Ardavan Saeedi, and Josh Tenenbaum. Hierarchical deep reinforcement learning: Integrating temporal abstraction and intrinsic motivation. In Advances in Neural Information Processing Systems 29, pages 3675–3683, 2016.
12. Dharshan Kumaran, Demis Hassabis, and James L. McClelland. What learning systems do intelligent agents need? Complementary learning systems theory updated. Trends in Cognitive Sciences, 20(7):512–534, 2016.
13. Dharshan Kumaran and Eleanor A. Maguire. The human hippocampus: Cognitive maps or relational memory? Journal of Neuroscience, 25(31):7254–7259, 2005.
14. Christian Lebiere and John Anderson. A connectionist implementation of the act-r production system. In Proceedings of the Fifteenth Annual Conference of the Cognitive Science Society, pages 635–640. Cognitive Science Society, 1993.


---

# References

1. J. Y. Lettvin, H. R. Maturana, W. S. McCulloch, and W. H. Pitts. What the frog’s eye tells the frog’s brain. Proceedings of the Institute for Radio Engineers, 47:1940–1951, 1959.
2. Long-Ji Lin. Self-improving reactive agents based on reinforcement learning, planning and teaching. Machine Learning, 8(3):293–321, 1992.
3. Michael Littman, Thomas Dean, and Leslie Kaelbling. On the complexity of solving Markov decision problems. In Proceedings of the 11th Conference on Uncertainty in Artificial Intelligence, pages 394–402, San Francisco, California, 1995. AUAI, Morgan Kaufmann Publishers.
4. Bria Long, Chen-Ping Yu, and Talia Konkle. Mid-level visual features underlie the high-level categorical organization of the ventral stream. Proceedings of the National Academy of Sciences, 115(38):E9015–E9024, 2018.
5. E. L. MacLean. Unraveling the evolution of uniquely human cognition. Proceedings of the National Academy of Sciences, 113(23):6348–6354, 2016.
6. D. Marr and Giles Skey Brindley. Simple memory: a theory for archicortex. Philosophical Transactions of the Royal Society of London. B, Biological Sciences, 262(841):23–81, 1971.
7. J. McClelland. On the time relations of mental processes: An examination of systems of processes in cascade. Psychological Review, 86:287–330, 1979.
8. J. McClelland and D. Rumelhart. An interactive activation model of context effects in letter perception: I. An account of basic findings. Psychological Review, 88:375–407, 1981.
9. J. L. McClelland and N. H. Goddard. Considerations arising from a complementary learning systems perspective on hippocampus and neocortex. Hippocampus, 6(6):654–665, 1996.
10. James L. McClelland, Bruce L. McNaughton, and Randall C. O’Reilly. Why there are complementary learning systems in the hippocampus and neocortex: Insights from the successes and failures of connectionist models of learning and memory. Psychological Review, 102(3):419–457, 1995.
11. DI McCloskey. Corollary discharges: motor commands and perception. Comprehensive physiology, pages 1415–1447, 2011.
12. W. S. McCulloch and W. H. Pitts. A logical calculus of ideas immanent in nervous activity. Bulletin of Mathematical Biophysics, 5:115–133, 1943.
13. William Menegas, Benedicte M Babayan, Naoshige Uchida, and Mitsuko Watabe-Uchida. Opposite initialization to novel cues in dopamine signaling in ventral and posterior striatum in mice. Elife, 6:e21886, 2017.
14. Shawn Mikula and Winfried Denk. High-resolution whole-brain staining for electron microscopic circuit reconstruction. Nature Methods, 2015.
15. Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, and Koray Kavukcuoglu. Asynchronous methods for deep reinforcement learning. CoRR, arXiv:1602.01783, 2016.
16. Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, and Martin Riedmiller. Playing Atari with deep reinforcement learning. CoRR, arXiv:1312.5602, 2013.


---

[127] Kristof Van Moffaert and Ann Now´ e. Multi-objective reinforcement learning using sets of pareto dominating policies. Journal of Machine Learning Research, 15:3663–3692, 2014.

[128] Zolt´ an Moln´ ar, Gavin J. Clowry, Nenad Sestan, Ayman Alzu’bi, Trygve Bakken, Robert F. Hevner, Petra S. H¨ uppi, Ivica Kostovi´ c, Pasko Rakic, E. S. Anton, David Edwards, Patricia Garcez, Anna Hoerder-Suabedissen, and Arnold Kriegstein. New insights into the development of the human cerebral cortex. Journal of Anatomy, 235(3):432–451, 2019.

[129] Felipe Mora-Berm´ udez, Farhath Badsha, Sabina Kanton, J. Gray Camp, Benjamin Vernot, Kathrin K¨ ohler, Birger Voigt, Keisuke Okita, Tomislav Maricic, Zhisong He, Robert Lachmann, Svante Paabo, Barbara Treutlein, and Wieland B. Huttner. Differences and similarities between human and chimpanzee neural progenitors during cerebral cortex development. eLife, 5:e18683, 2016.

[130] Richard G.M. Morris, Jennifer Inglis, James A. Ainge, Henry J. Olverman, Jane Tulloch, Yadin Dudai, and Paul A.T. Kelly. Memory reconsolidation: Sensitivity of spatial memory to inhibition of protein synthesis in dorsal hippocampus during encoding and retrieval. Neuron, 50(3):479–489, 2006.

[131] Arun Naira, Praveen Srinivasana, Sam Blackwella, Cagdas Alciceka, Rory Fearona, Alessan- dro De Mariaa, Vedavyas Panneershelvama, Mustafa Suleymana, Charles Beattiea, Stig Petersena, Shane Legga, Volodymyr Mniha, Koray Kavukcuoglua, and David Silver. Massively parallel methods for deep reinforcement learning. CoRR, arXiv:1507.04296, 2015.

[132] Karthik Narasimhan, Regina Barzilay, and Tommi Jaakkola. Grounding language for transfer in deep reinforcement learning. Journal of Artificial Intelligence Research, 63:849–874, 2018.

[133] Joshua P. Neunuebel and James J. Knierim. CA3 retrieves coherent representations from degraded input: Direct evidence for CA3 pattern completion and dentate gyrus pattern separation. Neuron, 81(2):416–427, 2014.

[134] Kenichi Oishi, Karl Zilles, Katrin Amunts, Andreia Faria, Hangyi Jiang, Xin Li, Kazi Akhter, Kegang Hua, Roger Woods, Arthur W. Toga, G. Bruce Pike, Pedro Rosa-Neto, Alan Evans, Jiangyang Zhang, Hao Huang, Michael I. Miller, Peter C.M. van Zijl, John Mazziotta, and Susumu Mori. Human brain white matter atlas: Identification and assignment of common anatomical structures in superficial white matter. NeuroImage, 43(3):447–457, 2008.

[135] H. Freyja ´ Olafsd´ ottir, Daniel Bush, and Caswell Barry. The role of hippocampal replay in memory and planning. Current Biology, 28(1):R37–R50, 2018.

[136] Randall C. O’Reilly. Biologically based computational models of high-level cognition. Science, 314:91–94, 2006.

[137] Randall C. O’Reilly, Rajan Bhattacharyya, Michael D. Howard, and Nicholas Ketz. Complementary learning systems. Cognitive Science, 38(6):1229–1248, 2014.

[138] Randall C. O’Reilly and Michael J. Frank. Making working memory work: A computational model of learning in the prefrontal cortex and basal ganglia. Neural Computation, 18:283–328, 2006.

[139] Randall C O’Reilly, Michael J Frank, Thomas E Hazy, and Brandon Watz. Pvlv: the primary value and learned value pavlovian learning algorithm. Behavioral neuroscience, 121(1):31, 2007.


---

[140] Randall C. O’Reilly, Thomas E. Hazy, and Seth A. Herd. The Leabra cognitive architecture: How to play 20 principles with nature and win! In Susan E. F. Chipman, editor, The Oxford Handbook of Cognitive Science, Oxford Handbooks, pages 91–115. Oxford University Press, 2016.

[141] Randall C. O’Reilly, Yuko Munakata, Michael J. Frank, Thomas E. Hazy, and Contributors. Computational Cognitive Neuroscience. Wiki Book, 1st Edition, 2012.

[142] Randall C. O’Reilly, Alex A. Petrov, Jonathan D. Cohen, Christian J. Lebiere, Seth A. Herd, and Trent Kriete. How limited systematicity emerges: A computational cognitive neuroscience approach. In Paco Calvo and John Symons, editors, The Architecture of Cognition, pages 191–224. MIT Press, Cambridge, Massachusetts, 2014.

[143] Razvan Pascanu, Yujia Li, Oriol Vinyals, Nicolas Heess, Lars Buesing, Sébastien Racanière, David P. Reichert, Theophane Weber, Daan Wierstra, and Peter Battaglia. Learning model-based planning from scratch. CoRR, arXiv:1707.06170, 2017.

[144] Alexander Pashevich, Danijar Hafner, James Davidson, Rahul Sukthankar, and Cordelia Schmid. Modulated policy hierarchies. CoRR, arXiv:1812.00025, 2018.

[145] M.L. Platt and E. S Spelke. What can developmental and comparative cognitive neuroscience tell us about the adult human brain? Current Opinion in Neurobiology, 19(1):1–5, 2009.

[146] Ruben Portugues, Claudia E. Feierstein, Florian Engert, and Michael B. Orger. Whole-brain activity maps reveal stereotyped, distributed networks for visuomotor behavior. Neuron, 81:1328–1343, 2014.

[147] Sebastien Racaniere, Andrew K. Lampinen, Adam Santoro, David P. Reichert, Vlad Firoiu, and Timothy P. Lillicrap. Automated curricula through setter-solver interactions. CoRR, arXiv:1909.12892, 2019.

[148] Pasko Rakik, Jon Arellano, and Joshua Breunig. Development of the primate cerebral cortex. In Michael S. Gazzaniga, editor, The Cognitive Neurosciences, 4th Edition, pages 7–28. The MIT Press, Cambridge, MA, 2009.

[149] Daniel Rasmussen, Aaron Voelker, and Chris Eliasmith. A neural model of hierarchical reinforcement learning. PLOS ONE, 12(7):1–39, 2017.

[150] J. J. Ribas-Fernandes, A. Solway, C. Diuk, J. T. McGuire, A. G. Barto, Y. Niv, and M. M. Botvinick. A neural signature of hierarchical reinforcement learning. Neuron, 71(2):370–379, 2011.

[151] Anthony Robins. Catastrophic forgetting, rehearsal and pseudorehearsal. Connection Science, 7(2):123–146, 1995.

[152] Alexandra G. Rosati, Victoria Wobber, Kelly Hughes, and Laurie R. Santos. Comparative developmental psychology: How is human cognitive development unique? Evolutionary Psychology, 12(2):147470491401200211, 2014.

[153] Eleanor Rosch. Cognitive reference points. Cognitive Psychology, 7(4):532–547, 1975.

[154] Eleanor H. Rosch. Natural categories. Cognitive Psychology, 4(3):328–350, 1973.


---

# References

1. S. A. Rose, J. F. Feldman, and J. J. Jankowski. A cognitive approach to the development of early language. Child Development, 80(1):134–150, 2009.
2. Jon W. Rueckemann and Elizabeth A. Buffalo. Auditory landscape on the cognitive map. Nature, 543:631, 2017.
3. Himanshu Sahni, Saurabh Kumar, Farhan Tejani, and Charles L. Isbell. Learning to compose skills. CoRR, arXiv:1711.11289, 2017.
4. Alvaro Sanchez-Gonzalez, Nicolas Heess, Jost Tobias Springenberg, Josh Merel, Martin A. Riedmiller, Raia Hadsell, and Peter Battaglia. Graph networks as learnable physics engines for inference and control. CoRR, arXiv:1806.01242, 2018.
5. Adam Santoro, David Raposo, David G Barrett, Mateusz Malinowski, Razvan Pascanu, Peter Battaglia, and Timothy Lillicrap. A simple neural network module for relational reasoning. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, Advances in Neural Information Processing Systems 30, pages 4967–4976. Curran Associates, Inc., 2017.
6. Anna C Schapiro, Elizabeth A McDevitt, Timothy T Rogers, Sara C Mednick, and Kenneth A Norman. Human hippocampal replay during rest prioritizes weakly learned information and predicts memory performance. Nature communications, 9(1):3920, 2018.
7. Tom Schaul, John Quan, Ioannis Antonoglou, and David Silver. Prioritized experience replay. CoRR, arXiv:1511.05952, 2015.
8. M. L. Schlichting and A. R. Preston. Memory integration: neural mechanisms and implications for behavior. Current Opinion in Behavioral Science, 1:1–8, 2015.
9. C. Schmidt-Hieber, P. Jonas, and J. Bischofberger. Enhanced synaptic plasticity in newly generated granule cells of the adult hippocampus. Nature, 429(6988):184–187, 2004.
10. NW Schuck and Y Niv. Sequential replay of non-spatial task states in the human hippocampus. biorxiv. DOI, 10:315978, 2018.
11. Yevgeny Seldin, Gill Bejerano, and Naftali Tishby. Unsupervised segmentation and classification of mixtures of Markovian sources. In Proceedings of the 33rd Symposium on the Interface of Computing Science and Statistics, 2001.
12. Yevgeny Seldin, Gill Bejerano, and Naftali Tishby. Unsupervised sequence segmentation by a mixture of switching variable memory Markov sources. In Proceedings of the Eighteenth International Conference on Machine Learning (ICML 2001), pages 513–520, 2001.
13. Rishabh Singh and Pushmeet Kohli. AP:Artificial Programming. In Summit on Advances in Programming Languages 2017, 2017.
14. Kirsty L. Spalding, Olaf Bergmann, Kanar Alkass, Samuel Bernard, Mehran Salehpour, Hagen B. Huttner, Emil Boström, Isabelle Westerlund, Celine Vial, Bruce A. Buchholz, Göran Possnert, Deborah C. Mash, Henrik Druid, and Jonas Frisén. Dynamics of hippocampal neurogenesis in adult humans. Cell, 153:1219–1227, 2013.
15. Kimberly L. Stachenfeld, Matthew M. Botvinick, and Samuel J. Gershman. The hippocampus as a predictive map. Nature Neuroscience, 20:1643, 2017.


---

# References

1. Larry W. Swanson. Mapping the human brain: past, present, and future. Trends in Neurosciences, 18(11):471–474, 1995.
2. CM Sylvester, GL Shulman, AI Jack, and M Corbetta. Anticipatory and stimulus-evoked blood oxygenation level-dependent modulations related to spatial attention reflect a common additive signal. The Journal of neuroscience: the official journal of the Society for Neuroscience, 29(34):10671, 2009.
3. Travis, Katherine E., Yael Leitner, Heidi M. Feldman, and Michal Ben-Shachar. Cerebellar white matter pathways are associated with reading skills in children and adolescents. Human Brain Mapping, 36(4):1536–1553, 2015.
4. F.J. Varela, Eleanor. Rosch, and E. Thompson. The Embodied Mind: Cognitive Science and Human Experience. MIT Press, 1991.
5. J. von Uexküll and D.L. Mackinnon. Theoretical Biology. International Library of Psychology, Philosophy and Scientific Method. K. Paul, Trench, Trubner &#x26; Company Limited, 1926.
6. Nicholas P Vyleta, Carolina Borges-Merjane, and Peter Jonas. Plasticity-dependent, full detonation at hippocampal mossy fiberCA3 pyramidal neuron synapses. eLife, 5:e17977, 2016.
7. S. Wakana, H. Jiang, L. M. Nagae-Poetscher, P. C. van Zijl, and S. Mori. Fiber tract-based atlas of human white matter anatomy. Radiology, 230(1):77–87, 2004.
8. Jane X. Wang, Zeb Kurth-Nelson, Dharshan Kumaran, Dhruva Tirumala, Hubert Soyer, Joel Z. Leibo, Demis Hassabis, and Matthew Botvinick. Prefrontal cortex as a meta-reinforcement learning system. Nature Neuroscience, 21:860–868, 2018.
9. Ke Wang, Rishabh Singh, and Zhendong Su. Dynamic neural program embedding for program repair. CoRR, arXiv:1711.07163, 2017.
10. Wei Wang and Guang-Zhong Wang. Understanding molecular mechanisms of the brain through transcriptomics. Frontiers in physiology, 10:214–214, 2019.
11. Theophane Weber, Sébastien Racanière, David P. Reichert, Lars Buesing, Arthur Guez, Danilo Jimenez Rezende, Adrià Puigdomènech Badia, Oriol Vinyals, Nicolas Heess, Yujia Li, Razvan Pascanu, Peter Battaglia, David Silver, and Daan Wierstra. Imagination-augmented agents for deep reinforcement learning. CoRR, arXiv:1707.06203, 2017.
12. Jason Weston, Sumit Chopra, and Antoine Bordes. Memory networks. CoRR, arXiv:1410.3916, 2014.
13. Romain Willemet. Understanding the evolution of mammalian brain structures; the need for a (new) cerebrotype approach. Brain sciences, 2:203–224, 2012.
14. D. J. Willshaw, P. Dayan, and R. G. M. Morris. Memory, modelling and marr: a commentary on marr (1971) simple memory: a theory of archicortex. Philosophical Transactions of the Royal Society B: Biological Sciences, 370(1666):20140383, 2015.
15. M. A. Wilson and B.L. McNaughton. Reactivation of hippocampal ensemble memories during sleep. Science, 265(5172):676–679, 1994.


---

# References

1. L. Wiskott, M. J. Rasch, and G. Kempermann. A functional hypothesis for adult hippocampal neurogenesis: avoidance of catastrophic interference in the dentate gyrus. Hippocampus, 16(3):329–343, 2006.
2. Anthony Wright. Higher cortical functions: Association and executive processing. In Neuroscience Online: An electronic textbook for the neurosciences. The University of Texas McGovern Medical School, 1997.
3. O. Yizhar, L.E. Fenno, T.J. Davidson, M. Mogri, and K. Deisseroth. Optogenetics in neural systems. Neuron, 71:9–34, 2011.
4. F. Zhang, V. Gradinaru, A.R. Adamantidis, R. Durand, R.D. Airan, L. de Lecea, and K. Deisseroth. Optogenetic interrogation of neural circuits: technology for probing mammalian brain structures. Nature Protocols, 5:439–56, 2010.
5. Zhihao Zheng, J. Scott Lauritzen, Eric Perlman, Camenzind G. Robinson, Matthew Nichols, Daniel Milkie, Omar Torrens, John Price, Corey B. Fisher, Nadiya Sharifi, Steven A. Calle-Schuler, Lucia Kmecova, Iqbal J. Ali, Bill Karsh, Eric T. Trautman, John Bogovic, Philipp Hanslovsky, Gregory S. X. E. Jefferis, Michael Kazhdan, Khaled Khairy, Stephan Saalfeld, Richard D. Fetter, and Davi D. Bock. A complete electron microscopy volume of the brain of adult drosophila melanogaster. Cell, 174:1–14, 2018.

